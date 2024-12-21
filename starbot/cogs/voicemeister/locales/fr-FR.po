from typing import Any, ClassVar
import discord
from starbot.core import Config, commands
from starbot.core.bot import Red
from .star_lib import Perms
from .star_template import Template
from Star-Utils import Cog
import asyncio
from .c_voicemeister import VoiceMeisterCommands
from .c_voicemeisterset import VoiceMeisterSet
from .vminterface import VMInterface

class VoiceMeister(Cog):
    """Advanced voice channel control with join-to-create and more."""

    default_global_settings: ClassVar[dict[str, int]] = {"schema_version": 0}
    default_guild_settings: ClassVar[dict[str, bool | list[int]]] = {
        "admin_access": True,
        "mod_access": False,
        "bot_access": [],
    }
    default_voicemeister_source_settings: ClassVar[dict[str, int | str | None]] = {
        "dest_category_id": None,
        "room_type": "public",
        "legacy_text_channel": False,
        "text_channel_hint": None,
        "text_channel_topic": "",
        "channel_name_type": "username",
        "channel_name_format": "",
        "perm_owner_manage_channels": True,
        "perm_send_messages": True,
    }
    default_channel_settings: ClassVar[dict[str, int | list[int] | None]] = {
        "source_channel": None,
        "owner": None,
        "associated_text_channel": None,
        "denied": [],
    }

    def __init__(self, bot: Red):
        """Set up the cog."""
        super().__init__(bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(**self.default_global_settings)
        self.config.register_guild(**self.default_guild_settings)
        self.config.init_custom("VOICEMEISTER_SOURCE", 2)
        self.config.register_custom("VOICEMEISTER_SOURCE", **self.default_voicemeister_source_settings)
        self.config.register_channel(**self.default_channel_settings)
        self.voicemeister_commands = VoiceMeisterCommands(bot, VMInterface)
        self.voicemeister_set = VoiceMeisterSet(bot)
        self.vm_interface = VMInterface(bot)
        bot.add_cog(self.voicemeister_commands)
        bot.add_cog(self.voicemeister_set)

        self.template = Template()

    async def initialize(self) -> None:
        """Perform setup actions before loading cog."""
        await self._migrate_config()
        self.bot.loop.create_task(self._cleanup_voicemeisters())

    async def _migrate_config(self) -> None:
        """Perform some configuration migrations."""
        schema_version = await self.config.schema_version()

        if schema_version < 7:  # noqa: PLR2004
            # Remove auto text channels
            guild_dict = await self.config.all_guilds()
            for guild_id in guild_dict:
                await self.config.guild_from_id(guild_id).clear_raw("admin_access_text")
                await self.config.guild_from_id(guild_id).clear_raw("mod_access_text")
            all_voicemeister_sources = await self.config.custom("VOICEMEISTER_SOURCE").all()
            for guild_id, guild_voicemeister_sources in all_voicemeister_sources.items():
                for avc_id in guild_voicemeister_sources:
                    await self.config.custom(
                        "VOICEMEISTER_SOURCE", guild_id, avc_id
                    ).clear_raw("text_channel")
            await self.config.schema_version.set(7)

    async def _cleanup_voicemeisters(self) -> None:
        """Remove non-existent VoiceMeisters from the config."""
        await self.bot.wait_until_ready()
        voice_channel_dict = await self.config.all_channels()
        for voice_channel_id, voice_channel_settings in voice_channel_dict.items():
            voice_channel = self.bot.get_channel(voice_channel_id)
            if voice_channel:
                if isinstance(voice_channel, discord.VoiceChannel):
                    # Delete VoiceMeister if it is empty
                    await self._process_voicemeister_delete(voice_channel)
            else:
                # VoiceMeister has already been deleted, clean up legacy text channel if it still exists
                legacy_text_channel = await self.get_voicemeister_legacy_text_channel(
                    voice_channel_settings["associated_text_channel"]
                )
                if legacy_text_channel:
                    await legacy_text_channel.delete(
                        reason="VoiceMeister: Associated voice channel deleted."
                    )
                await self.config.channel_from_id(voice_channel_id).clear()

    async def _process_voicemeister_create(
        self,
        voicemeister_source: discord.VoiceChannel,
        voicemeister_source_config: dict[str, Any],
        member: discord.Member,
    ) -> None:
        """Create a voice channel for a member in a VoiceMeister Source channel."""
        # Check perms for guild, source, and dest
        guild = voicemeister_source.guild
        dest_category = guild.get_channel(voicemeister_source_config["dest_category_id"])
        if not isinstance(dest_category, discord.CategoryChannel):
            return

        # Generate channel name
        taken_channel_names = [
            voice_channel.name for voice_channel in dest_category.voice_channels
        ]
        new_channel_name = self._generate_channel_name(
            voicemeister_source_config, member, taken_channel_names
        )

        # Generate overwrites
        perms = Perms()
        dest_perms = dest_category.permissions_for(dest_category.guild.me)
        source_overwrites = (
            voicemeister_source.overwrites if voicemeister_source.overwrites else {}
        )
        member_roles = self.get_member_roles(voicemeister_source)
        for target, permissions in source_overwrites.items():
            # We can't put manage_roles in overwrites, so just get rid of it
            permissions.update(manage_roles=None)
            # Check each permission for each overwrite target to make sure the bot has it allowed in the dest category
            failed_checks = {}
            for name, value in permissions:
                if value is not None:
                    permission_check_result = getattr(dest_perms, name)
                    if not permission_check_result:
                        # If the bot doesn't have the permission allowed in the dest category, just ignore it. Too bad!
                        failed_checks[name] = None
            if failed_checks:
                permissions.update(**failed_checks)
            perms.overwrite(target, permissions)
            if member_roles and target in member_roles:
                # If we have member roles and this target is one, apply VoiceMeister type permissions
                perms.update(target, voicemeister_source_config["perms"]["access"])

        # Update overwrites for default role to account for VoiceMeister type
        if member_roles:
            perms.update(guild.default_role, voicemeister_source_config["perms"]["deny"])
        else:
            perms.update(guild.default_role, voicemeister_source_config["perms"]["access"])

        # Bot overwrites
        perms.update(guild.me, self.perms_bot_dest)

        # VoiceMeister Owner overwrites
        if voicemeister_source_config["room_type"] != "server":
            perms.update(member, voicemeister_source_config["perms"]["owner"])

        # Admin/moderator/bot overwrites
        # Add bot roles to be allowed
        additional_allowed_roles = await self.get_bot_roles(guild)
        if await self.config.guild(guild).mod_access():
            # Add mod roles to be allowed
            additional_allowed_roles += await self.bot.get_mod_roles(guild)
        if await self.config.guild(guild).admin_access():
            # Add admin roles to be allowed
            additional_allowed_roles += await self.bot.get_admin_roles(guild)
        for role in additional_allowed_roles:
            # Add all the mod/admin roles, if required
            perms.update(role, voicemeister_source_config["perms"]["allow"])

        # Create new VoiceMeister
        new_voice_channel = await guild.create_voice_channel(
            name=new_channel_name,
            category=dest_category,
            reason="VoiceMeister: New VoiceMeister needed.",
            overwrites=perms.overwrites if perms.overwrites else {},
            bitrate=min(voicemeister_source.bitrate, int(guild.bitrate_limit)),
            user_limit=voicemeister_source.user_limit,
        )
        await self.config.channel(new_voice_channel).source_channel.set(
            voicemeister_source.id
        )
        if voicemeister_source_config["room_type"] != "server":
            await self.config.channel(new_voice_channel).owner.set(member.id)
        try:
            await member.move_to(
                new_voice_channel, reason="VoiceMeister: Move user to new VoiceMeister."
            )
        except discord.HTTPException:
            await self._process_voicemeister_delete(new_voice_channel)
            return

        # Create optional legacy text channel
        new_legacy_text_channel = None
        if voicemeister_source_config["legacy_text_channel"]:
            # Sanity check on required permissions
            for perm_name in self.perms_bot_dest_legacy_text:
                if not getattr(dest_perms, perm_name):
                    return
            # Generate overwrites
            perms = Perms()
            perms.update(guild.me, self.perms_bot_dest_legacy_text)
            perms.update(guild.default_role, self.perms_legacy_text_deny)
            if voicemeister_source_config["room_type"] != "server":
                perms.update(member, self.perms_voicemeister_owner_legacy_text)
            else:
                perms.update(member, self.perms_legacy_text_allow)
            # Admin/moderator overwrites
            additional_allowed_roles_text = []
            if await self.config.guild(guild).mod_access():
                # Add mod roles to be allowed
                additional_allowed_roles_text += await self.bot.get_mod_roles(guild)
            if await self.config.guild(guild).admin_access():
                # Add admin roles to be allowed
                additional_allowed_roles_text += await self.bot.get_admin_roles(guild)
            for role in additional_allowed_roles_text:
                # Add all the mod/admin roles, if required
                perms.update(role, self.perms_legacy_text_allow)
            # Create text channel
            text_channel_topic = self.template.render(
                voicemeister_source_config["text_channel_topic"],
                self.get_template_data(member),
            )
            new_legacy_text_channel = await guild.create_text_channel(
                name=new_channel_name.replace("'s ", " "),
                category=dest_category,
                topic=text_channel_topic,
                reason="VoiceMeister: New legacy text channel needed.",
                overwrites=perms.overwrites if perms.overwrites else {},
            )

            await self.config.channel(new_voice_channel).associated_text_channel.set(
                new_legacy_text_channel.id
            )

        # Send text chat hint if enabled
        if voicemeister_source_config["text_channel_hint"]:
            with suppress(RuntimeError):
                hint = self.template.render(
                    voicemeister_source_config["text_channel_hint"],
                    self.get_template_data(member),
                )
                if hint:
                    if new_legacy_text_channel:
                        await new_legacy_text_channel.send(hint)
                    else:
                        await new_voice_channel.send(hint)

    @staticmethod
    async def _process_voicemeister_delete(voice_channel: discord.VoiceChannel) -> bool:
        """Delete VoiceMeister if empty."""
        if (
            not voice_channel.members
            and voice_channel.permissions_for(voice_channel.guild.me).manage_channels
        ):
            with suppress(
                discord.NotFound
            ):  # Sometimes this happens when the user manually deletes their channel
                await voice_channel.delete(reason="VoiceMeister: Channel empty.")
                return True
        return False

    def _generate_channel_name(
        self,
        voicemeister_source_config: dict,
        member: discord.Member,
        taken_channel_names: list,
    ) -> str:
        """Return a channel name with an incrementing number appended to it, based on a formatting string."""
        template = None
        if voicemeister_source_config["channel_name_type"] in channel_name_template:
            template = channel_name_template[
                voicemeister_source_config["channel_name_type"]
            ]
        elif voicemeister_source_config["channel_name_type"] == "custom":
            template = voicemeister_source_config["channel_name_format"]
        template = template or channel_name_template["username"]

        data = self.get_template_data(member)
        new_channel_name = None
        attempt = 1
        with suppress(RuntimeError):
            new_channel_name = self.format_template_room_name(template, data, attempt)

        if not new_channel_name:
            # Either the user screwed with the template, or the template returned nothing. Use a default one instead.
            template = channel_name_template["username"]
            new_channel_name = self.format_template_room_name(template, data, attempt)

        # Check for duplicate names
        attempted_channel_names = []
        while (
            new_channel_name in taken_channel_names
            and new_channel_name not in attempted_channel_names
        ):
            attempt += 1
            attempted_channel_names.append(new_channel_name)
            new_channel_name = self.format_template_room_name(template, data, attempt)
        return new_channel_name

    @staticmethod
    def get_template_data(member: discord.Member | discord.User) -> dict[str, str]:
        """Return a dict of template data based on a member."""
        data = {"username": member.display_name, "mention": member.mention}
        if isinstance(member, discord.Member):
            for activity in member.activities:
                if activity.type == discord.ActivityType.playing:
                    data["game"] = activity.name or ""
                    break
        return data

    def format_template_room_name(self, template: str, data: dict, num: int = 1) -> str:
        """Return a formatted channel name, taking into account the 100 character channel name limit."""
        nums = {"dupenum": num}
        return self.template.render(
            template=template,
            data={**nums, **data},
        )[:100].strip()

    async def get_all_voicemeister_source_configs(
        self, guild: discord.Guild
    ) -> dict[int, dict[str, Any]]:
        """Return a dict of all voicemeister source configs, cleaning up any invalid ones."""
        unsorted_list_of_configs = []
        configs = await self.config.custom(
            "VOICEMEISTER_SOURCE", str(guild.id)
        ).all()  # Does NOT return default values
        for channel_id in configs:
            channel = guild.get_channel(int(channel_id))
            if not isinstance(channel, discord.VoiceChannel):
                continue
            config = await self.get_voicemeister_source_config(channel)
            if config:
                unsorted_list_of_configs.append((channel.position, channel_id, config))
            else:
                await self.config.custom(
                    "VOICEMEISTER_SOURCE", str(guild.id), channel_id
                ).clear()
        result = {}
        for _, channel_id, config in sorted(
            unsorted_list_of_configs, key=lambda source_config: source_config[0]
        ):
            result[int(channel_id)] = config
        return result

    async def get_voicemeister_source_config(
        self, voicemeister_source: discord.VoiceChannel | discord.abc.GuildChannel | None
    ) -> dict[str, Any] | None:
        """Return the config for a voicemeister source, or None if not set up yet."""
        if not voicemeister_source:
            return None
        if not isinstance(voicemeister_source, discord.VoiceChannel):
            return None
        config = await self.config.custom(
            "VOICEMEISTER_SOURCE", str(voicemeister_source.guild.id), str(voicemeister_source.id)
        ).all()  # Returns default values
        if not config["dest_category_id"]:
            return None

        perms = {
            "allow": {
                "view_channel": True,
                "connect": True,
                "send_messages": config["perm_send_messages"],
            },
            "lock": {"view_channel": True, "connect": False, "send_messages": False},
            "deny": {"view_channel": False, "connect": False, "send_messages": False},
        }
        perms["owner"] = {
            **perms["allow"],
            "manage_channels": True if config["perm_owner_manage_channels"] else None,
            "manage_messages": True,
        }
        if config["room_type"] == "private":
            perms["access"] = perms["deny"]
        elif config["room_type"] == "locked":
            perms["access"] = perms["lock"]
        else:
            perms["access"] = perms["allow"]

        config["perms"] = perms
        return config

    async def get_voicemeister_info(
        self, voicemeister: discord.VoiceChannel | None
    ) -> dict[str, Any] | None:
        """Get info for a VoiceMeister, or None if the voice channel isn't a VoiceMeister."""
        if not voicemeister:
            return None
        if not await self.config.channel(voicemeister).source_channel():
            return None
        return await self.config.channel(voicemeister).all()

    async def get_voicemeister_legacy_text_channel(
        self, voicemeister: discord.VoiceChannel | int | None
    ) -> discord.TextChannel | None:
        """Get the VoiceMeister legacy test channel, if it exists and we have manage channels permission."""
        if isinstance(voicemeister, discord.VoiceChannel):
            voicemeister = voicemeister.id
        if not voicemeister:
            return None
        legacy_text_channel_id = await self.config.channel_from_id(
            voicemeister
        ).associated_text_channel()
        legacy_text_channel = (
            self.bot.get_channel(legacy_text_channel_id)
            if legacy_text_channel_id
            else None
        )
        if (
            isinstance(legacy_text_channel, discord.TextChannel)
            and legacy_text_channel.permissions_for(
                legacy_text_channel.guild.me
            ).manage_channels
        ):
            return legacy_text_channel
        return None

    def get_member_roles(
        self, voicemeister_source: discord.VoiceChannel
    ) -> list[discord.Role]:
        """Get member roles set on a VoiceMeister Source."""
        member_roles = []
        # If @everyone is allowed to connect to the source channel, there are no member roles
        if not self.check_if_member_or_role_allowed(
            voicemeister_source,
            voicemeister_source.guild.default_role,
        ):
            # If it isn't allowed, then member roles are being used
            member_roles.extend(
                role
                for role, overwrite in voicemeister_source.overwrites.items()
                if isinstance(role, discord.Role)
                and role != voicemeister_source.guild.default_role
                and overwrite.pair()[0].connect
            )
        return member_roles

    async def get_bot_roles(self, guild: discord.Guild) -> list[discord.Role]:
        """Get the additional bot roles that are added to each VoiceMeister."""
        bot_roles = []
        bot_role_ids = []
        some_roles_were_not_found = False
        for bot_role_id in await self.config.guild(guild).bot_access():
            bot_role = guild.get_role(bot_role_id)
            if bot_role:
                bot_roles.append(bot_role)
                bot_role_ids.append(bot_role_id)
            else:
                some_roles_were_not_found = True
        if some_roles_were_not_found:
            # Update the bot role list to remove nonexistent roles
            await self.config.guild(guild).bot_access.set(bot_role_ids)
        return bot_roles

    @staticmethod
    def check_if_member_or_role_allowed(
        channel: discord.VoiceChannel,
        member_or_role: discord.Member | discord.Role,
    ) -> bool:
        """Check if a member/role is allowed to connect to a voice channel.

        Doesn't matter if they can't see it, it ONLY checks the connect permission.
        Mostly copied from https://github.com/Rapptz/discord.py/blob/master/discord/abc.py:GuildChannel.permissions_for()
        I needed the logic except the "if not base.read_messages:" part that removed all permissions.
        """
        if channel.guild.owner_id == member_or_role.id:
            return True

        default_role = channel.guild.default_role
        base = discord.Permissions(default_role.permissions.value)

        # Handle the role case first
        if isinstance(member_or_role, discord.Role):
            base.value |= member_or_role.permissions.value

            if base.administrator:
                return True

            # Apply @everyone allow/deny first since it's special
            with suppress(KeyError):
                default_allow, default_deny = channel.overwrites[default_role].pair()
                base.handle_overwrite(
                    allow=default_allow.value, deny=default_deny.value
                )

            if member_or_role.is_default():
                return base.connect

            with suppress(KeyError):
                role_allow, role_deny = channel.overwrites[member_or_role].pair()
                base.handle_overwrite(allow=role_allow.value, deny=role_deny.value)

            return base.connect

        member_roles = member_or_role.roles

        # Apply guild roles that the member has.
        for role in member_roles:
            base.value |= role.permissions.value

        # Guild-wide Administrator -> True for everything
        # Bypass all channel-specific overrides
        if base.administrator:
            return True

        # Apply @everyone allow/deny first since it's special
        with suppress(KeyError):
            default_allow, default_deny = channel.overwrites[default_role].pair()
            base.handle_overwrite(allow=default_allow.value, deny=default_deny.value)

        allows = 0
        denies = 0

        # Apply channel specific role permission overwrites
        for role, overwrite in channel.overwrites.items():
            if (
                isinstance(role, discord.Role)
                and role != default_role
                and role in member_roles
            ):
                allows |= overwrite.pair()[0].value
                denies |= overwrite.pair()[1].value

        base.handle_overwrite(allow=allows, deny=denies)

        # Apply member specific permission overwrites
        with suppress(KeyError):
            member_allow, member_deny = channel.overwrites[member_or_role].pair()
            base.handle_overwrite(allow=member_allow.value, deny=member_deny.value)

        if member_or_role.is_timed_out():
            # Timeout leads to every permission except VIEW_CHANNEL and READ_MESSAGE_HISTORY
            # being explicitly denied
            return False

        return base.connect

async def setup(bot: commands.Bot):
    """Setup function to add the main VoiceMeister cog to the bot."""
    await bot.add_cog(VoiceMeister(bot))
