import logging

from starbot.core import commands
from starbot.core.bot import Red
from Star-Utils import Cog, CogsUtils
from .abc import CompositeMetaClass
from .common import schemas
from .common.functions import Functions

log = logging.getLogger("red.vrt.assistantutils")


class AssistantUtils(Functions, Cog, metaclass=CompositeMetaClass):
    """
    Assistant Utils adds pre-baked functions to the Assistant cog, allowing extended functionality.
    """

    def __init__(self, bot: Red):
        super().__init__(bot)
        self.bot = bot
        self.logs = CogsUtils.get_logger("AssistantUtils")

    @commands.Cog.listener()
    async def on_assistant_cog_add(self, cog: Cog):
        await cog.register_function(self.qualified_name, schemas.GET_CHANNEL_ID)
        await cog.register_function(self.qualified_name, schemas.GET_CHANNEL_NAMED)
        await cog.register_function(self.qualified_name, schemas.GET_CHANNEL_MENTION)
        await cog.register_function(self.qualified_name, schemas.GET_CHANNEL_LIST)
        await cog.register_function(self.qualified_name, schemas.GET_CHANNEL_TOPIC)

        await cog.register_function(self.qualified_name, schemas.GET_SEARCH_URL)
        log.info("Functions have been registered")
