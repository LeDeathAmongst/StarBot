import discord
from starbot.core import commands
from Star-Utils import Cog
from .vminterface import VMInterface

class VoiceMeisterCommands(Cog):
    """Commands for managing existing VoiceMeisters."""
    def __init__(self, bot: commands.Bot, VMInterface):
        self.bot = bot
        self.voicemeister_cog = bot.get_cog("VoiceMeister")

    def _get_current_voice_channel(self, member: discord.Member) -> discord.VoiceChannel:
        """Get the member's current voice channel, or None if not in a voice channel."""
        if member.voice and isinstance(member.voice.channel, discord.VoiceChannel):
            return member.voice.channel
        return None

    @commands.group(name="voicemeister", aliases=["vm"])
    async def voicemeister_group(self, ctx: commands.Context):
        """Group for VoiceMeister commands."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @voicemeister_group.command()
    async def lock(self, ctx: commands.Context):
        """Lock your VoiceMeister."""
        voice_channel = self._get_current_voice_channel(ctx.author)
        if voice_channel:
            await self.voicemeister_cog.locked(ctx, voice_channel)

    @voicemeister_group.command()
    async def unlock(self, ctx: commands.Context):
        """Unlock your VoiceMeister."""
        voice_channel = self._get_current_voice_channel(ctx.author)
        if voice_channel:
            await self.voicemeister_cog.unlock(ctx, voice_channel)

    @voicemeister_group.command()
    async def claim(self, ctx: commands.Context):
        """Claim ownership of the VoiceMeister if there is no current owner, or override if admin/owner."""
        voice_channel = self._get_current_voice_channel(ctx.author)
        if voice_channel:
            await self.voicemeister_cog.claim(ctx, voice_channel)

    @voicemeister_group.command()
    async def delete_channel(self, ctx: commands.Context):
        """Delete the voice channel."""
        voice_channel = self._get_current_voice_channel(ctx.author)
        if voice_channel:
            await self.voicemeister_cog.delete_channel(ctx, voice_channel)

    @voicemeister_group.command()
    async def transfer_ownership(self, ctx: commands.Context, new_owner: discord.Member):
        """Transfer ownership of the channel."""
        voice_channel = self._get_current_voice_channel(ctx.author)
        if voice_channel:
            await self.voicemeister_cog.transfer_ownership(ctx, voice_channel, new_owner)

    @voicemeister_group.command()
    async def info(self, ctx: commands.Context):
        """Provide information about the current voice channel."""
        voice_channel = self._get_current_voice_channel(ctx.author)
        if voice_channel:
            await self.voicemeister_cog.info(ctx, voice_channel)
