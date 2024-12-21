import discord
from Star-Utils import Cog, CogsUtils
from starbot.core import commands, app_commands, Config
from starbot.core.bot import Red
from datetime import timedelta, datetime
import re
import uuid
import asyncio

@app_commands.context_menu(name="Adwarn User")
async def adwarn_context_menu(interaction: discord.Interaction, message: discord.Message):
    modal = discord.ui.Modal(title="Adwarn User")
    reason_input = discord.ui.TextInput(
        label="Reason",
        style=discord.TextStyle.paragraph,
        placeholder="Enter the reason for the warning",
        custom_id="warning_reason",
        required=True,
    )
    modal.add_item(reason_input)

    async def modal_submit(interaction: discord.Interaction):
        await interaction.response.defer()
        user = message.author
        reason = reason_input.value

        context = await CogsUtils.invoke_command(
            bot=interaction.client,
            author=interaction.user,
            channel=interaction.channel,
            command=f'adwarn {user.id} {reason}',
        )

        if not await discord.utils.async_all([check(context) for check in context.command.checks]):
            await interaction.followup.send(
                "You're not allowed to execute the `adwarn` command in this channel.",
                ephemeral=True,
            )
            return

        # Attempt to delete the original message
        try:
            await message.delete()
            deletion_status = "The original message has been deleted."
        except discord.Forbidden:
            deletion_status = "I couldn't delete the original message due to lack of permissions."
        except discord.NotFound:
            deletion_status = "The original message was already deleted."
        except discord.HTTPException:
            deletion_status = "An error occurred while trying to delete the original message."

        await interaction.followup.send(
            f"User {user.mention} has been warned for: {reason}\n{deletion_status}",
            ephemeral=True
        )

    modal.on_submit = modal_submit
    await interaction.response.send_modal(modal)

class Emojis:
    MOD = discord.PartialEmoji(name="mod", id="1297394034624434246")
    REASON = discord.PartialEmoji(name="reason", id="1297394094263238707")
    CHANNEL = discord.PartialEmoji(name="channel", id="1297394076672462858")
    USER = discord.PartialEmoji(name="user", id="1297394126173507624")
    TIME = discord.PartialEmoji(name="time", id="1297394056023769118")

class Adwarn(Cog):

#    __version__ = "1.0.1"

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        self.config.register_guild(warn_channel=None, tholds={},
            warnings_issued={}, mod_warnings={}, softban_duration=120,
            timeout_duration=120, weekly_stats={}, monthly_stats={})
        self.config.register_member(warnings=[], untimeout_time=None)
        self.logs = CogsUtils.get_logger("Adwarn")

    async def cog_load(self) -> None:
        await super().cog_load()
        self.bot.tree.add_command(adwarn_context_menu)

    async def cog_unload(self) -> None:
        self.bot.tree.remove_command(adwarn_context_menu.name)
        await super().cog_unload()
    @commands.command(hidden=True)
    async def adwarninfo(self, ctx: commands.Context):
        await ctx.send(await format_info(ctx, self.qualified_name, self.__version__))

    @commands.hybrid_command()
    @commands.has_permissions(manage_messages=True)
    async def adwarn(self, ctx, user: discord.Member, *, reason: str):
        """Warn a user and send an embed to the default warning channel."""
        warn_channel_id = await self.config.guild(ctx.guild).warn_channel()
        if warn_channel_id:
            warn_channel = self.bot.get_channel(warn_channel_id)
            if warn_channel:
                warnings = await self.config.member(user).warnings()
                warning_time = discord.utils.utcnow()
                warning_id = str(uuid.uuid4())
                warnings.append({'id': warning_id, 'reason': reason,
                    'moderator': ctx.author.id, 'time': warning_time.isoformat(),
                    'channel': ctx.channel.id})
                await self.config.member(user).warnings.set(warnings)
                warnings_issued = await self.config.guild(ctx.guild).warnings_issued()
                if str(ctx.author.id) not in warnings_issued:
                    warnings_issued[str(ctx.author.id)] = 0
                warnings_issued[str(ctx.author.id)] += 1
                await self.config.guild(ctx.guild).warnings_issued.set(warnings_issued)
                mod_warnings = await self.config.guild(ctx.guild).mod_warnings()
                if str(ctx.author.id) not in mod_warnings:
                    mod_warnings[str(ctx.author.id)] = []
                mod_warnings[str(ctx.author.id)].append({'user': user.id,
                    'reason': reason, 'time': warning_time.isoformat(),
                    'channel': ctx.channel.id})
                await self.config.guild(ctx.guild).mod_warnings.set(mod_warnings)
                timestamp = int(warning_time.timestamp())
                embed = discord.Embed(title='New Adwarn', color=discord.Color.red())
                embed.add_field(name=f'{Emojis.USER} | User', value=user.mention, inline=True)
                embed.add_field(name=f'{Emojis.CHANNEL} | Warned In', value=ctx.channel.mention, inline=True)
                embed.add_field(name=f'{Emojis.REASON} | Reason', value=reason, inline=True)
                embed.add_field(name=f'{Emojis.MOD} | Moderator', value=ctx.author.mention, inline=True)
                embed.add_field(name=f'{Emojis.TIME} | Time', value=f'<t:{timestamp}:F>', inline=True)
                embed.set_footer(text=f'Total warnings: {len(warnings)}')
                await warn_channel.send(embed=embed)
                await warn_channel.send(f'{user.mention}')
                await self.check_thresholds(ctx, user, len(warnings))
            else:
                error_embed = discord.Embed(title='Error 404', description='Warning channel not found. Please set it again using `[p]warnset channel`.', color=discord.Color.red())
                error_message = await ctx.send(embed=error_embed)
                await error_message.delete(delay=3)
        else:
            error_embed = discord.Embed(title='Error 404', description='No warning channel has been set. Please set it using `[p]warnset channel`.', color=discord.Color.red())
            error_message = await ctx.send(embed=error_embed)
            await error_message.delete(delay=3)
        await ctx.message.delete(delay=3)

    async def check_thresholds(self, ctx, user, warning_count):
        tholds = await self.config.guild(ctx.guild).tholds()
        softban_duration = await self.config.guild(ctx.guild).softban_duration()
        timeout_duration = await self.config.guild(ctx.guild).timeout_duration()
        for threshold_id, threshold in tholds.items():
            if threshold['count'] == warning_count:
                action = threshold['action']
                if action == 'kick':
                    await ctx.guild.kick(user, reason='Reached warning threshold')
                elif action == 'ban':
                    await ctx.guild.ban(user, reason='Reached warning threshold')
                elif action == 'timeout':
                    await self.timeout_user(ctx, user, timeout_duration)
                    if timeout_duration:
                        await self.schedule_untimeout(ctx, user, timeout_duration)
                elif action == 'softban':
                    await ctx.guild.ban(user, reason='Reached warning threshold', delete_message_days=softban_duration)
                    await ctx.guild.unban(user, reason='Softban duration expired')

    def parse_duration(self, duration_str):
        """Parse a duration string and return the duration in minutes."""
        match = re.match(r'(\d+)([mh])', duration_str)
        if match:
            value, unit = match.groups()
            value = int(value)
            if unit == 'h':
                return value * 60
            elif unit == 'm':
                return value
        return None

    async def timeout_user(self, ctx, user: discord.Member, duration: int=120):
        if duration:
            timeout_until = discord.utils.utcnow() + timedelta(minutes=duration)
            await user.edit(timed_out_until=timeout_until, reason='Reached warning threshold')
            await self.config.member(user).untimeout_time.set(timeout_until.isoformat())

    async def schedule_untimeout(self, ctx, user, duration):
        untimeout_time = discord.utils.utcnow() + timedelta(minutes=duration)
        await self.config.member(user).untimeout_time.set(untimeout_time.isoformat())

    @commands.Cog.listener()
    async def on_ready(self):
        await self.check_untimeout_times()

    async def check_untimeout_times(self):
        for guild in self.bot.guilds:
            for member in guild.members:
                untimeout_time = await self.config.member(member).untimeout_time()
                if untimeout_time:
                    untimeout_time = datetime.fromisoformat(untimeout_time)
                    if discord.utils.utcnow() >= untimeout_time:
                        await self.untimeout_user(member)
                        await self.config.member(member).untimeout_time.clear()

    async def untimeout_user(self, user: discord.Member):
        await user.edit(timed_out_until=None, reason='Timeout duration expired')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def removewarn(self, ctx, user: discord.Member, warning_id: str):
        """Remove a specific warning from a user by its UUID."""
        warnings = await self.config.member(user).warnings()
        warning_to_remove = next((warning for warning in warnings if warning['id'] == warning_id), None)
        if warning_to_remove:
            warnings.remove(warning_to_remove)
            await self.config.member(user).warnings.set(warnings)
            warn_channel_id = await self.config.guild(ctx.guild).warn_channel()
            if warn_channel_id:
                warn_channel = self.bot.get_channel(warn_channel_id)
                if warn_channel:
                    embed = discord.Embed(title='Adwarn Removed', color=discord.Color.green())
                    embed.add_field(name=f'{Emojis.REASON} | Warning', value=warning_to_remove['reason'], inline=True)
                    embed.add_field(name=f'{Emojis.MOD} | Moderator', value=ctx.author.mention, inline=True)
                    embed.add_field(name=f'{Emojis.TIME} | Removed Time', value=f'<t:{int(discord.utils.utcnow().timestamp())}:F>', inline=True)
                    embed.set_footer(text=f'Total warnings: {len(warnings)}')
                    await warn_channel.send(embed=embed)
                else:
                    error_embed = discord.Embed(title='Error 404', description='Warning channel not found. Please set it again using `[p]warnset channel`.', color=discord.Color.red())
                    await ctx.send(embed=error_embed)
            else:
                error_embed = discord.Embed(title='Error 404', description='No warning channel has been set. Please set it using `[p]warnset channel`.', color=discord.Color.red())
                await ctx.send(embed=error_embed)
        else:
            error_embed = discord.Embed(title='Error 404', description=f'Warning with ID {warning_id} not found.', color=discord.Color.red())
            await ctx.send(embed=error_embed)

    @commands.hybrid_command()
    @commands.has_permissions(manage_messages=True)
    async def warncount(self, ctx, user: discord.Member):
        """Get the total number of warnings a user has."""
        warnings = await self.config.member(user).warnings()
        embed = discord.Embed(title='Warning Count', description=f'{user.mention} has {len(warnings)} warnings.', color=discord.Color.blue())
        for warning in warnings:
            timestamp = int(datetime.fromisoformat(warning['time']).timestamp())
            embed.add_field(name=f"Warning ID: {warning['id']}", value=
                f"""{Emojis.REASON} | Reason: {warning['reason']}
{Emojis.MOD} | Moderator: <@{warning['moderator']}>
{Emojis.TIME} | Time: <t:{timestamp}:F>"""
                , inline=True)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @commands.has_permissions(manage_messages=True)
    async def clearwarns(self, ctx, user: discord.User):
        """Clear all warnings for a user."""
        await self.config.member_from_ids(ctx.guild.id, user.id).warnings.set([])
        warn_channel_id = await self.config.guild(ctx.guild).warn_channel()
        if warn_channel_id:
            warn_channel = self.bot.get_channel(warn_channel_id)
            if warn_channel:
                embed = discord.Embed(title='All Warnings Cleared', color=discord.Color.green())
                embed.add_field(name=f'{Emojis.USER} | User', value=user.mention, inline=True)
                embed.add_field(name=f'{Emojis.MOD} | Moderator', value=ctx.author.mention, inline=True)
                embed.add_field(name=f'{Emojis.TIME} | Cleared Time', value=f'<t:{int(discord.utils.utcnow().timestamp())}:F>', inline=True)
                await warn_channel.send(embed=embed)
            else:
                error_embed = discord.Embed(title='Error 404', description='Warning channel not found. Please set it again using `[p]warnset channel`.', color=discord.Color.red())
                await ctx.send(embed=error_embed)
        else:
            error_embed = discord.Embed(title='Error 404', description='No warning channel has been set. Please set it using `[p]warnset channel`.', color=discord.Color.red())
            await ctx.send(embed=error_embed)

    @commands.hybrid_command()
    @commands.has_permissions(manage_messages=True)
    async def unadwarn(self, ctx, user: discord.Member):
        """Clear the most recent warning for a user."""
        warnings = await self.config.member(user).warnings()
        if warnings:
            removed_warning = warnings.pop()
            await self.config.member(user).warnings.set(warnings)
            warn_channel_id = await self.config.guild(ctx.guild).warn_channel()
            if warn_channel_id:
                warn_channel = self.bot.get_channel(warn_channel_id)
                if warn_channel:
                    embed = discord.Embed(title='Most Recent Adwarn Removed', color=discord.Color.green())
                    embed.add_field(name=f'{Emojis.REASON} | Warning', value=removed_warning['reason'], inline=True)
                    embed.add_field(name=f'{Emojis.MOD} | Moderator', value=ctx.author.mention, inline=True)
                    embed.add_field(name=f'{Emojis.TIME} | Removed Time', value=f'<t:{int(discord.utils.utcnow().timestamp())}:F>', inline=True)
                    embed.set_footer(text=f'Total warnings: {len(warnings)}')
                    await warn_channel.send(embed=embed)
                else:
                    error_embed = discord.Embed(title='Error 404', description='Warning channel not found. Please set it again using `[p]warnset channel`.', color=discord.Color.red())
                    await ctx.send(embed=error_embed)
            else:
                error_embed = discord.Embed(title='Error 404', description='No warning channel has been set. Please set it using `[p]warnset channel`.', color=discord.Color.red())
                await ctx.send(embed=error_embed)
        else:
            error_embed = discord.Embed(title='Error 404', description=f'{user.mention} has no warnings.', color=discord.Color.red())
            await ctx.send(embed=error_embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def editaw(self, ctx, user: discord.Member, warning_id: str, *, new_reason: str):
        """Edit a specific warning by its UUID."""
        warnings = await self.config.member(user).warnings()
        warning_to_edit = next((warning for warning in warnings if warning['id'] == warning_id), None)
        if warning_to_edit:
            warning_to_edit['reason'] = new_reason
            await self.config.member(user).warnings.set(warnings)
            warn_channel_id = await self.config.guild(ctx.guild).warn_channel()
            if warn_channel_id:
                warn_channel = self.bot.get_channel(warn_channel_id)
                if warn_channel:
                    embed = discord.Embed(title='Adwarn Edited', color=discord.Color.orange())
                    embed.add_field(name=f'{Emojis.REASON} | Warning', value=new_reason, inline=True)
                    embed.add_field(name=f'{Emojis.MOD} | Moderator', value=ctx.author.mention, inline=True)
                    embed.add_field(name=f'{Emojis.TIME} | Edited Time', value=f'<t:{int(discord.utils.utcnow().timestamp())}:F>', inline=True)
                    embed.set_footer(text=f'Total warnings: {len(warnings)}')
                    await warn_channel.send(embed=embed)
                else:
                    error_embed = discord.Embed(title='Error 404', description='Warning channel not found. Please set it again using `[p]warnset channel`.', color=discord.Color.red())
                    await ctx.send(embed=error_embed)
            else:
                error_embed = discord.Embed(title='Error 404', description='No warning channel has been set. Please set it using `[p]warnset channel`.', color=discord.Color.red())
                await ctx.send(embed=error_embed)
        else:
            error_embed = discord.Embed(title='Error 404', description=f'Warning with ID {warning_id} not found.', color=discord.Color.red())
            await ctx.send(embed=error_embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def topwarners(self, ctx):
        """Show the top 5 users who have issued the most warnings in the current server."""
        warnings_issued = await self.config.guild(ctx.guild).warnings_issued()
        sorted_users = sorted(warnings_issued.items(), key=lambda item: item[1], reverse=True)
        embed = discord.Embed(title='Top 5 Warners', color=discord.Color.gold())
        if sorted_users:
            for rank, (user_id, count) in enumerate(sorted_users[:5], start=1):
                user = self.bot.get_user(int(user_id))
                embed.add_field(name=f'{rank}. {user} (ID: {user_id})', value=f'Warnings Issued: {count}', inline=True)
        else:
            embed.add_field(name='No data available', value='No warnings have been issued yet.', inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def modwarns(self, ctx, moderator: discord.Member):
        """Show the number of warnings issued by a moderator and who they have warned in the current server."""
        mod_warnings = await self.config.guild(ctx.guild).mod_warnings()
        if str(moderator.id) in mod_warnings:
            warnings = mod_warnings[str(moderator.id)]
            embed = discord.Embed(title=f'Warnings Issued by {moderator}', color=discord.Color.blue())
            embed.add_field(name='Total Warnings Issued', value=len(warnings), inline=True)
            for warning in warnings:
                warned_user = self.bot.get_user(warning['user'])
                timestamp = int(datetime.fromisoformat(warning['time']).timestamp())
                embed.add_field(name=f"{Emojis.USER} | User Warned: {warned_user} (ID: {warning['user']})", value=
                    f"""{Emojis.REASON} | Reason: {warning['reason']}
{Emojis.TIME} | Time: <t:{timestamp}:F>
{Emojis.CHANNEL} | Channel: <#{warning['channel']}>"""
                    , inline=True)
        else:
            embed = discord.Embed(title=f'{moderator} has not issued any warnings.', color=discord.Color.red())
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def adboard(self, ctx):
        """Show all users who have issued warnings and how many they have issued."""
        warnings_issued = await self.config.guild(ctx.guild).warnings_issued()
        sorted_users = sorted(warnings_issued.items(), key=lambda item: item[1], reverse=True)
        embed = discord.Embed(title='AdBoard - Warning Issuers', color=discord.Color.purple())
        if sorted_users:
            for rank, (user_id, count) in enumerate(sorted_users, start=1):
                user = self.bot.get_user(int(user_id))
                embed.add_field(name=f'{rank}. {user} (ID: {user_id})', value=f'Warnings Issued: {count}', inline=True)
        else:
            embed.add_field(name='No data available', value='No warnings have been issued yet.', inline=True)
        await ctx.send(embed=embed)

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def warnset(self, ctx):
        """Settings for the warning system."""
        pass

    @warnset.command()
    async def channel(self, ctx, channel: discord.TextChannel):
        """Set the default channel for warnings."""
        await self.config.guild(ctx.guild).warn_channel.set(channel.id)
        embed = discord.Embed(title='Warning Channel Set', description=f'Warning channel has been set to {channel.mention}', color=discord.Color.green())
        await ctx.send(embed=embed)

    @warnset.command()
    async def show(self, ctx):
        """Show the current warning channel and thresholds."""
        channel_id = await self.config.guild(ctx.guild).warn_channel()
        tholds = await self.config.guild(ctx.guild).tholds()
        embed = discord.Embed(title='Warning System Configuration', color=discord.Color.blue())
        if channel_id:
            channel = self.bot.get_channel(channel_id)
            embed.add_field(name=f'{Emojis.CHANNEL} | Current Warning Channel', value=channel.mention, inline=True)
        else:
            embed.add_field(name=f'{Emojis.CHANNEL} | Current Warning Channel', value='Not set', inline=True)
        if tholds:
            threshold_list = '\n'.join([f"{threshold_id}: {threshold['count']} warnings -> {threshold['action']}" for threshold_id, threshold in tholds.items()])
            embed.add_field(name='Warning Thresholds', value=threshold_list, inline=True)
        else:
            embed.add_field(name='Warning Thresholds', value='No thresholds set', inline=True)
        await ctx.send(embed=embed)

    @warnset.command()
    async def threshold(self, ctx, warning_count: int, action: str):
        """Set an action for a specific warning count threshold."""
        valid_actions = ['kick', 'ban', 'timeout', 'softban']
        if action not in valid_actions:
            await ctx.send(f"Invalid action. Valid actions are: {', '.join(valid_actions)}")
            return
        tholds = await self.config.guild(ctx.guild).tholds()
        threshold_id = str(uuid.uuid4())
        tholds[threshold_id] = {'count': warning_count, 'action': action}
        await self.config.guild(ctx.guild).tholds.set(tholds)
        await ctx.send(f"Set action '{action}' for reaching {warning_count} warnings.")

    @warnset.command()
    async def delthreshold(self, ctx, threshold_id: str):
        """Delete a specific warning count threshold by its UUID."""
        tholds = await self.config.guild(ctx.guild).tholds()
        if threshold_id in tholds:
            del tholds[threshold_id]
            await self.config.guild(ctx.guild).tholds.set(tholds)
            await ctx.send(f'Deleted threshold with ID {threshold_id}.')
        else:
            await ctx.send(f'No threshold set with ID {threshold_id}.')

    @warnset.command()
    async def softbanduration(self, ctx, days: int):
        """Set the duration (in days) for message deletion during a softban."""
        await self.config.guild(ctx.guild).softban_duration.set(days)
        await ctx.send(f'Softban message deletion duration set to {days} days.')

    @warnset.command()
    async def timeoutduration(self, ctx, minutes: int):
        """Set the duration (in minutes) for timeouts."""
        await self.config.guild(ctx.guild).timeout_duration.set(minutes)
        await ctx.send(f'Timeout duration set to {minutes} minutes.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def adrace(self, ctx, duration: int):
        """Start an adwarn race that lasts for a configurable amount of time."""
        custom_emoji = '<a:winner:1269746569872412785>'
        join_end_time = discord.utils.utcnow() + timedelta(seconds=60)
        join_end_timestamp = int(join_end_time.timestamp())
        embed = discord.Embed(title='Adwarn Race Join', description=
            f"""React with the custom emoji to join the Adwarn race!
To join, click the reaction <t:{join_end_timestamp}:R>."""
            , color=discord.Color.gold())
        join_message = await ctx.send(embed=embed)
        await join_message.add_reaction(custom_emoji)

        def check(reaction, user):
            return (str(reaction.emoji) == custom_emoji and reaction.message.id == join_message.id and user != self.bot.user)
        participants = []
        participants_mentions = ''
        while discord.utils.utcnow() < join_end_time:
            try:
                remaining = (join_end_time - discord.utils.utcnow()).total_seconds()
                reaction, user = await self.bot.wait_for('reaction_add', timeout=remaining, check=check)
                if user not in participants:
                    participants.append(user)
                    participants_mentions = ', '.join(user.mention for user in participants)
                    embed.description = f"""Participants: {participants_mentions}
You have until <t:{join_end_timestamp}:R> to join."""
                    await join_message.edit(embed=embed)
            except asyncio.TimeoutError:
                break
        if participants:
            embed.description = f"""Participants: {participants_mentions}
Time's up! The race is starting now."""
        else:
            embed.description = 'No one joined the race. The race is cancelled.'
        await join_message.clear_reactions()
        await join_message.edit(embed=embed)
        if not participants:
            return
        race_start_time = discord.utils.utcnow()
        race_end_time = race_start_time + timedelta(minutes=duration)
        embed = discord.Embed(title='Adwarn Race Started', color=discord.Color.gold())
        embed.add_field(name='Starts', value=f'<t:{int(race_start_time.timestamp())}:R>', inline=True)
        embed.add_field(name='Ends', value=f'<t:{int(race_end_time.timestamp())}:R>', inline=True)
        embed.add_field(name='Participants', value=participants_mentions, inline=True)
        race_message = await ctx.send(embed=embed)
        await asyncio.sleep(duration * 60)
        results = {}
        for participant in participants:
            warnings = 0
            for channel in ctx.guild.text_channels:
                async for message in channel.history(after=race_start_time, limit=None):
                    if (message.author == participant and 'adwarn' in message.content):
                        warnings += 1
            results[participant] = warnings
        sorted_results = sorted(results.items(), key=lambda item: item[1], reverse=True)
        embed.title = 'Adwarn Race Results'
        embed.description = f'The race lasted for {duration} minutes. Here are the results:'
        embed.clear_fields()
        for rank, (user, count) in enumerate(sorted_results, start=1):
            embed.add_field(name=f'{rank}. {user}', value=f'Warnings: {count}', inline=True)
        await race_message.edit(embed=embed)
