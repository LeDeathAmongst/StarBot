from starbot.core.bot import Red
from starbot.core.utils import get_end_user_data_statement

from .main import LevelUp

__red_end_user_data_statement__ = get_end_user_data_statement(__file__)


async def setup(bot: Red):
    await bot.add_cog(LevelUp(bot))
