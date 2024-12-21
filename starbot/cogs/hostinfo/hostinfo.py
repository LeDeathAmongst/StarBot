import socket
import discord
from discord import utils
from starbot.core import commands, data_manager, Config, checks, Config
from starbot.core.utils import embed
from Star-Utils import Cog, CogsUtils

from typing import List, Union, Optional

class HostInfo(Cog):
    def __init__(self, bot: Cog):
        self.bot: Cog = bot


    @commands.command()
    async def hostinfo(self, ctx: commands.Context):
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)

        formatted = f"{hostname}@{ip_addr}"
        embedded_response = discord.Embed(
            title=f"Host Info",
            type="rich",
            description=formatted
        )
        embedded_response = embed.randomize_colour(embedded_response)

        await ctx.send(embed=embedded_response)

