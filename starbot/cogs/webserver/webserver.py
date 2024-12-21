import asyncio
import threading
from starbot.core import commands, Config
from starbot.core.utils.chat_formatting import box
from starbot.core.bot import Red
import discord
import aiohttp
import logging
import uvicorn
from typing import Optional
from jinja2 import Environment, FileSystemLoader
import os
from collections import defaultdict
import json
from functools import partial
from Star_Utils import Cog, CogsUtils
from datetime import datetime

# Assuming webserver.py is in the same directory as this cog
from .webserversite import start_webserver, asgi_app, setup_webserver

log = logging.getLogger("red.webserver")

class WebServerCog(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_global = {
            "webserver_port": 8000,
            "public_key": None,
            "application_id": None,
            "log_channel": None,
            "max_log_entries": 100,
            "status_channel": None  # Add this line
        }
        self.config.register_global(**default_global)
        self.webserver_task: Optional[asyncio.Task] = None
        self.logs = CogsUtils.get_logger("Webserver")
        self.shutdown_event = threading.Event()
        self.webserver_thread = None
        self.start_time = None
        self.request_count = 0
        self.last_request_time = None
        self.status_message = None
        self.status_task = None

    def cog_unload(self):
        if self.webserver_task:
            self.webserver_task.cancel()

    async def update_status(self):
        while True:
            status_channel_id = await self.config.status_channel()
            if status_channel_id:
                channel = self.bot.get_channel(status_channel_id)
                if channel:
                    embed = await self.create_status_embed()
                    if self.status_message:
                        try:
                            await self.status_message.edit(embed=embed)
                        except discord.NotFound:
                            self.status_message = await channel.send(embed=embed)
                    else:
                        self.status_message = await channel.send(embed=embed)
            await asyncio.sleep(30)

    async def create_status_embed(self):
        config = await self.config.all()

        if self.webserver_thread and self.webserver_thread.is_alive():
            status = "🟢 Running "
            color = discord.Color.green()
        else:
            status = "🔴 Not running"
            color = discord.Color.red()

        log_channel = self.bot.get_channel(config['log_channel'])
        log_channel_mention = log_channel.mention if log_channel else "Not set"

        embed = discord.Embed(title="Webserver Status", color=color)

        status_info = (
            f"**Status:** {status}\n"
            f"**Port:** {config['webserver_port']}\n"
            f"**Log Channel:** {log_channel_mention}\n"
            f"**Max Log Entries:** {config['max_log_entries']}\n"
            f"**Public Key:** {config['public_key'][:10]}... (truncated)\n"
            f"**Application ID:** {config['application_id']}\n"
        )

        if self.start_time:
            uptime = datetime.utcnow() - self.start_time
            status_info += (
                f"**Uptime:** {str(uptime).split('.')[0]}\n"
                f"**Total Requests:** {self.request_count}\n"
            )
            if self.last_request_time:
                status_info += f"**Last Request:** {self.last_request_time.strftime('%Y-%m-%d %H:%M:%S UTC')}\n"

        embed.description = status_info
        embed.set_footer(text=f"Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")

        return embed

    @commands.group()
    @commands.is_owner()
    async def webserver(self, ctx: commands.Context):
        """Manage the webserver settings."""
        pass

    @webserver.command()
    @commands.is_owner()
    async def updatelog(self, ctx, version: str, *, changes: str):
        """Update the changelog with a new version and its changes."""
        changelog_path = '/data/cogs/CogManager/cogs/webserver/changelog.md'

        with open(changelog_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(f"## {version}\n\n{changes}\n\n{content}")

        await ctx.send(f"Changelog updated for version {version}")

    @webserver.command()
    @commands.is_owner()
    async def genhelp(self, ctx):
        """Generate the help data JSON."""
        # Collect command data
        commands_data = defaultdict(dict)
        for command in self.bot.commands:
            category = command.cog_name or 'Uncategorized'
            commands_data[category][command.name] = command.help or 'No description available.'

        # Save the data as JSON
        json_path = os.path.join(os.path.dirname(__file__), 'static', 'commands_data.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(commands_data, f, ensure_ascii=False, indent=2)

        await ctx.send("Help data has been generated successfully.")

    @webserver.command(name="start")
    async def webserver_start(self, ctx: commands.Context):
        """Start the webserver."""
        await ctx.send("Attempting to start webserver...")

        if self.webserver_thread and self.webserver_thread.is_alive():
            await ctx.send("Webserver is already running.")
            return

        config = await self.config.all()
        self.port = config['webserver_port']
        public_key = config['public_key']
        application_id = config['application_id']

        await ctx.send(f"Debug: port={self.port}, public_key={public_key[:10]}..., application_id={application_id}")

        if not public_key or not application_id:
            await ctx.send("Please set the public key and application ID before starting the webserver.")
            return

        setup_webserver(self.bot, self.port, public_key, application_id)

        self.shutdown_event = asyncio.Event()

        async def run_server():
            config = uvicorn.Config(asgi_app, host="0.0.0.0", port=self.port, log_level="info")
            server = uvicorn.Server(config)

            async def watch_shutdown_signal():
                await self.shutdown_event.wait()
                server.should_exit = True

            await asyncio.gather(
                server.serve(),
                watch_shutdown_signal()
            )

        self.webserver_thread = threading.Thread(target=lambda: asyncio.run(run_server()))
        self.webserver_thread.start()

        await ctx.send(f"Debug: Thread started. Is alive: {self.webserver_thread.is_alive()}")

        self.start_time = datetime.utcnow()
        self.request_count = 0
        self.last_request_time = None
        if not self.status_task:
            self.status_task = self.bot.loop.create_task(self.update_status())
        await ctx.send(f"Webserver started in a separate thread on port {self.port}.")

    @webserver.command(name="stop")
    async def webserver_stop(self, ctx: commands.Context):
        """Stop the webserver."""
        await ctx.send(f"Debug: webserver_thread exists: {hasattr(self, 'webserver_thread')}")
        if hasattr(self, 'webserver_thread'):
            await ctx.send(f"Debug: webserver_thread is not None: {self.webserver_thread is not None}")
            if self.webserver_thread is not None:
                await ctx.send(f"Debug: webserver_thread is alive: {self.webserver_thread.is_alive()}")
            else:
                await ctx.send("Debug: webserver_thread is None")

        if not hasattr(self, 'webserver_thread') or self.webserver_thread is None or not self.webserver_thread.is_alive():
            await ctx.send("Webserver is not running.")
            return

        await ctx.send("Attempting to stop the webserver...")

        if hasattr(self, 'shutdown_event'):
            self.shutdown_event.set()
            await ctx.send("Debug: Shutdown event set.")
        else:
            await ctx.send("Debug: No shutdown_event found.")

        for i in range(100):  # Wait for up to 10 seconds
            if not self.webserver_thread.is_alive():
                break
            await asyncio.sleep(0.1)
            if i % 20 == 0:  # Every 2 seconds
                await ctx.send(f"Debug: Still waiting for thread to stop... ({i/10}s)")

        if self.webserver_thread.is_alive():
            await ctx.send("Failed to stop the webserver gracefully. Attempting to force stop...")
            try:
                self.webserver_thread.join(timeout=1)  # Give it one more second
            except Exception as e:
                await ctx.send(f"Error while joining thread: {str(e)}")

            # Force kill the thread if it's still alive
            if self.webserver_thread.is_alive():
                await ctx.send("Thread still alive. Attempting to terminate...")
                if hasattr(self.webserver_thread, '_stop'):
                    self.webserver_thread._stop()
                else:
                    await ctx.send("Debug: Thread does not have _stop method.")

        await ctx.send(f"Debug: Thread alive after stop attempt: {self.webserver_thread.is_alive()}")

        self.webserver_thread = None
        self.start_time = None
        if hasattr(self, 'status_task') and self.status_task:
            self.status_task.cancel()
            self.status_task = None

        await ctx.send("Debug: Stop command completed.")

    @webserver.command(name="setport")
    async def set_port(self, ctx: commands.Context, port: int):
        """Set the port for the webserver."""
        await self.config.webserver_port.set(port)
        await ctx.send(f"Webserver port set to {port}. Restart the webserver for changes to take effect.")

    @webserver.command(name="setlogchannel")
    async def set_log_channel(self, ctx: commands.Context, channel: discord.TextChannel):
        """Set the channel for webserver logs."""
        await self.config.log_channel.set(channel.id)
        await ctx.send(f"Log channel set to {channel.mention}")

    @webserver.command(name="setmaxlogs")
    async def set_max_logs(self, ctx: commands.Context, max_logs: int):
        """Set the maximum number of log entries to keep."""
        await self.config.max_log_entries.set(max_logs)
        await ctx.send(f"Maximum log entries set to {max_logs}")

    @webserver.command(name="setpublickey")
    async def set_public_key(self, ctx: commands.Context, public_key: str):
        """Set the public key for Discord interaction verification."""
        await self.config.public_key.set(public_key)
        await ctx.send("Public key set. Restart the webserver for changes to take effect.")

    @webserver.command(name="setappid")
    async def set_application_id(self, ctx: commands.Context, app_id: str):
        """Set the application ID for invite links."""
        await self.config.application_id.set(app_id)
        await ctx.send("Application ID set. Restart the webserver for changes to take effect.")

    @webserver.command(name="setstatus")
    async def set_status_channel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        """Set the channel for dynamic status updates."""
        if channel:
            await self.config.status_channel.set(channel.id)
            await ctx.send(f"Status updates will now be sent to {channel.mention}")
            if not self.status_task:
                self.status_task = self.bot.loop.create_task(self.update_status())
        else:
            await self.config.status_channel.set(None)
            await ctx.send("Status updates have been disabled")
            if self.status_task:
                self.status_task.cancel()
                self.status_task = None

    async def log_to_website(self, data: dict):
        """Log data to the website and Discord channel if set."""
        max_logs = await self.config.max_log_entries()
        self.log_entries.append(data)
        if len(self.log_entries) > max_logs:
            self.log_entries = self.log_entries[-max_logs:]

        log_channel_id = await self.config.log_channel()
        if log_channel_id:
            channel = self.bot.get_channel(log_channel_id)
            if channel:
                embed = discord.Embed(title="Webserver Log", color=discord.Color.blue())
                for key, value in data.items():
                    embed.add_field(name=key, value=str(value), inline=False)
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        """Log when the bot joins a new guild."""
        await self.log_to_website({
            "event": "Guild Join",
            "guild_name": guild.name,
            "guild_id": guild.id,
            "member_count": guild.member_count
        })

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        """Log when the bot leaves a guild."""
        await self.log_to_website({
            "event": "Guild Leave",
            "guild_name": guild.name,
            "guild_id": guild.id
        })

async def setup(bot: Red):
    await bot.add_cog(WebServerCog(bot))
