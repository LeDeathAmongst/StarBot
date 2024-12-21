from typing import Optional

import discord
from starbot.core import commands
from Star-Utils import Cog, CogsUtils
from starbot.core.bot import Red


class HidePing(Cog):
    """
    Hidden pings cuz its cool ig.
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.logs = CogsUtils.get_logger("HidePing")

    @commands.command(name="hideping")
    @commands.mod_or_permissions(manage_messages=True)
    async def hideping(
        self, ctx: commands.Context, member: discord.Member, *, message: Optional[str]
    ):
        """
        Speak a message using a hidden ping!
        """
        if message is None:
            message = "ㅤ"
        msg = f"{message} " + "||\u200d" * 598 + f"<@{member.id}>"
        if len(msg) > 2000:
            return await ctx.send("Your message is too long.")
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            await ctx.tick()
        except discord.NotFound:  # when used with mock
            pass
        await ctx.send(msg)

    async def red_get_data_for_user(self, *, user_id: int):
        # this cog does not store any data
        return {}

    async def red_delete_data_for_user(self, *, requester, user_id: int) -> None:
        # this cog does not store any data
        pass
