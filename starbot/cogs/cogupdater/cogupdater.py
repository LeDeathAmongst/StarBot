import os
import re
import shutil
import discord
from starbot.core import commands, Config
from starbot.core.bot import Red
from Star-Utils import Cog, CogsUtils

class CogUpdater(Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {"datapath": "", "backup_path": ""}
        self.config.register_global(**default_global)

    @commands.command()
    @commands.is_owner()
    async def setpath(self, ctx, path: str):
        """Set the path to the cog data directory."""
        await self.config.datapath.set(path)
        backup_path = os.path.join(path, "cog_backups")
        await self.config.backup_path.set(backup_path)
        embed = discord.Embed(title="Path Set", color=discord.Color.green())
        embed.description = f"Data path set to: {path}\nBackup path set to: {backup_path}"
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def updatecogs(self, ctx, *, cogs: str = None):
        """Update specified cogs or all cogs if none specified."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath:
            embed = discord.Embed(title="Error", color=discord.Color.red())
            embed.description = "Please set the data path first using `setpath`."
            await ctx.send(embed=embed)
            return

        os.makedirs(backup_path, exist_ok=True)

        cog_list = [cog.strip() for cog in cogs.split(',')] if cogs else None

        updated_files = 0
        updated_cogs = set()
        for root, dirs, files in os.walk(datapath):
            for file in files:
                if file.endswith('.py'):
                    cog_name = os.path.splitext(file)[0]
                    if cog_list and cog_name not in cog_list:
                        continue

                    filepath = os.path.join(root, file)
                    relative_path = os.path.relpath(filepath, datapath)
                    backup_file = os.path.join(backup_path, relative_path)
                    os.makedirs(os.path.dirname(backup_file), exist_ok=True)
                    shutil.copy2(filepath, backup_file)

                    updated = await self.update_file(filepath)

                    if updated:
                        updated_files += 1
                        updated_cogs.add(cog_name)

        embed = discord.Embed(title="Cogs Updated", color=discord.Color.green())
        if cog_list:
            embed.description = f"Updated {updated_files} files for cogs: {', '.join(updated_cogs)}. Backups created in {backup_path}"
        else:
            embed.description = f"Updated {updated_files} files across all cogs. Backups created in {backup_path}"
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def undoupdates(self, ctx, *, cogs: str = None):
        """Undo the updates made to specified cogs or all cogs if none specified."""
        datapath = await self.config.datapath()
        backup_path = await self.config.backup_path()
        if not datapath or not backup_path:
            embed = discord.Embed(title="Error", color=discord.Color.red())
            embed.description = "Please set the data path first using `setpath`."
            await ctx.send(embed=embed)
            return

        cog_list = [cog.strip() for cog in cogs.split(',')] if cogs else None

        restored_files = 0
        restored_cogs = set()
        for root, dirs, files in os.walk(backup_path):
            for file in files:
                if file.endswith('.py'):
                    cog_name = file[:-3]
                    if cog_list and cog_name not in cog_list:
                        continue

                    backup_file = os.path.join(root, file)
                    relative_path = os.path.relpath(backup_file, backup_path)
                    original_file = os.path.join(datapath, relative_path)
                    shutil.copy2(backup_file, original_file)
                    restored_files += 1
                    restored_cogs.add(cog_name)

        embed = discord.Embed(title="Updates Undone", color=discord.Color.green())
        if cog_list:
            embed.description = f"Restored {restored_files} files for cogs: {', '.join(restored_cogs)}."
        else:
            embed.description = f"Restored {restored_files} files across all cogs."
            shutil.rmtree(backup_path)
            embed.add_field(name="Backup Removed", value="Backup directory has been removed.")
        await ctx.send(embed=embed)

    async def update_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.readlines()

        updated = False
        new_content = []
        in_class = False
        in_init = False
        has_init = False
        skip_block = False
        in_import_block = False
        has_Star-Utils_import = False
        class_name = None
        file_name = os.path.basename(os.path.dirname(filepath))
        needs_cog_import = False

        for i, line in enumerate(content):
            if line.strip().startswith('import ') or line.strip().startswith('from '):
                in_import_block = True
                if line.strip().startswith('from Star-Utils import'):
                    has_Star-Utils_import = True
                    if 'CogsUtils' not in line:
                        line = line.rstrip()
                        if line.endswith(','):
                            line += ' CogsUtils\n'
                        else:
                            line = line[:-1] + ', CogsUtils\n'
                    updated = True
                elif 'Star-Utils' in line:
                    line = line.replace('Star-Utils', 'Star-Utils')
                    has_Star-Utils_import = True
                    if 'CogsUtils' not in line:
                        line = line.rstrip()
                        if line.endswith(','):
                            line += ' CogsUtils\n'
                        else:
                            line = line[:-1] + ', CogsUtils\n'
                    updated = True
                new_content.append(line)
                continue
            elif in_import_block and not (line.strip().startswith('import ') or line.strip().startswith('from ')):
                in_import_block = False

            if not in_import_block:
                if 'class' in line and ':' in line:
                    in_class = True
                    class_name = line.strip().split()[1].split('(')[0]
                    if '(Cog)' in line:
                        needs_cog_import = True
                    if 'commands.Cog' in line:
                        line = line.replace('commands.Cog', 'Cog')
                        updated = True

                if 'def __init__' in line:
                    in_init = True
                    has_init = True

                if in_init and 'super().__init__()' in line:
                    line = line.replace('super().__init__()', 'super().__init__(bot)')
                    updated = True

                if in_init and 'super().__init__(bot)' in line:
                    new_content.append(line)
                    new_content.append(f'        self.logs = CogsUtils.get_logger("{class_name}")\n')
                    updated = True
                    continue

                if 'Cog.__init__()' in line:
                    line = line.replace('Cog.__init__()', 'Cog.__init__(bot)')
                    updated = True

                if 'Cog.listener' in line:
                    # Remove all 'commands.' prefixes
                    line = re.sub(r'(commands\.)+', '', line)
                    # Add a single 'commands.' prefix if it's not already there
                    if not line.strip().startswith('commands.Cog.listener'):
                        line = line.replace('Cog.listener', 'commands.Cog.listener')
                    updated = True

                if not in_class and re.search(r'\bCog\b', line):
                    line = re.sub(r'\bCog\b', 'commands.Cog', line)
                    updated = True

            if line.strip().startswith('__version__'):
                line = '__version__ = "1.0.0"\n'
                updated = True

            if 'def format_help_for_context' in line:
                skip_block = True
                updated = True
                continue

            if skip_block and not line.startswith((' ', '\t')):
                skip_block = False

            if in_init and not line.strip():
                in_init = False

            if not skip_block:
                new_content.append(line)

        if (needs_cog_import and not has_Star-Utils_import) or not has_Star-Utils_import:
            new_content.insert(0, 'from Star-Utils import Cog, CogsUtils\n')
            updated = True

        if in_class and not has_init:
            init_method = [
                f'    def __init__(self, bot):\n',
                f'        super().__init__(bot)\n',
                f'        self.logs = CogsUtils.get_logger("{class_name}")\n'
            ]
            for i, line in enumerate(new_content):
                if 'class' in line and ':' in line:
                    new_content[i+1:i+1] = init_method
                    updated = True
                    break

        if os.path.basename(filepath) == '__init__.py' and class_name:
            new_content = [
                "from Star-Utils import Cog, CogsUtils\n",
                "from starbot.core import errors\n",
                "import importlib\n",
                "import sys\n",
                "try:\n",
                "    import Star-Utils\n",
                "except ModuleNotFoundError:\n",
                "    raise errors.CogLoadError(\n",
                "        \"The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/LeDeathAmongst/Star-Utils.git`. A restart of the bot isn't necessary.\"\n",
                "    )\n",
                "modules = sorted([module for module in sys.modules if module.split('.')[0] == 'Star-Utils'], reverse=True)\n",
                "for module in modules:\n",
                "    try:\n",
                "        importlib.reload(sys.modules[module])\n",
                "    except ModuleNotFoundError:\n",
                "        pass\n",
                "del Star-Utils\n",
                "from starbot.core.bot import Red\n",
                "from starbot.core.utils import get_end_user_data_statement\n",
                f"from .{file_name} import {class_name}\n",
                "\n",
                "__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)\n",
                "\n",
                "async def setup(bot: Red) -> None:\n",
                f"    cog = {class_name}(bot)\n",
                "    await bot.add_cog(cog)\n"
            ]
            updated = True

        if updated:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.writelines(new_content)

        return updated
