from discord import ButtonStyle, Interaction, Message, ui
from starbot.core import commands

from aurora.utilities.config import config
from aurora.utilities.factory import guild_embed
from aurora.utilities.utils import create_pagesize_options


class Guild(ui.View):
    def __init__(self, ctx: commands.Context, message: Message, timeout: int = None):
        super().__init__()
        self.ctx = ctx
        self.message = message
        self.timeout = timeout

    async def on_timeout(self):
        await self.message.edit(view=None)

    @ui.button(label="Show Moderator", style=ButtonStyle.green, row=0)
    async def show_moderator(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).show_moderator()
        await config.guild(interaction.guild).show_moderator.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="Use Discord Permissions", style=ButtonStyle.green, row=0)
    async def use_discord_permissions(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).use_discord_permissions()
        await config.guild(interaction.guild).use_discord_permissions.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="Respect Hierarchy", style=ButtonStyle.green, row=0)
    async def respect_heirarchy(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).respect_hierarchy()
        await config.guild(interaction.guild).respect_hierarchy.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="Ignore Modlog", style=ButtonStyle.green, row=0)
    async def ignore_modlog(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).ignore_modlog()
        await config.guild(interaction.guild).ignore_modlog.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="Ignore Other Bots", style=ButtonStyle.green, row=0)
    async def ignore_other_bots(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).ignore_other_bots()
        await config.guild(interaction.guild).ignore_other_bots.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="DM Users", style=ButtonStyle.green, row=1)
    async def dm_users(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).dm_users()
        await config.guild(interaction.guild).dm_users.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="Auto Evidence Format", style=ButtonStyle.green, row=1)
    async def auto_evidenceformat(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).auto_evidenceformat()
        await config.guild(interaction.guild).auto_evidenceformat.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="Ephemeral", style=ButtonStyle.green, row=1)
    async def ephemeral(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).history_ephemeral()
        await config.guild(interaction.guild).history_ephemeral.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.button(label="History Inline", style=ButtonStyle.green, row=1)
    async def inline(self, interaction: Interaction, button: ui.Button): # pylint: disable=unused-argument
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        current_setting = await config.guild(interaction.guild).history_inline()
        await config.guild(interaction.guild).history_inline.set(not current_setting)
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.select(placeholder="History Pagesize", options=create_pagesize_options(), row=2)
    async def pagesize(self, interaction: Interaction, select: ui.Select,):
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        if select.values[0] == "default":
            await config.guild(interaction.guild).history_pagesize.clear()
        else:
            await config.guild(interaction.guild).history_pagesize.set(int(select.values[0]))
        await interaction.response.defer()
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.select(placeholder="History Inline Pagesize", options=create_pagesize_options(), row=3)
    async def inline_pagesize(self, interaction: Interaction, select: ui.Select,):
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        if select.values[0] == "default":
            await config.guild(interaction.guild).history_inline_pagesize.clear()
        else:
            await config.guild(interaction.guild).history_inline_pagesize.set(int(select.values[0]))
        await interaction.response.defer()
        await interaction.message.edit(embed=await guild_embed(self.ctx))

    @ui.select(placeholder="Log Channel", cls=ui.ChannelSelect, row=4)
    async def log_channel(self, interaction: Interaction, select: ui.ChannelSelect):
        if not interaction.user.guild_permissions.manage_guild and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You must have the manage guild permission to change this setting.", ephemeral=True)
            return
        await interaction.response.defer()
        await config.guild(interaction.guild).log_channel.set(select.values[0].id)
        await interaction.message.edit(embed=await guild_embed(self.ctx))
