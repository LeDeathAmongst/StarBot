from starbot.core import commands, app_commands, Config, checks
from starbot.core.bot import Red
import discord
from discord.utils import utcnow
from Star-Utils import Cog, CogsUtils, Settings
import typing

@app_commands.context_menu(name="Add Owner")
async def add_owner_context_menu(interaction: discord.Interaction, user: discord.User):
    bot = interaction.client
    if not await bot.is_owner(interaction.user):
        await interaction.response.send_message("You don't have permission to add owners.", ephemeral=True)
        return

    async with bot.get_cog("OwnerProtection").config.owners() as owners:
        if user.id in owners:
            await interaction.response.send_message(f"{user.mention} is already a protected owner.", ephemeral=True)
            return
        owners.append(user.id)

    await interaction.response.send_message(f"{user.mention} has been added as a protected owner.", ephemeral=True)
    await bot.get_cog("OwnerProtection").assign_roles_to_owners(interaction.guild)

@app_commands.context_menu(name="Remove Owner")
async def remove_owner_context_menu(interaction: discord.Interaction, user: discord.User):
    bot = interaction.client
    if not await bot.is_owner(interaction.user):
        await interaction.response.send_message("You don't have permission to remove owners.", ephemeral=True)
        return

    async with bot.get_cog("OwnerProtection").config.owners() as owners:
        if user.id not in owners:
            await interaction.response.send_message(f"{user.mention} is not a protected owner.", ephemeral=True)
            return
        owners.remove(user.id)

    await interaction.response.send_message(f"{user.mention} has been removed as a protected owner.", ephemeral=True)
class OwnerProtection(Cog):
    """A cog to protect the bot owner/trusted owners from being muted, timed out, kicked, or banned."""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("OwnerProtection")
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(owners=[])
        self.config.register_guild(
            kicked_owners={},
            owner_role_id=None,
            support_role_id=None,
            support_role_name="Support",
            support_role_message="Support Role created successfully.",
            owner_message="Support role made for support."
        )
        _settings = {
            'owner_role_name': {
                'converter': str,
                'description': 'The name of the owner role.'
            },
            'support_role_name': {
                'converter': str,
                'description': 'The name of the support role.'
            },
            'support_role_message': {
                'converter': str,
                'description': 'Message sent when the support role is created.'
            },
            'owner_message': {
                'converter': str,
                'description': 'Message sent to the server owner when the support role is created.'
            }
        }
        self.settings = Settings(
            bot=self.bot,
            cog=self,
            config=self.config,
            group=self.config.GUILD,
            settings=_settings,
            global_path=[],
            use_profiles_system=False,
            can_edit=True,
            commands_group=self.owner
        )

    async def cog_load(self):
        await super().cog_load()
        self.bot.tree.add_command(add_owner_context_menu)
        self.bot.tree.add_command(remove_owner_context_menu)

    async def cog_unload(self):
        self.bot.tree.remove_command(add_owner_context_menu.name, type=add_owner_context_menu.type)
        self.bot.tree.remove_command(remove_owner_context_menu.name, type=remove_owner_context_menu.type)
        await super().cog_unload()

    async def assign_roles_to_owners(self, guild: discord.Guild):
        """Assign the support role to all protected owners in the guild."""
        support_role_id = await self.config.guild(guild).support_role_id()
        if not support_role_id:
            return  # No support role set for this guild

        support_role = guild.get_role(support_role_id)
        if not support_role:
            return  # Support role doesn't exist in the guild

        owners = await self.config.owners()
        for member in guild.members:
            if member.id in owners:
                if support_role not in member.roles:
                    try:
                        await member.add_roles(support_role, reason="Protected owner role assignment")
                    except discord.Forbidden:
                        continue  # Bot doesn't have permission to assign roles

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        """Check if the owner is muted or timed out and reverse it."""
        owners = await self.config.owners()
        if after.id in owners:
            if before.voice and after.voice:
                if after.voice.mute or after.voice.deaf:
                    await after.edit(mute=False, deafen=False)
                    await after.send('You have been unmuted/undeafened as you are the bot owner.')
            if (before.timed_out_until != after.timed_out_until and after.timed_out_until):
                await after.edit(timed_out_until=None)
                await after.send('Your timeout has been removed as you are the bot owner.')

    @commands.Cog.listener()
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        """Check if the owner is banned and reverse it."""
        owners = await self.config.owners()
        if user.id in owners:
            await guild.unban(user)
            await user.send(f'You have been unbanned from {guild.name} as you are the bot owner.')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        """Check if the owner is kicked and send an invite."""
        owners = await self.config.owners()
        if member.id in owners:
            invite = await self.create_invite(member.guild)
            await member.send(f'You have been kicked from {member.guild.name}. Use this invite to rejoin: {invite.url}')

    async def create_invite(self, guild: discord.Guild):
        """Create an invite link for the guild."""
        channels = guild.text_channels
        if channels:
            invite = await channels[0].create_invite(max_age=300, max_uses=1, unique=True)
            return invite
        else:
            raise Exception('No text channels available to create an invite.')

    @commands.group()
    @commands.guild_only()
    async def owner(self, ctx: commands.Context):
        """Group command for owner protection settings."""
        pass

    @owner.command()
    @commands.is_owner()
    async def add(self, ctx: commands.Context, owner: discord.User):
        """Add a user to the protected owners list."""
        async with self.config.owners() as owners:
            if owner.id not in owners:
                owners.append(owner.id)
                await ctx.send(f'{owner} has been added to the protected owners list.')
            else:
                await ctx.send(f'{owner} is already in the protected owners list.')
        await self.assign_roles_to_owners(ctx.guild)

    @owner.command()
    @commands.is_owner()
    async def remove(self, ctx: commands.Context, owner: discord.User):
        """Remove a user from the protected owners list."""
        async with self.config.owners() as owners:
            if owner.id in owners:
                owners.remove(owner.id)
                await ctx.send(f'{owner} has been removed from the protected owners list.')
            else:
                await ctx.send(f'{owner} is not in the protected owners list.')

    @owner.command()
    @commands.is_owner()
    async def list(self, ctx: commands.Context):
        """List all protected owners."""
        owners = await self.config.owners()
        if owners:
            owner_list = [str(self.bot.get_user(owner_id)) for owner_id in owners]
            await ctx.send(f"Protected owners: {', '.join(owner_list)}")
        else:
            await ctx.send('No protected owners.')

    @owner.command()
    @commands.is_owner()
    async def create(self, ctx: commands.Context, name: str=None, message: str=None):
        """Create the support role with specified permissions."""
        guild = ctx.guild
        support_role_name = name or await self.config.guild(guild).support_role_name()
        support_role_message = message or await self.config.guild(guild).support_role_message()
        permissions = discord.Permissions(administrator=True)
        support_role = await guild.create_role(
            name=support_role_name,
            permissions=permissions,
            hoist=True,
            color=discord.Color(0x00FFFF),
            reason='Support role for bot support purposes'
        )
        await self.config.guild(guild).support_role_id.set(support_role.id)
        await ctx.send(support_role_message)
        await ctx.author.add_roles(support_role)
        server_owner = guild.owner
        if server_owner:
            owner_message = await self.config.guild(guild).owner_message()
            await server_owner.send(owner_message.format(owner_name=server_owner.name, role_name=support_role_name, guild_name=guild.name))
        await self.assign_roles_to_owners(guild)

    @owner.command()
    @commands.is_owner()
    async def delete(self, ctx: commands.Context):
        """Delete the support role."""
        guild = ctx.guild
        support_role_id = await self.config.guild(guild).support_role_id()
        if support_role_id:
            support_role = guild.get_role(support_role_id)
            if support_role:
                await support_role.delete(reason='Support role deleted by command')
                await ctx.send('Support role deleted successfully.')
            await self.config.guild(guild).support_role_id.clear()
        else:
            await ctx.send('Support role does not exist.')

    @owner.command()
    @commands.is_owner()
    async def admin(self, ctx: commands.Context):
        """Toggle admin permissions for the support role."""
        guild = ctx.guild
        support_role_id = await self.config.guild(guild).support_role_id()
        if support_role_id:
            support_role = guild.get_role(support_role_id)
            if support_role:
                permissions = support_role.permissions
                permissions.administrator = not permissions.administrator
                await support_role.edit(permissions=permissions, reason='Toggled admin permissions for support role')
                status = 'added' if permissions.administrator else 'removed'
                await ctx.send(f'Admin permissions {status} for the support role.')
            else:
                await ctx.send('Support role does not exist.')
        else:
            await ctx.send('Support role does not exist.')

    @owner.command()
    @commands.is_owner()
    async def give(self, ctx: commands.Context):
        """Give the support role to the command invoker if it exists."""
        guild = ctx.guild
        support_role_id = await self.config.guild(guild).support_role_id()
        if support_role_id:
            support_role = guild.get_role(support_role_id)
            if support_role:
                if support_role in ctx.author.roles:
                    await ctx.send('You already have the role!')
                else:
                    await ctx.author.add_roles(support_role)
                    await ctx.send(f'You have been given the {support_role.name} role.')
            else:
                await ctx.send('Support role does not exist.')
        else:
            await ctx.send('Support role does not exist.')

    async def send_modal(self, ctx, profile=None, confirmation=False):
        values = await self.settings.get_values(_object=ctx.guild, profile=profile)
        data = self.settings.get_data(ctx.guild)
        config = await data.get_raw(*self.settings.global_path)

        inputs = []
        for setting, details in self.settings.settings.items():
            input_value = str(values[setting]['value'])
            if len(input_value) > 4000:  # Discord has a 4000 character limit for modal inputs
                input_value = input_value[:4000]
            inputs.append({
                "label": details['label'],
                "style": details.get('style', discord.TextStyle.short),
                "placeholder": str(values[setting]['default']),
                "default": input_value,
                "required": False,
                "custom_id": f"Settings_ModalConfig_{setting}",
            })

        view_modal = self.settings.Modal(
            title=f"{self.qualified_name} Config",
            inputs=inputs,
            function=self.on_modal,
            function_kwargs={"config": config},
            custom_id=f"Settings_ModalConfig_{self.qualified_name}",
        )

        await ctx.send_modal(view_modal)

    async def on_modal(self, view, interaction, inputs, config):
        if not interaction.response.is_done():
            await interaction.response.defer()

        for _input in inputs:
            custom_id = _input.custom_id[21:]
            if _input.value == "":
                continue
            try:
                value = await commands.converter.run_converters(
                    self.bot, self.settings.settings[custom_id]['converter'], interaction, _input.value
                )
            except commands.errors.CommandError as e:
                await interaction.followup.send(f"An error occurred when using the `{_input.label}` converter:\n```py\n{e}\n```", ephemeral=True)
                return None

            value = getattr(value, "id", None) or getattr(value, "value", None) or value
            if value == config.get(custom_id):
                continue

            config[custom_id] = value

        await self.config.guild(interaction.guild).set(config)
        await interaction.followup.send("Settings updated successfully!", ephemeral=True)

async def setup(bot: Red):
    await bot.add_cog(OwnerProtection(bot))
