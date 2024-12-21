import discord
from starbot.core import commands
from Star_Utils import Cog, CogsUtils

class ServerOwnerFinder(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def find_owner(self, ctx, server_id: int):
        """Find the owner of a server by its ID."""
        try:
            guild = self.bot.get_guild(server_id)
            if guild is None:
                await ctx.send("I couldn't find a server with that ID. Make sure I'm in that server and the ID is correct.")
                return

            owner = guild.owner
            if owner:
                await ctx.send(f"The owner of the server '{guild.name}' (ID: {guild.id}) is {owner.name}#{owner.discriminator} (ID: {owner.id})")
            else:
                await ctx.send(f"I found the server '{guild.name}', but I couldn't determine its owner.")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(ServerOwnerFinder(bot))
