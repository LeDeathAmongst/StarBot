import discord
from starbot.core import commands, Config, app_commands
from starbot.core.bot import Red
from Star-Utils import Cog, CogsUtils, Settings, Buttons, Menu
import sqlite3
import asyncio
import os
import math
from datetime import datetime
import typing
from typing import List

class UserOrID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            return await commands.MemberConverter().convert(ctx, argument)
        except commands.MemberNotFound:
            try:
                return await commands.UserConverter().convert(ctx, argument)
            except commands.UserNotFound:
                try:
                    user_id = int(argument)
                    return await ctx.bot.fetch_user(user_id)
                except (ValueError, discord.NotFound):
                    raise commands.BadArgument("Not a valid user or user ID.")

class AppealModal(discord.ui.Modal, title='Global Ban Appeal'):
    understand = discord.ui.TextInput(label='Do you understand why you were banned?', style=discord.TextStyle.paragraph, max_length=1000)
    why_unban = discord.ui.TextInput(label='Why should you be unbanned?', style=discord.TextStyle.paragraph, max_length=1000)
    steps = discord.ui.TextInput(label='What will you do to stay unbanned?', style=discord.TextStyle.paragraph, max_length=1000)

    async def on_submit(self, interaction: discord.Interaction):
        appeal_text = f"Understanding: {self.understand.value}\n\nReason for unban: {self.why_unban.value}\n\nPreventive steps: {self.steps.value}"
        await interaction.client.get_cog('GlobalBanList').submit_appeal(interaction.user, appeal_text)
        await interaction.response.send_message("Your appeal has been submitted for review.", ephemeral=True)

class GlobalBanList(Cog):
    """A complex cog for managing global ban lists across multiple Discord servers."""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("GlobalBanList")
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(
            authorized_users=[],
            ban_appeal_channel=None,
            appeal_cooldown_days=30,
            owner_log_channel=None
        )
        self.config.register_guild(
            subscribed_lists=[],
            auto_ban=True,
            notify_channel=None,
            exempt_roles=[],
            general_log_channel=None,
            ban_list_channel=None
        )

        self.lists = ['raiders_nukers', 'scammers', 'tos_violators', 'dm_advertisers']
        self.databases = {}
        self.cursors = {}
        self.setup_databases()
        self.is_unloading = False
        self.periodic_check_task = None

    def setup_databases(self):
        for list_name in self.lists:
            db_path = f"data/globalbanlist/{list_name}.db"
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
            self.databases[list_name] = sqlite3.connect(db_path)
            self.cursors[list_name] = self.databases[list_name].cursor()
            self.setup_table(list_name)

    def setup_table(self, list_name):
        self.cursors[list_name].execute('''CREATE TABLE IF NOT EXISTS banned_users
                                          (user_id INTEGER PRIMARY KEY,
                                           reason TEXT,
                                           proof TEXT,
                                           banned_at TIMESTAMP)''')
        self.databases[list_name].commit()

    async def cog_load(self):
        await super().cog_load()
        self.periodic_check_task = self.bot.loop.create_task(self.periodic_check())

    async def cog_before_invoke(self, ctx: commands.Context):
        """This runs before every command in the cog"""
        await self.owner_log("Command Used", ctx.author, f"Command: {ctx.command.qualified_name}, Args: {ctx.args[2:]}, Kwargs: {ctx.kwargs}")

    @commands.group(name="globalbanlistowner", aliases=["gblo"])
    @commands.is_owner()
    async def gblo(self, ctx: commands.Context):
        """Group command for Global Ban List owner settings."""
        pass

    @gblo.command(name="addauth")
    async def addauth(self, ctx: commands.Context, user: discord.User):
        """Add a user to the authorized users list."""
        async with self.config.authorized_users() as authorized:
            if user.id not in authorized:
                authorized.append(user.id)
                await ctx.send(f"{user.name} has been added to the authorized users list.")
                await self.owner_log("Add Authorized User", ctx.author, f"Added {user.name} to authorized users")
            else:
                await ctx.send(f"{user.name} is already in the authorized users list.")

    @gblo.command(name="remauth")
    async def remauth(self, ctx: commands.Context, user: discord.User):
        """Remove a user from the authorized users list."""
        async with self.config.authorized_users() as authorized:
            if user.id in authorized:
                authorized.remove(user.id)
                await ctx.send(f"{user.name} has been removed from the authorized users list.")
                await self.owner_log("Remove Authorized User", ctx.author, f"Removed {user.name} from authorized users")
            else:
                await ctx.send(f"{user.name} is not in the authorized users list.")

    @gblo.command(name="setappealchannel")
    async def setappealchannel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        """Set the channel for ban appeals."""
        if channel is None:
            await self.config.ban_appeal_channel.clear()
            await ctx.send("Ban appeal channel has been cleared.")
        else:
            await self.config.ban_appeal_channel.set(channel.id)
            await ctx.send(f"Ban appeal channel has been set to {channel.mention}.")
        await self.owner_log("Set Appeal Channel", ctx.author, f"Set appeal channel to {channel.mention if channel else 'None'}")

    @gblo.command(name="setownerlog")
    async def setownerlog(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for owner logging."""
        await self.config.owner_log_channel.set(channel.id)
        await ctx.send(f"Owner log channel has been set to {channel.mention}.")
        await self.owner_log("Set Owner Log Channel", ctx.author, f"Set owner log channel to {channel.mention}")

    @gblo.command(name="refreshlists")
    async def refreshlists(self, ctx: commands.Context, list_name: str = None):
        """Manually refresh the embeds for a specific list or all lists."""
        if list_name and list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Use `{ctx.prefix}gbl list` to see available lists.")
            return

        if list_name:
            await self.update_list_embeds(list_name)
            await ctx.send(f"Embeds for the {list_name} list have been refreshed.")
        else:
            for lst in self.lists:
                await self.update_list_embeds(lst)
            await ctx.send("Embeds for all lists have been refreshed.")

    @commands.hybrid_group(name="globalbanlist", aliases=["gbl"])
    async def gbl(self, ctx: commands.Context):
        """Manage the global ban list."""
        pass

    @gbl.command(name="add")
    @app_commands.describe(
        list_name="The name of the ban list",
        user="The user to add to the ban list",
        reason_and_proof="Reason and proof separated by '|'"
    )
    async def add_user(self, ctx: commands.Context, list_name: str, user: UserOrID, *, reason_and_proof: str):
        """Add a user to a specific ban list."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Use `{ctx.prefix}gbl list` to see available lists.")
            return

        try:
            reason, proof = reason_and_proof.split('|')
            reason = reason.strip()
            proof = proof.strip()
        except ValueError:
            await ctx.send("Please provide both a reason and proof, separated by a '|' character.")
            return

        user_id = getattr(user, 'id', user)
        user_obj = user if isinstance(user, (discord.User, discord.Member)) else await self.bot.fetch_user(user)

        cursor = self.cursors[list_name]
        cursor.execute("INSERT OR REPLACE INTO banned_users (user_id, reason, proof, banned_at) VALUES (?, ?, ?, ?)",
                        (user_id, reason, proof, datetime.utcnow()))
        self.databases[list_name].commit()

        await ctx.send(f"User {user_obj} (ID: {user_id}) has been added to the {list_name} list.")
        await self.check_subscribed_servers(user_id, list_name)
        await self.update_list_embeds(list_name)

        # Log the new ban in the general log for all subscribed guilds
        for guild in self.bot.guilds:
            guild_config = await self.config.guild(guild).all()
            if list_name in guild_config['subscribed_lists']:
                await self.general_log(guild, "New Ban Added", user_obj, list_name, reason, proof)

        await self.owner_log("Add to Ban List", ctx.author, f"Added {user_obj} to {list_name} list")

    @gbl.command(name="remove")
    @app_commands.describe(
        list_name="The name of the ban list",
        user="The user to remove from the ban list"
    )
    async def remove_user(self, ctx: commands.Context, list_name: str, user: str):
        """Remove a user from a specific ban list."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Use `{ctx.prefix}gbl list` to see available lists.")
            return

        try:
            user_id = int(user)
            user_obj = await self.bot.fetch_user(user_id)
        except ValueError:
            await ctx.send("Invalid user ID provided.")
            return

        cursor = self.cursors[list_name]
        cursor.execute("DELETE FROM banned_users WHERE user_id = ?", (user_id,))
        self.databases[list_name].commit()

        await ctx.send(f"User {user_obj} (ID: {user_id}) has been removed from the {list_name} list.")
        await self.update_list_embeds(list_name)

        # Unban user from subscribed guilds
        await self.unban_from_subscribed_guilds(user_id, list_name)

        await self.owner_log("Remove from Ban List", ctx.author, f"Removed {user_obj} from {list_name} list")

    @gbl.command(name="list")
    async def list_users(self, ctx: commands.Context, list_name: str = None):
        """List all users in a specific ban list or show available lists."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if list_name is None:
            lists_str = "\n".join([f"- {name}" for name in self.lists])
            embed = discord.Embed(title="Available Ban Lists", description=lists_str, color=discord.Color.blue())
            await ctx.send(embed=embed)
            return

        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Use `{ctx.prefix}gbl list` to see available lists.")
            return

        embeds = await self.create_list_embed(list_name)
        await Menu(pages=embeds).start(ctx)

    @gbl.command(name="history")
    async def display_history(self, ctx: commands.Context, list_name: str):
        """Display the history of a specific ban list."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Use `{ctx.prefix}gbl list` to see available lists.")
            return
        embeds = await self.create_list_embed(list_name)
        await Menu(pages=embeds).start(ctx)

    @gbl.command(name="subscribe")
    @commands.has_permissions(administrator=True)
    @app_commands.describe(list_name="The name of the ban list to subscribe to")
    async def subscribe(self, ctx: commands.Context, list_name: str):
        """Subscribe to a specific ban list."""
        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Use `{ctx.prefix}gbl list` to see available lists.")
            return

        # Check if the bot has ban permissions
        if not ctx.guild.me.guild_permissions.ban_members:
            await ctx.send("I don't have permission to ban members in this server. Please give me the 'Ban Members' permission before subscribing to a ban list.")
            return

        async with self.config.guild(ctx.guild).subscribed_lists() as subscribed:
            if list_name not in subscribed:
                subscribed.append(list_name)
                await ctx.send(f"This server has been subscribed to the {list_name} list.")
                await self.owner_log("Subscribe", ctx.author, f"Subscribed to {list_name} list in {ctx.guild.name}")

                # Check existing members against the ban list
                await ctx.send("Checking existing members against the ban list. This may take a while...")
                await self.check_existing_members(ctx.guild, list_name)
            else:
                await ctx.send(f"This server is already subscribed to the {list_name} list.")

    @gbl.command(name="unsubscribe")
    @commands.has_permissions(administrator=True)
    @app_commands.describe(list_name="The name of the ban list to unsubscribe from")
    async def unsubscribe(self, ctx: commands.Context, list_name: str):
        """Unsubscribe from a specific ban list."""
        async with self.config.guild(ctx.guild).subscribed_lists() as subscribed:
            if list_name in subscribed:
                subscribed.remove(list_name)
                await ctx.send(f"This server has been unsubscribed from the {list_name} list.")
                await self.owner_log("Unsubscribe", ctx.author, f"Unsubscribed from {list_name} list in {ctx.guild.name}")
            else:
                await ctx.send(f"This server is not subscribed to the {list_name} list.")

    @gbl.command(name="setgenerallog")
    @commands.has_permissions(administrator=True)
    @app_commands.describe(channel="The channel to set for general logging")
    async def setgenerallog(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for general logging in this server."""
        await self.config.guild(ctx.guild).general_log_channel.set(channel.id)
        await ctx.send(f"General log channel for this server has been set to {channel.mention}.")

    @gblo.command(name="setbanlistchannel")
    @commands.has_permissions(administrator=True)
    @app_commands.describe(channel="The channel to set for displaying ban lists")
    async def setbanlistchannel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for displaying ban lists in this server."""
        await self.config.guild(ctx.guild).ban_list_channel.set(channel.id)
        await ctx.send(f"Ban list channel for this server has been set to {channel.mention}.")

    @gbl.command()
    async def appeal(self, ctx: commands.Context):
        """Submit an appeal for a global ban."""
        for list_name in self.lists:
            cursor = self.cursors[list_name]
            cursor.execute("SELECT 1 FROM banned_users WHERE user_id = ?", (ctx.author.id,))
            if cursor.fetchone():
                view = discord.ui.View()
                button = discord.ui.Button(label="Submit Appeal", style=discord.ButtonStyle.primary)

                async def button_callback(interaction: discord.Interaction):
                    try:
                        appeal_modal = AppealModal()
                        await interaction.response.send_modal(appeal_modal)
                    except Exception as e:
                        print(f"Error in button callback: {str(e)}")
                        await interaction.response.send_message("An error occurred. Please try again later.", ephemeral=True)

                button.callback = button_callback
                view.add_item(button)

                await ctx.send("Click the button below to submit your appeal:", view=view)
                return
        await ctx.send("You are not on any global ban list.")

    async def update_list_embeds(self, list_name: str):
        for guild in self.bot.guilds:
            channel_id = await self.config.guild(guild).ban_list_channel()
            if not channel_id:
                continue

            channel = guild.get_channel(channel_id)
            if not channel:
                continue

            new_embeds = await self.create_list_embed(list_name)

            # Try to find an existing message for this list
            existing_message = None
            async for message in channel.history(limit=100):
                if message.author == self.bot.user and message.embeds:
                    embed = message.embeds[0]
                    if embed.title and embed.title.startswith(f"Users in {list_name} list"):
                        existing_message = message
                        break

            if existing_message:
                # Update existing message
                if len(new_embeds) == 1:
                    await existing_message.edit(embed=new_embeds[0])
                else:
                    await existing_message.delete()
                    for new_embed in new_embeds:
                        await channel.send(embed=new_embed)
            else:
                # Create new message(s)
                for new_embed in new_embeds:
                    await channel.send(embed=new_embed)

    async def create_list_embed(self, list_name: str):
        cursor = self.cursors[list_name]
        cursor.execute("SELECT user_id, reason, proof, banned_at FROM banned_users ORDER BY banned_at DESC")
        users = cursor.fetchall()

        if not users:
            embed = discord.Embed(title=f"Users in {list_name} list", color=discord.Color.red(), timestamp=datetime.utcnow())
            embed.description = "No users found in this list."
            return [embed]

        embeds = []
        users_per_embed = 10
        total_embeds = math.ceil(len(users) / users_per_embed)

        for i in range(0, len(users), users_per_embed):
            embed = discord.Embed(title=f"Users in {list_name} list (Page {i//users_per_embed + 1}/{total_embeds})",
                                  color=discord.Color.red(), timestamp=datetime.utcnow())

            for user_id, reason, proof, banned_at in users[i:i+users_per_embed]:
                user = self.bot.get_user(user_id) or f"Unknown User ({user_id})"
                embed.add_field(
                    name=f"{user}",
                    value=f"Reason: {reason}\nProof: {proof}\nBanned at: {banned_at}",
                    inline=False
                )

            embed.set_footer(text=f"Total users: {len(users)}")
            embeds.append(embed)

        return embeds

    async def check_subscribed_servers(self, user_id: int, list_name: str):
        """Check all subscribed servers for a newly banned user."""
        for guild in self.bot.guilds:
            guild_config = await self.config.guild(guild).all()
            if list_name in guild_config['subscribed_lists']:
                member = guild.get_member(user_id)
                if member:
                    cursor = self.cursors[list_name]
                    cursor.execute("SELECT reason, proof FROM banned_users WHERE user_id = ?", (user_id,))
                    ban_info = cursor.fetchone()
                    if ban_info:
                        reason, proof = ban_info
                        try:
                            await member.ban(reason=f"Global Ban List: {list_name}")
                            if guild_config['notify_channel']:
                                channel = guild.get_channel(guild_config['notify_channel'])
                                if channel:
                                    await channel.send(f"{member} was banned due to being added to the {list_name} global ban list.")
                            await self.general_log(guild, "User Banned", member, list_name, reason, proof)
                        except discord.Forbidden:
                            print(f"Failed to ban {member.name} from {guild.name} - Insufficient permissions")

    async def unban_from_subscribed_guilds(self, user_id: int, list_name: str):
        """Unban a user from all guilds subscribed to the specified list."""
        for guild in self.bot.guilds:
            guild_config = await self.config.guild(guild).all()
            if list_name in guild_config['subscribed_lists']:
                try:
                    # Check if the user is banned
                    try:
                        ban_entry = await guild.fetch_ban(discord.Object(id=user_id))
                    except discord.NotFound:
                        continue  # User is not banned in this guild

                    # Unban the user
                    await guild.unban(discord.Object(id=user_id), reason=f"Removed from Global Ban List: {list_name}")

                    if guild_config['notify_channel']:
                        channel = guild.get_channel(guild_config['notify_channel'])
                        if channel:
                            user_obj = await self.bot.fetch_user(user_id)
                            user_str = f"{user_obj} ({user_id})" if user_obj else f"User ID: {user_id}"
                            await channel.send(f"{user_str} has been unbanned due to being removed from the {list_name} global ban list.")

                    await self.general_log(guild, "User Unbanned", user_id, list_name, "Removed from global ban list", "N/A")
                except discord.Forbidden:
                    print(f"Failed to unban user ID {user_id} from {guild.name} - Insufficient permissions")
                except discord.HTTPException as e:
                    print(f"Failed to unban user ID {user_id} from {guild.name} - {str(e)}")

    async def check_existing_members(self, guild: discord.Guild, list_name: str):
        cursor = self.cursors[list_name]
        cursor.execute("SELECT user_id FROM banned_users")
        banned_users = [row[0] for row in cursor.fetchall()]

        total_members = len(guild.members)
        banned_count = 0

        for member in guild.members:
            if member.id in banned_users:
                try:
                    await member.ban(reason=f"Global Ban List: {list_name}")
                    banned_count += 1
                    await self.general_log(guild, "User Banned", member, list_name, "Existing member ban", "N/A")
                except discord.Forbidden:
                    print(f"Failed to ban {member.name} from {guild.name} - Insufficient permissions")

        if guild.system_channel:
            await guild.system_channel.send(f"Finished checking existing members. Banned {banned_count} out of {total_members} members.")

    async def periodic_check(self):
        while not self.is_unloading:
            try:
                await asyncio.sleep(3600)  # Check every hour
                if self.is_unloading:
                    break
                for guild in self.bot.guilds:
                    guild_config = await self.config.guild(guild).all()
                    if guild_config['auto_ban']:
                        await self.check_guild_members(guild, guild_config['subscribed_lists'])
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"Error in periodic check: {str(e)}")

    async def check_guild_members(self, guild: discord.Guild, subscribed_lists: list):
        if self.is_unloading:
            return
        for member in guild.members:
            for list_name in subscribed_lists:
                if list_name not in self.lists or self.is_unloading:
                    continue
                cursor = self.cursors[list_name]
                try:
                    cursor.execute("SELECT reason, proof FROM banned_users WHERE user_id = ?", (member.id,))
                    ban_info = cursor.fetchone()
                    if ban_info:
                        reason, proof = ban_info
                        try:
                            await member.ban(reason=f"Global Ban List: {list_name} - {reason}")
                            guild_config = await self.config.guild(guild).all()
                            if guild_config['notify_channel']:
                                channel = guild.get_channel(guild_config['notify_channel'])
                                if channel:
                                    await channel.send(f"{member} was banned due to being on the {list_name} global ban list.")
                            await self.general_log(guild, "User Banned", member, list_name, reason, proof)
                        except discord.Forbidden:
                            print(f"Failed to ban {member.name} from {guild.name} - Insufficient permissions")
                except sqlite3.ProgrammingError:
                    if not self.is_unloading:
                        print(f"Database for {list_name} is closed unexpectedly.")

    async def is_authorized(self, user: discord.User) -> bool:
        """Check if a user is authorized to manage the global ban list."""
        authorized_users = await self.config.authorized_users()
        return user.id in authorized_users or await self.bot.is_owner(user)

    async def owner_log(self, action: str, user: discord.User, details: str):
        """Log owner actions."""
        channel_id = await self.config.owner_log_channel()
        if not channel_id:
            return

        channel = self.bot.get_channel(channel_id)
        if not channel:
            return

        embed = discord.Embed(title="Owner Action Log", color=discord.Color.blue(), timestamp=datetime.utcnow())
        embed.add_field(name="Action", value=action, inline=False)
        embed.add_field(name="User", value=f"{user} ({user.id})", inline=False)
        embed.add_field(name="Details", value=details, inline=False)
        embed.set_footer(text=f"User ID: {user.id}")

        await channel.send(embed=embed)

    async def general_log(self, guild: discord.Guild, action: str, user: typing.Union[discord.User, int], list_name: str, reason: str, proof: str):
        """Log general actions for a specific guild."""
        channel_id = await self.config.guild(guild).general_log_channel()
        if not channel_id:
            return

        channel = guild.get_channel(channel_id)
        if not channel:
            return

        embed = discord.Embed(title="Global Ban List Log", color=discord.Color.red(), timestamp=datetime.utcnow())
        embed.add_field(name="Action", value=action, inline=False)

        if isinstance(user, (discord.User, discord.Member)):
            user_str = f"{user} ({user.id})"
        else:
            user_obj = await self.bot.fetch_user(user)
            user_str = f"{user_obj} ({user})" if user_obj else f"User ID: {user}"

        embed.add_field(name="User", value=user_str, inline=False)
        embed.add_field(name="List", value=list_name, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Proof", value=proof, inline=False)
        embed.set_footer(text=f"User ID: {getattr(user, 'id', user)}")

        await channel.send(embed=embed)

    async def submit_appeal(self, user: discord.User, appeal_text: str):
        """Submit the appeal to the database and notify the appeal channel."""
        appeal_channel_id = await self.config.ban_appeal_channel()
        if appeal_channel_id:
            appeal_channel = self.bot.get_channel(appeal_channel_id)
            if appeal_channel:
                embed = discord.Embed(title="New Ban Appeal", color=discord.Color.blue())
                embed.add_field(name="User", value=f"{user} ({user.id})", inline=False)
                embed.add_field(name="Appeal", value=appeal_text, inline=False)

                async def handle_appeal_decision(view: Buttons, interaction: discord.Interaction):
                    decision = "approved" if interaction.data["custom_id"] == "approve_appeal" else "denied"
                    user_id = int(interaction.message.embeds[0].fields[0].value.split("(")[-1].split(")")[0])

                    if decision == "approved":
                        # Remove user from all ban lists
                        for list_name in self.lists:
                            cursor = self.cursors[list_name]
                            cursor.execute("DELETE FROM banned_users WHERE user_id = ?", (user_id,))
                            self.databases[list_name].commit()

                    appeal_user = self.bot.get_user(user_id)
                    if appeal_user:
                        await appeal_user.send(f"Your ban appeal has been {decision}.")

                    await interaction.message.edit(content=f"Appeal {decision} by {interaction.user}", view=None)
                    await self.owner_log("Appeal Decision", interaction.user, f"Appeal for user {user_id} was {decision}")

                buttons = Buttons(
                    timeout=600,
                    buttons=[
                        {"style": discord.ButtonStyle.green, "label": "Approve", "custom_id": "approve_appeal"},
                        {"style": discord.ButtonStyle.red, "label": "Deny", "custom_id": "deny_appeal"}
                    ],
                    members=self.bot.owner_ids,
                    function=handle_appeal_decision
                )

                await appeal_channel.send(embed=embed, view=buttons)

        await self.owner_log("Appeal Submitted", user, f"Appeal text: {appeal_text}")

    async def autocomplete_list_name(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=list_name, value=list_name)
            for list_name in self.lists if current.lower() in list_name.lower()
        ]

    async def autocomplete_banned_user(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        list_name = interaction.namespace.list_name
        if list_name not in self.lists:
            return []

        cursor = self.cursors[list_name]
        cursor.execute("SELECT user_id FROM banned_users")
        banned_users = [row[0] for row in cursor.fetchall()]

        choices = []
        for user_id in banned_users:
            user = self.bot.get_user(user_id)
            if user and (current.lower() in user.name.lower() or current in str(user_id)):
                choices.append(app_commands.Choice(name=f"{user.name} ({user_id})", value=str(user_id)))

        return choices[:25]  # Discord limits to 25 choices

    def cog_unload(self):
        self.is_unloading = True
        if self.periodic_check_task:
            self.periodic_check_task.cancel()
        asyncio.create_task(self._finish_unload())

    async def _finish_unload(self):
        await asyncio.sleep(1)  # Wait for 1 second
        for db in self.databases.values():
            db.close()
