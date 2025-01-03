from starbot.core import Config, commands
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import humanize_list

from .util import EmojiConverter

old_tick = commands.context.TICK


class TickChanger(commands.Cog):
    """
    Change the emoji that gets reacted with when `await ctx.tick()`
    is called anywhere in the bot"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(None, 987654321, True, "Tick")
        self.config.register_global(tick_emoji=old_tick)

    async def red_delete_data_for_user(self, *, requester, user_id: int):
        """No data to delete"""

    @classmethod
    async def initialize(cls, bot: Red):
        s = cls(bot)
        emoji = await s.config.tick_emoji()
        commands.context.TICK = emoji
        return s

    def cog_unload(self):
        commands.context.TICK = old_tick

    @commands.command(name="settickemoji", aliases=["ste"])
    @commands.is_owner()
    async def ste(self, ctx: commands.Context, emoji: EmojiConverter):
        """
        Change the emoji that gets reacted with when `await ctx.tick()`
        is called anywhere in the bot"""
        await self.config.tick_emoji.set(str(emoji))
        commands.context.TICK = emoji
        await ctx.tick()
        await ctx.send(f"{emoji} is now the tick emoji.")

    @commands.command(name="gettickemoji", aliases=["gte"])
    @commands.is_owner()
    async def gte(self, ctx: commands.Context):
        """
        See which emoji is currently set to react"""
        return await ctx.send(f"Your current tick emoji is {await self.config.tick_emoji()}")
