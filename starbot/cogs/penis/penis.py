import discord
import random
from starbot.core import commands
from starbot.core.utils.chat_formatting import pagify
from Star-Utils import Cog, CogsUtils


class Penis(Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("Penis")
    """Penis related commands."""

    @commands.command()
    async def penis(self, ctx, *users: discord.Member):
        """Detects user's penis length

        This is 100% accurate.
        Enter multiple users for an accurate comparison!"""
        if not users:
            await ctx.send_help()
            return

        dongs = {}
        msg = ""
        state = random.getstate()

        for user in users:
            random.seed(str(user.id))

            if ctx.bot.user.id == user.id:
                length = 50
            else:
                length = random.randint(0, 30)

            dongs[user] = "8{}D".format("=" * length)

        random.setstate(state)
        dongs = sorted(dongs.items(), key=lambda x: x[1])

        for user, dong in dongs:
            msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)

        for page in pagify(msg):
            await ctx.send(page)
