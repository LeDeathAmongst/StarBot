from starbot.core import errors  # isort:skip
import importlib
import sys

try:
    import Star-Utils
except ModuleNotFoundError:
    raise errors.CogLoadError(
        "The needed utils to run the cog were not found. Please execute the command `[p]pipinstall git+https://github.com/LeDeathAmongst/Star-Utils.git`. A restart of the bot isn't necessary."
    )
modules = sorted(
    [module for module in sys.modules if module.split(".")[0] == "Star-Utils"], reverse=True
)
for module in modules:
    try:
        importlib.reload(sys.modules[module])
    except ModuleNotFoundError:
        pass
del Star-Utils
# import Star-Utils
# import json
# import os
# # with open(os.path.join(os.path.dirname(__file__), "utils_version.json"), mode="r") as f:
#     data = json.load(f)
# needed_utils_version = data["needed_utils_version"]
# if __version__ > needed_utils_version:
#     raise errors.CogLoadError(
#         "The needed utils to run the cog has a higher version than the one supported by this version of the cog. Please update the cogs of the `StarCogs` repo."
#     )
# elif __version__ < needed_utils_version:
#     raise errors.CogLoadError(
#         "The needed utils to run the cog has a lower version than the one supported by this version of the cog. Please execute the command `[p]pipinstall --upgrade git+https://github.com/LeDeathAmongst/Star-Utils.git`. A restart of the bot isn't necessary."
#     )

from starbot.core.bot import Red  # isort:skip
import json
from pathlib import Path

from .dropdownstexts import DropdownsTexts

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


async def setup(bot: Red) -> None:
    cog = DropdownsTexts(bot)
    await bot.add_cog(cog)
