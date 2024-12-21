from abc import ABC

from starbot.core import Config
from starbot.core.bot import Red


class MixinMeta(ABC):
    """
    Base class for well behaved type hint detection with composite class.

    Basically, to keep developers sane when not all attributes are defined in each mixin.

    This is modified from
    https://github.com/Cog-Creators/StarBot/blob/V3/develop/starbot/cogs/mod/abc.py
    """

    def __init__(self, *_args):
        self.bot: Red
        self.config: Config
