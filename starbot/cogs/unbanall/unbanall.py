import discord
from starbot.core import commands
from Star-Utils import Cog, CogsUtils

from typing import Tuple

class UnbanAll(Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def get_ban_limit(ctx: commands.Context, limit: int) -> Tuple[int, list]:
        async with ctx.typing():
            limit = min(limit, 500000)  # Set the limit to 50000
            bans = [entry async for entry in ctx.guild.bans(limit=limit)]
            return len(bans), bans

    @commands.command()
    @commands.guild_only()
    @commands.admin()
    async def unbanall(self, ctx):
        """Unban all users from the server."""
        num_bans, banned_users = await self.get_ban_limit(ctx, 500000)

        # Unban all banned users
        async with ctx.typing():
            for entry in banned_users:
                user = entry.user
                await ctx.guild.unban(user, reason="Unban all command")

            await ctx.send(f"Successfully unbanned {num_bans} users.")
