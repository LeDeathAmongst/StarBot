from discord import ButtonStyle, Interaction, Message, ui
from starbot.core import commands
from starbot.core.utils.chat_formatting import error

from aurora.utilities.config import config
from aurora.utilities.factory import addrole_embed


class Addrole(ui.View):
    def __init__(self, ctx: commands.Context, message: Message, timeout: int = None):
        super().__init__()
        self.ctx = ctx
        self.message = message
        self.timeout = timeout

    async def on_timeout(self):
        await self.message.edit(view=None)

    @ui.select(cls=ui.RoleSelect, placeholder="Select a role", min_values=0, max_values=25)
    async def addrole_select(self, interaction: Interaction, select: ui.RoleSelect):
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(error("You must have the manage guild permission to add roles to the addrole whitelist."), ephemeral=True)
            return
        await interaction.response.defer()
        async with config.guild(self.ctx.guild).addrole_whitelist() as addrole_whitelist:
            addrole_whitelist: list # type hint
            for value in select.values:
                if value.id in addrole_whitelist:
                    addrole_whitelist.remove(value.id)
                else:
                    addrole_whitelist.append(value.id)
        await interaction.message.edit(embed=await addrole_embed(self.ctx))

    @ui.button(label="Clear", style=ButtonStyle.red, row=1)
    async def clear(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(error("You must have the manage guild permission to clear the guild's addrole whitelist."), ephemeral=True)
            return
        await interaction.response.defer()
        await config.guild(self.ctx.guild).addrole_whitelist.clear()
        await interaction.message.edit(embed=await addrole_embed(self.ctx))

    @ui.button(label="Close", style=ButtonStyle.gray)
    async def close(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(error("You can't do that!"), ephemeral=True)
            return
        await interaction.message.delete()
