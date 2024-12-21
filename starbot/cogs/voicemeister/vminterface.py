import os
from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont
import discord
from starbot.core.bot import Red
from Star-Utils import Buttons, Dropdown

MAX_CHANNEL_NAME_LENGTH = 100

DEFAULT_EMOJIS = {
    "lock": "<:Locked:1279848927587467447>",
    "unlock": "<:Unlocked:1279848944570073109>",
    "limit": "<:People:1279848931043573790>",
    "hide": "<:Crossed_Eye:1279848957475819723>",
    "unhide": "<:Eye:1279848986299076728>",
    "invite": "<:Invite:1279857570634272818>",
    "ban": "<:Hammer:1279848987922530365>",
    "permit": "<:Check_Mark:1279848948491747411>",
    "rename": "<:Pensil:1279848929126645879>",
    "bitrate": "<:Headphones:1279848994327232584>",
    "region": "<:Servers:1279848940786810891>",
    "claim": "<:Crown:1279848977658810451>",
    "transfer": "<:Person_With_Rotation:1279848936752021504>",
    "info": "<:Information:1279848926383702056>",
    "delete": "<:TrashCan:1279875131136806993>",
    "create_text": "<:SpeachBubble:1279890650535428198>"
}

class VMInterface:
    """Interface and button handling for VoiceMeister."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.image_path = "interface.png"

    async def interface(self, ctx: discord.ext.commands.Context):
        """Open the voice interface."""
        # Check if the image file already exists
        if not os.path.exists(self.image_path):
            await self._generate_interface_image(ctx)

        file = discord.File(fp=self.image_path, filename="interface.png")
        view = VoiceMeisterView(bot=self.bot, author=ctx.author, infinity=True)
        embed = discord.Embed(
            title="Voice Interface",
            description="Use these buttons to control your private voice!",
            color=discord.Color.blue()
        )
        embed.set_image(url="attachment://interface.png")
        await ctx.send(embed=embed, file=file, view=view)

    async def _generate_interface_image(self, ctx: discord.ext.commands.Context):
        """Generate an image for the interface description using Discord emojis."""
        actions = [
            ("lock", "Lock"),
            ("unlock", "Unlock"),
            ("hide", "Hide"),
            ("unhide", "Unhide"),
            ("limit", "Limit"),
            ("ban", "Ban"),
            ("permit", "Permit"),
            ("claim", "Claim"),
            ("transfer", "Transfer"),
            ("info", "Info"),
            ("rename", "Rename"),
            ("bitrate", "Bitrate"),
            ("region", "Region"),
            ("create_text", "WIP"),
            ("delete", "Delete"),
            ("invite", "Invite")
        ]

        # Calculate dimensions
        num_columns = 4
        num_rows = (len(actions) + num_columns - 1) // num_columns
        box_width = 100
        box_height = 30
        padding = 7
        total_width = box_width * num_columns + padding * (num_columns - 1)
        total_height = box_height * num_rows + padding * (num_rows - 1)

        # Use the bot's color for the box background
        bot_color = ctx.me.color.to_rgb()

        # Create the image with a transparent background
        image = Image.new("RGBA", (total_width, total_height), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Use a default font provided by Pillow
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)
        except IOError:
            font = ImageFont.load_default()

        def draw_rounded_rectangle(draw, xy, radius, fill, outline=None, width=1):
            """Draw a rounded rectangle."""
            x1, y1, x2, y2 = xy
            draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
            draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
            draw.pieslice([x1, y1, x1 + 2 * radius, y1 + 2 * radius], 180, 270, fill=fill)
            draw.pieslice([x2 - 2 * radius, y1, x2, y1 + 2 * radius], 270, 360, fill=fill)
            draw.pieslice([x1, y2 - 2 * radius, x1 + 2 * radius, y2], 90, 180, fill=fill)
            draw.pieslice([x2 - 2 * radius, y2 - 2 * radius, x2, y2], 0, 90, fill=fill)
            if outline:
                draw.arc([x1, y1, x1 + 2 * radius, y1 + 2 * radius], 180, 270, fill=outline, width=width)
                draw.arc([x2 - 2 * radius, y1, x2, y1 + 2 * radius], 270, 360, fill=outline, width=width)
                draw.arc([x1, y2 - 2 * radius, x1 + 2 * radius, y2], 90, 180, fill=outline, width=width)
                draw.arc([x2 - 2 * radius, y2 - 2 * radius, x2, y2], 0, 90, fill=outline, width=width)
                draw.line([x1 + radius, y1, x2 - radius, y1], fill=outline, width=width)
                draw.line([x1 + radius, y2, x2 - radius, y2], fill=outline, width=width)
                draw.line([x1, y1 + radius, x1, y2 - radius], fill=outline, width=width)
                draw.line([x2, y1 + radius, x2, y2 - radius], fill=outline, width=width)

        # Draw the boxes, emojis, and names
        for i, (emoji_name, name) in enumerate(actions):
            x = (i % num_columns) * (box_width + padding)
            y = (i // num_columns) * (box_height + padding)

            # Draw rounded rectangle with bot's color fill
            draw_rounded_rectangle(draw, [x, y, x + box_width, y + box_height], radius=10, fill=bot_color, outline=bot_color, width=2)

            # Fetch emoji image
            emoji_id = DEFAULT_EMOJIS[emoji_name].split(":")[2].strip(">")
            emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.png"
            response = requests.get(emoji_url)
            emoji_image = Image.open(BytesIO(response.content)).resize((20, 20))
            image.paste(emoji_image, (x + 5, y + (box_height - 20) // 2), emoji_image)

            # Draw the name next to the emoji
            text_bbox = font.getbbox(name)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            draw.text(
                (x + 30, y + (box_height - text_height) / 2),
                name,
                fill=(255, 255, 255),  # White text
                font=font
            )

        # Save the image to a file
        image.save(self.image_path, format="PNG")

# View Class for Control Panel

class VoiceMeisterView(Buttons):
    def __init__(self, bot: Red, author: discord.Member, infinity: bool = True):
        buttons = [
            {"emoji": DEFAULT_EMOJIS["lock"], "custom_id": "lock", "row": 0},
            {"emoji": DEFAULT_EMOJIS["unlock"], "custom_id": "unlock", "row": 0},
            {"emoji": DEFAULT_EMOJIS["hide"], "custom_id": "hide", "row": 0},
            {"emoji": DEFAULT_EMOJIS["unhide"], "custom_id": "unhide", "row": 0},
            {"emoji": DEFAULT_EMOJIS["limit"], "custom_id": "limit", "row": 1},
            {"emoji": DEFAULT_EMOJIS["ban"], "custom_id": "ban", "row": 1},
            {"emoji": DEFAULT_EMOJIS["permit"], "custom_id": "permit", "row": 1},
            {"emoji": DEFAULT_EMOJIS["claim"], "custom_id": "claim", "row": 1},
            {"emoji": DEFAULT_EMOJIS["transfer"], "custom_id": "transfer", "row": 2},
            {"emoji": DEFAULT_EMOJIS["info"], "custom_id": "info", "row": 2},
            {"emoji": DEFAULT_EMOJIS["rename"], "custom_id": "rename", "row": 2},
            {"emoji": DEFAULT_EMOJIS["bitrate"], "custom_id": "bitrate", "row": 2},
            {"emoji": DEFAULT_EMOJIS["region"], "custom_id": "region", "row": 3},
            {"emoji": DEFAULT_EMOJIS["create_text"], "custom_id": "wip", "row": 3},  # Changed custom_id to "wip"
            {"emoji": DEFAULT_EMOJIS["delete"], "custom_id": "delete", "row": 3},
            {"emoji": DEFAULT_EMOJIS["invite"], "custom_id": "invite", "row": 3},
        ]
        super().__init__(buttons=buttons, members=[author.id] + list(bot.owner_ids), function=self.on_button_click, infinity=infinity)
        self.bot = bot
        self.author = author

    async def on_button_click(self, view: Buttons, interaction: discord.Interaction):
        handlers = {
            "lock": self.handle_lock,
            "unlock": self.handle_unlock,
            "limit": self.handle_user_limit,
            "hide": self.handle_hide,
            "unhide": self.handle_unhide,
            "invite": self.handle_invite,
            "ban": self.handle_ban,
            "permit": self.handle_permit,
            "rename": self.handle_rename,
            "bitrate": self.handle_bitrate,
            "region": self.handle_region,
            "claim": self.handle_claim,
            "transfer": self.handle_transfer,
            "info": self.handle_info,
            "delete": self.handle_delete,
            "wip": self.handle_wip,  # Added handler for WIP
        }
        handler = handlers.get(interaction.data["custom_id"])
        if handler:
            voice_channel = self.bot.get_cog("VoiceMeister")._get_current_voice_channel(interaction.user)
            if voice_channel:
                owners = await self.bot.get_cog("VoiceMeister").config.guild(voice_channel.guild).owners()
                owner_id = owners.get(str(voice_channel.id))
                if interaction.data["custom_id"] == "info" or interaction.user.id == owner_id:
                    await handler(interaction, voice_channel)
                else:
                    await interaction.response.send_message("You are not the owner of this channel.", ephemeral=True)

    async def handle_lock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        if channel.overwrites_for(interaction.guild.default_role).connect is False:
            await interaction.response.send_message("The channel is already locked.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister").locked(interaction, channel)

    async def handle_unlock(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        if channel.overwrites_for(interaction.guild.default_role).connect is True:
            await interaction.response.send_message("The channel is already unlocked.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister").unlock(interaction, channel)

    async def handle_user_limit(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(SetUserLimitModal(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_hide(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Hide the channel by setting view permissions to False for @everyone."""
        try:
            overwrites = channel.overwrites_for(interaction.guild.default_role)
            if overwrites.view_channel is False:
                await interaction.response.send_message("The channel is already hidden.", ephemeral=True)
            else:
                overwrites.view_channel = False
                await channel.set_permissions(interaction.guild.default_role, overwrite=overwrites)
                await interaction.response.send_message("The channel is now hidden.", ephemeral=True)
        except Exception as e:
            await self.bot.get_cog("VoiceMeister").handle_error(interaction, e)

    async def handle_unhide(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Unhide the channel by setting view permissions to True for @everyone."""
        try:
            overwrites = channel.overwrites_for(interaction.guild.default_role)
            if overwrites.view_channel is True:
                await interaction.response.send_message("The channel is already visible.", ephemeral=True)
            else:
                overwrites.view_channel = True
                await channel.set_permissions(interaction.guild.default_role, overwrite=overwrites)
                await interaction.response.send_message("The channel is now visible.", ephemeral=True)
        except Exception as e:
            await self.bot.get_cog("VoiceMeister").handle_error(interaction, e)

    async def handle_invite(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        invite = await channel.create_invite(max_uses=5, unique=True)
        await interaction.response.send_message(content=f"Here is your invite to the voice channel: {invite.url}", ephemeral=True)

    async def handle_ban(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a member to ban.", view=DenyAllowSelect(self.bot.get_cog("VoiceMeister"), channel, action="deny"), ephemeral=True)

    async def handle_permit(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a member to permit.", view=DenyAllowSelect(self.bot.get_cog("VoiceMeister"), channel, action="allow"), ephemeral=True)

    async def handle_rename(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_modal(ChangeNameModal(self.bot.get_cog("VoiceMeister"), channel))

    async def handle_bitrate(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a bitrate.", view=BitrateSelectView(self.bot.get_cog("VoiceMeister"), channel), ephemeral=True)

    async def handle_region(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").change_region(interaction, channel)

    async def handle_claim(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        owners = await self.bot.get_cog("VoiceMeister").config.guild(channel.guild).owners()
        current_owner_id = owners.get(str(channel.id))
        if current_owner_id == interaction.user.id:
            await interaction.response.send_message("You already own this channel.", ephemeral=True)
        else:
            await self.bot.get_cog("VoiceMeister").claim(interaction, channel)

    async def handle_transfer(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await interaction.response.send_message("Select a member to transfer ownership to.", view=TransferOwnershipSelect(self.bot.get_cog("VoiceMeister"), channel), ephemeral=True)

    async def handle_info(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").info(interaction, channel)

    async def handle_delete(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await self.bot.get_cog("VoiceMeister").delete_channel(interaction, channel)

    async def handle_wip(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        """Handle the WIP button interaction."""
        await interaction.response.send_message("This item is a Work In Progress! Check back soon!", ephemeral=True)

class DenyAllowSelect(Dropdown):
    def __init__(self, cog, channel, action):
        user_options = [{"label": member.display_name, "value": str(member.id)} for member in channel.members]
        super().__init__(
            placeholder="Select a member",
            options=user_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel, "action": action},
            infinity=True
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel, action):
        try:
            selected_user_id = int(options[0])
            user = channel.guild.get_member(selected_user_id)

            if user:
                permission = True if action == "allow" else False
                await channel.set_permissions(user, connect=permission)
                await interaction.response.send_message(f"{user.display_name} has been {'allowed' if permission else 'denied'} access to the channel.", ephemeral=True)
        except Exception as e:
            await cog.handle_error(interaction, e)

class TransferOwnershipSelect(Dropdown):
    def __init__(self, cog, channel):
        member_options = [{"label": member.display_name, "value": str(member.id)} for member in channel.members]
        super().__init__(
            placeholder="Select a new owner",
            options=member_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel},
            infinity=True
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel):
        try:
            selected_user_id = int(options[0])
            new_owner = channel.guild.get_member(selected_user_id)

            if new_owner:
                await cog.transfer_ownership(interaction, channel, new_owner)
        except Exception as e:
            await cog.handle_error(interaction, e)

class BitrateSelectView(Dropdown):
    def __init__(self, cog, channel):
        bitrate_options = [{"label": f"{bitrate} kbps", "value": str(bitrate)} for bitrate in BITRATE_OPTIONS]
        super().__init__(
            placeholder="Select Bitrate",
            options=bitrate_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel},
            infinity=True
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel):
        try:
            selected_bitrate = int(options[0])
            await channel.edit(bitrate=selected_bitrate * 1000)
            await interaction.response.send_message(f"Bitrate changed to {selected_bitrate} kbps.", ephemeral=True)
        except Exception as e:
            await cog.handle_error(interaction, e)

class ChangeNameModal(discord.ui.Modal, title="Change Channel Name"):
    def __init__(self, cog, channel):
        self.cog = cog
        self.channel = channel
        super().__init__()

    new_name = discord.ui.TextInput(label="New Channel Name", custom_id="new_channel_name", style=discord.TextStyle.short, max_length=MAX_CHANNEL_NAME_LENGTH)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            new_name = self.new_name.value
            if not self.cog.is_name_valid(new_name):
                await interaction.followup.send("The channel name contains inappropriate content. Please choose another name.", ephemeral=True)
                return

            if self.channel:
                await self.channel.edit(name=new_name)
                await interaction.followup.send(f"Channel name changed to {new_name}.", ephemeral=True)
        except Exception as e:
            await self.cog.handle_error(interaction, e)

class SetUserLimitModal(discord.ui.Modal, title="Set User Limit"):
    def __init__(self, cog, channel):
        self.cog = cog
        self.channel = channel
        super().__init__()

    user_limit_input = discord.ui.TextInput(label="User Limit (0 for Unlimited)", custom_id="user_limit_input", style=discord.TextStyle.short)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            await interaction.response.defer(ephemeral=True)
            user_limit_value = self.user_limit_input.value
            if not user_limit_value.isdigit() or int(user_limit_value) < 0:
                await interaction.followup.send("Invalid user limit. Please enter a non-negative integer.", ephemeral=True)
                return

            user_limit = None if int(user_limit_value) == 0 else int(user_limit_value)
            await self.channel.edit(user_limit=user_limit)
            await interaction.followup.send(
                f"User limit set to {'Unlimited' if user_limit is None else str(user_limit) + ' members'}.",
                ephemeral=True
            )
        except Exception as e:
            await self.cog.handle_error(interaction, e)

class RegionSelectView(Dropdown):
    def __init__(self, cog, channel):
        region_options = [{"label": name, "value": region or "automatic"} for name, region in REGION_OPTIONS]
        super().__init__(
            placeholder="Select Region",
            options=region_options,
            function=self.on_select,
            function_kwargs={"cog": cog, "channel": channel},
            infinity=True
        )

    async def on_select(self, view: Dropdown, interaction: discord.Interaction, options: list, cog, channel):
        try:
            await interaction.response.defer(ephemeral=True)
            selected_region = options[0]
            rtc_region = None if selected_region == "automatic" else selected_region
            await channel.edit(rtc_region=rtc_region)
            await interaction.followup.send(f"Region changed to {selected_region if rtc_region else 'Automatic'}.", ephemeral=True)
        except Exception as e:
            await cog.handle_error(interaction, e)
