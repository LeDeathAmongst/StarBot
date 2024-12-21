# pylint: disable=cyclic-import
import json
from datetime import datetime
from datetime import timedelta as td
from typing import Optional, Union

from dateutil.relativedelta import relativedelta as rd
from discord import File, Guild, Interaction, Member, SelectOption, User
from discord.errors import Forbidden, NotFound
from starbot.core import commands, data_manager
from starbot.core.utils.chat_formatting import error

from .config import config


def check_permissions(
    user: User,
    permissions: list,
    ctx: Union[commands.Context, Interaction] = None,
    guild: Guild = None,
) -> Union[bool, str]:
    """Checks if a user has a specific permission (or a list of permissions) in a channel."""
    if ctx:
        member = ctx.guild.get_member(user.id)
        resolved_permissions = ctx.channel.permissions_for(member)

    elif guild:
        member = guild.get_member(user.id)
        resolved_permissions = member.guild_permissions

    else:
        raise (KeyError)

    for permission in permissions:
        if (
            not getattr(resolved_permissions, permission, False)
            and resolved_permissions.administrator is not True
        ):
            return permission

    return False


async def check_moddable(
    target: Union[User, Member], interaction: Interaction, permissions: list
) -> bool:
    """Checks if a moderator can moderate a target."""
    if check_permissions(interaction.client.user, permissions, guild=interaction.guild):
        await interaction.response.send_message(
            error(
                f"I do not have the `{permissions}` permission, required for this action."
            ),
            ephemeral=True,
        )
        return False

    if await config.guild(interaction.guild).use_discord_permissions() is True:
        if check_permissions(interaction.user, permissions, guild=interaction.guild):
            await interaction.response.send_message(
                error(
                    f"You do not have the `{permissions}` permission, required for this action."
                ),
                ephemeral=True,
            )
            return False

    if interaction.user.id == target.id:
        await interaction.response.send_message(
            content="You cannot moderate yourself!", ephemeral=True
        )
        return False

    if target.bot:
        await interaction.response.send_message(
            content="You cannot moderate bots!", ephemeral=True
        )
        return False

    if isinstance(target, Member):
        if interaction.user.top_role <= target.top_role and await config.guild(interaction.guild).respect_hierarchy() is True:
            await interaction.response.send_message(
                content=error(
                    "You cannot moderate members with a higher role than you!"
                ),
                ephemeral=True,
            )
            return False

        if (
            interaction.guild.get_member(interaction.client.user.id).top_role
            <= target.top_role
        ):
            await interaction.response.send_message(
                content=error(
                    "You cannot moderate members with a role higher than the bot!"
                ),
                ephemeral=True,
            )
            return False

        immune_roles = await config.guild(target.guild).immune_roles()

        for role in target.roles:
            if role.id in immune_roles:
                await interaction.response.send_message(
                    content=error("You cannot moderate members with an immune role!"),
                    ephemeral=True,
                )
                return False

    return True


async def get_next_case_number(guild_id: str, cursor=None) -> int:
    """This function returns the next case number from the MySQL table for a specific guild."""
    from .database import connect

    if not cursor:
        database = connect()
        cursor = database.cursor()
    cursor.execute(
        f"SELECT moderation_id FROM `moderation_{guild_id}` ORDER BY moderation_id DESC LIMIT 1"
    )
    result = cursor.fetchone()
    return (result[0] + 1) if result else 1


def generate_dict(result) -> dict:
    case = {
        "moderation_id": result[0],
        "timestamp": result[1],
        "moderation_type": result[2],
        "target_type": result[3],
        "target_id": result[4],
        "moderator_id": result[5],
        "role_id": result[6],
        "duration": result[7],
        "end_timestamp": result[8],
        "reason": result[9],
        "resolved": result[10],
        "resolved_by": result[11],
        "resolve_reason": result[12],
        "expired": result[13],
        "changes": json.loads(result[14]),
        "metadata": json.loads(result[15]),
    }
    return case


async def fetch_user_dict(client: commands.Bot, user_id: str) -> dict:
    """This function returns a dictionary containing either user information or a standard deleted user template."""
    if user_id == "?":
        user_dict = {"id": "?", "name": "Unknown User", "discriminator": "0"}

    else:
        try:
            user = client.get_user(int(user_id))
            if user is None:
                user = await client.fetch_user(int(user_id))

            user_dict = {
                "id": user.id,
                "name": user.name,
                "discriminator": user.discriminator,
            }

        except NotFound:
            user_dict = {
                "id": user_id,
                "name": "Deleted User",
                "discriminator": "0",
            }


    return user_dict


async def fetch_channel_dict(guild: Guild, channel_id: int) -> dict:
    """This function returns a dictionary containing either channel information or a standard deleted channel template."""
    try:
        channel = guild.get_channel(int(channel_id))
        if not channel:
            channel = await guild.fetch_channel(channel_id)

        channel_dict = {
            "id": channel.id,
            "name": channel.name,
            "mention": channel.mention,
        }

    except NotFound:
        channel_dict = {"id": channel_id, "name": "Deleted Channel", "mention": None}

    return channel_dict


async def fetch_role_dict(guild: Guild, role_id: int) -> dict:
    """This function returns a dictionary containing either role information or a standard deleted role template."""
    role = guild.get_role(int(role_id))
    if not role:
        role_dict = {"id": role_id, "name": "Deleted Role"}

    role_dict = {"id": role.id, "name": role.name}

    return role_dict


async def log(interaction: Interaction, moderation_id: int, resolved: bool = False) -> None:
    """This function sends a message to the guild's configured logging channel when an infraction takes place."""
    from .database import fetch_case
    from .factory import log_factory

    logging_channel_id = await config.guild(interaction.guild).log_channel()
    if logging_channel_id != " ":
        logging_channel = interaction.guild.get_channel(logging_channel_id)

        case = await fetch_case(moderation_id, interaction.guild.id)
        if case:
            embed = await log_factory(
                interaction=interaction, case_dict=case, resolved=resolved
            )
            try:
                await logging_channel.send(embed=embed)
            except Forbidden:
                return


async def send_evidenceformat(interaction: Interaction, case_dict: dict) -> None:
    """This function sends an ephemeral message to the moderator who took the moderation action, with a pre-made codeblock for use in the mod-evidence channel."""
    from .factory import evidenceformat_factory

    send_evidence_bool = (
        await config.user(interaction.user).auto_evidenceformat()
        or await config.guild(interaction.guild).auto_evidenceformat()
        or False
    )
    if send_evidence_bool is False:
        return

    content = await evidenceformat_factory(interaction=interaction, case_dict=case_dict)
    await interaction.followup.send(content=content, ephemeral=True)


def convert_timedelta_to_str(timedelta: td) -> str:
    """This function converts a timedelta object to a string."""
    total_seconds = int(timedelta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours}:{minutes}:{seconds}"


def get_bool_emoji(value: Optional[bool]) -> str:
    """Returns a unicode emoji based on a boolean value."""
    if value is True:
        return "\N{WHITE HEAVY CHECK MARK}"
    if value is False:
        return "\N{NO ENTRY SIGN}"
    return "\N{BLACK QUESTION MARK ORNAMENT}\N{VARIATION SELECTOR-16}"


def get_pagesize_str(value: Union[int, None]) -> str:
    """Returns a string based on a pagesize value."""
    if value is None:
        return "\N{BLACK QUESTION MARK ORNAMENT}\N{VARIATION SELECTOR-16}"
    return str(value) + " cases per page"


def create_pagesize_options() -> list[SelectOption]:
    """Returns a list of SelectOptions for pagesize configuration."""
    options = []
    options.append(
        SelectOption(
            label="Default",
            value="default",
            description="Reset the pagesize to the default value.",
        )
    )
    for i in range(1, 21):
        options.append(
            SelectOption(
                label=str(i),
                value=str(i),
                description=f"Set the pagesize to {i}.",
            )
        )
    return options

def timedelta_from_relativedelta(relativedelta: rd) -> td:
    """Converts a relativedelta object to a timedelta object."""
    now = datetime.now()
    then = now - relativedelta
    return now - then

def get_footer_image(coginstance: commands.Cog) -> File:
    """Returns the footer image for the embeds."""
    image_path = data_manager.bundled_data_path(coginstance) / "arrow.png"
    return File(image_path, filename="arrow.png", description="arrow")
