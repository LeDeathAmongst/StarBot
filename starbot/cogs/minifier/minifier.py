import contextlib
import io
from Star-Utils import Cog, CogsUtils

import discord
import python_minifier as minifier
from starbot.core import commands
from starbot.core.bot import Red


class Minifier(Cog):
    """Minify your code!"""

        
    def __init__(self, bot: Red):
        self.bot = bot


    async def red_delete_data_for_user(self, **kwargs):
        return

    @commands.has_permissions(attach_files=True)
    @commands.command(usage="<file>")
    async def minify(self, ctx):
        """Minify a python file.

        You need to attach a file to this command, and it's extension needs to be `.py`.
        """
        await ctx.typing()
        if not ctx.message.attachments:
            return await ctx.send_help()
        file = ctx.message.attachments[0]
        file_name = file.filename.lower()
        if not file_name.endswith((".py", ".python")):
            return await ctx.send("Must be a python file.")
        try:
            file = await file.read()
        except UnicodeDecodeError:
            return await ctx.send("Something went wrong when trying to decode this file.")
        converted = io.BytesIO(minifier.minify(file).encode(encoding="utf-8"))
        return await ctx.send(
            content="Please see the attached file below, with your minified code.",
            file=discord.File(converted, filename=file_name),
        )
