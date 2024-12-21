import logging

from starbot.core import commands
from starbot.core.bot import Red
from starbot.core.data_manager import cog_data_path, core_data_path

from .abc import CompositeMetaClass
from .commands import Utils

log = logging.getLogger("red.vrt.vrtutils")


class VrtUtils(Utils, commands.Cog, metaclass=CompositeMetaClass):
    """
    A collection of stateless utility commands for getting info about various things.
    """


    async def red_delete_data_for_user(self, *, requester, user_id: int):
        """No data to delete"""

    def __init__(self, bot: Red):
        super().__init__()
        self.bot: Red = bot
        self.path = cog_data_path(self)
        self.core = core_data_path()
