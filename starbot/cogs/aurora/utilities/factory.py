# pylint: disable=cyclic-import
from datetime import datetime, timedelta
from typing import Union

from discord import Color, Embed, Guild, Interaction, InteractionMessage, Member, Role, User
from starbot.core import commands
from starbot.core.utils.chat_formatting import bold, box, error, humanize_timedelta, warning

from aurora.utilities.config import config
from aurora.utilities.utils import fetch_channel_dict, fetch_user_dict, get_bool_emoji, get_next_case_number, get_pagesize_str


async def message_factory(
    color: Color,
    guild: Guild,
    reason: str,
    moderation_type: str,
    moderator: Union[Member, User] = None,
    duration: timedelta = None,
    response: InteractionMessage = None,
    role: Role = None,
) -> Embed:
    """This function creates a message from set parameters, meant for contacting the moderated user.

    Args:
        color (Color): The color of the embed.
        guild (Guild): The guild the moderation occurred in.
        reason (str): The reason for the moderation.
        moderation_type (str): The type of moderation.
        moderator (Union[Member, User], optional): The moderator who performed the moderation. Defaults to None.
        duration (timedelta, optional): The duration of the moderation. Defaults to None.
        response (InteractionMessage, optional): The response message. Defaults to None.
        role (Role, optional): The role that was added or removed. Defaults to None.


    Returns:
        embed: The message embed.
    """
    if response is not None and moderation_type not in [
        "kicked",
        "banned",
        "tempbanned",
        "unbanned",
    ]:
        guild_name = f"[{guild.name}]({response.jump_url})"
    else:
        guild_name = guild.name

    title = moderation_type

    if moderation_type in ["tempbanned", "muted"] and duration:
        embed_duration = f" for {humanize_timedelta(timedelta=duration)}"
    else:
        embed_duration = ""

    if moderation_type == "note":
        embed_desc = "received a"
    elif moderation_type == "addrole":
        embed_desc = f"received the {role.name} role"
        title = "Role Added"
        moderation_type = ""
    elif moderation_type == "removerole":
        embed_desc = f"lost the {role.name} role"
        title = "Role Removed"
        moderation_type = ""
    else:
        embed_desc = "been"

    embed = Embed(
        title=str.title(title),
        description=f"You have {embed_desc} {moderation_type}{embed_duration} in {guild_name}.",
        color=color,
        timestamp=datetime.now(),
    )

    if await config.guild(guild).show_moderator() and moderator is not None:
        embed.add_field(
            name="Moderator", value=f"`{moderator.name} ({moderator.id})`", inline=False
        )

    embed.add_field(name="Reason", value=f"`{reason}`", inline=False)

    if guild.icon.url is not None:
        embed.set_author(name=guild.name, icon_url=guild.icon.url)
    else:
        embed.set_author(name=guild.name)

    embed.set_footer(
        text=f"Case #{await get_next_case_number(guild.id):,}",
        icon_url="attachment://arrow.png",
    )

    return embed


async def log_factory(
    interaction: Interaction, case_dict: dict, resolved: bool = False
) -> Embed:
    """This function creates a log embed from set parameters, meant for moderation logging.

    Args:
        interaction (Interaction): The interaction object.
        case_dict (dict): The case dictionary.
        resolved (bool, optional): Whether the case is resolved or not. Defaults to False.
    """
    if resolved:
        if case_dict["target_type"] == "USER":
            target_user = await fetch_user_dict(interaction.client, case_dict["target_id"])
            target_name = (
                f"`{target_user['name']}`"
                if target_user["discriminator"] == "0"
                else f"`{target_user['name']}#{target_user['discriminator']}`"
            )
        elif case_dict["target_type"] == "CHANNEL":
            target_user = await fetch_channel_dict(interaction.guild, case_dict["target_id"])
            if target_user["mention"]:
                target_name = f"{target_user['mention']}"
            else:
                target_name = f"`{target_user['name']}`"

        moderator_user = await fetch_user_dict(interaction.client, case_dict["moderator_id"])
        moderator_name = (
            f"`{moderator_user['name']}`"
            if moderator_user["discriminator"] == "0"
            else f"`{moderator_user['name']}#{moderator_user['discriminator']}`"
        )

        embed = Embed(
            title=f"📕 Case #{case_dict['moderation_id']:,} Resolved",
            color=await interaction.client.get_embed_color(interaction.channel),
        )

        embed.description = f"**Type:** {str.title(case_dict['moderation_type'])}\n**Target:** {target_name} ({target_user['id']})\n**Moderator:** {moderator_name} ({moderator_user['id']})\n**Timestamp:** <t:{case_dict['timestamp']}> | <t:{case_dict['timestamp']}:R>"

        if case_dict["duration"] != "NULL":
            td = timedelta(
                **{
                    unit: int(val)
                    for unit, val in zip(
                        ["hours", "minutes", "seconds"],
                        case_dict["duration"].split(":"),
                    )
                }
            )
            duration_embed = (
                f"{humanize_timedelta(timedelta=td)} | <t:{case_dict['end_timestamp']}:R>"
                if case_dict["expired"] == "0"
                else str(humanize_timedelta(timedelta=td))
            )
            embed.description = (
                embed.description
                + f"\n**Duration:** {duration_embed}\n**Expired:** {bool(case_dict['expired'])}"
            )

        embed.add_field(name="Reason", value=box(case_dict["reason"]), inline=False)

        resolved_user = await fetch_user_dict(interaction.client, case_dict["resolved_by"])
        resolved_name = (
            resolved_user["name"]
            if resolved_user["discriminator"] == "0"
            else f"{resolved_user['name']}#{resolved_user['discriminator']}"
        )
        embed.add_field(
            name="Resolve Reason",
            value=f"Resolved by `{resolved_name}` ({resolved_user['id']}) for:\n"
            + box(case_dict["resolve_reason"]),
            inline=False,
        )
    else:
        if case_dict["target_type"] == "USER":
            target_user = await fetch_user_dict(interaction.client, case_dict["target_id"])
            target_name = (
                f"`{target_user['name']}`"
                if target_user["discriminator"] == "0"
                else f"`{target_user['name']}#{target_user['discriminator']}`"
            )
        elif case_dict["target_type"] == "CHANNEL":
            target_user = await fetch_channel_dict(interaction.guild, case_dict["target_id"])
            if target_user["mention"]:
                target_name = target_user["mention"]
            else:
                target_name = f"`{target_user['name']}`"

        moderator_user = await fetch_user_dict(interaction.client, case_dict["moderator_id"])
        moderator_name = (
            f"`{moderator_user['name']}`"
            if moderator_user["discriminator"] == "0"
            else f"`{moderator_user['name']}#{moderator_user['discriminator']}`"
        )

        embed = Embed(
            title=f"📕 Case #{case_dict['moderation_id']:,}",
            color=await interaction.client.get_embed_color(interaction.channel),
        )
        embed.description = f"**Type:** {str.title(case_dict['moderation_type'])}\n**Target:** {target_name} ({target_user['id']})\n**Moderator:** {moderator_name} ({moderator_user['id']})\n**Timestamp:** <t:{case_dict['timestamp']}> | <t:{case_dict['timestamp']}:R>"

        if case_dict["duration"] != "NULL":
            td = timedelta(
                **{
                    unit: int(val)
                    for unit, val in zip(
                        ["hours", "minutes", "seconds"],
                        case_dict["duration"].split(":"),
                    )
                }
            )
            embed.description = (
                embed.description
                + f"\n**Duration:** {humanize_timedelta(timedelta=td)} | <t:{case_dict['end_timestamp']}:R>"
            )

        embed.add_field(name="Reason", value=box(case_dict["reason"]), inline=False)
    return embed


async def case_factory(interaction: Interaction, case_dict: dict) -> Embed:
    """This function creates a case embed from set parameters.

    Args:
        interaction (Interaction): The interaction object.
        case_dict (dict): The case dictionary.
    """
    if case_dict["target_type"] == "USER":
        target_user = await fetch_user_dict(interaction.client, case_dict["target_id"])
        target_name = (
            f"`{target_user['name']}`"
            if target_user["discriminator"] == "0"
            else f"`{target_user['name']}#{target_user['discriminator']}`"
        )
    elif case_dict["target_type"] == "CHANNEL":
        target_user = await fetch_channel_dict(interaction.guild, case_dict["target_id"])
        if target_user["mention"]:
            target_name = f"{target_user['mention']}"
        else:
            target_name = f"`{target_user['name']}`"

    moderator_user = await fetch_user_dict(interaction.client, case_dict["moderator_id"])
    moderator_name = (
        f"`{moderator_user['name']}`"
        if moderator_user["discriminator"] == "0"
        else f"`{moderator_user['name']}#{moderator_user['discriminator']}`"
    )

    embed = Embed(
        title=f"📕 Case #{case_dict['moderation_id']:,}",
        color=await interaction.client.get_embed_color(interaction.channel),
    )
    embed.description = f"**Type:** {str.title(case_dict['moderation_type'])}\n**Target:** {target_name} ({target_user['id']})\n**Moderator:** {moderator_name} ({moderator_user['id']})\n**Resolved:** {bool(case_dict['resolved'])}\n**Timestamp:** <t:{case_dict['timestamp']}> | <t:{case_dict['timestamp']}:R>"

    if case_dict["duration"] != "NULL":
        td = timedelta(
            **{
                unit: int(val)
                for unit, val in zip(
                    ["hours", "minutes", "seconds"], case_dict["duration"].split(":")
                )
            }
        )
        duration_embed = (
            f"{humanize_timedelta(timedelta=td)} | <t:{case_dict['end_timestamp']}:R>"
            if bool(case_dict["expired"]) is False
            else str(humanize_timedelta(timedelta=td))
        )
        embed.description += f"\n**Duration:** {duration_embed}\n**Expired:** {bool(case_dict['expired'])}"

    embed.description += (
        f"\n**Changes:** {len(case_dict['changes']) - 1}"
        if case_dict["changes"]
        else "\n**Changes:** 0"
    )

    if case_dict["role_id"]:
        embed.description += f"\n**Role:** <@&{case_dict['role_id']}>"

    if case_dict["metadata"]:
        if case_dict["metadata"]["imported_from"]:
            embed.description += (
                f"\n**Imported From:** {case_dict['metadata']['imported_from']}"
            )

    embed.add_field(name="Reason", value=box(case_dict["reason"]), inline=False)

    if case_dict["resolved"] == 1:
        resolved_user = await fetch_user_dict(interaction.client, case_dict["resolved_by"])
        resolved_name = (
            f"`{resolved_user['name']}`"
            if resolved_user["discriminator"] == "0"
            else f"`{resolved_user['name']}#{resolved_user['discriminator']}`"
        )
        embed.add_field(
            name="Resolve Reason",
            value=f"Resolved by {resolved_name} ({resolved_user['id']}) for:\n{box(case_dict['resolve_reason'])}",
            inline=False,
        )

    return embed


async def changes_factory(interaction: Interaction, case_dict: dict) -> Embed:
    """This function creates a changes embed from set parameters.

    Args:
        interaction (Interaction): The interaction object.
        case_dict (dict): The case dictionary.
    """
    embed = Embed(
        title=f"📕 Case #{case_dict['moderation_id']:,} Changes",
        color=await interaction.client.get_embed_color(interaction.channel),
    )

    memory_dict = {}

    if case_dict["changes"]:
        for change in case_dict["changes"]:
            if change["user_id"] not in memory_dict:
                memory_dict[str(change["user_id"])] = await fetch_user_dict(
                    interaction.client, change["user_id"]
                )

            user = memory_dict[str(change["user_id"])]
            name = (
                user["name"]
                if user["discriminator"] == "0"
                else f"{user['name']}#{user['discriminator']}"
            )

            timestamp = f"<t:{change['timestamp']}> | <t:{change['timestamp']}:R>"

            if change["type"] == "ORIGINAL":
                embed.add_field(
                    name="Original",
                    value=f"**User:** `{name}` ({user['id']})\n**Reason:** {change['reason']}\n**Timestamp:** {timestamp}",
                    inline=False,
                )

            elif change["type"] == "EDIT":
                embed.add_field(
                    name="Edit",
                    value=f"**User:** `{name}` ({user['id']})\n**Reason:** {change['reason']}\n**Timestamp:** {timestamp}",
                    inline=False,
                )

            elif change["type"] == "RESOLVE":
                embed.add_field(
                    name="Resolve",
                    value=f"**User:** `{name}` ({user['id']})\n**Reason:** {change['reason']}\n**Timestamp:** {timestamp}",
                    inline=False,
                )

    else:
        embed.description = "*No changes have been made to this case.* 🙁"

    return embed


async def evidenceformat_factory(interaction: Interaction, case_dict: dict) -> str:
    """This function creates a codeblock in evidence format from set parameters.

    Args:
        interaction (Interaction): The interaction object.
        case_dict (dict): The case dictionary.
    """
    if case_dict["target_type"] == "USER":
        target_user = await fetch_user_dict(interaction.client, case_dict["target_id"])
        target_name = (
            target_user["name"]
            if target_user["discriminator"] == "0"
            else f"{target_user['name']}#{target_user['discriminator']}"
        )

    elif case_dict["target_type"] == "CHANNEL":
        target_user = await fetch_channel_dict(interaction.guild, case_dict["target_id"])
        target_name = target_user["name"]

    moderator_user = await fetch_user_dict(interaction.client, case_dict["moderator_id"])
    moderator_name = (
        moderator_user["name"]
        if moderator_user["discriminator"] == "0"
        else f"{moderator_user['name']}#{moderator_user['discriminator']}"
    )

    content = f"Case: {case_dict['moderation_id']:,} ({str.title(case_dict['moderation_type'])})\nTarget: {target_name} ({target_user['id']})\nModerator: {moderator_name} ({moderator_user['id']})"

    if case_dict["role_id"] != "0":
        role = interaction.guild.get_role(int(case_dict["role_id"]))
        content += "\nRole: " + (role.name if role is not None else case_dict["role_id"])

    if case_dict["duration"] != "NULL":
        hours, minutes, seconds = map(int, case_dict["duration"].split(":"))
        td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        content += f"\nDuration: {humanize_timedelta(timedelta=td)}"

    content += f"\nReason: {case_dict['reason']}"

    return box(content, "prolog")


########################################################################################################################
### Configuration Embeds                                                                                               #
########################################################################################################################


async def _config(ctx: commands.Context) -> Embed:
    """Generates the core embed for configuration menus to use."""
    e = Embed(title="Aurora Configuration Menu", color=await ctx.embed_color())
    e.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    return e


async def overrides_embed(ctx: commands.Context) -> Embed:
    """Generates a configuration menu embed for a user's overrides."""

    override_settings = {
        "ephemeral": await config.user(ctx.author).history_ephemeral(),
        "inline": await config.user(ctx.author).history_inline(),
        "inline_pagesize": await config.user(ctx.author).history_inline_pagesize(),
        "pagesize": await config.user(ctx.author).history_pagesize(),
        "auto_evidenceformat": await config.user(ctx.author).auto_evidenceformat(),
    }

    override_str = [
        "- "
        + bold("Auto Evidence Format: ")
        + get_bool_emoji(override_settings["auto_evidenceformat"]),
        "- " + bold("Ephemeral: ") + get_bool_emoji(override_settings["ephemeral"]),
        "- " + bold("History Inline: ") + get_bool_emoji(override_settings["inline"]),
        "- "
        + bold("History Inline Pagesize: ")
        + get_pagesize_str(override_settings["inline_pagesize"]),
        "- "
        + bold("History Pagesize: ")
        + get_pagesize_str(override_settings["pagesize"]),
    ]
    override_str = "\n".join(override_str)

    e = await _config(ctx)
    e.title += ": User Overrides"
    e.description = (
        """
    Use the buttons below to manage your user overrides.
    These settings will override the relevant guild settings.\n
    """
        + override_str
    )
    return e


async def guild_embed(ctx: commands.Context) -> Embed:
    """Generates a configuration menu field value for a guild's settings."""

    guild_settings = {
        "show_moderator": await config.guild(ctx.guild).show_moderator(),
        "use_discord_permissions": await config.guild(
            ctx.guild
        ).use_discord_permissions(),
        "ignore_modlog": await config.guild(ctx.guild).ignore_modlog(),
        "ignore_other_bots": await config.guild(ctx.guild).ignore_other_bots(),
        "dm_users": await config.guild(ctx.guild).dm_users(),
        "log_channel": await config.guild(ctx.guild).log_channel(),
        "history_ephemeral": await config.guild(ctx.guild).history_ephemeral(),
        "history_inline": await config.guild(ctx.guild).history_inline(),
        "history_pagesize": await config.guild(ctx.guild).history_pagesize(),
        "history_inline_pagesize": await config.guild(
            ctx.guild
        ).history_inline_pagesize(),
        "auto_evidenceformat": await config.guild(ctx.guild).auto_evidenceformat(),
        "respect_hierarchy": await config.guild(ctx.guild).respect_hierarchy(),
    }

    channel = ctx.guild.get_channel(guild_settings["log_channel"])
    if channel is None:
        channel = warning("Not Set")
    else:
        channel = channel.mention

    guild_str = [
        "- "
        + bold("Show Moderator: ")
        + get_bool_emoji(guild_settings["show_moderator"]),
        "- "
        + bold("Use Discord Permissions: ")
        + get_bool_emoji(guild_settings["use_discord_permissions"]),
        "- "
        + bold("Respect Hierarchy: ")
        + get_bool_emoji(guild_settings["respect_hierarchy"]),
        "- "
        + bold("Ignore Modlog: ")
        + get_bool_emoji(guild_settings["ignore_modlog"]),
        "- "
        + bold("Ignore Other Bots: ")
        + get_bool_emoji(guild_settings["ignore_other_bots"]),
        "- " + bold("DM Users: ") + get_bool_emoji(guild_settings["dm_users"]),
        "- "
        + bold("Auto Evidence Format: ")
        + get_bool_emoji(guild_settings["auto_evidenceformat"]),
        "- "
        + bold("Ephemeral: ")
        + get_bool_emoji(guild_settings["history_ephemeral"]),
        "- "
        + bold("History Inline: ")
        + get_bool_emoji(guild_settings["history_inline"]),
        "- "
        + bold("History Pagesize: ")
        + get_pagesize_str(guild_settings["history_pagesize"]),
        "- "
        + bold("History Inline Pagesize: ")
        + get_pagesize_str(guild_settings["history_inline_pagesize"]),
        "- " + bold("Log Channel: ") + channel,
    ]
    guild_str = "\n".join(guild_str)

    e = await _config(ctx)
    e.title += ": Server Configuration"
    e.description = (
        """
    Use the buttons below to manage Aurora's server configuration.\n
    """
        + guild_str
    )
    return e


async def addrole_embed(ctx: commands.Context) -> Embed:
    """Generates a configuration menu field value for a guild's addrole whitelist."""

    roles = []
    async with config.guild(ctx.guild).addrole_whitelist() as whitelist:
        for role in whitelist:
            evalulated_role = ctx.guild.get_role(role) or error(f"`{role}` (Not Found)")
            if isinstance(evalulated_role, Role):
                roles.append({
                    "id": evalulated_role.id,
                    "mention": evalulated_role.mention,
                    "position": evalulated_role.position
                })
            else:
                roles.append({
                    "id": role,
                    "mention": error(f"`{role}` (Not Found)"),
                    "position": 0
                })

    if roles:
        roles = sorted(roles, key=lambda x: x["position"], reverse=True)
        roles = [role["mention"] for role in roles]
        whitelist_str = "\n".join(roles)
    else:
        whitelist_str = warning("No roles are on the addrole whitelist!")

    e = await _config(ctx)
    e.title += ": Addrole Whitelist"
    e.description = (
        "Use the select menu below to manage this guild's addrole whitelist."
    )

    if len(whitelist_str) > 4000 and len(whitelist_str) < 5000:
        lines = whitelist_str.split("\n")
        chunks = []
        chunk = ""
        for line in lines:
            if len(chunk) + len(line) > 1024:
                chunks.append(chunk)
                chunk = line
            else:
                chunk += "\n" + line if chunk else line
        chunks.append(chunk)

        for chunk in chunks:
            e.add_field(name="", value=chunk)
    else:
        e.description += "\n\n" + whitelist_str

    return e


async def immune_embed(ctx: commands.Context) -> Embed:
    """Generates a configuration menu embed for a guild's immune roles."""

    roles = []
    async with config.guild(ctx.guild).immune_roles() as immune_roles:
        for role in immune_roles:
            evalulated_role = ctx.guild.get_role(role) or error(f"`{role}` (Not Found)")
            if isinstance(evalulated_role, Role):
                roles.append({
                    "id": evalulated_role.id,
                    "mention": evalulated_role.mention,
                    "position": evalulated_role.position
                })
            else:
                roles.append({
                    "id": role,
                    "mention": error(f"`{role}` (Not Found)"),
                    "position": 0
                })

    if roles:
        roles = sorted(roles, key=lambda x: x["position"], reverse=True)
        roles = [role["mention"] for role in roles]
        immune_str = "\n".join(roles)
    else:
        immune_str = warning("No roles are set as immune roles!")

    e = await _config(ctx)
    e.title += ": Immune Roles"
    e.description = "Use the select menu below to manage this guild's immune roles."

    if len(immune_str) > 4000 and len(immune_str) < 5000:
        lines = immune_str.split("\n")
        chunks = []
        chunk = ""
        for line in lines:
            if len(chunk) + len(line) > 1024:
                chunks.append(chunk)
                chunk = line
            else:
                chunk += "\n" + line if chunk else line
        chunks.append(chunk)

        for chunk in chunks:
            e.add_field(name="", value=chunk)
    else:
        e.description += "\n\n" + immune_str

    return e
