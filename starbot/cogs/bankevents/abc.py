from abc import ABCMeta

from discord.ext.commands.cog import CogMeta
from starbot.core.bot import Red


class CompositeMetaClass(CogMeta, ABCMeta):
    """Type detection"""


class MixinMeta(metaclass=ABCMeta):
    """Type hinting"""

    bot: Red
