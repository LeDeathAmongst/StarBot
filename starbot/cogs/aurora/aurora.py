#   _____                         _
#  / ____|                       (_)
# | (___   ___  __ _ _____      ___ _ __ ___  _ __ ___   ___ _ __
#  \___ \ / _ \/ _` / __\ \ /\ / / | '_ ` _ \| '_ ` _ \ / _ \ '__|
#  ____) |  __/ (_| \__ \\ V  V /| | | | | | | | | | | |  __/ |
# |_____/ \___|\__,_|___/ \_/\_/ |_|_| |_| |_|_| |_| |_|\___|_|

import json
import os
import sqlite3
import time
from datetime import datetime, timedelta, timezone
from math import ceil

import discord
from discord import Object
from discord.ext import tasks
from starbot.core import app_commands, commands, data_manager
from starbot.core.app_commands import Choice
from starbot.core.bot import Red
from starbot.core.commands.converter import parse_relativedelta, parse_timedelta
from starbot.core.utils.chat_formatting import box, error, humanize_list, humanize_timedelta, warning

from aurora.importers.aurora import ImportAuroraView
from aurora.importers.galacticbot import ImportGalacticBotView
from aurora.menus.addrole import Addrole
from aurora.menus.guild import Guild
from aurora.menus.immune import Immune
from aurora.menus.overrides import Overrides
from aurora.utilities.config import config, register_config
from aurora.utilities.database import connect, create_guild_table, fetch_case, mysql_log
from aurora.utilities.factory import addrole_embed, case_factory, changes_factory, evidenceformat_factory, guild_embed, immune_embed, message_factory, overrides_embed
from aurora.utilities.logger import logger
from aurora.utilities.utils import check_moddable, check_permissions, convert_timedelta_to_str, fetch_channel_dict, fetch_user_dict, generate_dict, get_footer_image, log, send_evidenceformat, timedelta_from_relativedelta

from Star-Utils import Cog, CogsUtils

class Aurora(Cog):
    """Aurora is a fully-featured moderation system.
    It is heavily inspired by GalacticBot, and is designed to be a more user-friendly alternative to Red's core Mod cogs.
    This cog stores all of its data in an SQLite database."""

    async def red_delete_data_for_user(self, *, requester, user_id: int):
        if requester == "discord_deleted_user":
            await config.user_from_id(user_id).clear()

            database = connect()
            cursor = database.cursor()

            cursor.execute("SHOW TABLES;")
            tables = [table[0] for table in cursor.fetchall()]

            condition = "target_id = %s OR moderator_id = %s;"

            for table in tables:
                delete_query = f"DELETE FROM {table[0]} WHERE {condition}"
                cursor.execute(delete_query, (user_id, user_id))

            database.commit()
            cursor.close()
            database.close()
        if requester == "owner":
            await config.user_from_id(user_id).clear()
        if requester == "user":
            await config.user_from_id(user_id).clear()
        if requester == "user_strict":
            await config.user_from_id(user_id).clear()
        else:
            logger.warning(
                "Invalid requester passed to red_delete_data_for_user: %s", requester
            )

    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot
        register_config(config)
        self.handle_expiry.start()
        self.logs = CogsUtils.get_logger("Snipe")

    async def cog_load(self):
        """This method prepares the database schema for all of the guilds the bot is currently in."""
        guilds: list[discord.Guild] = self.bot.guilds

        try:
            for guild in guilds:
                if not await self.bot.cog_disabled_in_guild(self, guild):
                    await create_guild_table(guild)

        except ConnectionRefusedError:
            return

    async def cog_unload(self):
        self.handle_expiry.cancel()

    @commands.Cog.listener("on_guild_join")
    async def db_generate_guild_join(self, guild: discord.Guild):
        """This method prepares the database schema whenever the bot joins a guild."""
        if not await self.bot.cog_disabled_in_guild(self, guild):
            try:
                await create_guild_table(guild)
            except ConnectionRefusedError:
                return

    @commands.Cog.listener("on_member_join")
    async def addrole_on_member_join(self, member: discord.Member):
        """This method automatically adds roles to users when they join the server."""
        if not await self.bot.cog_disabled_in_guild(self, member.guild):
            query = f"""SELECT moderation_id, role_id, reason FROM moderation_{member.guild.id} WHERE target_id = ? AND moderation_type = 'ADDROLE' AND expired = 0 AND resolved = 0;"""
            database = connect()
            cursor = database.cursor()
            cursor.execute(query, (member.id,))
            results = cursor.fetchall()
            for result in results:
                role = member.guild.get_role(result[1])
                reason = result[2]
                await member.add_roles(role, reason=f"Role automatically added on member rejoin for: {reason} (Case #{result[0]:,})")

    @commands.Cog.listener("on_audit_log_entry_create")
    async def autologger(self, entry: discord.AuditLogEntry):
        """This method automatically logs moderations done by users manually ("right clicks")."""
        if not await self.bot.cog_disabled_in_guild(self, entry.guild):
            if await config.guild(entry.guild).ignore_other_bots() is True:
                if entry.user.bot or entry.target.bot:
                    return
            else:
                if entry.user.id == self.bot.user.id:
                    return

            duration = "NULL"

            if entry.reason:
                reason = entry.reason + " (This action was performed without the bot.)"

            else:
                reason = "This action was performed without the bot."

            if entry.action == discord.AuditLogAction.kick:
                moderation_type = "KICK"

            elif entry.action == discord.AuditLogAction.ban:
                moderation_type = "BAN"

            elif entry.action == discord.AuditLogAction.unban:
                moderation_type = "UNBAN"

            elif entry.action == discord.AuditLogAction.member_update:
                if entry.after.timed_out_until is not None:
                    timed_out_until_aware = entry.after.timed_out_until.replace(
                        tzinfo=timezone.utc
                    )
                    duration_datetime = timed_out_until_aware - datetime.now(
                        tz=timezone.utc
                    )
                    minutes = round(duration_datetime.total_seconds() / 60)
                    duration = timedelta(minutes=minutes)
                    moderation_type = "MUTE"
                else:
                    moderation_type = "UNMUTE"
            else:
                return

            await mysql_log(
                entry.guild.id,
                entry.user.id,
                moderation_type,
                "USER",
                entry.target.id,
                0,
                duration,
                reason,
            )

    #######################################################################################################################
    ### COMMANDS
    #######################################################################################################################

    @app_commands.command(name="note")
    async def note(
        self,
        interaction: discord.Interaction,
        target: discord.User,
        reason: str,
        silent: bool = None,
    ):
        """Add a note to a user.

        Parameters
        -----------
        target: discord.User
            Who are you noting?
        reason: str
            Why are you noting this user?
        silent: bool
            Should the user be messaged?"""
        if not await check_moddable(target, interaction, ["moderate_members"]):
            return

        await interaction.response.send_message(
            content=f"{target.mention} has recieved a note!\n**Reason** - `{reason}`"
        )

        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="note",
                    response=await interaction.original_response(),
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "NOTE",
            "USER",
            target.id,
            0,
            "NULL",
            reason,
        )
        await interaction.edit_original_response(
            content=f"{target.mention} has received a note! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`"
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="warn")
    async def warn(
        self,
        interaction: discord.Interaction,
        target: discord.Member,
        reason: str,
        silent: bool = None,
    ):
        """Warn a user.

        Parameters
        -----------
        target: discord.Member
            Who are you warning?
        reason: str
            Why are you warning this user?
        silent: bool
            Should the user be messaged?"""
        if not await check_moddable(target, interaction, ["moderate_members"]):
            return

        await interaction.response.send_message(
            content=f"{target.mention} has been warned!\n**Reason** - `{reason}`"
        )

        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="warned",
                    response=await interaction.original_response(),
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "WARN",
            "USER",
            target.id,
            0,
            "NULL",
            reason,
        )
        await interaction.edit_original_response(
            content=f"{target.mention} has been warned! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`"
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="addrole")
    async def addrole(
        self,
        interaction: discord.Interaction,
        target: discord.Member,
        role: discord.Role,
        reason: str,
        duration: str = None,
        silent: bool = None,
    ):
        """Add a role to a user.

        Parameters
        -----------
        target: discord.Member
            Who are you adding a role to?
        role: discord.Role
            What role are you adding to the target?
        reason: str
            Why are you adding a role to this user?
        duration: str
            How long are you adding this role for?
        silent: bool
            Should the user be messaged?"""
        addrole_whitelist = await config.guild(interaction.guild).addrole_whitelist()

        if not addrole_whitelist:
            await interaction.response.send_message(
                content=error("There are no whitelisted roles set for this server!"),
                ephemeral=True,
            )
            return

        if duration is not None:
            parsed_time = parse_timedelta(duration)
            if parsed_time is None:
                await interaction.response.send_message(
                    content=error("Please provide a valid duration!"), ephemeral=True
                )
                return
        else:
            parsed_time = "NULL"

        if role.id not in addrole_whitelist:
            await interaction.response.send_message(
                content=error("That role isn't whitelisted!"), ephemeral=True
            )
            return

        if not await check_moddable(
            target, interaction, ["moderate_members", "manage_roles"]
        ):
            return

        if role.id in [user_role.id for user_role in target.roles]:
            await interaction.response.send_message(
                content=error(f"{target.mention} already has this role!"),
                ephemeral=True,
            )
            return

        await interaction.response.defer()
        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="addrole",
                    response=await interaction.original_response(),
                    duration=parsed_time,
                    role=role,
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        await target.add_roles(
            role,
            reason=f"Role added by {interaction.user.id}{' for ' + humanize_timedelta(timedelta=parsed_time) if parsed_time != 'NULL' else ''} for: {reason}",
        )
        response: discord.WebhookMessage = await interaction.followup.send(
            content=f"{target.mention} has been given the {role.mention} role{' for ' + humanize_timedelta(timedelta=parsed_time) if parsed_time != 'NULL' else ''}!\n**Reason** - `{reason}`"
        )

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "ADDROLE",
            "USER",
            target.id,
            role.id,
            parsed_time,
            reason,
        )
        await response.edit(
            content=f"{target.mention} has been given the {role.mention} role{' for ' + humanize_timedelta(timedelta=parsed_time) if parsed_time != 'NULL' else ''}! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`",
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="removerole")
    async def removerole(
        self,
        interaction: discord.Interaction,
        target: discord.Member,
        role: discord.Role,
        reason: str,
        duration: str = None,
        silent: bool = None,
    ):
        """Remove a role from a user.

        Parameters
        -----------
        target: discord.Member
            Who are you removing a role from?
        role: discord.Role
            What role are you removing from the target?
        reason: str
            Why are you removing a role from this user?
        duration: str
            How long are you removing this role for?
        silent: bool
            Should the user be messaged?"""
        addrole_whitelist = await config.guild(interaction.guild).addrole_whitelist()

        if not addrole_whitelist:
            await interaction.response.send_message(
                content=error("There are no whitelisted roles set for this server!"),
                ephemeral=True,
            )
            return

        if duration is not None:
            parsed_time = parse_timedelta(duration)
            if parsed_time is None:
                await interaction.response.send_message(
                    content=error("Please provide a valid duration!"), ephemeral=True
                )
                return
        else:
            parsed_time = "NULL"

        if role.id not in addrole_whitelist:
            await interaction.response.send_message(
                content=error("That role isn't whitelisted!"), ephemeral=True
            )
            return

        if not await check_moddable(
            target, interaction, ["moderate_members", "manage_roles"]
        ):
            return

        if role.id not in [user_role.id for user_role in target.roles]:
            await interaction.response.send_message(
                content=error(f"{target.mention} does not have this role!"),
                ephemeral=True,
            )
            return

        await interaction.response.defer()
        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="removerole",
                    response=await interaction.original_response(),
                    duration=parsed_time,
                    role=role,
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        await target.remove_roles(
            role,
            reason=f"Role removed by {interaction.user.id}{' for ' + humanize_timedelta(timedelta=parsed_time) if parsed_time != 'NULL' else ''} for: {reason}",
        )
        response: discord.WebhookMessage = await interaction.followup.send(
            content=f"{target.mention} has had the {role.mention} role removed{' for ' + humanize_timedelta(timedelta=parsed_time) if parsed_time != 'NULL' else ''}!\n**Reason** - `{reason}`"
        )

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "REMOVEROLE",
            "USER",
            target.id,
            role.id,
            parsed_time,
            reason,
        )
        await response.edit(
            content=f"{target.mention} has had the {role.mention} role removed{' for ' + humanize_timedelta(timedelta=parsed_time) if parsed_time != 'NULL' else ''}! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`",
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="mute")
    async def mute(
        self,
        interaction: discord.Interaction,
        target: discord.Member,
        duration: str,
        reason: str,
        silent: bool = None,
    ):
        """Mute a user.

        Parameters
        -----------
        target: discord.Member
            Who are you unbanning?
        duration: str
            How long are you muting this user for?
        reason: str
            Why are you unbanning this user?
        silent: bool
            Should the user be messaged?"""
        if not await check_moddable(target, interaction, ["moderate_members"]):
            return

        if target.is_timed_out() is True:
            await interaction.response.send_message(
                error(f"{target.mention} is already muted!"),
                allowed_mentions=discord.AllowedMentions(users=False),
                ephemeral=True,
            )
            return

        try:
            parsed_time = parse_timedelta(duration, maximum=timedelta(days=28))
            if parsed_time is None:
                await interaction.response.send_message(
                    error("Please provide a valid duration!"), ephemeral=True
                )
                return
        except commands.BadArgument:
            await interaction.response.send_message(
                error("Please provide a duration that is less than 28 days."), ephemeral=True
            )
            return

        await target.timeout(
            parsed_time, reason=f"Muted by {interaction.user.id} for: {reason}"
        )

        await interaction.response.send_message(
            content=f"{target.mention} has been muted for {humanize_timedelta(timedelta=parsed_time)}!\n**Reason** - `{reason}`"
        )

        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="muted",
                    response=await interaction.original_response(),
                    duration=parsed_time,
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "MUTE",
            "USER",
            target.id,
            0,
            parsed_time,
            reason,
        )
        await interaction.edit_original_response(
            content=f"{target.mention} has been muted for {humanize_timedelta(timedelta=parsed_time)}! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`"
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="unmute")
    async def unmute(
        self,
        interaction: discord.Interaction,
        target: discord.Member,
        reason: str = None,
        silent: bool = None,
    ):
        """Unmute a user.

        Parameters
        -----------
        target: discord.user
            Who are you unmuting?
        reason: str
            Why are you unmuting this user?
        silent: bool
            Should the user be messaged?"""
        if not await check_moddable(target, interaction, ["moderate_members"]):
            return

        if target.is_timed_out() is False:
            await interaction.response.send_message(
                error(f"{target.mention} is not muted!"),
                allowed_mentions=discord.AllowedMentions(users=False),
                ephemeral=True,
            )
            return

        if reason:
            await target.timeout(
                None, reason=f"Unmuted by {interaction.user.id} for: {reason}"
            )
        else:
            await target.timeout(None, reason=f"Unbanned by {interaction.user.id}")
            reason = "No reason given."

        await interaction.response.send_message(
            content=f"{target.mention} has been unmuted!\n**Reason** - `{reason}`"
        )

        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="unmuted",
                    response=await interaction.original_response(),
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "UNMUTE",
            "USER",
            target.id,
            0,
            "NULL",
            reason,
        )
        await interaction.edit_original_response(
            content=f"{target.mention} has been unmuted! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`"
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="kick")
    async def kick(
        self,
        interaction: discord.Interaction,
        target: discord.Member,
        reason: str,
        silent: bool = None,
    ):
        """Kick a user.

        Parameters
        -----------
        target: discord.user
            Who are you kicking?
        reason: str
            Why are you kicking this user?
        silent: bool
            Should the user be messaged?"""
        if not await check_moddable(target, interaction, ["kick_members"]):
            return

        await interaction.response.send_message(
            content=f"{target.mention} has been kicked!\n**Reason** - `{reason}`"
        )

        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="kicked",
                    response=await interaction.original_response(),
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        await target.kick(reason=f"Kicked by {interaction.user.id} for: {reason}")

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "KICK",
            "USER",
            target.id,
            0,
            "NULL",
            reason,
        )
        await interaction.edit_original_response(
            content=f"{target.mention} has been kicked! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`"
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="ban")
    @app_commands.choices(
        delete_messages=[
            Choice(name="None", value=0),
            Choice(name="1 Hour", value=3600),
            Choice(name="12 Hours", value=43200),
            Choice(name="1 Day", value=86400),
            Choice(name="3 Days", value=259200),
            Choice(name="7 Days", value=604800),
        ]
    )
    async def ban(
        self,
        interaction: discord.Interaction,
        target: discord.User,
        reason: str,
        duration: str = None,
        delete_messages: Choice[int] = None,
        silent: bool = None,
    ):
        """Ban a user.

        Parameters
        -----------
        target: discord.user
            Who are you banning?
        duration: str
            How long are you banning this user for?
        reason: str
            Why are you banning this user?
        delete_messages: Choices[int]
            How many days of messages to delete?
        silent: bool
            Should the user be messaged?"""
        if not await check_moddable(target, interaction, ["ban_members"]):
            return

        if delete_messages is None:
            delete_messages_seconds = 0
        else:
            delete_messages_seconds = delete_messages.value

        try:
            await interaction.guild.fetch_ban(target)
            await interaction.response.send_message(
                content=error(f"{target.mention} is already banned!"), ephemeral=True
            )
            return
        except discord.errors.NotFound:
            pass

        if duration:
            parsed_time = parse_relativedelta(duration)
            if parsed_time is None:
                await interaction.response.send_message(
                    content=error("Please provide a valid duration!"), ephemeral=True
                )
                return
            try:
                parsed_time = timedelta_from_relativedelta(parsed_time)
            except ValueError:
                await interaction.response.send_message(
                    content=error("Please provide a valid duration!"), ephemeral=True
                )
                return

            await interaction.response.send_message(
                content=f"{target.mention} has been banned for {humanize_timedelta(timedelta=parsed_time)}!\n**Reason** - `{reason}`"
            )

            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="tempbanned",
                    response=await interaction.original_response(),
                    duration=parsed_time,
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

            await interaction.guild.ban(
                target,
                reason=f"Tempbanned by {interaction.user.id} for: {reason} (Duration: {parsed_time})",
                delete_message_seconds=delete_messages_seconds,
            )

            moderation_id = await mysql_log(
                interaction.guild.id,
                interaction.user.id,
                "TEMPBAN",
                "USER",
                target.id,
                0,
                parsed_time,
                reason,
            )
            await interaction.edit_original_response(
                content=f"{target.mention} has been banned for {humanize_timedelta(timedelta=parsed_time)}! (Case `#{moderation_id}`)\n**Reason** - `{reason}`"
            )
            await log(interaction, moderation_id)

            case = await fetch_case(moderation_id, interaction.guild.id)
            await send_evidenceformat(interaction, case)
        else:
            await interaction.response.send_message(
                content=f"{target.mention} has been banned!\n**Reason** - `{reason}`"
            )

            if silent is None:
                silent = not await config.guild(interaction.guild).dm_users()
            if silent is False:
                try:
                    embed = embed = await message_factory(
                        await self.bot.get_embed_color(interaction.channel),
                        guild=interaction.guild,
                        moderator=interaction.user,
                        reason=reason,
                        moderation_type="banned",
                        response=await interaction.original_response(),
                    )
                    await target.send(embed=embed, file=get_footer_image(self))
                except discord.errors.HTTPException:
                    pass

            await interaction.guild.ban(
                target,
                reason=f"Banned by {interaction.user.id} for: {reason}",
                delete_message_seconds=delete_messages_seconds,
            )

            moderation_id = await mysql_log(
                interaction.guild.id,
                interaction.user.id,
                "BAN",
                "USER",
                target.id,
                0,
                "NULL",
                reason,
            )
            await interaction.edit_original_response(
                content=f"{target.mention} has been banned! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`"
            )
            await log(interaction, moderation_id)

            case = await fetch_case(moderation_id, interaction.guild.id)
            await send_evidenceformat(interaction, case)

    @app_commands.command(name="unban")
    async def unban(
        self,
        interaction: discord.Interaction,
        target: discord.User,
        reason: str = None,
        silent: bool = None,
    ):
        """Unban a user.

        Parameters
        -----------
        target: discord.user
            Who are you unbanning?
        reason: str
            Why are you unbanning this user?
        silent: bool
            Should the user be messaged?"""
        if not await check_moddable(target, interaction, ["ban_members"]):
            return

        try:
            await interaction.guild.fetch_ban(target)
        except discord.errors.NotFound:
            await interaction.response.send_message(
                content=error(f"{target.mention} is not banned!"), ephemeral=True
            )
            return

        if reason:
            await interaction.guild.unban(
                target, reason=f"Unbanned by {interaction.user.id} for: {reason}"
            )
        else:
            await interaction.guild.unban(
                target, reason=f"Unbanned by {interaction.user.id}"
            )
            reason = "No reason given."

        await interaction.response.send_message(
            content=f"{target.mention} has been unbanned!\n**Reason** - `{reason}`"
        )

        if silent is None:
            silent = not await config.guild(interaction.guild).dm_users()
        if silent is False:
            try:
                embed = await message_factory(
                    await self.bot.get_embed_color(interaction.channel),
                    guild=interaction.guild,
                    moderator=interaction.user,
                    reason=reason,
                    moderation_type="unbanned",
                    response=await interaction.original_response(),
                )
                await target.send(embed=embed, file=get_footer_image(self))
            except discord.errors.HTTPException:
                pass

        moderation_id = await mysql_log(
            interaction.guild.id,
            interaction.user.id,
            "UNBAN",
            "USER",
            target.id,
            0,
            "NULL",
            reason,
        )
        await interaction.edit_original_response(
            content=f"{target.mention} has been unbanned! (Case `#{moderation_id:,}`)\n**Reason** - `{reason}`"
        )
        await log(interaction, moderation_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        await send_evidenceformat(interaction, case)

    @app_commands.command(name="history")
    async def history(
        self,
        interaction: discord.Interaction,
        target: discord.User = None,
        moderator: discord.User = None,
        pagesize: app_commands.Range[int, 1, 20] = None,
        page: int = 1,
        ephemeral: bool = None,
        inline: bool = None,
        export: bool = False,
    ):
        """List previous infractions.

        Parameters
        -----------
        target: discord.User
            User whose infractions to query, overrides moderator if both are given
        moderator: discord.User
            Query by moderator
        pagesize: app_commands.Range[int, 1, 25]
            Amount of infractions to list per page
        page: int
            Page to select
        ephemeral: bool
            Hide the command response
        inline: bool
            Display infractions in a grid arrangement (does not look very good)
        export: bool
            Exports the server's entire moderation history to a JSON file"""
        if ephemeral is None:
            ephemeral = (
                await config.user(interaction.user).history_ephemeral()
                or await config.guild(interaction.guild).history_ephemeral()
                or False
            )

        if inline is None:
            inline = (
                await config.user(interaction.user).history_inline()
                or await config.guild(interaction.guild).history_inline()
                or False
            )

        if pagesize is None:
            if inline is True:
                pagesize = (
                    await config.user(interaction.user).history_inline_pagesize()
                    or await config.guild(interaction.guild).history_inline_pagesize()
                    or 6
                )
            else:
                pagesize = (
                    await config.user(interaction.user).history_pagesize()
                    or await config.guild(interaction.guild).history_pagesize()
                    or 5
                )

        await interaction.response.defer(ephemeral=ephemeral)

        permissions = check_permissions(
            interaction.client.user, ["embed_links"], interaction
        )
        if permissions:
            await interaction.followup.send(
                error(
                    f"I do not have the `{permissions}` permission, required for this action."
                ),
                ephemeral=True,
            )
            return

        database = connect()

        if export:
            database.row_factory = sqlite3.Row
            cursor = database.cursor()

            query = f"""SELECT *
                FROM moderation_{interaction.guild.id}
                ORDER BY moderation_id DESC;"""
            cursor.execute(query)

            results = cursor.fetchall()

            cases = []
            for result in results:
                case = dict(result)
                cases.append(case)

            try:
                filename = (
                    str(data_manager.cog_data_path(cog_instance=self))
                    + str(os.sep)
                    + f"moderation_{interaction.guild.id}.json"
                )

                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(cases, f, indent=2)

                await interaction.followup.send(
                    file=discord.File(
                        filename, f"moderation_{interaction.guild.id}.json"
                    ),
                    ephemeral=ephemeral,
                )

                os.remove(filename)
            except json.JSONDecodeError as e:
                await interaction.followup.send(
                    content=error(
                        "An error occured while exporting the moderation history.\nError:\n"
                    )
                    + box(e, "py"),
                    ephemeral=ephemeral,
                )
            cursor.close()
            database.close()
            return

        cursor = database.cursor()

        if target:
            query = f"""SELECT *
                FROM moderation_{interaction.guild.id}
                WHERE target_id = ?
                ORDER BY moderation_id DESC;"""
            cursor.execute(query, (target.id,))
        elif moderator:
            query = f"""SELECT *
                FROM moderation_{interaction.guild.id}
                WHERE moderator_id = ?
                ORDER BY moderation_id DESC;"""
            cursor.execute(query, (moderator.id,))
        else:
            query = f"""SELECT *
                FROM moderation_{interaction.guild.id}
                ORDER BY moderation_id DESC;"""
            cursor.execute(query)

        results = cursor.fetchall()
        result_dict_list = []

        for result in results:
            case_dict = generate_dict(result)
            if case_dict["moderation_id"] == 0:
                continue
            result_dict_list.append(case_dict)

        case_quantity = len(result_dict_list)
        page_quantity = ceil(case_quantity / pagesize)
        start_index = (page - 1) * pagesize
        end_index = page * pagesize

        embed = discord.Embed(color=await self.bot.get_embed_color(interaction.channel))
        embed.set_author(icon_url=interaction.guild.icon.url, name="Infraction History")
        embed.set_footer(
            text=f"Page {page:,}/{page_quantity:,} | {case_quantity:,} Results"
        )

        memory_dict = {}

        for case in result_dict_list[start_index:end_index]:
            if case["target_id"] not in memory_dict:
                if case["target_type"] == "USER":
                    memory_dict[str(case["target_id"])] = await fetch_user_dict(
                        interaction.client, case["target_id"]
                    )
                elif case["target_type"] == "CHANNEL":
                    memory_dict[str(case["target_id"])] = await fetch_channel_dict(
                        interaction.guild, case["target_id"]
                    )
            target_user = memory_dict[str(case["target_id"])]

            if case["target_type"] == "USER":
                target_name = (
                    f"`{target_user['name']}`"
                    if target_user["discriminator"] == "0"
                    else f"`{target_user['name']}#{target_user['discriminator']}`"
                )
            elif case["target_type"] == "CHANNEL":
                target_name = f"`{target_user['mention']}`"

            if case["moderator_id"] not in memory_dict:
                memory_dict[str(case["moderator_id"])] = await fetch_user_dict(
                    interaction.client, case["moderator_id"]
                )
            moderator_user = memory_dict[str(case["moderator_id"])]
            moderator_name = (
                f"`{moderator_user['name']}`"
                if moderator_user["discriminator"] == "0"
                else f"`{moderator_user['name']}#{moderator_user['discriminator']}`"
            )

            field_name = f"Case #{case['moderation_id']:,} ({str.title(case['moderation_type'])})"
            field_value = f"**Target:** {target_name} ({target_user['id']})\n**Moderator:** {moderator_name} ({moderator_user['id']})"

            if len(case["reason"]) > 125:
                field_value += f"\n**Reason:** `{str(case['reason'])[:125]}...`"
            else:
                field_value += f"\n**Reason:** `{str(case['reason'])}`"

            if case["duration"] != "NULL":
                td = timedelta(
                    **{
                        unit: int(val)
                        for unit, val in zip(
                            ["hours", "minutes", "seconds"], case["duration"].split(":")
                        )
                    }
                )
                duration_embed = (
                    f"{humanize_timedelta(timedelta=td)} | <t:{case['end_timestamp']}:R>"
                    if bool(case["expired"]) is False
                    else f"{humanize_timedelta(timedelta=td)} | Expired"
                )
                field_value += f"\n**Duration:** {duration_embed}"

            field_value += (
                f"\n**Timestamp:** <t:{case['timestamp']}> | <t:{case['timestamp']}:R>"
            )

            if case["role_id"] != "0":
                role = interaction.guild.get_role(int(case["role_id"]))
                if role is not None:
                    field_value += f"\n**Role:** {role.mention}"
                else:
                    field_value += f"\n**Role:** Deleted Role ({case['role_id']})"

            if bool(case["resolved"]):
                field_value += "\n**Resolved:** True"

            embed.add_field(name=field_name, value=field_value, inline=inline)

        await interaction.followup.send(embed=embed, ephemeral=ephemeral)

    @app_commands.command(name="resolve")
    async def resolve(
        self, interaction: discord.Interaction, case: int, reason: str = None
    ):
        """Resolve a specific case.

        Parameters
        -----------
        case: int
            Case number of the case you're trying to resolve
        reason: str
            Reason for resolving case"""
        permissions = check_permissions(
            interaction.client.user,
            ["embed_links", "moderate_members", "ban_members"],
            interaction,
        )
        if permissions:
            await interaction.response.send_message(
                error(
                    f"I do not have the `{permissions}` permission, required for this action."
                ),
                ephemeral=True,
            )
            return

        database = connect()
        cursor = database.cursor()

        query_1 = (
            f"SELECT * FROM moderation_{interaction.guild.id} WHERE moderation_id = ?;"
        )
        cursor.execute(query_1, (case,))
        result_1 = cursor.fetchone()
        if result_1 is None or case == 0:
            await interaction.response.send_message(
                content=error(f"There is no moderation with a case number of {case}."),
                ephemeral=True,
            )
            return

        query_2 = f"SELECT * FROM moderation_{interaction.guild.id} WHERE moderation_id = ? AND resolved = 0;"
        cursor.execute(query_2, (case,))
        result_2 = cursor.fetchone()
        if result_2 is None:
            await interaction.response.send_message(
                content=error(
                    f"This moderation has already been resolved!\nUse `/case {case}` for more information."
                ),
                ephemeral=True,
            )
            return

        case_dict = generate_dict(result_2)
        if reason is None:
            reason = "No reason given."

        changes: list = case_dict["changes"]
        if len(changes) > 25:
            await interaction.response.send_message(
                content=error(
                    "Due to limitations with Discord's embed system, you cannot edit a case more than 25 times."
                ),
                ephemeral=True,
            )
            return
        if not changes:
            changes.append(
                {
                    "type": "ORIGINAL",
                    "timestamp": case_dict["timestamp"],
                    "reason": case_dict["reason"],
                    "user_id": case_dict["moderator_id"],
                }
            )
        changes.append(
            {
                "type": "RESOLVE",
                "timestamp": int(time.time()),
                "reason": reason,
                "user_id": interaction.user.id,
            }
        )

        if case_dict["moderation_type"] in ["UNMUTE", "UNBAN"]:
            await interaction.response.send_message(
                content=error("You cannot resolve this type of moderation!"),
                ephemeral=True,
            )
            return

        if case_dict["moderation_type"] in ["MUTE", "TEMPBAN", "BAN"]:
            if case_dict["moderation_type"] == "MUTE":
                try:
                    member = await interaction.guild.fetch_member(
                        case_dict["target_id"]
                    )

                    await member.timeout(
                        None, reason=f"Case #{case:,} resolved by {interaction.user.id}"
                    )
                except discord.NotFound:
                    pass

            if case_dict["moderation_type"] in ["TEMPBAN", "BAN"]:
                try:
                    user = await interaction.client.fetch_user(case_dict["target_id"])

                    await interaction.guild.unban(
                        user, reason=f"Case #{case} resolved by {interaction.user.id}"
                    )
                except discord.NotFound:
                    pass

            resolve_query = f"UPDATE `moderation_{interaction.guild.id}` SET resolved = 1, changes = ?, resolved_by = ?, resolve_reason = ? WHERE moderation_id = ?"
        else:
            resolve_query = f"UPDATE `moderation_{interaction.guild.id}` SET resolved = 1, changes = ?, resolved_by = ?, resolve_reason = ? WHERE moderation_id = ?"

        cursor.execute(
            resolve_query,
            (
                json.dumps(changes),
                interaction.user.id,
                reason,
                case_dict["moderation_id"],
            ),
        )
        database.commit()

        embed = await case_factory(
            interaction=interaction,
            case_dict=await fetch_case(case, interaction.guild.id),
        )
        await interaction.response.send_message(
            content=f"✅ Moderation #{case:,} resolved!", embed=embed
        )
        await log(interaction, case, resolved=True)

        cursor.close()
        database.close()

    @app_commands.command(name="case")
    @app_commands.choices(
        export=[
            Choice(name="Export as File", value="file"),
            Choice(name="Export as Codeblock", value="codeblock"),
        ]
    )
    async def case(
        self,
        interaction: discord.Interaction,
        case: int,
        ephemeral: bool = None,
        evidenceformat: bool = False,
        changes: bool = False,
        export: Choice[str] = None,
    ):
        """Check the details of a specific case.

        Parameters
        -----------
        case: int
            What case are you looking up?
        ephemeral: bool
            Hide the command response
        changes: bool
            List the changes made to the case
        export: bool
            Export the case to a JSON file or codeblock"""
        permissions = check_permissions(
            interaction.client.user, ["embed_links"], interaction
        )
        if permissions:
            await interaction.response.send_message(
                error(
                    f"I do not have the `{permissions}` permission, required for this action."
                ),
                ephemeral=True,
            )
            return

        if ephemeral is None:
            ephemeral = (
                await config.user(interaction.user).history_ephemeral()
                or await config.guild(interaction.guild).history_ephemeral()
                or False
            )

        if case != 0:
            case_dict = await fetch_case(case, interaction.guild.id)
            if case_dict:
                if export:
                    if export.value == "file" or len(str(case_dict)) > 1800:
                        filename = (
                            str(data_manager.cog_data_path(cog_instance=self))
                            + str(os.sep)
                            + f"moderation_{interaction.guild.id}_case_{case}.json"
                        )

                        with open(filename, "w", encoding="utf-8") as f:
                            json.dump(case_dict, f, indent=2)

                        if export.value == "codeblock":
                            content = f"Case #{case:,} exported.\n" + warning(
                                "Case was too large to export as codeblock, so it has been uploaded as a `.json` file."
                            )
                        else:
                            content = f"Case #{case:,} exported."

                        await interaction.response.send_message(
                            content=content,
                            file=discord.File(
                                filename,
                                f"moderation_{interaction.guild.id}_case_{case}.json",
                            ),
                            ephemeral=ephemeral,
                        )

                        os.remove(filename)
                        return
                    await interaction.response.send_message(
                        content=box(json.dumps(case_dict, indent=2), 'json'),
                        ephemeral=ephemeral,
                    )
                    return
                if changes:
                    embed = await changes_factory(
                        interaction=interaction, case_dict=case_dict
                    )
                    await interaction.response.send_message(
                        embed=embed, ephemeral=ephemeral
                    )
                elif evidenceformat:
                    content = await evidenceformat_factory(
                        interaction=interaction, case_dict=case_dict
                    )
                    await interaction.response.send_message(
                        content=content, ephemeral=ephemeral
                    )
                else:
                    embed = await case_factory(
                        interaction=interaction, case_dict=case_dict
                    )
                    await interaction.response.send_message(
                        embed=embed, ephemeral=ephemeral
                    )
                return
        await interaction.response.send_message(
            content=f"No case with case number `{case}` found.", ephemeral=True
        )

    @app_commands.command(name="edit")
    async def edit(
        self,
        interaction: discord.Interaction,
        case: int,
        reason: str,
        duration: str = None,
    ):
        """Edit the reason of a specific case.

        Parameters
        -----------
        case: int
            What case are you editing?
        reason: str
            What is the new reason?
        duration: str
            What is the new duration? Does not reapply the moderation if it has already expired.
        """
        permissions = check_permissions(
            interaction.client.user, ["embed_links"], interaction
        )
        if permissions:
            await interaction.response.send_message(
                error(
                    f"I do not have the `{permissions}` permission, required for this action."
                ),
                ephemeral=True,
            )
            return

        if case != 0:
            parsed_time = None
            case_dict = await fetch_case(case, interaction.guild.id)
            if case_dict:
                if duration:
                    parsed_time = parse_timedelta(duration)
                    if parsed_time is None:
                        await interaction.response.send_message(
                            error("Please provide a valid duration!"), ephemeral=True
                        )
                        return

                    end_timestamp = case_dict["timestamp"] + parsed_time.total_seconds()

                    if case_dict["moderation_type"] == "MUTE":
                        if (
                            time.time() - case_dict["timestamp"]
                        ) + parsed_time.total_seconds() > 2419200:
                            await interaction.response.send_message(
                                error(
                                    "Please provide a duration that is less than 28 days from the initial moderation."
                                )
                            )
                            return

                        try:
                            member = await interaction.guild.fetch_member(
                                case_dict["target_id"]
                            )

                            await member.timeout(
                                parsed_time,
                                reason=f"Case #{case:,} edited by {interaction.user.id}",
                            )
                        except discord.NotFound:
                            pass

                changes: list = case_dict["changes"]
                if len(changes) > 25:
                    await interaction.response.send_message(
                        content=error(
                            "Due to limitations with Discord's embed system, you cannot edit a case more than 25 times."
                        ),
                        ephemeral=True,
                    )
                    return
                if not changes:
                    changes.append(
                        {
                            "type": "ORIGINAL",
                            "timestamp": case_dict["timestamp"],
                            "reason": case_dict["reason"],
                            "user_id": case_dict["moderator_id"],
                            "duration": case_dict["duration"],
                            "end_timestamp": case_dict["end_timestamp"],
                        }
                    )
                if parsed_time:
                    changes.append(
                        {
                            "type": "EDIT",
                            "timestamp": int(time.time()),
                            "reason": reason,
                            "user_id": interaction.user.id,
                            "duration": convert_timedelta_to_str(parsed_time),
                            "end_timestamp": end_timestamp,
                        }
                    )
                else:
                    changes.append(
                        {
                            "type": "EDIT",
                            "timestamp": int(time.time()),
                            "reason": reason,
                            "user_id": interaction.user.id,
                            "duration": case_dict["duration"],
                            "end_timestamp": case_dict["end_timestamp"],
                        }
                    )

                database = connect()
                cursor = database.cursor()

                if parsed_time:
                    update_query = f"UPDATE `moderation_{interaction.guild.id}` SET changes = ?, reason = ?, duration = ?, end_timestamp = ? WHERE moderation_id = ?"
                    cursor.execute(
                        update_query,
                        (
                            json.dumps(changes),
                            reason,
                            convert_timedelta_to_str(parsed_time),
                            end_timestamp,
                            case,
                        ),
                    )
                else:
                    update_query = f"UPDATE `moderation_{interaction.guild.id}` SET changes = ?, reason = ? WHERE moderation_id = ?"
                    cursor.execute(update_query, (json.dumps(changes), reason, case))
                database.commit()

                new_case = await fetch_case(case, interaction.guild.id)
                embed = await case_factory(interaction=interaction, case_dict=new_case)

                await interaction.response.send_message(
                    content=f"✅ Moderation #{case:,} edited!",
                    embed=embed,
                    ephemeral=True,
                )
                await log(interaction, case)

                cursor.close()
                database.close()
                return
        await interaction.response.send_message(
            content=error(f"No case with case number `{case}` found."), ephemeral=True
        )

    @tasks.loop(minutes=1)
    async def handle_expiry(self):
        await self.bot.wait_until_red_ready()
        current_time = time.time()
        database = connect()
        cursor = database.cursor()
        global_unban_num = 0
        global_addrole_num = 0
        global_removerole_num = 0

        guilds: list[discord.Guild] = self.bot.guilds
        for guild in guilds:
            if not await self.bot.cog_disabled_in_guild(self, guild):
                time_per_guild = time.time()

                tempban_query = f"SELECT target_id, moderation_id FROM moderation_{guild.id} WHERE end_timestamp != 0 AND end_timestamp <= ? AND moderation_type = 'TEMPBAN' AND expired = 0"

                try:
                    cursor.execute(tempban_query, (time.time(),))
                    result = cursor.fetchall()
                except sqlite3.OperationalError:
                    continue

                target_ids = [row[0] for row in result]
                moderation_ids = [row[1] for row in result]

                unban_num = 0
                for target_id, moderation_id in zip(target_ids, moderation_ids):
                    user: discord.User = await self.bot.fetch_user(target_id)
                    name = (
                        f"{user.name}#{user.discriminator}"
                        if user.discriminator != "0"
                        else user.name
                    )
                    try:
                        await guild.unban(
                            user, reason=f"Automatic unban from case #{moderation_id}"
                        )

                        embed = await message_factory(
                            await self.bot.get_embed_color(guild.channels[0]),
                            guild=guild,
                            reason=f"Automatic unban from case #{moderation_id}",
                            moderation_type="unbanned",
                        )

                        try:
                            await user.send(embed=embed, file=get_footer_image(self))
                        except discord.errors.HTTPException:
                            pass

                        logger.debug(
                            "Unbanned %s (%s) from %s (%s)",
                            name,
                            user.id,
                            guild.name,
                            guild.id,
                        )
                        unban_num = unban_num + 1
                    except (
                        discord.errors.NotFound,
                        discord.errors.Forbidden,
                        discord.errors.HTTPException,
                    ) as e:
                        logger.error(
                            "Failed to unban %s (%s) from %s (%s)\n%s",
                            name,
                            user.id,
                            guild.name,
                            guild.id,
                            e,
                        )

                removerole_num = 0
                addrole_query = f"SELECT target_id, moderation_id, role_id FROM moderation_{guild.id} WHERE end_timestamp != 0 AND end_timestamp <= ? AND moderation_type = 'ADDROLE' AND expired = 0"
                try:
                    cursor.execute(addrole_query, (time.time(),))
                    result = cursor.fetchall()
                except sqlite3.OperationalError:
                    continue
                target_ids = [row[0] for row in result]
                moderation_ids = [row[1] for row in result]
                role_ids = [row[2] for row in result]

                for target_id, moderation_id, role_id in zip(
                    target_ids, moderation_ids, role_ids
                ):
                    try:
                        member = await guild.fetch_member(target_id)

                        await member.remove_roles(
                            Object(role_id), reason=f"Automatic role removal from case #{moderation_id}"
                        )

                        removerole_num = removerole_num + 1
                    except (
                        discord.errors.NotFound,
                        discord.errors.Forbidden,
                        discord.errors.HTTPException,
                    ) as e:
                        logger.error(
                            "Removing the role %s from user %s failed due to: \n%s",
                            role_id,
                            target_id,
                            e,
                        )
                        continue

                addrole_num = 0
                removerole_query = f"SELECT target_id, moderation_id, role_id FROM moderation_{guild.id} WHERE end_timestamp != 0 AND end_timestamp <= ? AND moderation_type = 'REMOVEROLE' AND expired = 0"
                try:
                    cursor.execute(removerole_query, (time.time(),))
                    result = cursor.fetchall()
                except sqlite3.OperationalError:
                    continue
                target_ids = [row[0] for row in result]
                moderation_ids = [row[1] for row in result]
                role_ids = [row[2] for row in result]

                for target_id, moderation_id, role_id in zip(
                    target_ids, moderation_ids, role_ids
                ):
                    try:
                        member = await guild.fetch_member(target_id)

                        await member.add_roles(
                            Object(role_id), reason=f"Automatic role addition from case #{moderation_id}"
                        )

                        addrole_num = addrole_num + 1
                    except (
                        discord.errors.NotFound,
                        discord.errors.Forbidden,
                        discord.errors.HTTPException,
                    ) as e:
                        logger.error("Adding the role %s to user %s failed due to: \n%s", role_id, target_id, e)
                        continue

                expiry_query = f"UPDATE `moderation_{guild.id}` SET expired = 1 WHERE (end_timestamp != 0 AND end_timestamp <= ? AND expired = 0) OR (expired = 0 AND resolved = 1);"
                cursor.execute(expiry_query, (time.time(),))

                per_guild_completion_time = (time.time() - time_per_guild) * 1000
                logger.debug(
                    "Completed expiry loop for %s (%s) in %sms with %s users unbanned, %s roles added, and %s roles removed",
                    guild.name,
                    guild.id,
                    f"{per_guild_completion_time:.6f}",
                    unban_num,
                    addrole_num,
                    removerole_num,
                )
                global_unban_num = global_unban_num + unban_num
                global_addrole_num = global_addrole_num + addrole_num
                global_removerole_num = global_removerole_num + removerole_num

        database.commit()
        cursor.close()
        database.close()

        completion_time = (time.time() - current_time) * 1000
        logger.debug(
            "Completed expiry loop in %sms with %s users unbanned, %s roles added, and %s roles removed",
            f"{completion_time:.6f}",
            global_unban_num,
            global_addrole_num,
            global_removerole_num,
        )

    ########################################################################################################################
    ### Configuration Commands                                                                                             #
    ########################################################################################################################

    @commands.group(autohelp=True, aliases=["moderation", "mod"])
    async def aurora(self, ctx: commands.Context):
        """Settings and miscellaneous commands for Aurora."""

    @aurora.group(autohelp=True, name="settings", aliases=["config", "options", "set"])
    async def aurora_settings(self, ctx: commands.Context):
        """Configure Aurora's settings."""

    @aurora_settings.command(name="overrides", aliases=["override", "user"])
    async def aurora_settings_overrides(self, ctx: commands.Context):
        """Manage Aurora's user overriddable settings."""
        msg = await ctx.send(embed=await overrides_embed(ctx))
        await msg.edit(view=Overrides(ctx, msg, 60))

    @aurora_settings.command(name="guild", aliases=["server"])
    @commands.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    async def aurora_settings_guild(self, ctx: commands.Context):
        """Manage Aurora's guild settings."""
        msg = await ctx.send(embed=await guild_embed(ctx))
        await msg.edit(view=Guild(ctx, msg, 60))

    @aurora_settings.command(name="addrole", aliases=["removerole"])
    @commands.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    async def aurora_settings_addrole(self, ctx: commands.Context):
        """Manage the addrole whitelist.

        Roles added to this list are also applied to `/removerole`."""
        msg = await ctx.send(embed=await addrole_embed(ctx))
        await msg.edit(view=Addrole(ctx, msg, 60))

    @aurora_settings.command(name="immunity")
    @commands.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    async def aurora_settings_immunity(self, ctx: commands.Context):
        """Manage the immunity whitelist."""
        msg = await ctx.send(embed=await immune_embed(ctx))
        await msg.edit(view=Immune(ctx, msg, 60))

    @aurora.group(autohelp=True, name="import")
    @commands.admin()
    @commands.guild_only()
    async def aurora_import(self, ctx: commands.Context):
        """Import moderation history from other bots."""

    @aurora_import.command(name="aurora")
    @commands.admin()
    async def aurora_import_aurora(self, ctx: commands.Context):
        """Import moderation history from another bot using Aurora."""
        if (
            ctx.message.attachments
            and ctx.message.attachments[0].content_type
            == "application/json; charset=utf-8"
        ):
            message = await ctx.send(
                warning(
                    "Are you sure you want to import moderations from another bot?\n**This will overwrite any moderations that already exist in this guild's moderation table.**\n*The import process will block the rest of your bot until it is complete.*"
                )
            )
            await message.edit(view=ImportAuroraView(60, ctx, message))
        else:
            await ctx.send(error("Please provide a valid Aurora export file."))

    @aurora_import.command(name="galacticbot")
    @commands.admin()
    async def aurora_import_galacticbot(self, ctx: commands.Context):
        """Import moderation history from GalacticBot."""
        if (
            ctx.message.attachments
            and ctx.message.attachments[0].content_type
            == "application/json; charset=utf-8"
        ):
            message = await ctx.send(
                warning(
                    "Are you sure you want to import GalacticBot moderations?\n**This will overwrite any moderations that already exist in this guild's moderation table.**\n*The import process will block the rest of your bot until it is complete.*"
                )
            )
            await message.edit(view=ImportGalacticBotView(60, ctx, message))
        else:
            await ctx.send(
                error("Please provide a valid GalacticBot moderation export file.")
            )

    @aurora.command(aliases=["tdc", "td", "timedeltaconvert"])
    async def timedelta(self, ctx: commands.Context, *, duration: str) -> None:
        """Convert a string to a timedelta.

        This command converts a duration to a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) Python object.
        You cannot convert years or months as they are not fixed units. Use `[p]aurora relativedelta` for that.

        **Example usage**
        `[p]aurora timedelta 1 day 15hr 82 minutes 52s`
        **Output**
        `1 day, 16:22:52`"""
        parsed_time = parse_timedelta(duration)
        if parsed_time is None:
            await ctx.send(error("Please provide a convertible value!"))
            return
        await ctx.send(f"`{parsed_time}`")

    @aurora.command(aliases=["rdc", "rd", "relativedeltaconvert"])
    async def relativedelta(self, ctx: commands.Context, *, duration: str) -> None:
        """Convert a string to a relativedelta.

        This command converts a duration to a [`relativedelta`](https://dateutil.readthedocs.io/en/stable/relativedelta.html) Python object.

        **Example usage**
        `[p]aurora relativedelta 3 years 1 day 15hr 82 minutes 52s`
        **Output**
        `relativedelta(years=+3, days=+1, hours=+15, minutes=+82, seconds=+52)`"""
        parsed_time = parse_relativedelta(duration)
        if parsed_time is None:
            await ctx.send(error("Please provide a convertible value!"))
            return
        await ctx.send(f"`{parsed_time}`")
