import contextlib
import importlib
import json
from pathlib import Path

import discord
from starbot.core import VersionInfo
from starbot.core.bot import Red
from starbot.core.errors import CogLoadError

from . import vexutils
from .buttonpoll import ButtonPoll
from .vexutils.meta import out_of_date_check

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


async def setup(bot: Red):
    cog = ButtonPoll(bot)
    await out_of_date_check("buttonpoll", cog.__version__)
    await bot.add_cog(cog)
