from starbot.core.bot import Red

from .image import Image


async def setup(bot: Red) -> None:
    await bot.add_cog(Image(bot))
