"""Triggered cog
`triggered from spoopy.
"""

from starbot.core import commands

from .commandHandlers import CommandHandlers


class Triggered(Cog, CommandHandlers):
    def __init__(self, bot):
        super().__init__(bot)
        self.logs = CogsUtils.get_logger("Triggered")
        self.logs = CogsUtils.get_logger("Triggered")
        self.logs = CogsUtils.get_logger("Triggered")
    """We triggered, fam."""
