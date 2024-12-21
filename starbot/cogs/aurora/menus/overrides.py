from discord import ButtonStyle, Interaction, Message, ui
from starbot.core import commands

from aurora.utilities.config import config
from aurora.utilities.factory import overrides_embed
from aurora.utilities.utils import create_pagesize_options


class Overrides(ui.View):
    def __init__(self, ctx: commands.Context, message: Message, timeout: int = None):
        super().__init__()
        self.ctx = ctx
        self.message = message
        self.timeout = timeout

    async def on_timeout(self):
        await self.message.edit(view=None)

    @ui.button(label="Auto Evidence Format", style=ButtonStyle.green, row=0)
    async def auto_evidenceformat(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if self.ctx.author != interaction.user:
            await interaction.response.send_message("You cannot change this setting for other users.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.user(self.ctx.author).auto_evidenceformat()
        if current_setting is False:
            await config.user(self.ctx.author).auto_evidenceformat.clear()
        elif current_setting is None:
            await config.user(self.ctx.author).auto_evidenceformat.set(True)
        else:
            await config.user(self.ctx.author).auto_evidenceformat.set(False)
        await interaction.message.edit(embed=await overrides_embed(self.ctx))

    @ui.button(label="Ephemeral", style=ButtonStyle.green, row=0)
    async def ephemeral(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if self.ctx.author != interaction.user:
            await interaction.response.send_message("You cannot change this setting for other users.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.user(self.ctx.author).history_ephemeral()
        if current_setting is False:
            await config.user(self.ctx.author).history_ephemeral.clear()
        elif current_setting is None:
            await config.user(self.ctx.author).history_ephemeral.set(True)
        else:
            await config.user(self.ctx.author).history_ephemeral.set(False)
        await interaction.message.edit(embed=await overrides_embed(self.ctx))

    @ui.button(label="Inline", style=ButtonStyle.green, row=0)
    async def inline(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if self.ctx.author != interaction.user:
            await interaction.response.send_message("You cannot change this setting for other users.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.user(self.ctx.author).history_inline()
        if current_setting is False:
            await config.user(self.ctx.author).history_inline.clear()
        elif current_setting is None:
            await config.user(self.ctx.author).history_inline.set(True)
        else:
            await config.user(self.ctx.author).history_inline.set(False)
        await interaction.message.edit(embed=await overrides_embed(self.ctx))

    @ui.select(placeholder="Inline Pagesize", options=create_pagesize_options(), row=1)
    async def inline_pagesize(self, interaction: Interaction, select: ui.Select,):
        if self.ctx.author != interaction.user:
            await interaction.response.send_message("You cannot change this setting for other users.", ephemeral=True)
            return
        await interaction.response.defer()
        if select.values[0] == "default":
            await config.user(self.ctx.author).history_inline_pagesize.clear()
        else:
            await config.user(self.ctx.author).history_inline_pagesize.set(int(select.values[0]))
        await interaction.message.edit(embed=await overrides_embed(self.ctx))

    @ui.select(placeholder="Pagesize", options=create_pagesize_options(), row=2)
    async def pagesize(self, interaction: Interaction, select: ui.Select,):
        if self.ctx.author != interaction.user:
            await interaction.response.send_message("You cannot change this setting for other users.", ephemeral=True)
            return
        await interaction.response.defer()
        if select.values[0] == "default":
            await config.user(self.ctx.author).history_pagesize.clear()
        else:
            await config.user(self.ctx.author).history_pagesize.set(int(select.values[0]))
        await interaction.message.edit(embed=await overrides_embed(self.ctx))
