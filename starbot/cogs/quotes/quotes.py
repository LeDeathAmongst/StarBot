import ssl
import aiohttp

from starbot.core import commands
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import bold, warning


class Quotes(commands.Cog):
    """Get a random quote."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.api = "https://zenquotes.io/api/random"
        self.session = aiohttp.ClientSession()

    async def cog_unload(self):
        await self.session.close()

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    @commands.command()
    async def quote(self, ctx: commands.Context):
        """Get a random quote."""
        await ctx.typing()
        async with self.session.get(self.api, ssl=False) as r:
            content = (await r.json())[0]
        await ctx.send(f"From **{content['a']}**\n{content['q']}")
