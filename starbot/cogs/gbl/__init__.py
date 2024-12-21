from starbot.core import errors
import importlib
import sys

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

from starbot.core.bot import Red
from starbot.core.utils import get_end_user_data_statement
from .gbl import GlobalBanList

__red_end_user_data_statement__ = get_end_user_data_statement(file=__file__)

async def setup(bot: Red):
    cog = GlobalBanList(bot)
    await bot.add_cog(cog)

    # Set up autocomplete for app commands
    gbl_group = cog.gbl
    if gbl_group:
        add_user_command = gbl_group.get_command("add")
        remove_user_command = gbl_group.get_command("remove")
        subscribe_command = gbl_group.get_command("subscribe")
        unsubscribe_command = gbl_group.get_command("unsubscribe")

        if add_user_command:
            add_user_command.autocomplete("list_name")(cog.autocomplete_list_name)
        if remove_user_command:
            remove_user_command.autocomplete("list_name")(cog.autocomplete_list_name)
            remove_user_command.autocomplete("user")(cog.autocomplete_banned_user)
        if subscribe_command:
            subscribe_command.autocomplete("list_name")(cog.autocomplete_list_name)
        if unsubscribe_command:
            unsubscribe_command.autocomplete("list_name")(cog.autocomplete_list_name)
