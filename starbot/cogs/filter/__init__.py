from .filter import Filter
from starbot.core.bot import Red


async def setup(bot: Red) -> None:
    await bot.add_cog(Filter(bot))
