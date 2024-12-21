from abc import ABC, ABCMeta, abstractmethod
from concurrent.futures import ThreadPoolExecutor

import discord
import pandas as pd
from discord.ext.commands.cog import CogMeta
from starbot.core.bot import Red
from starbot.core.config import Config


class CompositeMetaClass(CogMeta, ABCMeta):
    """Type detection"""


class MixinMeta(ABC):
    """Type hinting"""

    bot: Red
    config: Config
    executor: ThreadPoolExecutor

    @abstractmethod
    async def get_plot(self, df: pd.DataFrame, y_label: str) -> discord.File:
        raise NotImplementedError
