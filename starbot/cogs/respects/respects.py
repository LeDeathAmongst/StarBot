"""Respects cog
A replica of +f seen in another bot, except smarter..
"""

from starbot.core import commands
from Star-Utils import Cog, CogsUtils
from .commandHandlers import CommandHandlers


class Respects(Cog, CommandHandlers):
    def __init__(self, bot):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("Respects")
        self.logs = CogsUtils.get_logger("Respects")
    """Pay your respects."""
