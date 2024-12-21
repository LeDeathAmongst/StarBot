import contextlib
import importlib
import json
from pathlib import Path

from starbot.core import VersionInfo
from starbot.core.bot import Red

from . import vexutils
from .madtranslate import MadTranslate
from .vexutils.meta import out_of_date_check

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


async def setup(bot: Red) -> None:
    cog = MadTranslate(bot)
    await out_of_date_check("madtranslate", cog.__version__)
    await bot.add_cog(cog)
