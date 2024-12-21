import discord
from starbot.core import commands
from Star-Utils import Cog, CogsUtils


class LockUnlock(Cog):
    """A cog to lock and unlock all channels."""

    def __init__(self, bot):
        self.bot = bot
#        self.log - CogsUtils.get_logger("LockUnlock")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockall(self, ctx):
        """Lock all channels for all users without admin permissions."""
        guild = ctx.guild
        for channel in guild.channels:
            if isinstance(channel, (discord.TextChannel, discord.VoiceChannel)):
                await channel.set_permissions(guild.default_role, send_messages=False, speak=False)
            elif isinstance(channel, discord.CategoryChannel):
                for child_channel in channel.channels:
                    if isinstance(child_channel, discord.TextChannel):
                        await child_channel.set_permissions(guild.default_role, send_messages=False)
                    elif isinstance(child_channel, discord.VoiceChannel):
                        await child_channel.set_permissions(guild.default_role, speak=False)

        await ctx.send("All channels have been locked.")

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlockall(self, ctx):
        """Unlock all channels for all users without admin permissions."""
        guild = ctx.guild
        for channel in guild.channels:
            if isinstance(channel, (discord.TextChannel, discord.VoiceChannel)):
                await channel.set_permissions(guild.default_role, send_messages=True, speak=True)
            elif isinstance(channel, discord.CategoryChannel):
                for child_channel in channel.channels:
                    if isinstance(child_channel, discord.TextChannel):
                        await child_channel.set_permissions(guild.default_role, send_messages=True)
                    elif isinstance(child_channel, discord.VoiceChannel):
                        await child_channel.set_permissions(guild.default_role, speak=True)

        await ctx.send("All channels have been unlocked.")

async def setup(bot):
    await bot.add_cog(LockUnlock(bot))
