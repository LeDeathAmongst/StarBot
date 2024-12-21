import discord
from starbot.core import commands, Config
from starbot.core.bot import Red
from Star-Utils import Cog, CogsUtils, Settings, Buttons, Menu, Modal, Dropdown
import asyncio
import datetime
import typing
import uuid

class QuestionType:
    TEXT = "text"
    YES_NO = "yes_no"

class ApplicationType:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions  # List of (question, type) tuples

class Application:
    def __init__(self, user_id, app_type, guild_id):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.app_type = app_type
        self.guild_id = guild_id
        self.thread_id = None
        self.message_id = None
        self.answers = {}
        self.status = "In Progress"
        self.created_at = datetime.datetime.utcnow()
        self.last_updated = datetime.datetime.utcnow()

class Applications(Cog):
    """A complex application system for Discord servers."""

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_guild = {
            "application_types": {},
            "log_channel": None,
            "application_channel": None,
            "apply_message": "Select an application type from the dropdown below to start your application.",
            "apply_message_id": None,
            "applications_locked": False
        }
        self.config.register_guild(**default_guild)
        self.applications = {}

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def appset(self, ctx: commands.Context):
        """Configure the application system."""
        pass

    @appset.group(name="edit")
    async def edit_application(self, ctx: commands.Context):
        """Edit an existing application type."""
        pass

    @edit_application.command(name="add")
    async def add_question(self, ctx: commands.Context, app_name: str, index: int):
        """Add a new question to an existing application type at the specified index."""
        async with self.config.guild(ctx.guild).application_types() as app_types:
            if app_name not in app_types:
                await ctx.send(f"Application type '{app_name}' does not exist.")
                return

            questions = app_types[app_name]["questions"]

            if index < 1 or index > len(questions) + 1:
                await ctx.send(f"Invalid index. Please choose a number between 1 and {len(questions) + 1}.")
                return

            question_type = await self.get_question_type(ctx)
            if question_type is None:
                return

            question = await self.get_question(ctx)
            if question is None:
                return

            questions.insert(index - 1, (question, question_type))
            await ctx.send(f"Question added at index {index} in application '{app_name}'.")

    @edit_application.command(name="remove")
    async def remove_question(self, ctx: commands.Context, app_name: str, index: int):
        """Remove a question from an existing application type at the specified index."""
        async with self.config.guild(ctx.guild).application_types() as app_types:
            if app_name not in app_types:
                await ctx.send(f"Application type '{app_name}' does not exist.")
                return

            questions = app_types[app_name]["questions"]

            if index < 1 or index > len(questions):
                await ctx.send(f"Invalid index. Please choose a number between 1 and {len(questions)}.")
                return

            removed_question = questions.pop(index - 1)
            await ctx.send(f"Question removed from index {index} in application '{app_name}':\n{removed_question[0]}")

    @edit_application.command(name="list")
    async def list_questions(self, ctx: commands.Context, app_name: str):
        """List all questions in an existing application type."""
        async with self.config.guild(ctx.guild).application_types() as app_types:
            if app_name not in app_types:
                await ctx.send(f"Application type '{app_name}' does not exist.")
                return

            questions = app_types[app_name]["questions"]

            if not questions:
                await ctx.send(f"Application '{app_name}' has no questions.")
                return

            embed = discord.Embed(title=f"Questions for {app_name}", color=discord.Color.blue())
            for i, (question, q_type) in enumerate(questions, 1):
                embed.add_field(name=f"Q{i} ({q_type})", value=question, inline=False)

            await ctx.send(embed=embed)

    @appset.command(name="remove")
    async def remove_application(self, ctx: commands.Context, app_name: str, permanent: bool = False):
        """
        Remove an application type.

        If 'permanent' is not specified or is False, the application will be stored in memory for easy re-adding.
        If 'permanent' is True, the application will be permanently deleted.
        """
        async with self.config.guild(ctx.guild).application_types() as app_types:
            if app_name not in app_types:
                await ctx.send(f"Application type '{app_name}' does not exist.")
                return

            removed_app = app_types.pop(app_name)

            if permanent:
                await ctx.send(f"Application type '{app_name}' has been permanently removed.")
            else:
                if not hasattr(self, 'removed_apps'):
                    self.removed_apps = {}

                self.removed_apps[ctx.guild.id] = self.removed_apps.get(ctx.guild.id, {})
                self.removed_apps[ctx.guild.id][app_name] = removed_app

                await ctx.send(f"Application type '{app_name}' has been removed and stored in memory for potential re-adding.")

    @appset.command(name="readd")
    async def readd_application(self, ctx: commands.Context, app_name: str):
        """Re-add a previously removed application type."""
        if not hasattr(self, 'removed_apps') or ctx.guild.id not in self.removed_apps or app_name not in self.removed_apps[ctx.guild.id]:
            await ctx.send(f"No removed application type '{app_name}' found in memory.")
            return

        async with self.config.guild(ctx.guild).application_types() as app_types:
            if app_name in app_types:
                await ctx.send(f"An application type named '{app_name}' already exists. Please choose a different name.")
                return

            app_types[app_name] = self.removed_apps[ctx.guild.id].pop(app_name)

            if not self.removed_apps[ctx.guild.id]:
                del self.removed_apps[ctx.guild.id]

            await ctx.send(f"Application type '{app_name}' has been re-added.")

    @appset.command(name="lock")
    async def lock_applications(self, ctx: commands.Context):
        """Lock all applications, preventing new submissions."""
        await self.config.guild(ctx.guild).applications_locked.set(True)
        await ctx.send("Applications are now locked. No new submissions will be accepted.")

    @appset.command(name="unlock")
    async def unlock_applications(self, ctx: commands.Context):
        """Unlock applications, allowing new submissions."""
        await self.config.guild(ctx.guild).applications_locked.set(False)
        await ctx.send("Applications are now unlocked. New submissions will be accepted.")

    async def start_application(self, interaction: discord.Interaction, app_type: str):
        guild = interaction.guild
        user = interaction.user

        # Check if applications are locked
        if await self.config.guild(guild).applications_locked():
            await interaction.response.send_message("Applications are currently closed. Please try again later.", ephemeral=True)
            return

    @appset.command(name="setlogchannel")
    async def set_log_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for application logs."""
        await self.config.guild(ctx.guild).log_channel.set(channel.id)
        await ctx.send(f"Log channel set to {channel.mention}.")

    @appset.command(name="setchannel")
    async def set_application_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel where applications will be sent."""
        await self.config.guild(ctx.guild).application_channel.set(channel.id)
        await ctx.send(f"Application channel set to {channel.mention}.")

    @appset.command(name="setmessage")
    async def set_apply_message(self, ctx: commands.Context, *, message: str):
        """Set the message for the application embed."""
        await self.config.guild(ctx.guild).apply_message.set(message)
        await ctx.send("Application message has been set.")

    @commands.command(name="createapplyembed")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def create_apply_embed(self, ctx: commands.Context):
        """Create an embed with a dropdown for users to start applications."""
        app_types = await self.config.guild(ctx.guild).application_types()
        if not app_types:
            await ctx.send("No applications have been set up yet.")
            return

        custom_message = await self.config.guild(ctx.guild).apply_message()
        embed = discord.Embed(
            title="Start an Application",
            description=custom_message,
            color=discord.Color.blue()
        )

        options = [{"label": name, "value": name} for name in app_types.keys()]
        select_menu = Dropdown(
            placeholder="What are you applying for?",
            options=options,
            min_values=1,
            max_values=1
        )

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: typing.List[str]):
            app_type = values[0]
            await self.start_application(interaction, app_type)

        select_menu.function = handle_selection

        message = await ctx.send(embed=embed, view=select_menu)
        await self.config.guild(ctx.guild).apply_message_id.set(message.id)

    @commands.command(name="apps")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def apps(self, ctx: commands.Context):
        """Manage application types and questions."""
        await self.add_application(ctx)

    async def add_application(self, ctx: commands.Context):
        questions = []
        while True:
            question_type = await self.get_question_type(ctx)
            if question_type is None:
                return
            question = await self.get_question(ctx)
            if question is None:
                return
            questions.append((question, question_type))

            if not await self.add_another_question(ctx):
                break

        app_name = await self.get_application_name(ctx)
        if app_name:
            await self.save_application(ctx, app_name, questions)

    async def get_question_type(self, ctx: commands.Context):
        options = [
            {"label": "Text Question", "value": QuestionType.TEXT},
            {"label": "Yes/No Question", "value": QuestionType.YES_NO}
        ]
        select_menu = Dropdown(
            placeholder="What kind of question?",
            options=options,
            min_values=1,
            max_values=1
        )

        message = await ctx.send("Select the type of question:", view=select_menu)

        try:
            interaction, values, _ = await select_menu.wait_result()
            await message.delete()
            return values[0]
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("Question creation timed out.")
            return None

    async def get_question(self, ctx: commands.Context):
        await ctx.send("What is the question?")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            message = await self.bot.wait_for('message', check=check, timeout=300.0)
            return message.content
        except asyncio.TimeoutError:
            await ctx.send("Question input timed out.")
            return None

    async def add_another_question(self, ctx: commands.Context):
        options = [
            {"label": "Yes", "value": "yes"},
            {"label": "No", "value": "no"}
        ]
        select_menu = Dropdown(
            placeholder="Do you want to add another question?",
            options=options,
            min_values=1,
            max_values=1
        )

        message = await ctx.send("Do you want to add another question?", view=select_menu)

        try:
            interaction, values, _ = await select_menu.wait_result()
            await message.delete()
            return values[0] == "yes"
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("Selection timed out.")
            return False

    async def get_application_name(self, ctx: commands.Context):
        await ctx.send("What is this application for? (This will be the name of the application type)")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            message = await self.bot.wait_for('message', check=check, timeout=300.0)
            return message.content
        except asyncio.TimeoutError:
            await ctx.send("Application name input timed out.")
            return None

    async def save_application(self, ctx: commands.Context, app_name: str, questions: typing.List[typing.Tuple[str, str]]):
        if not app_name:
            await ctx.send("Application creation cancelled due to missing name.")
            return

        async with self.config.guild(ctx.guild).application_types() as app_types:
            if app_name in app_types:
                await ctx.send(f"An application type named '{app_name}' already exists. Please choose a different name.")
                return

            app_types[app_name] = {"questions": questions}

        await ctx.send(f"Application '{app_name}' has been created with {len(questions)} questions.")

    @commands.command()
    @commands.guild_only()
    async def apply(self, ctx: commands.Context):
        """Start a new application."""
        app_types = await self.config.guild(ctx.guild).application_types()
        if not app_types:
            await ctx.send("No application types have been set up yet.")
            return

        options = [{"label": name, "value": name} for name in app_types.keys()]
        select_menu = Dropdown(
            placeholder="What are you applying for?",
            options=options,
            min_values=1,
            max_values=1
        )

        async def handle_selection(view: Dropdown, interaction: discord.Interaction, values: typing.List[str]):
            app_type = values[0]
            await self.start_application(interaction, app_type)

        select_menu.function = handle_selection
        await ctx.send("Please select an application:", view=select_menu)

    async def start_application(self, interaction: discord.Interaction, app_type: str):
        guild = interaction.guild
        user = interaction.user

        app_types = await self.config.guild(guild).application_types()
        if app_type not in app_types:
            await interaction.response.send_message("Invalid application type.", ephemeral=True)
            return

        application = Application(user.id, app_type, guild.id)
        self.applications[application.id] = application

        await interaction.response.send_message("I've sent you a DM to start your application.", ephemeral=True)
        await self.send_application_questions(user, app_types[app_type]["questions"], application)

    async def send_application_questions(self, user: discord.User, questions: typing.List[typing.Tuple[str, str]], application: Application):
        await user.send("Please answer the following questions:")
        for i, (question, q_type) in enumerate(questions, 1):
            await user.send(f"**Question {i}:** {question}")

            if q_type == QuestionType.YES_NO:
                options = [
                    {"label": "Yes", "value": "Yes"},
                    {"label": "No", "value": "No"}
                ]
                view = Dropdown(
                    placeholder="Select your answer",
                    options=options,
                    min_values=1,
                    max_values=1
                )
                message = await user.send("Please select your answer:", view=view)

                try:
                    interaction, values, _ = await view.wait_result()
                    application.answers[i] = values[0]
                    await message.edit(content=f"You answered: {values[0]}", view=None)
                except asyncio.TimeoutError:
                    await user.send("You took too long to answer. The application has been cancelled.")
                    del self.applications[application.id]
                    return
            else:
                def check(m):
                    return m.author == user and isinstance(m.channel, discord.DMChannel)

                try:
                    answer = await self.bot.wait_for('message', check=check, timeout=600)
                    application.answers[i] = answer.content
                except asyncio.TimeoutError:
                    await user.send("You took too long to answer. The application has been cancelled.")
                    del self.applications[application.id]
                    return

        await self.finish_application(user, application)

    async def finish_application(self, user: discord.User, application: Application):
        application.status = "Submitted"
        application.last_updated = datetime.datetime.utcnow()

        guild = self.bot.get_guild(application.guild_id)
        channel_id = await self.config.guild(guild).application_channel()
        channel = guild.get_channel(channel_id)

        if not channel:
            await user.send("There was an error submitting your application. Please contact a server administrator.")
            return

        embed = await self.create_application_embed(application)

        buttons = [
            {"style": discord.ButtonStyle.green, "label": "Approve", "custom_id": "approve"},
            {"style": discord.ButtonStyle.red, "label": "Deny", "custom_id": "deny"},
            {"style": discord.ButtonStyle.blurple, "label": "Approve with Reason", "custom_id": "approve_reason"},
            {"style": discord.ButtonStyle.blurple, "label": "Deny with Reason", "custom_id": "deny_reason"},
            {"style": discord.ButtonStyle.grey, "label": "Ask Extra Questions", "custom_id": "ask_questions"}
        ]

        view = Buttons(
            timeout=None,
            buttons=buttons,
            function=self.handle_review_action,
            infinity=True
        )

        message = await channel.send(embed=embed, view=view)
        application.message_id = message.id
        thread = await message.create_thread(name=f"{user.name}'s {application.app_type} Application")
        application.thread_id = thread.id

        start_message = await thread.send("Application submitted. Please review.")
        await start_message.pin()

        await user.send("Your application has been submitted. You will be notified if there are any updates.")

    async def create_application_embed(self, application: Application, action_user: discord.User = None, reason: str = None) -> discord.Embed:
        user = self.bot.get_user(application.user_id)

        if application.status == "Submitted":
            color = discord.Color.blue()
            title = f"New application from {user.name}"
            description = f"{user.mention} has submitted a new application."
        elif application.status == "Approved":
            color = discord.Color.green()
            title = f"Application Approved: {user.name}"
            if reason:
                description = f"Application was approved by {action_user.mention} for `{reason}`"
            else:
                description = f"Application was approved by {action_user.mention}"
        elif application.status == "Denied":
            color = discord.Color.red()
            title = f"Application Denied: {user.name}"
            if reason:
                description = f"Application was denied by {action_user.mention} for `{reason}`"
            else:
                description = f"Application was denied by {action_user.mention}"
        else:
            color = discord.Color.gold()
            title = f"{user.name} | {application.app_type}"
            description = f"Application status: {application.status}"

        embed = discord.Embed(title=title, description=description, color=color)

        for question, answer in application.answers.items():
            embed.add_field(name=f"Question {question}", value=answer, inline=False)

        embed.set_footer(text=f"Status: {application.status} | Created: {application.created_at.strftime('%Y-%m-%d %H:%M:%S')}\nUpdated: {application.last_updated.strftime('%Y-%m-%d %H:%M:%S')}")
        return embed

    async def handle_review_action(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]
        message = interaction.message

        application = next((app for app in self.applications.values() if app.message_id == message.id), None)

        if not application:
            await interaction.response.send_message("Could not find the associated application.", ephemeral=True)
            return

        if action in ["approve", "deny", "approve_reason", "deny_reason"]:
            for child in view.children:
                child.disabled = True
            await message.edit(view=view)

        if action == "approve":
            await self.approve_application(interaction, application)
        elif action == "deny":
            await self.deny_application(interaction, application)
        elif action == "approve_reason":
            await self.approve_with_reason(interaction, application)
        elif action == "deny_reason":
            await self.deny_with_reason(interaction, application)
        elif action == "ask_questions":
            await self.create_question_channel(interaction, application)

    async def approve_application(self, interaction: discord.Interaction, application: Application):
        application.status = "Approved"
        application.last_updated = datetime.datetime.utcnow()
        await interaction.response.send_message("Application approved!", ephemeral=True)
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been approved!")
        await self.update_application_embed(interaction.message, application, interaction.user)

    async def deny_application(self, interaction: discord.Interaction, application: Application):
        application.status = "Denied"
        application.last_updated = datetime.datetime.utcnow()
        await interaction.response.send_message("Application denied.", ephemeral=True)
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been denied.")
        await self.update_application_embed(interaction.message, application, interaction.user)

    async def approve_with_reason(self, interaction: discord.Interaction, application: Application):
        modal = Modal(title="Approve Application", inputs=[
            {"label": "Reason", "style": discord.TextStyle.paragraph, "custom_id": "reason"}
        ])
        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            await interaction.followup.send("Approval timed out.", ephemeral=True)
            return

        reason = inputs[0].value
        application.status = "Approved"
        application.last_updated = datetime.datetime.utcnow()
        await modal_interaction.response.send_message(f"Application approved with reason.", ephemeral=True)
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been approved. Reason: {reason}")
        await self.update_application_embed(interaction.message, application, interaction.user, reason)

    async def deny_with_reason(self, interaction: discord.Interaction, application: Application):
        modal = Modal(title="Deny Application", inputs=[
            {"label": "Reason", "style": discord.TextStyle.paragraph, "custom_id": "reason"}
        ])
        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            await interaction.followup.send("Denial timed out.", ephemeral=True)
            return

        reason = inputs[0].value
        application.status = "Denied"
        application.last_updated = datetime.datetime.utcnow()
        await modal_interaction.response.send_message(f"Application denied with reason.", ephemeral=True)
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been denied. Reason: {reason}")
        await self.update_application_embed(interaction.message, application, interaction.user, reason)

    async def create_question_channel(self, interaction: discord.Interaction, application: Application):
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name="Application Questions")
        if not category:
            category = await guild.create_category("Application Questions")

        user = self.bot.get_user(application.user_id)
        channel_name = f"{application.app_type}-{user.name}-questions"

        modal = Modal(title="Create Question Channel", inputs=[
            {"label": "Reason (Optional)", "style": discord.TextStyle.short, "custom_id": "reason", "required": False}
        ])
        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            await interaction.followup.send("Channel creation timed out.", ephemeral=True)
            return

        reason = inputs[0].value if inputs[0].value else "No reason provided"

        channel = await category.create_text_channel(channel_name)

        # Set permissions
        staff_roles = [role for role in guild.roles if role.permissions.manage_messages]
        await channel.set_permissions(guild.default_role, read_messages=False)
        for staff_role in staff_roles:
            await channel.set_permissions(staff_role, read_messages=True, send_messages=True)
        await channel.set_permissions(user, read_messages=True, send_messages=True)

        embed = discord.Embed(
            title="A member of staff will be with you shortly.",
            description=f"Ticket created by {interaction.user.mention} with reason: {reason}",
            color=discord.Color.blue()
        )

        close_buttons = [
            {"style": discord.ButtonStyle.red, "label": "Close", "custom_id": "close"},
            {"style": discord.ButtonStyle.red, "label": "Close with Reason", "custom_id": "close_reason"}
        ]

        view = Buttons(
            timeout=None,
            buttons=close_buttons,
            function=self.handle_close_action,
            infinity=True
        )

        await channel.send(f"{user.mention}", embed=embed, view=view)
        await modal_interaction.response.send_message(f"Created question channel: {channel.mention}", ephemeral=True)

        # Update application status
        application.status = "Additional Questions"
        application.last_updated = datetime.datetime.utcnow()
        await self.update_application_embed(interaction.message, application)

    async def handle_close_action(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]

        if action == "close":
            await self.close_question_channel(interaction)
        elif action == "close_reason":
            await self.close_question_channel_with_reason(interaction)

    async def close_question_channel(self, interaction: discord.Interaction):
        await interaction.response.send_message("Closing the channel...", ephemeral=True)
        await asyncio.sleep(5)  # Give some time for users to see the message
        await interaction.channel.delete()

    async def close_question_channel_with_reason(self, interaction: discord.Interaction):
        modal = Modal(title="Close Question Channel", inputs=[
            {"label": "Reason", "style": discord.TextStyle.short, "custom_id": "reason"}
        ])
        await interaction.response.send_modal(modal)

        try:
            modal_interaction, inputs, _ = await modal.wait_result()
        except asyncio.TimeoutError:
            await interaction.followup.send("Channel closure timed out.", ephemeral=True)
            return

        reason = inputs[0].value
        await modal_interaction.response.send_message(f"Closing the channel. Reason: {reason}", ephemeral=True)
        await asyncio.sleep(5)  # Give some time for users to see the message
        await interaction.channel.delete()

    async def update_application_embed(self, message: discord.Message, application: Application, action_user: discord.User = None, reason: str = None):
        embed = await self.create_application_embed(application, action_user, reason)
        await message.edit(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def appstats(self, ctx: commands.Context):
        """View application statistics."""
        guild_apps = [app for app in self.applications.values() if app.guild_id == ctx.guild.id]
        total_apps = len(guild_apps)
        status_counts = {status: len([app for app in guild_apps if app.status == status]) for status in set(app.status for app in guild_apps)}

        embed = discord.Embed(title="Application Statistics", color=discord.Color.blue())
        embed.add_field(name="Total Applications", value=str(total_apps), inline=False)
        for status, count in status_counts.items():
            embed.add_field(name=f"{status} Applications", value=str(count), inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def appsearch(self, ctx: commands.Context, *, search_term: str):
        """Search for applications by user or type."""
        guild_apps = [app for app in self.applications.values() if app.guild_id == ctx.guild.id]
        matching_apps = [
            app for app in guild_apps
            if search_term.lower() in self.bot.get_user(app.user_id).name.lower()
            or search_term.lower() in app.app_type.lower()
        ]

        if not matching_apps:
            await ctx.send("No matching applications found.")
            return

        embeds = []
        for app in matching_apps:
            embeds.append(await self.create_application_embed(app))

        await Menu(pages=embeds).start(ctx)
