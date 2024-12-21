import logging
from typing import Union
from Star_Utils import Cog, CogsUtils

import discord
from starbot.core import commands

from .abc import MixinMeta

log = logging.getLogger("red.angiedale.owner")


class Events(MixinMeta):
    def __init__(self, bot):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("Events")
        self.logs = CogsUtils.get_logger("Events")
    @commands.commands.Cog.listener()
    async def on_reaction_add(
        self, reaction: discord.Reaction, user: Union[discord.Member, discord.User]
    ):
        if user in self.interaction:
            channel = reaction.message.channel
            if isinstance(channel, discord.DMChannel):
                await self.stop_interaction(user)

    @commands.commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        if await self.admin_config.serverlocked():
            if len(self.bot.guilds) == 1:  # will be 0 once left
                log.warning(
                    f"Leaving guild '{guild.name}' ({guild.id}) due to serverlock. You can "
                    "temporarily disable serverlock by starting up the bot with the --no-cogs flag."
                )
            else:
                log.info(f"Leaving guild '{guild.name}' ({guild.id}) due to serverlock.")
            await guild.leave()
