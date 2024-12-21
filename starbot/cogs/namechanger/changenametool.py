from Star-Utils import Cog
from starbot.core import commands
import discord

class NameChanger(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command()
    async def changename(self, ctx, *, new_name: str):
        """
        Change your nickname using the bot!
        """
        try:
            await ctx.author.edit(nick=new_name)
            await ctx.send(f"Your nickname has been changed to '{new_name}'")
        except discord.Forbidden:
            await ctx.send("Sorry, I can't change your nickname because my role is below yours in the role hierarchy.")
