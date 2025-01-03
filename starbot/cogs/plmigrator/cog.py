from __future__ import annotations

import asyncio
import typing
from pathlib import Path

import aiopath
from starbot.cogs.audio.apis.api_utils import PlaylistFetchResult
from starbot.cogs.audio.apis.playlist_wrapper import PlaylistWrapper
from starbot.cogs.audio.utils import (
    DEFAULT_LAVALINK_SETTINGS,
    DEFAULT_LAVALINK_YAML,
    PlaylistScope,
    change_dict_naming_convention,
)
from starbot.core import Config, commands
from starbot.core.data_manager import cog_data_path
from starbot.core.i18n import Translator, cog_i18n
from starbot.core.utils.dbtools import APSWConnectionWrapper

from pylav.constants.config import DEFAULT_PLAYER_VOLUME
from pylav.core.client import Client
from pylav.core.context import PyLavContext
from pylav.extension.red.utils import recursive_merge
from pylav.logging import getLogger
from pylav.players.query.obj import Query
from pylav.type_hints.bot import DISCORD_BOT_TYPE, DISCORD_COG_TYPE_MIXIN

LOGGER = getLogger("PyLav.cog.Migrator")

_ = Translator("PyLavMigrator", Path(__file__))


@cog_i18n(_)
class PyLavMigrator(DISCORD_COG_TYPE_MIXIN):
    """Copy the Red Audio settings over to PyLav"""

    lavalink: Client

    __version__ = "1.0.0"

    def __init__(self, bot: DISCORD_BOT_TYPE, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="plmigrate")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def command_pylavmigrate(self, context: PyLavContext, confirm: bool, /) -> None:
        """Migrate Audio settings to PyLav

        Please note that this will replace any settings already in PyLav.

        If you are sure you want to proceed please run this command again with the confirmation argument set to 1
        i.e `[p]pylavmigrate 1`

        Once you complete the migration unload this cog and uninstall it as you will not need it again.
        """
        if not confirm:
            await context.send_help()
            return
        audio_config, playlist_api = await self._init_audio_cog_dependencies()
        await self._process_global_settings(audio_config, context)
        for guild, guild_config in (await audio_config.all_guilds()).items():
            await self._process_server_settings(guild, guild_config)
        await self._process_playlists(playlist_api, context)
        await context.send(
            content=_(
                "Migration of Audio cog settings to PyLav complete. "
                "Restart the bot for it to take effect.\n{requester_variable_do_not_translate}."
            ).format(requester_variable_do_not_translate=context.author.mention),
            ephemeral=True,
        )

    @commands.is_owner()
    @commands.command(name="plm-playlists")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def command_pylavmigrate_playlist(self, context: PyLavContext, confirm: bool, /) -> None:
        """Migrate Audio Playlists to PyLav

        If you are sure you want to proceed please run this command again with the confirmation argument set to 1
        i.e `[p]pl,-playlists 1`

        Do Note this is a best effort task, somethings may not migrate.
        """
        if not confirm:
            await context.send_help()
            return
        __, playlist_api = await self._init_audio_cog_dependencies()
        await self._process_playlists(playlist_api, context)
        await context.send(
            content=_(
                "Migration of Audio cog Playlists to PyLav complete.\n{requester_variable_do_not_translate}."
            ).format(requester_variable_do_not_translate=context.author.mention),
            ephemeral=True,
        )

    @commands.is_owner()
    @commands.command(name="plmigrate-revert")
    async def command_pylavmigrate(self, context: PyLavContext, confirm: bool, /) -> None:
        """Reverts the Playlist migration which can cause broken autoplaylists.

        Please note that this will replace any settings already in PyLav.

        If you are sure you want to proceed please run this command again with the confirm argument set to 1
        i.e `[p]plmigrate-revert 1`
        """
        if not confirm:
            await context.send_help()
            return
        audio_config, playlist_api = await self._init_audio_cog_dependencies()
        for guild, guild_config in (await audio_config.all_guilds()).items():
            player_config = self.pylav.player_config_manager.get_config(guild)
            await player_config.update_auto_play_playlist_id(1)
            if guild_config.get("autoplaylist", {}).get("enabled", False):
                await player_config.update_auto_play(True)
            else:
                await player_config.update_auto_play(False)

    async def _process_playlists(self, playlist_api: PlaylistWrapper, context: PyLavContext) -> None:
        query = """
                    SELECT
                        playlist_id,
                        playlist_name,
                        scope_id,
                        author_id,
                        playlist_url,
                        tracks
                    FROM
                        playlists
                    WHERE
                        deleted = false
                """
        row_results = await asyncio.to_thread(playlist_api.database.cursor().execute, query)
        for row in row_results:
            pl = PlaylistFetchResult(*row)
            queries = [await Query.from_string(track["info"]["uri"]) for track in pl.tracks if track.get("info")]
            url = pl.playlist_url
            try:
                if pl.playlist_id == 42069:
                    continue
                if url:
                    response = await self.pylav.get_tracks(await Query.from_string(url))
                    match response.loadType:
                        case "track":
                            tracks = [response.data]
                        case "search":
                            tracks = response.data
                        case "playlist":
                            tracks = response.data.tracks
                        case __:
                            LOGGER.error(
                                "Failed to fetch v4+ tracks playlist %s (%s) from scope: %s",
                                pl.playlist_name,
                                pl.playlist_id,
                                pl.scope_id,
                            )
                            continue
                else:
                    tracks, __, __ = await self.bot.pylav.get_all_tracks_for_queries(
                        *queries, requester=context.guild.me
                    )

                if tracks:
                    await self.pylav.playlist_db_manager.create_or_update_playlist(
                        identifier=pl.playlist_id,
                        name=pl.playlist_name,
                        scope=pl.scope_id,
                        author=pl.author_id,
                        url=pl.playlist_url,
                        tracks=tracks,
                    )
                    LOGGER.info(
                        "Successfully migrated playlist %s (%s) from guild: %s in scope: %s",
                        pl.playlist_name,
                        pl.playlist_id,
                        pl.author_id,
                        pl.scope_id,
                    )
            except Exception as exc:
                LOGGER.error(
                    "Failed to migrate playlist %s (%s) from guild: %s in scope: %s",
                    pl.playlist_name,
                    pl.playlist_id,
                    pl.author_id,
                    pl.scope_id,
                    exc_info=exc,
                )

    async def _process_server_settings(self, guild: int, guild_config: typing.MutableMapping[str, typing.Any]) -> None:
        player_config = self.pylav.player_config_manager.get_config(guild)
        if not guild_config.get("auto_deafen", True):
            await player_config.update_self_deaf(False)
        if guild_config.get("dj_enabled", False) is True:
            if dj_role := guild_config.get("dj_role"):
                if guild_obj := self.bot.get_guild(guild):
                    if role := guild_obj.get_role(dj_role):
                        await player_config.add_to_dj_roles(role)
        if guild_config.get("autoplaylist", {}).get("enabled", False):
            await player_config.update_auto_play(True)
        else:
            await player_config.update_auto_play(False)
        if guild_config.get("shuffle", False):
            await player_config.update_shuffle(True)
        if guild_config.get("volume", 100) not in {100, DEFAULT_PLAYER_VOLUME}:
            await player_config.update_volume(guild_config.get("volume"))
        if guild_config.get("max_volume", 150) != 150:
            await player_config.update_max_volume(int((guild_config.get("max_volume") / 150) * 1000))
        if guild_config.get("emptypause_enabled"):
            await player_config.update_alone_pause({"enabled": True, "time": guild_config.get("emptypause_timer", 60)})
        if guild_config.get("emptydc_enabled"):
            await player_config.update_alone_dc({"enabled": True, "time": guild_config.get("emptydc_timer", 60)})
        if guild_config.get("disconnect"):
            await player_config.update_empty_queue_dc({"enabled": True, "time": 60})

    async def _process_global_settings(self, audio_config: Config, context: PyLavContext) -> None:
        global_config = self.pylav.lib_db_manager.get_config()
        if r := await audio_config.localpath():
            path = aiopath.AsyncPath(r)
            localtracks_path = path / "localtracks"
            try:
                if await localtracks_path.exists():
                    await self.pylav.update_localtracks_folder(f"{localtracks_path}")
            except PermissionError:
                await context.send(
                    embed=await self.pylav.construct_embed(
                        description=_("I do not have permission to access {folder_variable_do_not_translate}.").format(
                            folder_variable_do_not_translate=localtracks_path
                        )
                    )
                )
        if await audio_config.status():
            await global_config.update_update_bot_activity(True)
        # # if __ := await audio_config.use_external_lavalink():
        #     await global_config.update_enable_managed_node(False)
        #     await self.pylav.add_node(
        #         unique_identifier=context.message.id,
        #         name="AudioMigratedExternal",
        #         host=await audio_config.host(),
        #         password=await audio_config.password(),
        #         port=await audio_config.rest_port(),
        #         ssl=await audio_config.secured_ws(),
        #         search_only=False,
        #         managed=False,
        #         extras=None,
        #         disabled_sources=None,
        #         yaml=None,
        #     )
        # else:
        audio_yaml = change_dict_naming_convention(await audio_config.yaml.all())
        bundled_node_config = self.pylav.node_db_manager.bundled_node_config()
        await bundled_node_config.update_yaml(recursive_merge(await bundled_node_config.fetch_yaml(), audio_yaml))
        extras = await bundled_node_config.fetch_extras()
        extras["max_ram"] = await audio_config.java.Xmx()
        await bundled_node_config.update_extras(extras)

    async def _init_audio_cog_dependencies(self) -> tuple[Config, PlaylistWrapper]:
        from starbot.cogs.audio import Audio

        if cog := typing.cast(Audio, self.bot.get_cog("Audio")):
            playlist_api = cog.playlist_api
            audio_config = cog.config
        else:
            audio_config = Config.get_conf(None, identifier=2711759130, cog_name="Audio")
            default_global = dict(
                use_external_lavalink=False,  # Supported in PyLav
                status=False,  # Supported in PyLav
                localpath=str(cog_data_path(raw_name="Audio")),  # Supported in PyLav
                java_exc_path="java",  # Supported in PyLav
                **DEFAULT_LAVALINK_YAML,  # Supported in PyLav
                **DEFAULT_LAVALINK_SETTINGS,  # Supported in PyLav
            )

            default_guild = dict(
                auto_play=False,  # Supported in PyLav
                auto_deafen=True,  # Supported in PyLav
                autoplaylist=dict(
                    enabled=True,  # Supported in PyLav
                    id=42069,  # Supported in PyLav
                ),
                disconnect=False,  # Supported in PyLav
                emptydc_enabled=False,  # Supported in PyLav
                emptydc_timer=0,  # Supported in PyLav
                emptypause_enabled=False,  # Supported in PyLav
                emptypause_timer=0,  # Supported in PyLav
                max_volume=150,  # Supported in PyLav
                shuffle=None,  # Supported in PyLav
                volume=DEFAULT_PLAYER_VOLUME,  # Supported in PyLav
                dj_enabled=False,  # Supported in PyLav
                dj_role=None,  # Supported in PyLav
            )
            _playlist = dict(id=None, author=None, name=None, playlist_url=None, tracks=[])
            audio_config.init_custom("EQUALIZER", 1)
            audio_config.register_custom("EQUALIZER", eq_bands=[], eq_presets={})
            audio_config.init_custom(PlaylistScope.GLOBAL.value, 1)
            audio_config.register_custom(PlaylistScope.GLOBAL.value, **_playlist)
            audio_config.init_custom(PlaylistScope.GUILD.value, 2)
            audio_config.register_custom(PlaylistScope.GUILD.value, **_playlist)
            audio_config.init_custom(PlaylistScope.USER.value, 2)
            audio_config.register_custom(PlaylistScope.USER.value, **_playlist)
            audio_config.register_guild(**default_guild)
            audio_config.register_global(**default_global)
            audio_config.register_user(country_code=None)
            audio_db_conn = APSWConnectionWrapper(str(cog_data_path(self.bot.get_cog("Audio")) / "Audio.db"))
            playlist_api = PlaylistWrapper(self.bot, audio_config, audio_db_conn)
            await playlist_api.init()
        return audio_config, playlist_api
