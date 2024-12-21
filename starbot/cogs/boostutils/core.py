"""
MIT License

Copyright (c) 2024-present japandotorg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Dict, Final, List, Union

from starbot.core import Config, commands
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import humanize_list

from ._tagscript import TAGSCRIPT_LIMIT, TagCharacterLimitReached, boosted, unboosted
from .abc import CompositeMetaClass
from .commands.message import MessageCommands
from .events import EventMixin
from Star-Utils import Cog, CogsUtils

class BoostUtils(
    Cog,
    EventMixin,
    MessageCommands,
    metaclass=CompositeMetaClass,
):
    """Nitro Boost Utilities."""

    def __init__(self, bot: Red) -> None:
        self.bot: Red = bot
        self.logs = CogsUtils.get_logger("BoostUtils")
        self.config: Config = Config.get_conf(
            self,
            identifier=69_666_420,
            force_registration=True,
        )
        default_guild: Dict[str, Dict[str, Union[bool, List[int], str]]] = {
            "boost_message": {
                "toggle": False,
                "channels": [],
                "boosted": boosted,
                "unboosted": unboosted,
            }
        }
        self.config.register_guild(**default_guild)

    @staticmethod
    async def validate_tagscript(tagscript: str) -> bool:
        length = len(tagscript)
        if length > TAGSCRIPT_LIMIT:
            raise TagCharacterLimitReached(TAGSCRIPT_LIMIT, length)
        return True
