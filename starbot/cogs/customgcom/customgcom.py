from starbot.core import commands, Config, checks
from starbot.core.utils.chat_formatting import pagify, box
import asyncio
import os
import re
from Star-Utils import Cog, CogsUtils

# Define the path for your data
PATH = 'data/customgcom/'
JSON = PATH + 'commands.json'

class CustomGlobalCommands(Cog):
    """Global custom commands."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_global = {"COMMANDS": {}, "ALIASES": {}, "_CGCOM_VERSION": 2}
        self.config.register_global(**default_global)

    @commands.command()
    @checks.is_owner()
    async def setgcom(self, ctx, command: str, *, text):
        """Adds a global custom command"""
        command = command.lower()
        if command in self.bot.all_commands:
            await ctx.send("That command is already a normal command.")
            return

        async with self.config.COMMANDS() as commands:
            if command not in commands:
                commands[command] = text
                await ctx.send("Custom command successfully added.")
            else:
                await ctx.send("This command already exists. Are you sure "
                               "you want to redefine it? [y/N]")
                try:
                    response = await self.bot.wait_for("message", check=lambda m: m.author == ctx.author, timeout=30.0)
                except asyncio.TimeoutError:
                    await ctx.send("No response. Command not redefined.")
                    return

                if response.content.lower().strip() in ['y', 'yes']:
                    commands[command] = text
                    await ctx.send("Custom command successfully set.")
                else:
                    await ctx.send("OK, leaving that command alone.")

    @commands.command()
    @checks.is_owner()
    async def rmgcom(self, ctx, command: str):
        """Removes a global custom command"""
        command = command.lower()
        async with self.config.COMMANDS() as commands:
            if command in commands:
                commands.pop(command)
                await ctx.send("Global custom command successfully deleted.")
            else:
                await ctx.send("That command doesn't exist.")

    @commands.command()
    async def lsgcom(self, ctx):
        """Shows global custom commands list"""
        commands = await self.config.COMMANDS()
        if commands:
            sections = []
            for command, text in sorted(commands.items()):
                item = f'Name: {command}\nText: {text}'
                sections.append(item)

            for cmds in pagify('\n\n'.join(sections)):
                await ctx.send(box(cmds))
        else:
            await ctx.send("There are no global custom commands defined. Use setgcom [command] [text]")

    @commands.group(invoke_without_command=True)
    @checks.is_owner()
    async def agcom(self, ctx, command=None):
        """Create aliases for Global Custom Commands"""
        if ctx.invoked_subcommand is None:
            if command:
                await ctx.invoke(self.ls_aliases, command)
            else:
                await ctx.invoke(self.lsgcom)

    @agcom.command(name='show')
    @checks.is_owner()
    async def ls_aliases(self, ctx, command):
        """Shows aliases for a command, or the command bound to an alias"""
        aliases = await self.config.ALIASES()
        base = aliases.get(command)
        commands = await self.config.COMMANDS()
        cmd = commands.get(base or command)
        if base:
            msg = f"`{command}` is an alias for `{base}`"
        elif cmd:
            alias_list = [k for k, v in aliases.items() if v == command]
            alias_str = ', '.join(f'`{x}`' for x in alias_list)
            if alias_str:
                msg = f"`{command}` has the following aliases: {alias_str}."
            else:
                msg = f"`{command}` has no aliases."
        else:
            msg = f"`{command}` isn't a custom command or alias."

        await ctx.send(msg)

    @agcom.command(name='add')
    @checks.is_owner()
    async def add_aliases(self, ctx, command, *aliases):
        """Add one or more aliases for a custom command"""
        command = command.lower()
        commands = await self.config.COMMANDS()
        if command not in commands:
            await ctx.send(f"`{command}` isn't a custom command.")
            return

        existing_a = []
        existing_c = []
        count = 0

        async with self.config.ALIASES() as alias_config:
            for alias in aliases:
                if alias in alias_config:
                    existing_a.append(alias)
                elif alias in self.bot.all_commands:
                    existing_c.append(alias)
                else:
                    alias_config[alias] = command
                    count += 1

        msg = f"{count if count else 'No'} new aliases added."
        if existing_a:
            joined = ', '.join(f'`{x}`' for x in existing_a)
            msg += f"\nThe following are already aliases: {joined}."
        if existing_c:
            joined = ', '.join(f'`{x}`' for x in existing_c)
            msg += f"\nThe following are already normal commands: {joined}."

        await ctx.send(msg)

    @agcom.command(name='rm')
    @checks.is_owner()
    async def rm_aliases(self, ctx, *aliases):
        """Remove an alias from a global cc"""
        count = 0
        skipped = []

        async with self.config.ALIASES() as alias_config:
            for alias in aliases:
                if alias in alias_config:
                    del alias_config[alias]
                    count += 1
                else:
                    skipped.append(alias)

        msg = f"{count if count else 'No'} aliases removed."
        if skipped:
            skipped = ', '.join(f'`{x}`' for x in skipped)
            msg += f"\nThe following aliases could not be found: {skipped}."

        await ctx.send(msg)

    async def on_message(self, message):
        if message.author.bot:
            return

        msg = message.content
        prefix = await self.get_prefix(message)
        if not prefix:
            return

        cmd = msg[len(prefix):].lower()
        aliases = await self.config.ALIASES()
        commands = await self.config.COMMANDS()
        cmd = aliases.get(cmd, cmd)
        if cmd in commands:
            ret = commands[cmd]
            ret = self.format_cc(ret, message)
            await message.channel.send(ret)

    async def get_prefix(self, msg):
        prefixes = await self.bot.get_valid_prefixes()
        for p in prefixes:
            if msg.content.startswith(p):
                return p
        return None

    def format_cc(self, command, message):
        results = re.findall(r"\{([^}]+)\}", command)
        for result in results:
            param = self.transform_parameter(result, message)
            command = command.replace("{" + result + "}", param)
        return command

    def transform_parameter(self, result, message):
        """
        For security reasons only specific objects are allowed
        Internals are ignored
        """
        raw_result = "{" + result + "}"
        objects = {
            "message": message,
            "author": message.author,
            "channel": message.channel,
            "guild": message.guild
        }
        if result in objects:
            return str(objects[result])
        try:
            first, second = result.split(".")
        except ValueError:
            return raw_result
        if first in objects and not second.startswith("_"):
            first = objects[first]
        else:
            return raw_result
        return str(getattr(first, second, raw_result))
