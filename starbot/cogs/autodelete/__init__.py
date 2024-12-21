from starbot.core.bot import Red
from .autodelete import AutoDelete

async def setup(bot: Red):
  await bot.add_cog(AutoDelete(bot))
