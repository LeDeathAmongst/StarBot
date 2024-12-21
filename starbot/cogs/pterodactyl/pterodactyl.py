from Star-Utils import Cog, CogsUtils
import asyncio
import json
from typing import Mapping, Optional, Tuple, Union

import discord
import websockets
from discord.ext import tasks
from pydactyl import PterodactylClient
from starbot.core import app_commands, commands
from starbot.core.app_commands import Choice
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import bold, box, error, humanize_list
from starbot.core.utils.views import ConfirmView

from pterodactyl import mcsrvstatus
from pterodactyl.config import config, register_config
from pterodactyl.logger import logger


class Pterodactyl(Cog):
    """Pterodactyl allows you to manage your Pterodactyl Panel from Discord."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.client: Optional[PterodactylClient] = None
        self.task: Optional[asyncio.Task] = None
        self.websocket: Optional[websockets.WebSocketClientProtocol] = None
        self.retry_counter: int = 0
        register_config(config)
        self.task = self.get_task()
        self.update_topic.start()


    async def cog_load(self) -> None:
        pterodactyl_keys = await self.bot.get_shared_api_tokens("pterodactyl")
        api_key = pterodactyl_keys.get("api_key")
        if api_key is None:
            self.task.cancel()
            raise ValueError("Pterodactyl API key not set. Please set it using `[p]set api`.")
        base_url = await config.base_url()
        if base_url is None:
            self.task.cancel()
            raise ValueError("Pterodactyl base URL not set. Please set it using `[p]pterodactyl config url`.")
        server_id = await config.server_id()
        if server_id is None:
            self.task.cancel()
            raise ValueError("Pterodactyl server ID not set. Please set it using `[p]pterodactyl config serverid`.")

        self.client = PterodactylClient(base_url, api_key).client

    async def cog_unload(self) -> None:
        self.update_topic.cancel()
        self.task.cancel()
        self.retry_counter = 0
        await self.client._session.close() # pylint: disable=protected-access

    def get_task(self) -> asyncio.Task:
        from pterodactyl.websocket import establish_websocket_connection
        task = self.bot.loop.create_task(establish_websocket_connection(self), name="Pterodactyl Websocket Connection")
        task.add_done_callback(self.error_callback)
        return task

    def error_callback(self, fut) -> None: #NOTE - Thanks flame442 and zephyrkul for helping me figure this out
        try:
            fut.result()
        except asyncio.CancelledError:
            logger.info("WebSocket task has been cancelled.")
        except Exception as e: # pylint: disable=broad-exception-caught
            logger.error("WebSocket task has failed: %s", e, exc_info=e)
            self.task.cancel()
            if self.retry_counter < 5:
                self.retry_counter += 1
                logger.info("Retrying in %s seconds...", 5 * self.retry_counter)
                self.task = self.bot.loop.call_later(5 * self.retry_counter, self.get_task)
            else:
                logger.info("Retry limit reached. Stopping task.")

    @tasks.loop(minutes=6)
    async def update_topic(self):
        await self.bot.wait_until_red_ready()
        topic = await self.get_topic()
        console = self.bot.get_channel(await config.console_channel())
        chat = self.bot.get_channel(await config.chat_channel())
        if console:
            await console.edit(topic=topic)
        if chat:
            await chat.edit(topic=topic)

    @commands.Cog.listener()
    async def on_message_without_command(self, message: discord.Message) -> None:
        if message.channel.id == await config.console_channel() and message.author.bot is False:
            if await config.console_commands_enabled() is False:
                await message.channel.send("Console commands are disabled.")
                logger.debug("Received console command from %s, but console commands are disabled: %s", message.author.id, message.content)
                return
            logger.debug("Received console command from %s: %s", message.author.id, message.content)
            await message.channel.send(f"Received console command from {message.author.id}: {message.content[:1900]}", allowed_mentions=discord.AllowedMentions.none())
            try:
                await self.websocket.send(json.dumps({"event": "send command", "args": [message.content]}))
            except websockets.exceptions.ConnectionClosed as e:
                logger.error("WebSocket connection closed: %s", e)
                self.task.cancel()
                self.retry_counter = 0
                self.task = self.get_task()
        if message.channel.id == await config.chat_channel() and message.author.bot is False:
            logger.debug("Received chat message from %s: %s", message.author.id, message.content)
            channel = self.bot.get_channel(await config.console_channel())
            if channel:
                await channel.send(f"Received chat message from {message.author.id}: {message.content[:1900]}", allowed_mentions=discord.AllowedMentions.none())
            msg = json.dumps({"event": "send command", "args": [await self.get_chat_command(message)]})
            logger.debug("Sending chat message to server:\n%s", msg)
            try:
                await self.websocket.send(msg)
            except websockets.exceptions.ConnectionClosed as e:
                logger.error("WebSocket connection closed: %s", e)
                self.task.cancel()
                self.retry_counter = 0
                self.task = self.get_task()

    async def get_topic(self) -> str:
        topic: str = await config.topic()
        placeholders = {
            "H": await config.topic_hostname() or "unset",
            "O": str(await config.topic_port()),
        }
        if await config.api_endpoint() == "minecraft":
            status, response = await mcsrvstatus.get_status(await config.topic_hostname(), await config.topic_port())
            if status:
                placeholders.update({
                    "I": response['ip'],
                    "M": str(response['players']['max']),
                    "P": str(response['players']['online']),
                    "V": response['version'],
                    "D": response['motd']['clean'][0] if response['motd']['clean'] else "unset",
                })
            else:
                placeholders.update({
                    "I": response['ip'],
                    "M": "0",
                    "P": "0",
                    "V": "Server Offline",
                    "D": "Server Offline",
                })
        for key, value in placeholders.items():
            topic = topic.replace('.$' + key, value)
        return topic

    async def get_chat_command(self, message: discord.Message) -> str:
        command: str = await config.chat_command()
        placeholders = {
            "C": str(message.author.color),
            "D": message.author.discriminator,
            "I": str(message.author.id),
            "M": message.content.replace('"','').replace("\n", " "),
            "N": message.author.display_name,
            "U": message.author.name,
            "V": await config.invite() or "use [p]pterodactyl config invite to change me",
        }
        for key, value in placeholders.items():
            command = command.replace('.$' + key, value)
        return command

    async def get_player_list(self) -> Optional[Tuple[str, list]]:
        if await config.api_endpoint() == "minecraft":
            status, response = await mcsrvstatus.get_status(await config.topic_hostname(), await config.topic_port())
            if status and 'list' in response['players']:
                output_str = '\n'.join(response['players']['list'])
                return output_str, response['players']['list']
            return None

    async def get_player_list_embed(self, ctx: Union[commands.Context, discord.Interaction]) -> Optional[discord.Embed]:
        player_list = await self.get_player_list()
        if player_list:
            embed = discord.Embed(color=await self.bot.get_embed_color(ctx.channel), title="Players Online")
            embed.description = player_list[0]
            return embed
        return None

    async def power(self, ctx: Union[discord.Interaction, commands.Context], action: str, action_ing: str, warning: str = '') -> None:
        if isinstance(ctx, discord.Interaction):
            ctx = await self.bot.get_context(ctx)

        current_status = await config.current_status()

        if current_status == action_ing:
            return await ctx.send(f"Server is already {action_ing}.", ephemeral=True)

        if current_status in ["starting", "stopping"] and action != "kill":
            return await ctx.send("Another power action is already in progress.", ephemeral=True)

        view = ConfirmView(ctx.author, disable_buttons=True)

        message = await ctx.send(f"{warning}Are you sure you want to {action} the server?", view=view)

        await view.wait()

        if view.result is True:
            await message.edit(content=f"Sending websocket command to {action} server...", view=None)

            await self.websocket.send(json.dumps({"event": "set state", "args": [action]}))

            await message.edit(content=f"Server {action_ing}", view=None)

        else:
            await message.edit(content="Cancelled.", view=None)

    async def send_command(self, ctx: Union[discord.Interaction, commands.Context], command: str):
        channel = self.bot.get_channel(await config.console_channel())
        if isinstance(ctx, discord.Interaction):
            ctx = await self.bot.get_context(ctx)
        if channel:
            await channel.send(f"Received console command from {ctx.author.id}: {command[:1900]}", allowed_mentions=discord.AllowedMentions.none())
        try:
            await self.websocket.send(json.dumps({"event": "send command", "args": [command]}))
            await ctx.send(f"Command sent to server. {box(command, 'json')}")
        except websockets.exceptions.ConnectionClosed as e:
            logger.error("WebSocket connection closed: %s", e)
            await ctx.send(error("WebSocket connection closed."))
            self.task.cancel()
            self.retry_counter = 0
            self.task = self.get_task()

    @commands.Cog.listener()
    async def on_red_api_tokens_update(self, service_name: str, api_tokens: Mapping[str,str]): # pylint: disable=unused-argument
        if service_name == "pterodactyl":
            logger.info("Configuration value set: api_key\nRestarting task...")
            self.task.cancel()
            self.retry_counter = 0
            self.task = self.get_task()

    slash_pterodactyl = app_commands.Group(name="pterodactyl", description="Pterodactyl allows you to manage your Pterodactyl Panel from Discord.")

    @slash_pterodactyl.command(name = "command", description = "Send a command to the server console.")
    async def slash_pterodactyl_command(self, interaction: discord.Interaction, command: str) -> None:
        """Send a command to the server console.

        Parameters:
        -----------
        command: str
            The command to send to the server."""
        return await self.send_command(interaction, command)

    @slash_pterodactyl.command(name = "players", description = "Retrieve a list of players on the server.")
    async def slash_pterodactyl_players(self, interaction: discord.Interaction) -> None:
        """Retrieve a list of players on the server."""
        e = await self.get_player_list_embed(interaction)
        if e:
            await interaction.response.send_message(embed=e, ephemeral=True)
        else:
            await interaction.response.send_message("No players online.", ephemeral=True)

    @slash_pterodactyl.command(name = "power", description = "Send power actions to the server.")
    @app_commands.choices(action=[
        Choice(name="Start", value="start"),
        Choice(name="Stop", value="stop"),
        Choice(name="Restart", value="restart"),
        Choice(name="⚠️ Kill ⚠️", value="kill")
    ])
    async def slash_pterodactyl_power(self, interaction: discord.Interaction, action: app_commands.Choice[str]) -> None:
        """Send power actions to the server.

        Parameters:
        -----------
        action: app_commands.Choice[str]
            The action to perform on the server."""
        if action.value == "kill":
            return await self.power(interaction, action.value, "stopping... (forcefully killed)", warning="**⚠️ Forcefully killing the server process can corrupt data in some cases. ⚠️**\n")
        if action.value == "stop":
            return await self.power(interaction, action.value, "stopping...")
        return await self.power(interaction, action.value, f"{action.value}ing...")

    @commands.group(autohelp = True, name = "pterodactyl", aliases = ["ptero"])
    async def pterodactyl(self, ctx: commands.Context) -> None:
        """Pterodactyl allows you to manage your Pterodactyl Panel from Discord."""

    @pterodactyl.command(name = "players", aliases=["list", "online", "playerlist", "who"])
    async def pterodactyl_players(self, ctx: commands.Context) -> None:
        """Retrieve a list of players on the server."""
        e = await self.get_player_list_embed(ctx)
        if e:
            await ctx.send(embed=e)
        else:
            await ctx.send("No players online.")

    @pterodactyl.command(name = "command", aliases = ["cmd", "execute", "exec"])
    @commands.admin()
    async def pterodactyl_command(self, ctx: commands.Context, *, command: str) -> None:
        """Send a command to the server console."""
        return await self.send_command(ctx, command)

    @pterodactyl.group(autohelp = True, name = "power")
    @commands.admin()
    async def pterodactyl_power(self, ctx: commands.Context) -> None:
        """Send power actions to the server."""

    @pterodactyl_power.command(name = "start")
    async def pterodactyl_power_start(self, ctx: commands.Context) -> Optional[discord.Message]:
        """Start the server."""
        return await self.power(ctx, "start", "starting...")

    @pterodactyl_power.command(name = "stop")
    async def pterodactyl_power_stop(self, ctx: commands.Context) -> Optional[discord.Message]:
        """Stop the server."""
        return await self.power(ctx, "stop", "stopping...")

    @pterodactyl_power.command(name = "restart")
    async def pterodactyl_power_restart(self, ctx: commands.Context) -> Optional[discord.Message]:
        """Restart the server."""
        return await self.power(ctx, "restart", "restarting...")

    @pterodactyl_power.command(name = "kill")
    async def pterodactyl_power_kill(self, ctx: commands.Context) -> Optional[discord.Message]:
        """Kill the server."""
        return await self.power(ctx, "kill", "stopping... (forcefully killed)", warning="**⚠️ Forcefully killing the server process can corrupt data in some cases. ⚠️**\n")

    @pterodactyl.group(autohelp = True, name = "config", aliases = ["settings", "set"])
    @commands.is_owner()
    async def pterodactyl_config(self, ctx: commands.Context) -> None:
        """Configure Pterodactyl settings."""

    @pterodactyl_config.command(name = "url")
    async def pterodactyl_config_base_url(self, ctx: commands.Context, *, base_url: str) -> None:
        """Set the base URL of your Pterodactyl Panel.

        Please include the protocol (http/https).
        Example: `https://panel.example.com`"""
        await config.base_url.set(base_url)
        await ctx.send(f"Base URL set to {base_url}")
        logger.info("Configuration value set: base_url = %s\nRestarting task...", base_url)
        self.task.cancel()
        self.retry_counter = 0
        self.task = self.get_task()

    @pterodactyl_config.command(name = "serverid")
    async def pterodactyl_config_server_id(self, ctx: commands.Context, *, server_id: str) -> None:
        """Set the ID of your server."""
        await config.server_id.set(server_id)
        await ctx.send(f"Server ID set to {server_id}")
        logger.info("Configuration value set: server_id = %s\nRestarting task...", server_id)
        self.task.cancel()
        self.retry_counter = 0
        self.task = self.get_task()

    @pterodactyl_config.group(name = "console")
    async def pterodactyl_config_console(self, ctx: commands.Context):
        """Configure console settings."""

    @pterodactyl_config_console.command(name = "channel")
    async def pterodactyl_config_console_channel(self, ctx: commands.Context, channel: discord.TextChannel) -> None:
        """Set the channel to send console output to."""
        await config.console_channel.set(channel.id)
        await ctx.send(f"Console channel set to {channel.mention}")

    @pterodactyl_config_console.command(name = "commands")
    async def pterodactyl_config_console_commands(self, ctx: commands.Context, enabled: bool) -> None:
        """Enable or disable console commands."""
        await config.console_commands_enabled.set(enabled)
        await ctx.send(f"Console commands set to {enabled}")

    @pterodactyl_config.command(name = "invite")
    async def pterodactyl_config_invite(self, ctx: commands.Context, invite: str) -> None:
        """Set the invite link for your server."""
        await config.invite.set(invite)
        await ctx.send(f"Invite link set to {invite}")

    @pterodactyl_config.group(name = "topic")
    async def pterodactyl_config_topic(self, ctx: commands.Context):
        """Set the topic for the console and chat channels."""

    @pterodactyl_config_topic.command(name = "host", aliases = ["hostname", "ip"])
    async def pterodactyl_config_topic_host(self, ctx: commands.Context, host: str) -> None:
        """Set the hostname or IP address of your server."""
        await config.topic_hostname.set(host)
        await ctx.send(f"Hostname/IP set to `{host}`")

    @pterodactyl_config_topic.command(name = "port")
    async def pterodactyl_config_topic_port(self, ctx: commands.Context, port: int) -> None:
        """Set the port of your server."""
        await config.topic_port.set(port)
        await ctx.send(f"Port set to `{port}`")

    @pterodactyl_config_topic.command(name = "text")
    async def pterodactyl_config_topic_text(self, ctx: commands.Context, *, text: str) -> None:
        """Set the text for the console and chat channels.

        Available placeholders:
        - `.$H` (hostname)
        - `.$O` (port)
        Available for Minecraft servers:
        - `.$I` (ip)
        - `.$M` (max players)
        - `.$P` (players online)
        - `.$V` (version)
        - `.$D` (description / Message of the Day)"""
        await config.topic.set(text)
        await ctx.send(f"Topic set to:\n{box(text, 'yaml')}")

    @pterodactyl_config.group(name = "chat")
    async def pterodactyl_config_chat(self, ctx: commands.Context):
        """Configure chat settings."""

    @pterodactyl_config_chat.command(name = "channel")
    async def pterodactyl_config_chat_channel(self, ctx: commands.Context, channel: discord.TextChannel) -> None:
        """Set the channel to send chat output to."""
        await config.chat_channel.set(channel.id)
        await ctx.send(f"Chat channel set to {channel.mention}")

    @pterodactyl_config_chat.command(name = "command")
    async def pterodactyl_config_chat_command(self, ctx: commands.Context, *, command: str) -> None:
        """Set the command that will be used to send messages from Discord.

        Required placeholders: `.$U` (username), `.$M` (message), `.$C` (color)
        See [documentation](https://seacogs.coastalcommits.com/pterodactyl/setup/#changing-the-tellraw-command) for more information."""
        await config.chat_command.set(command)
        await ctx.send(f"Chat command set to:\n{box(command, 'json')}")

    @pterodactyl_config.group(name = "regex")
    async def pterodactyl_config_regex(self, ctx: commands.Context) -> None:
        """Set regex patterns."""

    @pterodactyl_config_regex.command(name = "chat")
    async def pterodactyl_config_regex_chat(self, ctx: commands.Context, *, regex: str) -> None:
        """Set the regex pattern to match chat messages on the server.

        See [documentation](https://seacogs.coastalcommits.com/pterodactyl/setup/#my-chat-messages-arent-detected) for more information."""
        await config.chat_regex.set(regex)
        await ctx.send(f"Chat regex set to:\n{box(regex, 'regex')}")

    @pterodactyl_config_regex.command(name = "server")
    async def pterodactyl_config_regex_server(self, ctx: commands.Context, *, regex: str) -> None:
        """Set the regex pattern to match server messages on the server.

        See [documentation](https://seacogs.coastalcommits.com/pterodactyl/setup/#my-chat-messages-arent-detected) for more information."""
        await config.server_regex.set(regex)
        await ctx.send(f"Server regex set to:\n{box(regex, 'regex')}")

    @pterodactyl_config_regex.command(name = "join")
    async def pterodactyl_config_regex_join(self, ctx: commands.Context, *, regex: str) -> None:
        """Set the regex pattern to match join messages on the server.

        See [documentation](https://seacogs.coastalcommits.com/pterodactyl/setup/#my-chat-messages-arent-detected) for more information."""
        await config.join_regex.set(regex)
        await ctx.send(f"Join regex set to:\n{box(regex, 'regex')}")

    @pterodactyl_config_regex.command(name = "leave")
    async def pterodactyl_config_regex_leave(self, ctx: commands.Context, *, regex: str) -> None:
        """Set the regex pattern to match leave messages on the server.

        See [documentation](https://seacogs.coastalcommits.com/pterodactyl/setup/#my-chat-messages-arent-detected) for more information."""
        await config.leave_regex.set(regex)
        await ctx.send(f"Leave regex set to:\n{box(regex, 'regex')}")

    @pterodactyl_config_regex.command(name = "achievement")
    async def pterodactyl_config_regex_achievement(self, ctx: commands.Context, *, regex: str) -> None:
        """Set the regex pattern to match achievement messages on the server.

        See [documentation](https://seacogs.coastalcommits.com/pterodactyl/setup/#my-chat-messages-arent-detected) for more information."""
        await config.achievement_regex.set(regex)
        await ctx.send(f"Achievement regex set to:\n{box(regex, 'regex')}")

    @pterodactyl_config.group(name = "messages", aliases = ['msg', 'msgs', 'message'])
    async def pterodactyl_config_messages(self, ctx: commands.Context):
        """Configure message settings."""

    @pterodactyl_config_messages.command(name = "startup")
    async def pterodactyl_config_messages_startup(self, ctx: commands.Context, *, message: str) -> None:
        """Set the message that will be sent when the server starts."""
        await config.startup_msg.set(message)
        await ctx.send(f"Startup message set to: {message}")

    @pterodactyl_config_messages.command(name = "shutdown")
    async def pterodactyl_config_messages_shutdown(self, ctx: commands.Context, *, message: str) -> None:
        """Set the message that will be sent when the server stops."""
        await config.shutdown_msg.set(message)
        await ctx.send(f"Shutdown message set to: {message}")

    @pterodactyl_config_messages.command(name = "join")
    async def pterodactyl_config_messages_join(self, ctx: commands.Context, *, message: str) -> None:
        """Set the message that will be sent when a user joins the server. This is only shown in embeds."""
        await config.join_msg.set(message)
        await ctx.send(f"Join message set to: {message}")

    @pterodactyl_config_messages.command(name = "leave")
    async def pterodactyl_config_messages_leave(self, ctx: commands.Context, *, message: str) -> None:
        """Set the message that will be sent when a user leaves the server. This is only shown in embeds."""
        await config.leave_msg.set(message)
        await ctx.send(f"Leave message set to: {message}")

    @pterodactyl_config.command(name = "ip")
    async def pterodactyl_config_mask_ip(self, ctx: commands.Context, mask: bool) -> None:
        """Mask the IP addresses of users in console messages."""
        await config.mask_ip.set(mask)
        await ctx.send(f"IP masking set to {mask}")

    @pterodactyl_config.command(name = "api")
    async def pterodactyl_config_api(self, ctx: commands.Context, endpoint: str) -> None:
        """Set the API endpoint for retrieving user avatars.

        This is only used for retrieving user avatars for webhook messages.
        See [PlayerDB](https://playerdb.co/) for valid endpoints. Usually, you should leave this as default."""
        await config.api_endpoint.set(endpoint)
        await ctx.send(f"API endpoint set to {endpoint}")

    @pterodactyl_config_regex.group(name = "blacklist", aliases = ['block', 'blocklist'],)
    async def pterodactyl_config_regex_blacklist(self, ctx: commands.Context):
        """Blacklist regex patterns."""

    @pterodactyl_config_regex_blacklist.command(name = "add")
    async def pterodactyl_config_regex_blacklist_add(self, ctx: commands.Context, name: str, *, regex: str) -> None:
        """Add a regex pattern to the blacklist."""
        async with config.regex_blacklist() as blacklist:
            blacklist: dict
            if name not in blacklist:
                blacklist.update({name: regex})
                await ctx.send(f"Added `{name}` to the regex blacklist.\n{box(regex, 're')}")
            else:
                view = ConfirmView(ctx.author, disable_buttons=True)
                msg = await ctx.send(f"Name `{name}` already exists in the blacklist. Would you like to update it? Current value:\n{box(blacklist[name], 're')}", view=view)
                await view.wait()
                if view.result is True:
                    blacklist.update({name: regex})
                    await msg.edit(content=f"Updated `{name}` in the regex blacklist.\n{box(regex, 're')}")
                else:
                    await msg.edit(content="Cancelled.")

    @pterodactyl_config_regex_blacklist.command(name = "remove")
    async def pterodactyl_config_regex_blacklist_remove(self, ctx: commands.Context, name: str) -> None:
        """Remove a regex pattern from the blacklist."""
        async with config.regex_blacklist() as blacklist:
            blacklist: dict
            if name in blacklist:
                view = ConfirmView(ctx.author, disable_buttons=True)
                msg = await ctx.send(f"Are you sure you want to remove `{name}` from the regex blacklist?\n{box(blacklist[name], 're')}", view=view)
                await view.wait()
                if view.result is True:
                    del blacklist[name]
                    await msg.edit(content=f"Removed `{name}` from the regex blacklist.")
                else:
                    await msg.edit(content="Cancelled.")
            else:
                await ctx.send(f"Name `{name}` does not exist in the blacklist.")

    @pterodactyl_config.command(name = 'view', aliases = ['show'])
    async def pterodactyl_config_view(self, ctx: commands.Context) -> None:
        """View the current configuration."""
        base_url = await config.base_url()
        server_id = await config.server_id()
        console_channel = await config.console_channel()
        console_commands_enabled = await config.console_commands_enabled()
        chat_channel = await config.chat_channel()
        chat_command = await config.chat_command()
        chat_regex = await config.chat_regex()
        server_regex = await config.server_regex()
        join_regex = await config.join_regex()
        leave_regex = await config.leave_regex()
        achievement_regex = await config.achievement_regex()
        startup_msg = await config.startup_msg()
        shutdown_msg = await config.shutdown_msg()
        join_msg = await config.join_msg()
        leave_msg = await config.leave_msg()
        mask_ip = await config.mask_ip()
        api_endpoint = await config.api_endpoint()
        invite = await config.invite()
        regex_blacklist: dict = await config.regex_blacklist()
        topic_text = await config.topic()
        topic_hostname = await config.topic_hostname()
        topic_port = await config.topic_port()
        embed = discord.Embed(color = await ctx.embed_color(), title="Pterodactyl Configuration")
        embed.description = f"""**Base URL:** {base_url}
                       **Server ID:** `{server_id}`
                       **Console Channel:** <#{console_channel}>
                       **Console Commands:** {self.get_bool_str(console_commands_enabled)}
                       **Chat Channel:** <#{chat_channel}>
                       **Startup Message:** {startup_msg}
                       **Shutdown Message:** {shutdown_msg}
                       **Join Message:** {join_msg}
                       **Leave Message:** {leave_msg}
                       **Mask IP:** {self.get_bool_str(mask_ip)}
                       **API Endpoint:** `{api_endpoint}`
                       **Invite:** {invite}

                        **Topic Hostname:** `{topic_hostname}`
                        **Topic Port:** `{topic_port}`
                        **Topic Text:** {box(topic_text, 'yaml')}

                       **Chat Command:** {box(chat_command, 'json')}
                       **Chat Regex:** {box(chat_regex, 're')}
                       **Server Regex:** {box(server_regex, 're')}
                       **Join Regex:** {box(join_regex, 're')}
                       **Leave Regex:** {box(leave_regex, 're')}
                       **Achievement Regex:** {box(achievement_regex, 're')}"""
        await ctx.send(embed=embed)
        if not len(regex_blacklist) == 0:
            regex_blacklist_embed = discord.Embed(color = await ctx.embed_color(), title="Regex Blacklist")
            for name, regex in regex_blacklist.items():
                regex_blacklist_embed.add_field(name=name, value=box(regex, 're'), inline=False)
            await ctx.send(embed=regex_blacklist_embed)

    def get_bool_str(self, inp: bool) -> str:
        """Return a string representation of a boolean."""
        return "Enabled" if inp else "Disabled"
