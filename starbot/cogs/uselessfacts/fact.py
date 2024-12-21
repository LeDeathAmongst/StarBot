import discord
from starbot.core import commands
import requests
from Star-Utils import Cog
class UselessFacts(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'

    @commands.command()
    async def uselessfact(self, ctx):
        """Get a random useless fact!"""
        try:
            response = requests.get(self.api_url)
            if response.status_code == requests.codes.ok:
                data = response.json()
                
                fact_text = data['text']
                fact_source = data['source']
                fact_source_url = data['source_url']

                embed = discord.Embed(title="Useless Fact", description=fact_text, color=await ctx.embed_color())
                
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Error: {response.status_code}")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
