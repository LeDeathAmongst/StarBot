from starbot.core import commands, Config
from starbot.core.bot import Red
from starbot.core.utils import AsyncIter
from .config import Settings
import re
import aiohttp
from collections import namedtuple
from typing import Optional, Literal
import discord
from humanize import intcomma
from starbot.core.i18n import Translator, cog_i18n
from Star-Utils import Cog
_ = Translator("RYDCog", __file__)

votes_tuple = namedtuple("Votes", ['video_id', 'likes', 'dislikes'])


class ChannelScan:
    DISABLED = 0
    ENABLED = 1
    WHITELISTED = 2


@cog_i18n(_)
class RYD(Cog):
    """'Return YouTube Dislikes' cog"""
    def __init__(self, bot: Red):
        self.bot: Red = bot
        super().__init__(bot)
        self.config = Config.get_conf(self, identifier=1984027022015)  # RIP Nemtsov, Fuck Kadyrov
        default_global = {
            "enabled_scan": True,
            "ignore_max": Settings.IGNORE_MAX_REACHED  # True by default
        }
        default_guild = {
            "enabled_scan": True,
            "whitelist_mode": False
        }
        default_member = {
            "enabled_scan": True
        }
        default_channel = {
            "enabled_scan": ChannelScan.ENABLED
        }
        self.config.register_global(**default_global)
        self.config.register_guild(**default_guild)
        self.config.register_member(**default_member)
        self.config.register_channel(**default_channel)

    async def red_delete_data_for_user(
        self,
        *,
        requester: Literal["discord_deleted_user", "owner", "user", "user_strict"],
        user_id: int,
    ):
        """Tnx for bobloy from Fox-V3
        (https://github.com/bobloy/Fox-V3/blob/db3ce301220604d537ea68a7fee10a20f4d50230/lseen/lseen.py)"""
        all_members = await self.config.all_members()
        async for guild_id, guild_data in AsyncIter(all_members.items(), steps=100):
            if user_id in guild_data:
                await self.config.member_from_ids(guild_id, user_id).clear()


    @staticmethod
    def find_video_ids(text):
        res_ids = list()
        for match in re.finditer(Settings.YT_ID_REGEX_TEXT, text):
            if (video_id := match.groupdict().get("videoId")) is not None:
                res_ids.append(video_id)
        return res_ids

    @staticmethod
    async def get_votes(video_id) -> Optional[votes_tuple]:
        async with aiohttp.ClientSession(headers=Settings.REQUEST_HEADERS) as session:
            async with session.get(Settings.VOTES_URL, params={"videoId": video_id}) as response:
                if response.status in (404, 400):
                    return None
                json_resp = await response.json()
        return votes_tuple(json_resp['id'], json_resp['likes'], json_resp['dislikes'])

    @staticmethod
    def get_readable_votes_pbar(votes: votes_tuple, per_ratio=None,
                                ratio_full=None, ratio_empty=None,
                                display_like=None, display_dislike=None):
        if per_ratio is None:
            per_ratio = Settings.DISPLAY_PER_RATIO
        if ratio_full is None:
            ratio_full = Settings.DISPLAY_RATIO_FULL
        if ratio_empty is None:
            ratio_empty = Settings.DISPLAY_RATIO_EMPTY
        if display_like is None:
            display_like = Settings.DISPLAY_LIKE
        if display_dislike is None:
            display_dislike = Settings.DISPLAY_DISLIKE
        result = "{like} {likes} `{ratio}` {dislikes} {dislike}"
        size = per_ratio * 2
        ratio_full_len = round((votes.likes / (votes.likes + votes.dislikes)) * size)
        ratio = ratio_full * ratio_full_len + ratio_empty * (size - ratio_full_len)
        result = result.format(like=display_like, dislike=display_dislike,
                               ratio=ratio,
                               likes=intcomma(votes.likes), dislikes=intcomma(votes.dislikes))
        return result

    async def get_readable_line_votes_by_ctx(self, ctx, votes: votes_tuple):
        return self.get_readable_votes_pbar(votes)

    @commands.command(aliases=("returnyoutubedislike", "ytdislikes"))
    async def ryd(self, ctx, url):
        """Insert YouTube video url or id as argument to get dislikes count"""
        if not (video_id := self.find_video_ids(url)):
            video_id = [url]
        try:
            votes = await self.get_votes(video_id[0])
        except IndexError:
            votes = None
        if votes is None:
            return None
        msg = await self.get_readable_line_votes_by_ctx(ctx, votes)
        return await ctx.reply(msg)

    async def should_ignore(self, message: discord.Message, *, edit: bool = False) -> bool:
        """What messages should be ignored?
        - If it's not new message, and just edit
        - If scan disabled globally
        - If DM
        - If cog disabled in guild
        - If scan disabled in guild
        - If scan disabled in channel, or whitelist mode is on and it's not whitelisted
        - If member disabled scan for himself"""
        if edit:
            return True
        if not await self.config.enabled_scan():
            return True
        guild = message.guild
        if guild is None or message.author.bot:
            return True
        if await self.bot.cog_disabled_in_guild(self, guild):
            return True
        if not await self.config.guild(guild).enabled_scan():
            return True
        whitelist_mode = await self.config.guild(guild).whitelist_mode()
        channel_scan = await self.config.channel(message.channel).enabled_scan()
        if whitelist_mode:
            if channel_scan != ChannelScan.WHITELISTED:
                return True
        else:
            if channel_scan == ChannelScan.DISABLED:
                return True
        if not await self.config.member(message.author).enabled_scan():
            return True
        prefix = await self.bot.get_prefix(message)
        if isinstance(prefix, list):
            prefix = prefix[0]  # XXX: needs to be fixed
        if any([message.content.startswith(prefix + x) for x in ("ryd", "returnyoutubedislike", "ytdislikes")]):
            return True
        return False

    @Cog.listener()
    async def on_message(self, message: discord.Message, *, edit: bool = False) -> None:
        if await self.should_ignore(message, edit=edit):
            return
        if not (video_ids := self.find_video_ids(message.content)):
            return
        if len(video_ids) > Settings.MAX_DISPLAYED:
            if await self.config.ignore_max():
                return
            video_ids = video_ids[:Settings.MAX_DISPLAYED]
        lines = list()
        for video_id in video_ids:
            votes = await self.get_votes(video_id)
            lines.append(await self.get_readable_line_votes_by_ctx(await self.bot.get_context(message), votes))
        return await message.reply("\n".join(lines))

    @commands.group(name="ryd-config")
    async def ryd_config(self, ctx):
        """Change settings of RYD Cog"""
        pass

    @ryd_config.group(name="global")
    @commands.is_owner()
    async def config_global(self, ctx):
        pass

    @config_global.command(name="disable")
    async def global_disable_toggle(self, ctx):
        """Disable/Enable message scanning for the bot"""
        old_value = await self.config.enabled_scan()
        new_value = not old_value
        await self.config.enabled_scan.set(new_value)
        return await ctx.reply(_("Message scanning is {} now").format({True: _("Enabled"), False: _("Disabled")}[new_value]))

    @ryd_config.group(name="me")
    @commands.guild_only()
    async def config_member(self, ctx):
        pass

    @config_member.command(name="disable")
    async def member_disable_toggle(self, ctx):
        """Disable/Enable message scanning for the specific person"""
        old_value = await self.config.member(ctx.author).enabled_scan()
        new_value = not old_value
        await self.config.member(ctx.author).enabled_scan.set(new_value)
        return await ctx.reply(_("Message scanning is {} now").format({True: _("Enabled"), False: _("Disabled")}[new_value]))

    @ryd_config.group("guild")
    @commands.admin()
    @commands.guild_only()
    async def config_guild(self, ctx):
        pass

    @config_guild.command(name="disable")
    async def guild_disable_toggle(self, ctx):
        """Disable/Enable message scanning for guild"""
        old_value = await self.config.guild(ctx.guild).enabled_scan()
        new_value = not old_value
        await self.config.guild(ctx.guild).enabled_scan.set(new_value)
        return await ctx.reply(_("Message scanning is {} now").format({True: _("Enabled"), False: _("Disabled")}[new_value]))

    @config_guild.command(name="whitelist")
    async def guild_whitelist_mode_toggle(self, ctx):
        """Enable/Disable whitelist mode for guild"""
        old_value = await self.config.guild(ctx.guild).whitelist_mode()
        new_value = not old_value
        await self.config.guild(ctx.guild).whitelist_mode.set(new_value)
        return await ctx.reply(_("Whitelist mode is {} now").format({True: _("Enabled"), False: _("Disabled")}[new_value]))

    @config_guild.command(name="channel")
    async def channel_disable_toggle(self, ctx, channel: discord.TextChannel = None):
        """Disable/Enable message scanning for channel. Even in whitelist mode"""
        if channel is None:
            channel = ctx.channel
        whitelist_mode = await self.config.guild(ctx.guild).whitelist_mode()
        old_value = await self.config.channel(channel).enabled_scan()
        if old_value in (ChannelScan.ENABLED, ChannelScan.WHITELISTED) and not whitelist_mode:
            new_value = ChannelScan.DISABLED
            str_new = _("Disabled")
        elif old_value == ChannelScan.WHITELISTED and whitelist_mode:
            new_value = ChannelScan.ENABLED
            str_new = _("not Whitelisted")
        elif old_value == ChannelScan.DISABLED and not whitelist_mode:
            new_value = ChannelScan.ENABLED
            str_new = _("Enabled")
        elif old_value in (ChannelScan.DISABLED, ChannelScan.ENABLED) and whitelist_mode:
            new_value = ChannelScan.WHITELISTED
            str_new = _("Whitelisted")
        else:
            return
        await self.config.channel(channel).enabled_scan.set(new_value)
        return await ctx.reply(_("Message scanning is {} now").format(str_new))
