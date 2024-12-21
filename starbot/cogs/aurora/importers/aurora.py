# pylint: disable=duplicate-code
import json
from datetime import timedelta
from typing import Dict

from discord import ButtonStyle, Interaction, Message, ui
from starbot.core import commands
from starbot.core.utils.chat_formatting import box, warning

from ..utilities.database import connect, create_guild_table, mysql_log


class ImportAuroraView(ui.View):
    def __init__(self, timeout, ctx, message):
        super().__init__()
        self.ctx: commands.Context = ctx
        self.message: Message = message

    @ui.button(label="Yes", style=ButtonStyle.success)
    async def import_button_y(
        self, interaction: Interaction, button: ui.Button
    ): # pylint: disable=unused-argument
        await self.message.delete()
        await interaction.response.send_message(
            "Deleting original table...", ephemeral=True
        )

        database = connect()
        cursor = database.cursor()

        query = f"DROP TABLE IF EXISTS moderation_{self.ctx.guild.id};"
        cursor.execute(query)

        cursor.close()
        database.commit()

        await interaction.edit_original_response(content="Creating new table...")

        await create_guild_table(self.ctx.guild)

        await interaction.edit_original_response(content="Importing moderations...")

        file = await self.ctx.message.attachments[0].read()
        data: list[dict] = sorted(json.loads(file), key=lambda x: x["moderation_id"])

        user_mod_types = ["NOTE", "WARN", "ADDROLE", "REMOVEROLE", "MUTE", "UNMUTE", "KICK", "TEMPBAN", "BAN", "UNBAN"]

        channel_mod_types = ["SLOWMODE", "LOCKDOWN"]

        failed_cases = []

        for case in data:
            if case["moderation_id"] == 0:
                continue

            if "target_type" not in case or not case["target_type"]:
                if case["moderation_type"] in user_mod_types:
                    case["target_type"] = "USER"
                elif case["moderation_type"] in channel_mod_types:
                    case["target_type"] = "CHANNEL"
                else:
                    case["target_type"] = "USER"

            if "role_id" not in case or not case["role_id"]:
                case["role_id"] = 0

            if "changes" not in case or not case["changes"]:
                case["changes"] = []

            if "metadata" not in case:
                metadata = {}
            else:
                metadata: Dict[str, any] = json.loads(case["metadata"])
            if not metadata.get("imported_from"):
                metadata.update({"imported_from": "Aurora"})

            if case["duration"] != "NULL":
                hours, minutes, seconds = map(int, case["duration"].split(":"))
                duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            else:
                duration = "NULL"

            await mysql_log(
                self.ctx.guild.id,
                case["moderator_id"],
                case["moderation_type"],
                case["target_type"],
                case["target_id"],
                case["role_id"],
                duration,
                case["reason"],
                timestamp=case["timestamp"],
                resolved=case["resolved"],
                resolved_by=case["resolved_by"],
                resolved_reason=case["resolve_reason"],
                expired=case["expired"],
                changes=case["changes"],
                metadata=metadata,
                database=database,
            )

        await interaction.edit_original_response(content="Import complete.")
        if failed_cases:
            await interaction.edit_original_response(
                content="Import complete.\n"
                + warning("Failed to import the following cases:\n")
                + box(failed_cases)
            )

    @ui.button(label="No", style=ButtonStyle.danger)
    async def import_button_n(
        self, interaction: Interaction, button: ui.Button
    ): # pylint: disable=unused-argument
        await self.message.edit(content="Import cancelled.", view=None)
        await self.message.delete(10)
        await self.ctx.message.delete(10)
