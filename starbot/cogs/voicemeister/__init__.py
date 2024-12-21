import importlib
import sys
from starbot.core import errors
from starbot.core.bot import Red
from starbot.core.utils import get_end_user_data_statement
from .voicemeister import VoiceMeister
#from .c_voicemeister import VoiceMeisterCommands
#from .c_voicemeisterset import VoiceMeisterSet
#from .vminterface import VMInterface

# Ensure Star-Utils is available
try:
    import Star-Utils
except ModuleNotFoundError:
    raise errors.CogLoadError(
        "The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/LeDeathAmongst/Star-Utils.git`. A restart of the bot isn't necessary."
    )

# Reload Star-Utils modules
modules = sorted([module for module in sys.modules if module.split('.')[0] == 'Star-Utils'], reverse=True)
for module in modules:
    try:
        importlib.reload(sys.modules[module])
    except ModuleNotFoundError:
        pass
del Star-Utils

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)

async def setup(bot: Red) -> None:
#    vm_interface = VMInterface(bot)
    voicemeister_cog = VoiceMeister(bot)
#    voicemeister_commands_cog = VoiceMeisterCommands(bot, vm_interface)
#    voicemeister_set_cog = VoiceMeisterSet(bot)

    await bot.add_cog(voicemeister_cog)
#    await bot.add_cog(voicemeister_commands_cog)
#    await bot.add_cog(voicemeister_set_cog)
