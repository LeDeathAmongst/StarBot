# pylint: disable=cyclic-import
import json
import re
from pathlib import Path
from typing import Optional, Tuple, Union

import aiohttp
import discord
import websockets
from pydactyl import PterodactylClient
from starbot.core.data_manager import bundled_data_path
from starbot.core.utils.chat_formatting import bold, pagify

from pterodactyl.config import config
from pterodactyl.logger import logger, websocket_logger
from pterodactyl.pterodactyl import Pterodactyl


async def establish_websocket_connection(coginstance: Pterodactyl) -> None:
    await coginstance.bot.wait_until_red_ready()
    base_url = await config.base_url()
    base_url = base_url[:-1] if base_url.endswith('/') else base_url

    logger.info("Establishing WebSocket connection")

    websocket_credentials = await retrieve_websocket_credentials(coginstance)

    async with websockets.connect(websocket_credentials['data']['socket'], origin=base_url, ping_timeout=60, logger=websocket_logger) as websocket:
        logger.info("WebSocket connection established")

        auth_message = json.dumps({"event": "auth", "args": [websocket_credentials['data']['token']]})
        await websocket.send(auth_message)
        logger.info("Authentication message sent")

        coginstance.websocket = websocket

        while True: # pylint: disable=too-many-nested-blocks
            message = json.loads(await websocket.recv())
            if message['event'] in ('token expiring', 'token expired'):
                logger.info("Received token expiring/expired event. Refreshing token.")
                websocket_credentials = await retrieve_websocket_credentials(coginstance)
                auth_message = json.dumps({"event": "auth", "args": [websocket_credentials['data']['token']]})
                await websocket.send(auth_message)
                logger.info("Authentication message sent")

            if message['event'] == 'auth success':
                logger.info("WebSocket authentication successful")

            if message['event'] == 'console output' and await config.console_channel() is not None:
                regex_blacklist: dict = await config.regex_blacklist()
                matches = [re.search(regex, message['args'][0]) for regex in regex_blacklist.values()]

                if await config.current_status() in ('running', '') and not any(matches):
                    content = remove_ansi_escape_codes(message['args'][0])
                    if await config.mask_ip() is True:
                        content = mask_ip(content)

                    console_channel = coginstance.bot.get_channel(await config.console_channel())
                    chat_channel = coginstance.bot.get_channel(await config.chat_channel())
                    if console_channel is not None:
                        if content.startswith('['):
                            pagified_content = pagify(content, delims=[" ", "\n"])
                            for page in pagified_content:
                                await console_channel.send(content=page, allowed_mentions=discord.AllowedMentions.none())

                    server_message = await check_if_server_message(content)
                    if server_message:
                        if chat_channel is not None:
                            await chat_channel.send(server_message if len(server_message) < 2000 else server_message[:1997] + '...', allowed_mentions=discord.AllowedMentions.none())

                    chat_message = await check_if_chat_message(content)
                    if chat_message:
                        info = await get_info(chat_message['username'])
                        if info is not None:
                            await send_chat_discord(coginstance, chat_message['username'], chat_message['message'], info['data']['player']['avatar'])
                        else:
                            await send_chat_discord(coginstance, chat_message['username'], chat_message['message'], 'https://seafsh.cc/u/j3AzqQ.png')

                    join_message = await check_if_join_message(content)
                    if join_message:
                        if chat_channel is not None:
                            if coginstance.bot.embed_requested(chat_channel):
                                embed, img = await generate_join_leave_embed(coginstance=coginstance, username=join_message,join=True)
                                if img:
                                    with open(img, 'rb') as file:
                                        await chat_channel.send(embed=embed, file=file)
                                else:
                                    await chat_channel.send(embed=embed)
                            else:
                                await chat_channel.send(f"{join_message} joined the game", allowed_mentions=discord.AllowedMentions.none())

                    leave_message = await check_if_leave_message(content)
                    if leave_message:
                        if chat_channel is not None:
                            if coginstance.bot.embed_requested(chat_channel):
                                embed, img = await generate_join_leave_embed(coginstance=coginstance, username=leave_message,join=False)
                                if img:
                                    with open(img, 'rb') as file:
                                        await chat_channel.send(embed=embed, file=file)
                                else:
                                    await chat_channel.send(embed=embed)
                            else:
                                await chat_channel.send(f"{leave_message} left the game", allowed_mentions=discord.AllowedMentions.none())

                    achievement_message = await check_if_achievement_message(content)
                    if achievement_message:
                        if chat_channel is not None:
                            if coginstance.bot.embed_requested(chat_channel):
                                await chat_channel.send(embed=await generate_achievement_embed(coginstance, achievement_message['username'], achievement_message['achievement'], achievement_message['challenge']))
                            else:
                                await chat_channel.send(f"{achievement_message['username']} has {'completed the challenge' if achievement_message['challenge'] else 'made the advancement'} {achievement_message['achievement']}")

            if message['event'] == 'status':
                old_status = await config.current_status()
                current_status = message['args'][0]
                if old_status != current_status:
                    await config.current_status.set(current_status)
                    if await config.console_channel() is not None:
                        console = coginstance.bot.get_channel(await config.console_channel())
                        if console is not None:
                            await console.send(f"Server status changed! `{current_status}`")
                    if await config.chat_channel() is not None:
                        if current_status == 'running' and await config.startup_msg() is not None:
                            chat = coginstance.bot.get_channel(await config.chat_channel())
                            if chat is not None:
                                await chat.send(await config.startup_msg())
                        if current_status == 'stopping' and await config.shutdown_msg() is not None:
                            chat = coginstance.bot.get_channel(await config.chat_channel())
                            if chat is not None:
                                await chat.send(await config.shutdown_msg())

async def retrieve_websocket_credentials(coginstance: Pterodactyl) -> Optional[dict]:
    pterodactyl_keys = await coginstance.bot.get_shared_api_tokens("pterodactyl")
    api_key = pterodactyl_keys.get("api_key")
    if api_key is None:
        coginstance.task.cancel()
        raise ValueError("Pterodactyl API key not set. Please set it using `[p]set api`.")
    base_url = await config.base_url()
    if base_url is None:
        coginstance.task.cancel()
        raise ValueError("Pterodactyl base URL not set. Please set it using `[p]pterodactyl config url`.")
    server_id = await config.server_id()
    if server_id is None:
        coginstance.task.cancel()
        raise ValueError("Pterodactyl server ID not set. Please set it using `[p]pterodactyl config serverid`.")

    client = PterodactylClient(base_url, api_key).client
    coginstance.client = client
    websocket_credentials = client.servers.get_websocket(server_id)
    logger.debug("""Websocket connection details retrieved:
                        Socket: %s
                        Token: %s...""",
                        websocket_credentials['data']['socket'],
                        websocket_credentials['data']['token'][:20]
                    )
    return websocket_credentials
    #NOTE - The token is truncated to prevent it from being logged in its entirety, for security reasons

def remove_ansi_escape_codes(text: str) -> str:
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    #NOTE - https://chat.openai.com/share/d92f9acf-d776-4fd6-a53f-b14ac15dd540
    return ansi_escape.sub('', text)

async def check_if_server_message(text: str) -> Union[bool, str]:
    regex = await config.server_regex()
    match: Optional[re.Match[str]] = re.match(regex, text)
    if match:
        logger.trace("Message is a server message")
        return match.group(1)
    return False

async def check_if_chat_message(text: str) -> Union[bool, dict]:
    regex = await config.chat_regex()
    match: Optional[re.Match[str]] = re.match(regex, text)
    if match:
        groups = {"username": match.group(1), "message": match.group(2)}
        logger.trace("Message is a chat message\n%s", json.dumps(groups))
        return groups
    return False

async def check_if_join_message(text: str) -> Union[bool, str]:
    regex = await config.join_regex()
    match: Optional[re.Match[str]] = re.match(regex, text)
    if match:
        logger.trace("Message is a join message")
        return match.group(1)
    return False

async def check_if_leave_message(text: str) -> Union[bool, str]:
    regex = await config.leave_regex()
    match: Optional[re.Match[str]] = re.match(regex, text)
    if match:
        logger.trace("Message is a leave message")
        return match.group(1)
    return False

async def check_if_achievement_message(text: str) -> Union[bool, dict]:
    regex = await config.achievement_regex()
    match: Optional[re.Match[str]] = re.match(regex, text)
    if match:
        groups = {"username": match.group(1), "achievement": match.group(3)}
        if match.group(2) == "completed the challenge":
            groups["challenge"] = True
        else:
            groups["challenge"] = False
        logger.trace("Message is an achievement message")
        return groups
    return False

async def get_info(username: str) -> Optional[dict]:
    logger.verbose("Retrieving player info for %s", username)
    endpoint = await config.api_endpoint()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://playerdb.co/api/player/{endpoint}/{username}") as response:
            if response.status == 200:
                logger.verbose("Player info retrieved for %s", username)
                return await response.json()
            logger.warning("Failed to retrieve player info for %s: %s", username, response.status)
            return None

async def send_chat_discord(coginstance: Pterodactyl, username: str, message: str, avatar_url: str) -> None:
    logger.trace("Sending chat message to Discord")
    channel = coginstance.bot.get_channel(await config.chat_channel())
    if channel is not None:
        webhooks = await channel.webhooks()
        webhook = discord.utils.get(webhooks, name="Pterodactyl Chat")
        if webhook is None:
            webhook = await channel.create_webhook(name="Pterodactyl Chat")
        await webhook.send(content=message, username=username, avatar_url=avatar_url, allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True))
        logger.trace("Chat message sent to Discord")
    else:
        logger.warning("Chat channel not set. Skipping sending chat message to Discord")

async def generate_join_leave_embed(coginstance: Pterodactyl, username: str, join: bool) -> Tuple[discord.Embed, Optional[Union[str, Path]]]:
    embed = discord.Embed()
    embed.color = discord.Color.green() if join else discord.Color.red()
    embed.description = await config.join_msg() if join else await config.leave_msg()
    info = await get_info(username)
    if info:
        img = None
        embed.set_author(name=username, icon_url=info['data']['player']['avatar'])
    else:
        img = bundled_data_path(coginstance) / "unknown.png"
        embed.set_author(name=username, icon_url='attachment://unknown.png')
    embed.timestamp = discord.utils.utcnow()
    return embed, img

async def generate_achievement_embed(coginstance: Pterodactyl, username: str, achievement: str, challenge: bool) -> Tuple[discord.Embed, Optional[Union[str, Path]]]:
    embed = discord.Embed()
    embed.color = discord.Color.from_str('#a800a7') if challenge else discord.Color.from_str('#54fb54')
    embed.description = f"{bold(username)} has {'completed the challenge' if challenge else 'made the advancement'} {bold(achievement)}"
    info = await get_info(username)
    if info:
        img = None
        embed.set_author(name=username, icon_url=info['data']['player']['avatar'])
    else:
        img = bundled_data_path(coginstance) / "unknown.png"
        embed.set_author(name=username, icon_url='attachment://unknown.png')
    embed.timestamp = discord.utils.utcnow()
    return embed, img

def mask_ip(string: str) -> str:
    def check(match: re.Match[str]):
        ip = match.group(0)
        masked_ip = '.'.join(r'\*' * len(octet) for octet in ip.split('.'))
        return masked_ip
    return re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', check, string)
