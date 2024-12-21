import json
import os
import discord
import uuid
from Star-Utils import Cog
from starbot.core import commands, Config
from starbot.core.bot import Red
from discord.ext import commands as ext_commands

class FeatureRequest(Cog):
    """Cog to handle feature requests."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567892, force_registration=True)
        default_global = {'request_channels': {}, 'requests': {}}
        self.config.register_global(**default_global)

    async def save_to_json(self, request_data, file_name='feature_requests.json'):
        file_path = f'/data/cogs/FeatureRequest/{file_name}'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
        else:
            data = []

        # Check if the request already exists
        for i, request in enumerate(data):
            if request['request_id'] == request_data['request_id']:
                data[i] = request_data  # Update existing request
                break
        else:
            data.append(request_data)  # Add new request if not found

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    async def delete_from_json(self, request_id, file_name='feature_requests.json'):
        file_path = f'/data/cogs/FeatureRequest/{file_name}'
        if not os.path.exists(file_path):
            return False

        with open(file_path, 'r') as f:
            data = json.load(f)

        new_data = [request for request in data if request['request_id'] != request_id]

        with open(file_path, 'w') as f:
            json.dump(new_data, f, indent=2)

        return True

    @commands.hybrid_group(name='frequest', description="Feature Request Commands", aliases=['fr'])
    async def frequest(self, ctx: commands.Context):
        """Base command for feature requests."""
        pass

    @frequest.command(name='submit', description="Submit a new feature request")
    async def submit(self, ctx: commands.Context, feature: str):
        """Request a new feature for the bot."""
        request_channels = await self.config.request_channels()
        request_channel_id = request_channels.get(str(ctx.guild.id))
        if not request_channel_id:
            await ctx.send('Request channel is not set. Please ask the bot owner to set it using the frequest channel command.', ephemeral=True)
            return
        request_channel = self.bot.get_channel(request_channel_id)
        if not request_channel:
            await ctx.send('Request channel not found. Please ask the bot owner to set it again using the frequest channel command.', ephemeral=True)
            return

        request_id = str(uuid.uuid4())
        embed = discord.Embed(title='Feature Request', description=f'Feature requested by {ctx.author.mention}', color=discord.Color.blue())
        embed.add_field(name='Feature', value=feature, inline=True)
        embed.add_field(name='Status', value='Pending', inline=True)
        embed.add_field(name='Request ID', value=request_id, inline=True)

        # Add consider, accept, deny, and delete buttons
        view = RequestButtonsView(request_id, self)

        message = await request_channel.send(embed=embed, view=view)
        request_data = {
            'requester_id': ctx.author.id,
            'feature': feature,
            'status': 'pending',
            'message_id': message.id,
            'request_id': request_id
        }
        async with self.config.requests() as requests:
            requests[request_id] = request_data

        await self.save_to_json(request_data)

        await ctx.send(f'Your feature request has been successfully submitted! Your request ID is {request_id}', ephemeral=True)

    async def update_status_and_respond(self, interaction, request_id, status, color):
        async with self.config.requests() as requests:
            request_data = requests.get(request_id)
            if not request_data:
                await interaction.followup.send(f'No feature request found with ID: {request_id}', ephemeral=True)
                return
            request_data['status'] = status

            requester = self.bot.get_user(request_data['requester_id'])
            if requester:
                description = f'Your feature request with ID `{request_id}` was {status}.'
                try:
                    await requester.send(embed=discord.Embed(title=f'Feature Request {status.capitalize()}', description=description, color=color))
                except discord.Forbidden:
                    pass

            request_channels = await self.config.request_channels()
            request_channel_id = request_channels.get(str(interaction.guild.id))
            request_channel = self.bot.get_channel(request_channel_id)
            if request_channel:
                try:
                    message = await request_channel.fetch_message(request_data['message_id'])
                    embed = message.embeds[0]
                    embed.set_field_at(1, name='Status', value=status.capitalize(), inline=True)
                    embed.color = color
                    view = RequestButtonsView(request_id, self)
                    if status in ['accepted', 'denied', 'deleted']:
                        view.disable_all_buttons()
                    elif status == 'considering':
                        view.disable_consider_and_delete_buttons()
                    await message.edit(embed=embed, view=view)
                except discord.NotFound:
                    await interaction.followup.send(f"Message with ID {request_data['message_id']} not found in the request channel.", ephemeral=True)
                except discord.Forbidden:
                    await interaction.followup.send("I don't have permission to edit the message in the request channel.", ephemeral=True)

            if status == 'deleted':
                await self.delete_from_json(request_id)
            else:
                await self.save_to_json(request_data)

            await interaction.followup.send(f'Feature request with ID `{request_id}` has been {status}.', ephemeral=True)

    @frequest.command(name='channel', description="Set the channel for feature requests")
    @commands.is_owner()
    async def channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for feature requests."""
        async with self.config.request_channels() as channels:
            channels[str(ctx.guild.id)] = channel.id
        await ctx.send(f'Request channel set to: {channel.mention}')

    @frequest.command(name='sendembed', description="Send the feature request embed")
    @commands.is_owner()
    async def sendembed(self, ctx: commands.Context, for_bot_owner: bool = True):
        """Send the feature request embed."""
        bot_name = self.bot.user.name
        if for_bot_owner:
            description = (
                f"Like my work, but wish for something extra? Click this button below and answer the question sent to your DM's about the feature you want! "
                f"We also have options where you can buy your own version, through a different set of pre-configured bots!"
            )
        else:
            description = (
                f"Do you wish {bot_name} had a feature that it doesn't? Well, fear not! You can click this button to make a suggestion, and a developer on the team will determine if it's applicable! "
                f"Clicking the button will then send you a message in DM's, simply reply with the feature you want!"
            )

        embed = discord.Embed(title="Feature Request", description=description, color=discord.Color.blue())
        view = FeatureRequestButtonView(self)

        await ctx.send(embed=embed, view=view)


class SlashRequest(Cog):
    """Cog to handle slash command feature requests."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567893, force_registration=True)
        default_global = {'request_channels': {}, 'requests': {}}
        self.config.register_global(**default_global)

    async def save_to_json(self, request_data, file_name='slash_requests.json'):
        file_path = f'/data/cogs/FeatureRequest/{file_name}'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
        else:
            data = []

        # Check if the request already exists
        for i, request in enumerate(data):
            if request['request_id'] == request_data['request_id']:
                data[i] = request_data  # Update existing request
                break
        else:
            data.append(request_data)  # Add new request if not found

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    async def delete_from_json(self, request_id, file_name='slash_requests.json'):
        file_path = f'/data/cogs/FeatureRequest/{file_name}'
        if not os.path.exists(file_path):
            return False

        with open(file_path, 'r') as f:
            data = json.load(f)

        new_data = [request for request in data if request['request_id'] != request_id]

        with open(file_path, 'w') as f:
            json.dump(new_data, f, indent=2)

        return True

    @commands.hybrid_group(name='srequest', description="Slash Request Commands", aliases=['sr'])
    async def srequest(self, ctx: commands.Context):
        """Base command for slash feature requests."""
        pass

    @srequest.command(name='submit', description="Submit a new slash feature request")
    async def submit(self, ctx: commands.Context, feature: str):
        """Request a new slash feature for the bot."""
        request_channels = await self.config.request_channels()
        request_channel_id = request_channels.get(str(ctx.guild.id))
        if not request_channel_id:
            await ctx.send('Request channel is not set. Please ask the bot owner to set it using the srequest channel command.', ephemeral=True)
            return
        request_channel = self.bot.get_channel(request_channel_id)
        if not request_channel:
            await ctx.send('Request channel not found. Please ask the bot owner to set it again using the srequest channel command.', ephemeral=True)
            return

        request_id = str(uuid.uuid4())
        embed = discord.Embed(title='Slash Feature Request', description=f'Slash feature requested by {ctx.author.mention}', color=discord.Color.blue())
        embed.add_field(name='Feature', value=feature, inline=True)
        embed.add_field(name='Status', value='Pending', inline=True)
        embed.add_field(name='Request ID', value=request_id, inline=True)

        # Add consider, accept, deny, and delete buttons
        view = RequestButtonsView(request_id, self)

        message = await request_channel.send(embed=embed, view=view)
        request_data = {
            'requester_id': ctx.author.id,
            'feature': feature,
            'status': 'pending',
            'message_id': message.id,
            'request_id': request_id
        }
        async with self.config.requests() as requests:
            requests[request_id] = request_data

        await self.save_to_json(request_data)

        await ctx.send(f'Your slash feature request has been successfully submitted! Your request ID is {request_id}', ephemeral=True)

    async def update_status_and_respond(self, interaction, request_id, status, color):
        async with self.config.requests() as requests:
            request_data = requests.get(request_id)
            if not request_data:
                await interaction.followup.send(f'No slash feature request found with ID: {request_id}', ephemeral=True)
                return
            request_data['status'] = status

            requester = self.bot.get_user(request_data['requester_id'])
            if requester:
                description = f'Your slash feature request with ID `{request_id}` was {status}.'
                try:
                    await requester.send(embed=discord.Embed(title=f'Slash Feature Request {status.capitalize()}', description=description, color=color))
                except discord.Forbidden:
                    pass

            request_channels = await self.config.request_channels()
            request_channel_id = request_channels.get(str(interaction.guild.id))
            request_channel = self.bot.get_channel(request_channel_id)
            if request_channel:
                try:
                    message = await request_channel.fetch_message(request_data['message_id'])
                    embed = message.embeds[0]
                    embed.set_field_at(1, name='Status', value=status.capitalize(), inline=True)
                    embed.color = color
                    view = RequestButtonsView(request_id, self)
                    if status in ['accepted', 'denied', 'deleted']:
                        view.disable_all_buttons()
                    elif status == 'considering':
                        view.disable_consider_and_delete_buttons()
                    await message.edit(embed=embed, view=view)
                except discord.NotFound:
                    await interaction.followup.send(f"Message with ID {request_data['message_id']} not found in the request channel.", ephemeral=True)
                except discord.Forbidden:
                    await interaction.followup.send("I don't have permission to edit the message in the request channel.", ephemeral=True)

            if status == 'deleted':
                await self.delete_from_json(request_id)
            else:
                await self.save_to_json(request_data)

            await interaction.followup.send(f'Slash feature request with ID `{request_id}` has been {status}.', ephemeral=True)

    @srequest.command(name='channel', description="Set the channel for slash feature requests")
    @commands.is_owner()
    async def channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for slash feature requests."""
        async with self.config.request_channels() as channels:
            channels[str(ctx.guild.id)] = channel.id
        await ctx.send(f'Request channel set to: {channel.mention}')


class RequestButtonsView(discord.ui.View):
    def __init__(self, request_id, cog):
        super().__init__(timeout=None)
        self.request_id = request_id
        self.cog = cog

    @discord.ui.button(label="Consider", style=discord.ButtonStyle.primary, custom_id="consider")
    async def consider_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.update_status_and_respond(interaction, self.request_id, 'considering', discord.Color.blue())
        self.disable_consider_and_delete_buttons()
        await interaction.message.edit(view=self)

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.success, custom_id="accept")
    async def accept_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.update_status_and_respond(interaction, self.request_id, 'accepted', discord.Color.green())
        self.disable_all_buttons()
        await interaction.message.edit(view=self)

    @discord.ui.button(label="Deny", style=discord.ButtonStyle.danger, custom_id="deny")
    async def deny_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.update_status_and_respond(interaction, self.request_id, 'denied', discord.Color.red())
        self.disable_all_buttons()
        await interaction.message.edit(view=self)

    @discord.ui.button(label="Delete", style=discord.ButtonStyle.danger, custom_id="delete")
    async def delete_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.cog.update_status_and_respond(interaction, self.request_id, 'deleted', discord.Color.greyple())
        self.disable_all_buttons()
        await interaction.message.edit(view=self)

    def disable_all_buttons(self):
        for child in self.children:
            child.disabled = True

    def disable_consider_and_delete_buttons(self):
        for child in self.children:
            if child.custom_id in ["consider", "delete"]:
                child.disabled = True


class FeatureRequestButtonView(discord.ui.View):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog

    @discord.ui.button(label="Submit Feature Request", style=discord.ButtonStyle.primary, custom_id="submit_request")
    async def submit_request_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        try:
            await user.send("What is the feature you wish to have?")
            await interaction.followup.send("Please check your DM's to submit your feature request.", ephemeral=True)

            def check(m):
                return m.author == user and isinstance(m.channel, discord.DMChannel)

            message = await self.cog.bot.wait_for('message', check=check)
            feature = message.content
            
            # Simulate a context for the submit command
            ctx = await self.cog.bot.get_context(message)
            await self.cog.submit(ctx, feature)

        except discord.Forbidden:
            await interaction.followup.send("I couldn't send you a DM. Please make sure your DMs are open.", ephemeral=True)


def setup(bot):
    bot.add_cog(FeatureRequest(bot))
    bot.add_cog(SlashRequest(bot))
