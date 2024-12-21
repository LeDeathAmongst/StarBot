from starbot.core import errors  # isort:skip
import importlib
import sys

try:
    import Star-Utils  # Attempt to import Star-Utils
except ModuleNotFoundError:
    raise errors.CogLoadError(
        "The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/LeDeathAmongst/Star-Utils.git`. A restart of the bot isn't necessary."
    )

# Reload Star-Utils modules if they are already loaded
modules = sorted(
    [module for module in sys.modules if module.split(".")[0] == "Star-Utils"], reverse=True
)
for module in modules:
    try:
        importlib.reload(sys.modules[module])
    except ModuleNotFoundError:
        pass
del Star-Utils

# Import Red and get_end_user_data_statement
from starbot.core.bot import Red  # isort:skip
from starbot.core.utils import get_end_user_data_statement

from .cycle_status import CycleStatus  # Import your cog

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)

async def setup(bot: Red) -> None:
    cog = CycleStatus(bot)
    await bot.add_cog(cog)
