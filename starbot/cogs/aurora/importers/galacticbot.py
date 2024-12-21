# pylint: disable=duplicate-code
import json
from datetime import timedelta

from discord import ButtonStyle, Interaction, Message, ui
from starbot.core import commands
from starbot.core.utils.chat_formatting import box, warning

from ..utilities.database import connect, create_guild_table, mysql_log


class ImportGalacticBotView(ui.View):
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

        accepted_types = [
            "NOTE",
            "WARN",
            "MUTE",
            "UNMUTE",
            "KICK",
            "SOFTBAN",
            "BAN",
            "UNBAN",
            "SLOWMODE",
            "LOCKDOWN",
        ]

        file = await self.ctx.message.attachments[0].read()
        data = sorted(json.loads(file), key=lambda x: x["case"])

        failed_cases = []

        for case in data:
            if case["type"] not in accepted_types:
                continue

            timestamp = round(case["timestamp"] / 1000)

            try:
                if case["duration"] is not None and float(case["duration"]) != 0:
                    duration = timedelta(seconds=round(float(case["duration"]) / 1000))
                else:
                    duration = "NULL"
            except OverflowError:
                failed_cases.append(case["case"])
                continue

            metadata = {"imported_from": "GalacticBot"}

            if case["type"] == "SLOWMODE":
                metadata["seconds"] = case["data"]["seconds"]

            if case["resolved"]:
                resolved = 1
                resolved_by = None
                resolved_reason = None
                resolved_timestamp = None
                if case["changes"]:
                    for change in case["changes"]:
                        if change["type"] == "RESOLVE":
                            resolved_by = change["staff"]
                            resolved_reason = change["reason"]
                            resolved_timestamp = round(change["timestamp"] / 1000)
                            break
                if resolved_by is None:
                    resolved_by = "?"
                if resolved_reason is None:
                    resolved_reason = (
                        "Could not get resolve reason during moderation import."
                    )
                if resolved_timestamp is None:
                    resolved_timestamp = timestamp
                changes = [
                    {
                        "type": "ORIGINAL",
                        "reason": case["reason"],
                        "user_id": case["executor"],
                        "timestamp": timestamp,
                    },
                    {
                        "type": "RESOLVE",
                        "reason": resolved_reason,
                        "user_id": resolved_by,
                        "timestamp": resolved_timestamp,
                    },
                ]
            else:
                resolved = 0
                resolved_by = "NULL"
                resolved_reason = "NULL"
                changes = []

            if case["reason"] and case["reason"] != "N/A":
                reason = case["reason"]
            else:
                reason = "NULL"

            await mysql_log(
                self.ctx.guild.id,
                case["executor"],
                case["type"],
                case["targetType"],
                case["target"],
                0,
                duration,
                reason,
                timestamp=timestamp,
                resolved=resolved,
                resolved_by=resolved_by,
                resolved_reason=resolved_reason,
                changes=changes,
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
