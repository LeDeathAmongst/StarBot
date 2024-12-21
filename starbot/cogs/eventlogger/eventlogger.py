from Star-Utils import Cog, Settings, CogsUtils
from starbot.core import commands, Config
from starbot.core.bot import Red
from starbot.core.i18n import Translator, cog_i18n
import discord
import typing
from typing import Union, List
import asyncio
from datetime import datetime
from .dashboard_integration import DashboardIntegration


_ = Translator('EventLogger', __file__)

@cog_i18n(_)
class EventLogger(DashboardIntegration, Cog):
    """Cog to log various Discord events"""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("EventLogger")
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)

        settings_dict = {
                "integration_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging integration creation events.",
                },
                "integration_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging integration deletion events.",
                },
                "integration_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging integration update events.",
                },
                "guild_channel_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel creation events.",
                },
                "guild_channel_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel deletion events.",
                },
                "guild_channel_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel update events.",
                },
                "guild_channel_pins_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging channel pins update events.",
                },
                "voice_state_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging voice state update events.",
                },
                "member_ban": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member ban events.",
                },
                "member_unban": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member unban events.",
                },
                "invite_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging invite creation events.",
                },
                "invite_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging invite deletion events.",
                },
                "message_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging message deletion events.",
                },
                "bulk_message_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging bulk message deletion events.",
                },
                "message_edit": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging message edit events.",
                },
                "reaction_add": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging reaction add events.",
                },
                "reaction_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging reaction remove events.",
                },
                "member_join": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member join events.",
                },
                "member_remove": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member remove events.",
                },
                "member_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging member update events.",
                },
                "user_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging user update events.",
                },
                "guild_role_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging role creation events.",
                },
                "guild_role_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging role deletion events.",
                },
                "guild_role_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging role update events.",
                },
                "guild_emojis_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging emoji update events.",
                },
                "guild_sticker_create": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging sticker creation events.",
                },
                "guild_sticker_delete": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging sticker deletion events.",
                },
                "guild_sticker_update": {
                        "converter": discord.TextChannel,
                        "description": "Channel for logging sticker update events.",
                },
        }

        default_guild = {event: None for event in settings_dict.keys()}
        self.config.register_guild(**default_guild)

        self.logs = CogsUtils.get_logger(cog=self)

        self.event_queue = asyncio.Queue()
        self.bot.loop.create_task(self.process_event_queue())

        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GUILD,
            settings=settings_dict,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.setlog
        )

    async def cog_load(self) -> None:
        await super().cog_load()
        await self.settings.add_commands()

    @commands.guild_only()
    @commands.has_permissions(manage_guild=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.group(name='setlog', invoke_without_command=True)
    async def setlog(self, ctx: commands.Context, event: str, channel: discord.TextChannel) -> None:
        """Set the logging channel for a specific event"""
        await self.config.guild(ctx.guild).set_raw(event, value=channel.id)
        await ctx.send(f'Logging channel for {event} set to {channel.mention}')

    @commands.guild_only()
    @commands.is_owner()
    @commands.bot_has_permissions(manage_channels=True)
    @commands.group(name='seteventlogger', invoke_without_command=True)
    async def seteventlogger(self, ctx: commands.Context) -> None:
        """Configure EventLogger for your server."""
        pass

    async def create_embed(self, event: str, description: str, color: discord.Color = discord.Color.blue()):
        embed = discord.Embed(
            title=f"📝 {event.replace('_', ' ').title()}",
            description=description,
            color=color,
            timestamp=datetime.utcnow()
        )
        embed.set_footer(text=f"Event Logger | {self.bot.user.name}", icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        return embed

    async def log_event(self, guild: typing.Optional[discord.Guild], event: str, description: str, color: discord.Color = discord.Color.blue()):
        if guild is None:
            return
        channel_id = await self.config.guild(guild).get_raw(event, default=None)
        if channel_id:
            channel = guild.get_channel(channel_id)
            if channel:
                embed = await self.create_embed(event, description, color)
                await self.event_queue.put((channel, embed))

    async def log_command(self, ctx, command_name: str):
        command_log_channel_id = await self.config.guild(ctx.guild).command_log_channel()
        if command_log_channel_id:
            channel = ctx.guild.get_channel(command_log_channel_id)
            if channel:
                description = (
                    f"🔧 **Command Executed**\n\n"
                    f"**Command:** {command_name}\n"
                    f"**User:** {ctx.author} (ID: {ctx.author.id})\n"
                    f"**Channel:** {ctx.channel.mention} (ID: {ctx.channel.id})\n"
                    f"**Guild:** {ctx.guild.name} (ID: {ctx.guild.id})\n"
                    f"**Executed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
                )
                embed = await self.create_embed('Command Executed', description, discord.Color.green())
                await self.event_queue.put((channel, embed))

    async def process_event_queue(self):
        while True:
            events = []
            while not self.event_queue.empty():
                events.append(await self.event_queue.get())
            for channel, embed in events:
                await channel.send(embed=embed)
            await asyncio.sleep(10)

    @setlog.command()
    async def categories(self, ctx):
        """View the event categories and their events"""
        event_categories = {
            'app': ['integration_create', 'integration_delete', 'integration_update'],
            'ban': ['member_ban', 'member_unban'],
            'channel': [
                'guild_channel_create', 'guild_channel_delete', 'guild_channel_update',
                'guild_channel_pins_update'
            ],
            'emoji': ['guild_emojis_update'],
            'invite': ['invite_create', 'invite_delete'],
            'message': ['bulk_message_delete', 'message_delete', 'message_edit'],
            'reaction': ['reaction_add', 'reaction_remove'],
            'role': ['guild_role_create', 'guild_role_delete', 'guild_role_update'],
            'sticker': ['guild_sticker_create', 'guild_sticker_delete', 'guild_sticker_update'],
            'user': [
                'member_join', 'member_remove', 'member_update', 'user_update'
            ],
            'voice': ['voice_state_update'],
        }
        embed = discord.Embed(title='Event Categories and Their Events', color=discord.Color.blue())
        for category, events in sorted(event_categories.items()):
            embed.add_field(name=category.capitalize(), value='\n'.join(sorted(events)), inline=False)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_integration_create(self, integration: discord.Integration):
        # Use getattr to safely get created_at, or use current time if not available
        created_at = getattr(integration, 'created_at', datetime.utcnow())

        description = (
            f"#  New Integration Added\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Account:** {integration.account.name} (ID: {integration.account.id})\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Created At:** <t:{int(created_at.timestamp())}:F>\n\n"
            f"[Integration Settings](https://discord.com/channels/{integration.guild.id}/integrations)"
        )
        await self.log_event(integration.guild, 'integration_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_integration_delete(self, integration: discord.Integration):
        description = (
            f"# 🗑️  Integration Removed\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Integration Settings](https://discord.com/channels/{integration.guild.id}/integrations)"
        )
        await self.log_event(integration.guild, 'integration_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_integration_update(self, integration: discord.Integration):
        description = (
            f"# 🔄 Integration Updated\n\n"
            f"**Name:** {integration.name}\n"
            f"**ID:** `{integration.id}`\n"
            f"**Type:** {integration.type}\n"
            f"**Guild:** {integration.guild.name}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Integration Settings](https://discord.com/channels/{integration.guild.id}/integrations)"
        )
        await self.log_event(integration.guild, 'integration_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        description = (
            f"# 📢 New Channel Created\n\n"
            f"**Name:** {channel.name}\n"
            f"**ID:** `{channel.id}`\n"
            f"**Type:** `{channel.type}`\n"
            f"**Category:** {channel.category.name if channel.category else 'None'}\n"
            f"**Position:** {channel.position}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Go to Channel]({channel.jump_url}) | [Channel Settings](https://discord.com/channels/{channel.guild.id}/{channel.id}/edit)"
        )
        await self.log_event(channel.guild, 'guild_channel_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        description = (
            f"# 🗑️ Channel  Deleted\n\n"
            f"**Name:** {channel.name}\n"
            f"**ID:** `{channel.id}`\n"
            f"**Type:** `{channel.type}`\n"
            f"**Category:** {channel.category.name if channel.category else 'None'}\n"
            f"**Position:** {channel.position}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(channel.guild, 'guild_channel_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.category != after.category:
            changes.append(f"**Category:** {before.category.name if before.category else 'None'} → {after.category.name if after.category else 'None'}")
        if before.position != after.position:
            changes.append(f"**Position:** {before.position} → {after.position}")
        if isinstance(before, discord.TextChannel) and isinstance(after, discord.TextChannel):
            if before.topic != after.topic:
                changes.append(f"**Topic:** {before.topic} → {after.topic}")
            if before.slowmode_delay != after.slowmode_delay:
                changes.append(f"**Slowmode:** {before.slowmode_delay}s → {after.slowmode_delay}s")

        if changes:
            description = (
                f"# 🔄 Channel Updated\n\n"
                f"**Channel:** {after.name} (`{after.id}`)\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Go to Channel]({after.jump_url}) | [Channel Settings](https://discord.com/channels/{after.guild.id}/{after.id}/edit)"
            )
            await self.log_event(after.guild, 'guild_channel_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_channel_pins_update(self, channel: discord.abc.GuildChannel, last_pin: typing.Optional[datetime]):
        description = (
            f"# 📌 Channel Pins Updated\n\n"
            f"**Channel:** {channel.name} (`{channel.id}`)\n"
            f"**Last Pin:** {'None' if last_pin is None else f'<t:{int(last_pin.timestamp())}:F>'}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Go to Channel]({channel.jump_url})"
        )
        await self.log_event(channel.guild, 'guild_channel_pins_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel != after.channel:
            if after.channel:
                action = f"joined {after.channel.mention}"
            elif before.channel:
                action = f"left {before.channel.mention}"
            else:
                return

            description = (
                f"# 🎙 ️ Voice State Updated\n\n"
                f"**Member:** {member.mention} ({member.name})\n"
                f"**Action:** {action}\n"
                f"**Self Mute:** {'Yes' if after.self_mute else 'No'}\n"
                f"**Self Deaf:** {'Yes' if after.self_deaf else 'No'}\n"
                f"**Server Mute:** {'Yes' if after.mute else 'No'}\n"
                f"**Server Deaf:** {'Yes' if after.deaf else 'No'}\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>"
            )
            await self.log_event(member.guild, 'voice_state_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        description = (
            f"# 🚫 Member Banned\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Account Created:** <t:{int(user.created_at.timestamp())}:F>\n"
            f"**Banned At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Audit Log](https://discord.com/channels/{guild.id}/audit-log?action_type=22)"
        )
        await self.log_event(guild, 'member_ban', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        description = (
            f"# 🔓 Member Unbanned\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**User ID:** `{user.id}`\n"
            f"**Account Created:** <t:{int(user.created_at.timestamp())}:F>\n"
            f"**Unbanned At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Audit Log](https://discord.com/channels/{guild.id}/audit-log?action_type=23)"
        )
        await self.log_event(guild, 'member_unban', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        description = (
            f"# 📨 Invite Created\n\n"
            f"**Inviter:** {invite.inviter.mention} ({invite.inviter.name})\n"
            f"**Channel:** {invite.channel.mention}\n"
            f"**Code:** {invite.code}\n"
            f"**Max Uses:** {invite.max_uses if invite.max_uses else 'Unlimited'}\n"
            f"**Max Age:** {invite.max_age if invite.max_age else 'Never'}\n"
            f"**Temporary:** {'Yes' if invite.temporary else 'No'}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Use Invite](https://discord.gg/{invite.code})"
        )
        await self.log_event(invite.guild, 'invite_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_invite_delete(self, invite: discord.Invite):
        description = (
            f"# 🗑️ Invite  Deleted\n\n"
            f"**Channel:** {invite.channel.mention}\n"
            f"**Code:** {invite.code}\n"
            f"**Uses:** {invite.uses}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(invite.guild, 'invite_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.guild is None:
            return
        description = (
            f"# 🗑️  Message Deleted\n\n"
            f"**Author:** {message.author.mention} ({message.author.name})\n"
            f"**Channel:** {message.channel.mention}\n"
            f"**Created At:** <t:{int(message.created_at.timestamp())}:F>\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"**Content:**\n>>> {message.content[:1000]}"
        )
        await self.log_event(message.guild, 'message_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages: List[discord.Message]):
        if not messages:
            return
        guild = messages[0].guild
        if guild is None:
            return
        description = (
            f"# 🗑️ Bulk  Message Delete\n\n"
            f"**Channel:** {messages[0].channel.mention}\n"
            f"**Message Count:** {len(messages)}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"**Messages:**\n"
        )
        for message in messages[:10]:  # Limit to first 10 messages to avoid hitting character limits
            description += f"> {message.author.name}: {message.content[:100]}...\n"
        if len(messages) > 10:
            description += f"\n... and {len(messages) - 10} more messages."
        await self.log_event(guild, 'bulk_message_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.guild is None:
            return
        if before.content == after.content:
            return
        description = (
            f"# ✏️ Message Edited\n\n"
            f"**Author:** {before.author.mention} ({before.author.name})\n"
            f"**Channel:** {before.channel.mention}\n"
            f"**Created At:** <t:{int(before.created_at.timestamp())}:F>\n"
            f"**Edited At:** <t:{int(after.edited_at.timestamp() if after.edited_at else datetime.utcnow().timestamp())}:F>\n\n"
            f"**Before:**\n>>> {before.content[:500]}\n\n"
            f"**After:**\n>>> {after.content[:500]}\n\n"
            f"[Jump to Message]({after.jump_url})"
        )
        await self.log_event(before.guild, 'message_edit', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
        if reaction.message.guild is None:
            return

        if isinstance(reaction.message.channel, discord.abc.GuildChannel):
            channel_info = reaction.message.channel.mention
        else:
            channel_info = f"#{reaction.message.channel.name}" if hasattr(reaction.message.channel, 'name') else "Unknown Channel"

        description = (
            f"# 👍 Reaction Added\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**Channel:** {channel_info}\n"
            f"**Message:** [Jump to Message]({reaction.message.jump_url})\n"
            f"**Emoji:** {reaction.emoji}\n"
            f"**Added At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(reaction.message.guild, 'reaction_add', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: discord.Reaction, user: Union[discord.Member, discord.User]):
        if reaction.message.guild is None:
            return
        description = (
            f"# 👎 Reaction Removed\n\n"
            f"**User:** {user.mention} ({user.name})\n"
            f"**Channel:** {reaction.message.channel.mention}\n"
            f"**Message:** [Jump to Message]({reaction.message.jump_url})\n"
            f"**Emoji:** {reaction.emoji}\n"
            f"**Removed At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(reaction.message.guild, 'reaction_remove', description, discord.Color.orange())

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        description = (
            f"# 👋 New Member\n\n"
            f"**Member:** {member.mention} ({member.name})\n"
            f"**ID:** `{member.id}`\n"
            f"**Account Created:** <t:{int(member.created_at.timestamp())}:R>\n"
            f"**Joined At:** <t:{int(member.joined_at.timestamp())}:F>\n"
            f"**Server Member Count:** {member.guild.member_count}\n\n"
            f"[Member Profile](https://discord.com/channels/@me/{member.id})"
        )
        await self.log_event(member.guild, 'member_join', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        description = (
            f"# 👋 Member Left\n\n"
            f"**Member:** {member.mention} ({member.name})\n"
            f"**Member ID:** `{member.id}`\n"
            f"**Joined At:** <t:{int(member.joined_at.timestamp())}:F>\n"
            f"**Account Created:** <t:{int(member.created_at.timestamp())}:F>\n"
            f"**Roles:** {', '.join([role.name for role in member.roles[1:]])}\n"
            f"**Left At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"Server Member Count: {member.guild.member_count}"
        )
        await self.log_event(member.guild, 'member_remove', description, discord.Color.orange())

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        print("Member updated event triggered")
        changes = []
        if before.nick != after.nick:
            changes.append(f"**Nickname:** {before.nick} → {after.nick}")
        if before.roles != after.roles:
            added_roles = set(after.roles) - set(before.roles)
            removed_roles = set(before.roles) - set(after.roles)
            if added_roles:
                changes.append(f"**Roles Added:** {', '.join(role.name for role in added_roles)}")
            if removed_roles:
                changes.append(f"**Roles Removed:** {', '.join(role.name for role in removed_roles)}")
        if before.avatar != after.avatar:
            changes.append(f"**Avatar:** [Before]({before.avatar.url}) → [After]({after.avatar.url})")

        if changes:
            description = (
                f"# 🔄 Member Updated\n\n"
                f"**Member:** {after.mention} ({after.name})\n"
                f"**Member ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Member Profile](https://discord.com/channels/@me/{after.id})"
            )
            await self.log_event(after.guild, 'member_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_user_update(self, before: discord.User, after: discord.User):
        print("User updated event triggered")
        changes = []
        if before.name != after.name:
            changes.append(f"**Username:** {before.name} → {after.name}")
        if before.discriminator != after.discriminator:
            changes.append(f"**Discriminator:** {before.discriminator} → {after.discriminator}")
        if before.avatar != after.avatar:
            changes.append(f"**Avatar:** [Before]({before.display_avatar.url}) → [After]({after.display_avatar.url})")

        if changes:
            description = (
                f"# 🔄 User Updated\n\n"
                f"**User:** {after.mention} ({after.name})\n"
                f"**User ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[User Profile](https://discord.com/channels/@me/{after.id})"
            )
            await self.log_event(None, 'user_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_role_create(self, role: discord.Role):
        description = (
            f"# 🆕 Role Created\n\n"
            f"**Name:** {role.name}\n"
            f"**ID:** `{role.id}`\n"
            f"**Color:** {role.color}\n"
            f"**Permissions:** `{role.permissions.value}`\n"
            f"**Position:** {role.position}\n"
            f"**Mentionable:** {'Yes' if role.mentionable else 'No'}\n"
            f"**Hoisted:** {'Yes' if role.hoist else 'No'}\n"
            f"**Created At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Role Settings](https://discord.com/channels/{role.guild.id}/roles/{role.id})"
        )
        await self.log_event(role.guild, 'guild_role_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role: discord.Role):
        description = (
            f"# 🗑️  Role Deleted\n\n"
            f"**Name:** {role.name}\n"
            f"**ID:** `{role.id}`\n"
            f"**Color:** {role.color}\n"
            f"**Permissions:** `{role.permissions.value}`\n"
            f"**Position:** {role.position}\n"
            f"**Mentionable:** {'Yes' if role.mentionable else 'No'}\n"
            f"**Hoisted:** {'Yes' if role.hoist else 'No'}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(role.guild, 'guild_role_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_role_update(self, before: discord.Role, after: discord.Role):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.color != after.color:
            changes.append(f"**Color:** {before.color} → {after.color}")
        if before.permissions != after.permissions:
            changes.append(f"**Permissions:** `{before.permissions.value}` → `{after.permissions.value}`")
        if before.hoist != after.hoist:
            changes.append(f"**Hoisted:** {'Yes' if before.hoist else 'No'} → {'Yes' if after.hoist else 'No'}")
        if before.mentionable != after.mentionable:
            changes.append(f"**Mentionable:** {'Yes' if before.mentionable else 'No'} → {'Yes' if after.mentionable else 'No'}")
        if before.position != after.position:
            changes.append(f"**Position:** {before.position} → {after.position}")

        if changes:
            description = (
                f"# 🔄 Role Updated\n\n"
                f"**Role:** {after.name}\n"
                f"**ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Role Settings](https://discord.com/channels/{after.guild.id}/roles/{after.id})"
            )
            await self.log_event(before.guild, 'guild_role_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild: discord.Guild, before: List[discord.Emoji], after: List[discord.Emoji]):
        added_emojis = [emoji for emoji in after if emoji not in before]
        removed_emojis = [emoji for emoji in before if emoji not in after]
        description = (
            f"# 😀 Guild Emojis Updated\n\n"
            f"**Added Emojis:** {', '.join([str(emoji) for emoji in added_emojis]) or 'None'}\n"
            f"**Removed Emojis:** {', '.join([str(emoji) for emoji in removed_emojis]) or 'None'}\n"
            f"**Total Emojis:** {len(after)}\n"
            f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
            f"[Emoji Settings](https://discord.com/channels/{guild.id}/emojis)"
        )
        await self.log_event(guild, 'guild_emojis_update', description, discord.Color.blue())

    @commands.Cog.listener()
    async def on_guild_sticker_create(self, sticker: discord.GuildSticker):
        description = (
            f"# 🆕 Sticker Created\n\n"
            f"**Name:** {sticker.name}\n"
            f"**ID:** `{sticker.id}`\n"
            f"**Description:** {sticker.description}\n"
            f"**Emoji:** {sticker.emoji}\n"
            f"**Created By:** {sticker.user.name if sticker.user else 'Unknown'} (`{sticker.user.id if sticker.user else 'Unknown'}`)\n"
            f"**Created At:** <t:{int(sticker.created_at.timestamp())}:F>\n\n"
            f"[Sticker URL]({sticker.url})"
        )
        await self.log_event(sticker.guild, 'guild_sticker_create', description, discord.Color.green())

    @commands.Cog.listener()
    async def on_guild_sticker_delete(self, sticker: discord.GuildSticker):
        description = (
            f"# 🗑️ St icker Deleted\n\n"
            f"**Name:** {sticker.name}\n"
            f"**ID:** `{sticker.id}`\n"
            f"**Description:** {sticker.description}\n"
            f"**Emoji:** {sticker.emoji}\n"
            f"**Deleted At:** <t:{int(datetime.utcnow().timestamp())}:F>"
        )
        await self.log_event(sticker.guild, 'guild_sticker_delete', description, discord.Color.red())

    @commands.Cog.listener()
    async def on_guild_sticker_update(self, before: discord.GuildSticker, after: discord.GuildSticker):
        changes = []
        if before.name != after.name:
            changes.append(f"**Name:** {before.name} → {after.name}")
        if before.description != after.description:
            changes.append(f"**Description:** {before.description} → {after.description}")
        if before.emoji != after.emoji:
            changes.append(f"**Emoji:** {before.emoji} → {after.emoji}")

        if changes:
            description = (
                f"# 🔄 Sticker Updated\n\n"
                f"**Sticker:** {after.name}\n"
                f"**ID:** `{after.id}`\n"
                f"**Changes:**\n" + "\n".join(changes) + f"\n\n"
                f"**Updated At:** <t:{int(datetime.utcnow().timestamp())}:F>\n\n"
                f"[Sticker URL]({after.url})"
            )
            await self.log_event(after.guild, 'guild_sticker_update', description, discord.Color.blue())
