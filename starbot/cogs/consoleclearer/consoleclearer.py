import datetime
import os
from Star-Utils import Cog, CogsUtils

from starbot.core import commands
from starbot.core.bot import Red


class ConsoleClearer(Cog):
    """Clear your console."""

        
    def __init__(self, bot: Red):
        self.bot = bot


    async def red_delete_data_for_user(self, **kwargs):
        return

    @commands.is_owner()
    @commands.command(aliases=["cleanconsole", "consoleclear", "consoleclean"])
    async def clearconsole(self, ctx: commands.Context):
        """
        Completely clears [botname]'s console.
        """
        os.system("clear" if os.name == "posix" else "cls")
        print(
            f"Red console cleared | {datetime.datetime.utcnow().strftime('%b %d %Y %H:%M:%S')} (UTC)"
        )
        await ctx.send("Red console cleared.")
