from typing import Literal
from Star-Utils import Cog, CogsUtils

from starbot.core import commands
from starbot.core.bot import Red

from .utils import BoardMenu

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]

# Notes:
# If something doesn't edit the board, it goes into utils, else it's in the game class


class Snake(Cog):
    """
    A simple Snake Game
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot

    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.command()
    async def snake(self, ctx):
        menu = BoardMenu(ctx.author.display_name, clear_reactions_after=True)
        await menu.start(ctx, wait=True)
