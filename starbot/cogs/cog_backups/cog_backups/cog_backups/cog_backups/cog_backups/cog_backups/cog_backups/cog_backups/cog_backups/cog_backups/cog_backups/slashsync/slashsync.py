from starbot.core import commands
from Star_Utils import Cog, CogsUtils

from .commandHandlers import CommandHandlers


class SlashSync(Cog, CommandHandlers):
    def __init__(self, bot):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("SlashSync")
        self.logs = CogsUtils.get_logger("SlashSync")
        self.logs = CogsUtils.get_logger("SlashSync")
        self.logs = CogsUtils.get_logger("SlashSync")
    """Synchronize slash commands on the bot to Discord"""
