import discord
from starbot.core import commands, Config
from typing import Optional
from Star-Utils import Cog, CogsUtils

class SMC(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_guild = {"channel_id": None}
        self.config.register_guild(**default_guild)
        self.logs = CogsUtils.get_logger("SCM")


    @commands.group()
    @commands.admin_or_permissions(manage_guild=True)
    async def sm(self, ctx):
        """Commands for managing the single message channel."""
        pass

    @sm.command()
    async def setchannel(self, ctx, channel: discord.TextChannel):
        """Set the channel for single message mode."""
        await self.config.guild(ctx.guild).channel_id.set(channel.id)
        await ctx.send(f"Single message channel set to {channel.mention}")

    @sm.command()
    async def disable(self, ctx):
        """Disable the single message channel feature."""
        await self.config.guild(ctx.guild).channel_id.set(None)
        await ctx.send("Single message channel feature disabled.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        channel_id = await self.config.guild(message.guild).channel_id()
        if channel_id and message.channel.id == channel_id:
            async for msg in message.channel.history(limit=None):
                if msg.id != message.id:
                    await msg.delete()
