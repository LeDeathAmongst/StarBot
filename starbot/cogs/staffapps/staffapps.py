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

class StaffApps(Cog):
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
            "apply_message_id": None
        }
        self.config.register_guild(**default_guild)
        self.applications = {}

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def appsete(self, ctx: commands.Context):
        """Configure the application system."""
        pass

    @appsete.command(name="setlogcheannel")
    async def set_log_chanenel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for application logs."""
        await self.config.guild(ctx.guild).log_channel.set(channel.id)
        await ctx.send(f"Log channel set to {channel.mention}.")

    @appsete.command(name="setchanenel")
    async def set_applicaetion_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel where applications will be sent."""
        await self.config.guild(ctx.guild).application_channel.set(channel.id)
        await ctx.send(f"Application channel set to {channel.mention}.")

    @appsete.command(name="setmeessage")
    async def set_apply_emessage(self, ctx: commands.Context, *, message: str):
        """Set the message for the application embed."""
        await self.config.guild(ctx.guild).apply_message.set(message)
        await ctx.send("Application message has been set.")

    @commands.command(name="creaeteapplyembed")
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def create_apply_embed(self, ctx: commands.Context):
        """Create an embed with a dropdown for users to start applications."""
        app_types = await self.config.guild(ctx.guild).application_types()
        if not app_types:
            await ctx.send("No application types have been set up yet.")
            return

        custom_message = await self.config.guild(ctx.guild).apply_message()
        embed = discord.Embed(
            title="Start an Application",
            description=custom_message,
            color=discord.Color.blue()
        )

        options = [{"label": name, "value": name} for name in app_types.keys()]
        select_menu = Dropdown(
            placeholder="Choose an application type",
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

    @commands.command(name="aepps")
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

    async def start_application(self, interaction: discord.Interaction, app_type: str):
        guild = interaction.guild
        user = interaction.user

        app_types = await self.config.guild(guild).application_types()
        if app_type not in app_types:
            await interaction.response.send_message("Invalid application type.", ephemeral=True)
            return

        application = Application(user.id, app_type, guild.id)
        self.applications[application.id] = application

        questions = app_types[app_type]["questions"]
        await self.send_application_questions(interaction, questions, application)

    async def send_application_questions(self, interaction: discord.Interaction, questions: typing.List[typing.Tuple[str, str]], application: Application):
        for i, (question, q_type) in enumerate(questions, 1):
            if q_type == QuestionType.YES_NO:
                modal = Modal(title=f"Question {i}", inputs=[
                    {"label": question, "style": discord.TextStyle.short, "custom_id": f"q_{i}", "placeholder": "Yes or No"}
                ])
            else:
                modal = Modal(title=f"Question {i}", inputs=[
                    {"label": question, "style": discord.TextStyle.paragraph, "custom_id": f"q_{i}"}
                ])

            await interaction.response.send_modal(modal)

            try:
                modal_interaction, inputs, _ = await modal.wait_result()
            except asyncio.TimeoutError:
                await interaction.followup.send("Application timed out.", ephemeral=True)
                del self.applications[application.id]
                return

            application.answers[i] = inputs[0].value

            if i < len(questions):
                interaction = modal_interaction

        await self.finish_application(interaction, application)

    async def finish_application(self, interaction: discord.Interaction, application: Application):
        application.status = "Pending Review"
        application.last_updated = datetime.datetime.utcnow()

        guild = self.bot.get_guild(application.guild_id)
        channel_id = await self.config.guild(guild).application_channel()
        channel = guild.get_channel(channel_id)

        if not channel:
            await interaction.followup.send("There was an error submitting your application. Please contact a server administrator.", ephemeral=True)
            return

        embed = await self.create_application_embed(application)

        buttons = [
            {"style": discord.ButtonStyle.green, "label": "Approve", "custom_id": "approve"},
            {"style": discord.ButtonStyle.red, "label": "Deny", "custom_id": "deny"},
            {"style": discord.ButtonStyle.grey, "label": "Ask Extra Questions", "custom_id": "ask_questions"}
        ]

        view = Buttons(
            timeout=None,
            buttons=buttons,
            function=self.handle_review_action
        )

        status_message = f"Status: {application.status}"
        message = await channel.send(content=status_message, embed=embed, view=view)
        application.message_id = message.id
        thread = await message.create_thread(name=f"{interaction.user.name}'s {application.app_type} Application")
        application.thread_id = thread.id

        start_message = await thread.send("Application submitted. Please review.")
        await start_message.pin()

        await interaction.followup.send("Your application has been submitted. You will be notified if there are any updates.", ephemeral=True)
        await self.log_application_event(guild, "Application Submitted", application)

    async def create_application_embed(self, application: Application) -> discord.Embed:
        user = self.bot.get_user(application.user_id)

        if application.status == "Submitted" or application.status == "Pending Review":
            color = discord.Color.blue()
        elif application.status == "Approved":
            color = discord.Color.green()
        elif application.status == "Denied":
            color = discord.Color.red()
        else:
            color = discord.Color.default()

        embed = discord.Embed(title=f"{user.name} | {application.app_type}", color=color)

        for question, answer in application.answers.items():
            embed.add_field(name=f"Question {question}", value=answer, inline=False)

        embed.set_footer(text=f"Created: {application.created_at.strftime('%Y-%m-%d %H:%M:%S')} | Updated: {application.last_updated.strftime('%Y-%m-%d %H:%M:%S')}")
        return embed

    async def handle_review_action(self, view: Buttons, interaction: discord.Interaction):
        action = interaction.data["custom_id"]
        message = interaction.message

        application = next((app for app in self.applications.values() if app.message_id == message.id), None)

        if not application:
            await interaction.response.send_message("Could not find the associated application.", ephemeral=True)
            return

        if action == "approve":
            await self.approve_application(interaction, application)
        elif action == "deny":
            await self.deny_application(interaction, application)
        elif action == "ask_questions":
            await self.create_question_channel(interaction, application)

    async def update_application_status(self, message: discord.Message, application: Application, new_status: str, reviewer: discord.Member):
        application.status = new_status
        application.last_updated = datetime.datetime.utcnow()
        status_message = f"Status: {application.status} | {new_status} by {reviewer.name}"
        await message.edit(content=status_message)
        embed = await self.create_application_embed(application)
        await message.edit(embed=embed)

    async def approve_application(self, interaction: discord.Interaction, application: Application):
        await self.update_application_status(interaction.message, application, "Approved", interaction.user)
        await interaction.response.send_message("Application approved!", ephemeral=True)
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been approved!")
        await self.log_application_event(interaction.guild, "Application Approved", application)

    async def deny_application(self, interaction: discord.Interaction, application: Application):
        await self.update_application_status(interaction.message, application, "Denied", interaction.user)
        await interaction.response.send_message("Application denied.", ephemeral=True)
        user = self.bot.get_user(application.user_id)
        if user:
            await user.send(f"Your {application.app_type} application has been denied.")
        await self.log_application_event(interaction.guild, "Application Denied", application)

    async def create_question_channel(self, interaction: discord.Interaction, application: Application):
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name="Application Questions")
        if not category:
            category = await guild.create_category("Application Questions")

        user = self.bot.get_user(application.user_id)
        channel_name = f"{application.app_type}-{user.name}-questions"
        channel = await category.create_text_channel(channel_name)

        # Set permissions
        staff_roles = [role for role in guild.roles if role.permissions.manage_messages]
        await channel.set_permissions(guild.default_role, read_messages=False)
        for staff_role in staff_roles:
            await channel.set_permissions(staff_role, read_messages=True, send_messages=True)
        await channel.set_permissions(user, read_messages=True, send_messages=True)

        await channel.send(f"{user.mention}, staff members have some additional questions about your {application.app_type} application.")
        await self.update_application_status(interaction.message, application, "Additional Questions", interaction.user)
        await interaction.response.send_message(f"Created question channel: {channel.mention}", ephemeral=True)

        await self.log_application_event(guild, "Additional Questions Requested", application)

    async def log_application_event(self, guild: discord.Guild, event: str, application: Application):
        log_channel_id = await self.config.guild(guild).log_channel()
        if not log_channel_id:
            return

        log_channel = guild.get_channel(log_channel_id)
        if not log_channel:
            return

        user = self.bot.get_user(application.user_id)
        embed = discord.Embed(title=f"Application Event: {event}", color=discord.Color.gold())
        embed.add_field(name="User", value=f"{user.name}#{user.discriminator}", inline=False)
        embed.add_field(name="Application Type", value=application.app_type, inline=False)
        embed.add_field(name="Status", value=application.status, inline=False)
        embed.add_field(name="Event Time", value=datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), inline=False)

        await log_channel.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def appstatse(self, ctx: commands.Context):
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
    async def appsearceh(self, ctx: commands.Context, *, search_term: str):
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
