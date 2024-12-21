import discord
from starbot.core import commands, Config
from starbot.core.utils.chat_formatting import humanize_number
from datetime import datetime
from Star-Utils import Cog, CogsUtils

class AutoDelete(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        self.config.register_guild(auto_delete=False)
        self.config.register_global(log_channel_id=None)

    @commands.group(name="autodelete", invoke_without_command=True)
    async def autodelete(self, ctx):
        """Manage the AutoDelete settings."""
        await ctx.send_help(ctx.command)

    @autodelete.command(name="toggle")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def autodelete_toggle(self, ctx):
        """Toggle the auto-delete feature for this server."""
        auto_delete = await self.config.guild(ctx.guild).auto_delete()
        await self.config.guild(ctx.guild).auto_delete.set(not auto_delete)
        status = "enabled" if not auto_delete else "disabled"
        await ctx.send(f"Auto-delete feature has been {status} for this server.")

    @autodelete.command(name="logchannel")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def autodelete_logchannel(self, ctx, channel: discord.TextChannel):
        """Set the log channel for auto-delete messages."""
        await self.config.log_channel_id.set(channel.id)
        await ctx.send(f"Log channel for auto-delete messages has been set to {channel.mention}.")

    @commands.commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        auto_delete = await self.config.guild(member.guild).auto_delete()
        if not auto_delete:
            return

        log_channel_id = await self.config.log_channel_id()
        log_channel = self.bot.get_channel(log_channel_id) if log_channel_id else None

        total_deleted = 0
        channel_count = 0
        category_count = 0
        channels_processed = set()

        for channel in member.guild.text_channels:
            if not channel.permissions_for(member.guild.me).manage_messages:
                continue

            deleted = await self._delete_messages_from_user(channel, member)
            if deleted > 0:
                total_deleted += deleted
                channel_count += 1
                if channel.category and channel.category.id not in channels_processed:
                    category_count += 1
                    channels_processed.add(channel.category.id)

        if log_channel:
            embed = discord.Embed(title="Auto-Deleted Messages", color=discord.Color.red())
            embed.description = (
                f"Deleted {humanize_number(total_deleted)} messages in {humanize_number(channel_count)} channels\n"
                f"Deleted {humanize_number(total_deleted)} messages in {humanize_number(category_count)} categories\n"
                f"Deleted {humanize_number(total_deleted)} messages from {member.mention} ({member})"
            )
            embed.set_footer(text=f"Deleted by {self.bot.user.name} at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
            await log_channel.send(embed=embed)

    async def _delete_messages_from_user(self, channel: discord.TextChannel, user: discord.User):
        deleted = 0
        async for message in channel.history(limit=None):
            if message.author.id == user.id:
                await message.delete()
                deleted += 1
        return deleted
