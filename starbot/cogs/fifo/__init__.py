import sys
import importlib

from starbot.core import errors
from starbot.core.bot import Red
from starbot.core.utils import get_end_user_data_statement

try:
    import Star-Utils
except ModuleNotFoundError:
    raise errors.CogLoadError(
        "The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/LeDeathAmongst/Star-Utils.git`. A restart of the bot isn't necessary."
    )

modules = sorted([module for module in sys.modules if module.split('.')[0] == 'Star-Utils'], reverse=True)
for module in modules:
    try:
        importlib.reload(sys.modules[module])
    except ModuleNotFoundError:
        pass
del Star-Utils

from Star-Utils import Cog
from .fifo import FIFO

# Applying fix from: https://github.com/Azure/azure-functions-python-worker/issues/640
# [Fix] Create a wrapper for importing imgres
from .date_trigger import *
from . import CustomDateTrigger

# [Fix] Register imgres into system modules
sys.modules["CustomDateTrigger"] = CustomDateTrigger

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)

async def setup(bot: Red) -> None:
    fifo_cog = FIFO(bot)
    await bot.add_cog(fifo_cog)

async def teardown(bot: Red) -> None:
    pass
