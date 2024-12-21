from Star-Utils import Cog, CogsUtils
import io

import aiohttp
import discord
from colorthief import ColorThief
from red_commons.logging import RedTraceLogger, getLogger
from starbot.core import app_commands, commands
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import bold, humanize_list

from .model import PartialEmoji


class EmojiInfo(Cog):
    """Retrieve information about emojis."""

    def __init__(self, bot: Red) -> None:
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("EmojiInfo")
        self.bot: Red = bot
        self.logger: RedTraceLogger = getLogger(name="red.SeaCogs.Emoji")



    async def fetch_twemoji(self, unicode_emoji) -> str:
        base_url = "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/"
        emoji_codepoint = "-".join([hex(ord(char))[2:] for char in unicode_emoji])
        segments = emoji_codepoint.split("-")
        valid_segments = [seg for seg in segments if len(seg) >= 4]
        emoji_url = f"{base_url}{valid_segments[0]}.png"
        return emoji_url

    async def fetch_primary_color(self, emoji_url: str) -> discord.Color | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(emoji_url) as response:
                if response.status != 200:
                    return None
                image = await response.read()
        dominant_color = ColorThief(io.BytesIO(image)).get_color(quality=1)
        color = discord.Color.from_rgb(*dominant_color)
        return color

    async def get_emoji_info(self, emoji: PartialEmoji) -> tuple[str, str]:
        if emoji.is_unicode_emoji():
            try:
                emoji_url = await self.fetch_twemoji(unicode_emoji=emoji.name)
            except IndexError as e:
                raise e
        else:
            emoji_url = emoji.url

        if emoji.id is not None:
            emoji_id = f"{bold('ID:')} `{emoji.id}`\n"
            markdown = f"`<{'a' if emoji.animated else ''}:{emoji.name}:{emoji.id}>`"
            name = f"{bold('Name:')} {emoji.name}\n"
            aliases = ""
            group = ""
        else:
            emoji_id = ""
            markdown = f"`{emoji}`"
            name = f"{bold('Name:')} {emoji.aliases.pop(0)}\n"
            aliases = f"{bold('Aliases:')} {', '.join(emoji.aliases)}\n" if emoji.aliases else ""
            group = f"{bold('Group:')} {emoji.group}\n"

        return (
            f"{name}"
            f"{emoji_id}"
            f"{bold('Native:')} {emoji.is_unicode_emoji()}\n"
            f"{group}"
            f"{aliases}"
            f"{bold('Animated:')} {emoji.animated}\n"
            f"{bold('Markdown:')} {markdown}\n"
            f"{bold('URL:')} [Click Here]({emoji_url})"
        ), emoji_url

    @app_commands.command(name="emoji")
    @app_commands.describe(
        emoji="What emoji would you like to get information on?",
        ephemeral="Would you like the response to be hidden?"
    )
    async def emoji_slash(self, interaction: discord.Interaction, emoji: str, ephemeral: bool = True) -> None:
        """Retrieve information about an emoji."""
        await interaction.response.defer(ephemeral=ephemeral)

        try:
            emoji: PartialEmoji = PartialEmoji.from_str(self, value=emoji)
            string, emoji_url, = await self.get_emoji_info(emoji)
            self.logger.verbose(f"Emoji:\n{string}")
        except (IndexError, UnboundLocalError):
            return await interaction.followup.send("Please provide a valid emoji!")

        if await self.bot.embed_requested(channel=interaction.channel):
            embed = embed = discord.Embed(title="Emoji Information", description=string, color = await self.fetch_primary_color(emoji_url) or await self.bot.get_embed_color(interaction.channel))
            embed.set_thumbnail(url=emoji_url)

            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(content=string)

    @commands.command(name="emoji")
    async def emoji(self, ctx: commands.Context, *, emoji: str) -> None:
        """Retrieve information about an emoji."""
        try:
            emoji: PartialEmoji = PartialEmoji.from_str(self, value=emoji)
            string, emoji_url, = await self.get_emoji_info(emoji)
            self.logger.verbose(f"Emoji:\n{string}")
        except (IndexError, UnboundLocalError):
            return await ctx.send("Please provide a valid emoji!")

        if await ctx.embed_requested():
            embed = embed = discord.Embed(title="Emoji Information", description=string, color = await self.fetch_primary_color(emoji_url) or await ctx.embed_color)
            embed.set_thumbnail(url=emoji_url)

            await ctx.send(embed=embed)
        else:
            await ctx.send(content=string)
