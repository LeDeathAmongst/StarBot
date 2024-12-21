from openai import OpenAI
from starbot.core import commands, Config
import os
import json
import ast
import re
import asyncio
from pathlib import Path
import typing
import discord
from starbot.core.i18n import Translator
from starbot.core.utils.chat_formatting import humanize_list, box, inline
from starbot.core.utils.menus import start_adding_reactions
from starbot.core.utils.predicates import ReactionPredicate, MessagePredicate

from Star-Utils import Cog, CogsUtils
from Star-Utils.menus import Menu, Reactions

_ = Translator("DashIntGen", __file__)

class DashIntGen(Cog):
    """Cog to generate advanced dashboard integration for other cogs using GPT-4."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_global = {"data_path": "", "openai_api_key": ""}
        self.config.register_global(**default_global)
        self.logs = CogsUtils.get_logger("DashIntGen")

    @commands.command()
    @commands.is_owner()
    async def setdatapath(self, ctx, *, path: str):
        """Set the data path for cog integrations."""
        await self.config.data_path.set(path)
        await ctx.send(f"Data path set to: {path}")

    @commands.command()
    @commands.is_owner()
    async def setopenaikey(self, ctx, *, api_key: str):
        """Set the OpenAI API key for GPT-4 integration."""
        await self.config.openai_api_key.set(api_key)
        await ctx.send("OpenAI API key has been set.")

    @commands.command()
    async def dashint(self, ctx, cogname: str):
        """Generate advanced dashboard integration for a specified cog using GPT-4."""
        data_path = await self.config.data_path()
        openai_api_key = await self.config.openai_api_key()

        if not data_path:
            await ctx.send("Data path not configured. Use `[p]setdatapath` first.")
            return

        if not openai_api_key:
            await ctx.send("OpenAI API key not configured. Use `[p]setopenaikey` first.")
            return

        cog_path = Path(data_path) / cogname
        if not cog_path.is_dir():
            await ctx.send(f"Cog directory for `{cogname}` not found.")
            return

        try:
            integration_file_path = cog_path / 'dashboard_integration.py'
            cog_files = self.get_cog_files(cog_path)

            integration_content = await self.create_integration_file(integration_file_path, cogname, cog_files, openai_api_key)

            confirmed = await self.confirm_integration_file(ctx, cogname, integration_content)
            if confirmed:
                with open(integration_file_path, 'w', encoding='utf-8') as f:
                    f.write(integration_content)

                self.modify_cog_files(cog_path, cogname)
                info_file_path = cog_path / 'info.json'
                if info_file_path.exists():
                    self.update_info_json(info_file_path)
                init_file_path = cog_path / '__init__.py'
                self.modify_init_file(init_file_path, cogname)
                await ctx.send(f"Advanced dashboard integration generated for `{cogname}`.")
                await self._reload(ctx, cogname)
            else:
                await ctx.send(f"Dashboard integration generation cancelled for `{cogname}`.")
        except Exception as e:
            self.logs.error(f"Error during dashboard integration generation for {cogname}", exc_info=True)
            await ctx.send(f"An error occurred while generating dashboard integration for `{cogname}`: {str(e)}")

    def get_cog_files(self, cog_path):
        cog_files = {}
        for root, _, files in os.walk(cog_path):
            for file in files:
                if file.endswith('.py') and not file.endswith('.po') and 'locales' not in root:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        cog_files[file] = f.read()
        return cog_files

    async def create_integration_file(self, file_path, cogname, cog_files, openai_api_key):
        client = OpenAI(api_key=openai_api_key)
        main_file_content = cog_files.get(f"{cogname.lower()}.py", "")

        tree = ast.parse(main_file_content)
        cog_class = next((node for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and any(self.is_cog_base(base) for base in node.bases)), None)

        if not cog_class:
            raise ValueError(f"Could not find a Cog class in {cogname.lower()}.py")

        system_prompt = """
        You are an expert Python developer specializing in Red Discord Bot cog development and dashboard integration.
        Your task is to create an advanced, strong, and durable dashboard_integration.py file for Red's web dashboard third-party integration.
        Focus on creating pages for configuration and viewing settings, not executing commands.
        Follow these guidelines:
        1. Use the dashboard_page decorator for main and guild-specific pages.
        2. Implement proper error handling and permission checks.
        3. Use the Form utility for configuration settings.
        4. Return appropriate responses as dictionaries with the required keys.
        5. Integrate with the cog's existing configuration.
        6. Provide clear documentation and comments throughout the code.
        """

        user_prompt = f"""
        Create an advanced dashboard_integration.py file for a Red Discord Bot cog named {cogname}.
        Use the following template structure and expand upon it:

        ```python
        from Star-Utils import CogsUtils  # isort:skip
        from starbot.core import commands  # isort:skip
        from starbot.core.bot import Red  # isort:skip
        from starbot.core.i18n import Translator  # isort:skip
        import discord  # isort:skip
        import typing  # isort:skip

        _ = Translator("{cogname}", __file__)

        def dashboard_page(*args, **kwargs):
            def decorator(func: typing.Callable):
                func.__dashboard_decorator_params__ = (args, kwargs)
                return func
            return decorator

        class DashboardIntegration:
            bot: Red

            @Cog.listener()
            async def on_dashboard_cog_add(self, dashboard_cog: Cog) -> None:
                dashboard_cog.rpc.third_parties_handler.add_third_party(self)

            @dashboard_page(name=None, description="Manage {cogname}")
            async def dashboard_main(self, **kwargs) -> typing.Dict[str, typing.Any]:
                # Implement main dashboard logic here
                return {{
                    "status": 0,
                    "web_content": {{
                        "source": '<h1>{cogname} Dashboard</h1><p>Welcome to the {cogname} dashboard!</p>',
                        "standalone": True
                    }}
                }}

            @dashboard_page(
                name="guild",
                description="Manage {cogname} for a specific guild",
                methods=("GET", "POST"),
            )
            async def dashboard_guild(self, user: discord.User, guild: discord.Guild, **kwargs) -> typing.Dict[str, typing.Any]:
                is_owner = user.id in self.bot.owner_ids
                member = guild.get_member(user.id)
                if not is_owner and not await self.bot.is_mod(member):
                    return {{
                        "status": 0,
                        "error_code": 403,
                        "message": _("You don't have permissions to access this page."),
                    }}

                import wtforms

                class SettingsForm(kwargs["Form"]):
                    def __init__(self) -> None:
                        super().__init__(prefix="{cogname.lower()}_settings_")

                    # Add form fields for {cogname} settings here
                    submit = wtforms.SubmitField(_("Save Changes"))

                form = SettingsForm()

                if form.validate_on_submit():
                    # Save the form data to the config
                    return {{
                        "status": 0,
                        "notifications": [{{"message": _("Settings updated successfully!"), "category": "success"}}],
                        "redirect_url": kwargs["request_url"],
                    }}

                # Load current settings

                return {{
                    "status": 0,
                    "web_content": {{
                        "source": f'''
                        <h2>{cogname} Settings for {{guild.name}}</h2>
                        {{{{ form|safe }}}}
                        ''',
                        "form": form,
                        "standalone": True
                    }},
                }}

        ```

        Expand on this template to create configuration pages for the cog's settings.
        Use the provided configuration attributes to create form fields and implement saving/loading of settings.
        Ensure proper error handling, permission checks, and integration with the cog's configuration.
        Only output the Python code for the dashboard_integration.py file, without any additional explanations.
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,
            max_tokens=2500
        )

        return response.choices[0].message.content

    def is_cog_base(self, base):
        if isinstance(base, ast.Name):
            return base.id == 'Cog'
        elif isinstance(base, ast.Attribute):
            return base.attr == 'Cog'
        return False

    async def confirm_integration_file(self, ctx, cogname, integration_content):
        message = f"Generated dashboard_integration.py for {cogname}:\n"
        chunks = [integration_content[i:i+1900] for i in range(0, len(integration_content), 1900)]
        for chunk in chunks:
            chunk_message = message + f"```python\n{chunk}\n```"
            await ctx.send(chunk_message)
        await ctx.send("Do you want to create this dashboard_integration.py file? (yes/no)")
        pred = MessagePredicate.yes_or_no(ctx)
        try:
            await self.bot.wait_for("message", check=pred, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("No response received. Cancelling operation.")
            return False
        return pred.result

    def modify_cog_files(self, cog_path, cogname):
        main_file = self.find_main_cog_file(cog_path, cogname)
        if main_file:
            self.modify_main_file(cog_path / main_file, cogname)

    def find_main_cog_file(self, cog_path, cogname):
        for file in os.listdir(cog_path):
            if file.endswith('.py') and file != '__init__.py' and file != 'dashboard_integration.py':
                with open(cog_path / file, 'r', encoding='utf-8') as f:
                    content = f.read()
                if f"class {cogname}" in content:
                    return file
        return None

    def modify_main_file(self, file_path, cogname):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if "from Star-Utils import Cog, CogsUtils" not in content:
            import_statement = "from Star-Utils import Cog, CogsUtils\n"
            content = import_statement + content
        content = re.sub(r"from starbot\.core import commands.*?\n", "", content)
        content = re.sub(r"from starbot\.core\.commands import Cog.*?\n", "", content)
        if "from .dashboard_integration import DashboardIntegration" not in content:
            import_statement = "from .dashboard_integration import DashboardIntegration\n"
            content = import_statement + content
        class_pattern = r"class (\w+)\s*\((commands\.)?Cog.*?\):"
        class_match = re.search(class_pattern, content)
        if class_match:
            class_name = class_match.group(1)
            content = re.sub(class_pattern, f"class {class_name}(DashboardIntegration, Cog):", content)
        init_pattern = r"def __init__\s*\(self, bot\):"
        init_match = re.search(init_pattern, content)
        if init_match:
            logger_line = f"\n        self.logs = CogsUtils.get_logger(f'{cogname}')\n"
            content = content[:init_match.end()] + logger_line + content[init_match.end():]
        else:
            class_end = content.find(':', content.find(class_name)) + 1
            init_method = f"\n    def __init__(self, bot):\n        super().__init__(bot)\n        self.logs = CogsUtils.get_logger(f'{cogname}')\n"
            content = content[:class_end] + init_method + content[class_end:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def modify_init_file(self, file_path, cogname):
        main_file_name, class_name = self.find_main_file_and_class(file_path.parent, cogname)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        import_pattern = r'from \.[\w.]+ import [\w]+'
        new_import = f'from .{main_file_name} import {class_name}'
        content = re.sub(import_pattern, new_import, content)
        setup_pattern = r'async def setup\(bot: Red\) -> None:[\s\S]*?bot\.add_cog\([^)]+\)'
        new_setup = f'''async def setup(bot: Red) -> None:
    cog = {class_name}(bot)
    await bot.add_cog(cog)'''
        content = re.sub(setup_pattern, new_setup, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def find_main_file_and_class(self, cog_path, cogname):
        for file in os.listdir(cog_path):
            if file.endswith('.py') and file != '__init__.py' and file != 'dashboard_integration.py':
                with open(cog_path / file, 'r', encoding='utf-8') as f:
                    content = f.read()
                class_match = re.search(r'class\s+(\w+)\s*\((commands\.)?Cog.*?\):', content)
                if class_match:
                    return file[:-3], class_match.group(1)
        return cogname.lower(), cogname

    def update_info_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            info_content = json.load(f)
        info_content['author'] = ["Star"]
        if 'requirements' not in info_content:
            info_content['requirements'] = []
        if "git+https://github.com/LeDeathAmongst/Star-Utils.git" not in info_content['requirements']:
            info_content['requirements'].append("git+https://github.com/LeDeathAmongst/Star-Utils.git")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(info_content, f, indent=4)

    @commands.command()
    @commands.is_owner()
    async def listdashints(self, ctx):
        """List all cogs with dashboard integrations."""
        data_path = await self.config.data_path()
        if not data_path:
            await ctx.send("Data path not configured. Use `[p]setdatapath` first.")
            return
        dashboard_cogs = []
        for item in os.listdir(data_path):
            cog_path = Path(data_path) / item
            if cog_path.is_dir() and (cog_path / 'dashboard_integration.py').exists():
                dashboard_cogs.append(item)
        if dashboard_cogs:
            chunks = [dashboard_cogs[i:i + 20] for i in range(0, len(dashboard_cogs), 20)]
            for i, chunk in enumerate(chunks, 1):
                message = f"Cogs with dashboard integrations (Part {i}/{len(chunks)}):\n{box(humanize_list(chunk))}"
                await ctx.send(message)
        else:
            await ctx.send("No cogs with dashboard integrations found.")

    @commands.command()
    @commands.is_owner()
    async def removedashint(self, ctx, cogname: str):
        """Remove the dashboard integration for a specified cog."""
        data_path = await self.config.data_path()
        if not data_path:
            await ctx.send("Data path not configured. Use `[p]setdatapath` first.")
            return
        cog_path = Path(data_path) / cogname
        integration_file = cog_path / 'dashboard_integration.py'
        if integration_file.exists():
            os.remove(integration_file)
            main_file = self.find_main_cog_file(cog_path, cogname)
            if main_file:
                self.remove_dashboard_integration(cog_path / main_file, cogname)
            info_file_path = cog_path / 'info.json'
            if info_file_path.exists():
                self.remove_Star-Utils_requirement(info_file_path)
            await ctx.send(f"Dashboard integration for `{cogname}` has been removed. Reloading cog...")
            await self._reload(ctx, cogname)
        else:
            await ctx.send(f"No dashboard integration found for `{cogname}`.")

    def remove_dashboard_integration(self, file_path, cogname):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r"from \.dashboard_integration import DashboardIntegration\n?", "", content)
        content = re.sub(
            r"class (\w+)\s*\(DashboardIntegration,\s*(.*?)\):",
            r"class \1(\2):",
            content
        )
        content = re.sub(r"\s*self\.logs = CogsUtils\.get_logger\(f'.*?'\)\n", "", content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def remove_Star-Utils_requirement(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            info_content = json.load(f)
        if 'requirements' in info_content:
            info_content['requirements'] = [req for req in info_content['requirements'] if "Star-Utils" not in req]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(info_content, f, indent=4)

    async def _reload(self, ctx: commands.Context, cogname: str):
        async with ctx.typing():
            unload_result = await self._unload([cogname])
            load_result = await self._load([cogname])
        output = []
        if unloaded := unload_result["unloaded_packages"]:
            formed = _("The following package was unloaded: {pack}.").format(pack=inline(unloaded[0]))
            output.append(formed)
        if failed_unload := unload_result["notloaded_packages"]:
            formed = _("The following package was not loaded: {pack}.").format(pack=inline(failed_unload[0]))
            output.append(formed)
        if loaded := load_result["loaded_packages"]:
            formed = _("Loaded {packs}.").format(packs=inline(loaded[0]))
            output.append(formed)
        if already_loaded := load_result["alreadyloaded_packages"]:
            formed = _("The following package is already loaded: {pack}").format(pack=inline(already_loaded[0]))
            output.append(formed)
        if failed_load := load_result["failed_packages"]:
            formed = _("Failed to load the following package: {pack}.\nCheck your console or logs for details.").format(pack=inline(failed_load[0]))
            output.append(formed)
        if output:
            await Menu(pages=output).start(ctx)
        else:
            await ctx.send(_("No changes were made."))

    async def _load(self, cogs):
        core_cog = self.bot.get_cog("Core")
        if core_cog:
            return await core_cog._load(cogs)
        return {"loaded_packages": [], "failed_packages": cogs, "alreadyloaded_packages": []}

    async def _unload(self, cogs):
        core_cog = self.bot.get_cog("Core")
        if core_cog:
            return await core_cog._unload(cogs)
        return {"unloaded_packages": [], "notloaded_packages": cogs}
