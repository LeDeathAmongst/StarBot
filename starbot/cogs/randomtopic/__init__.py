from starbot.core.bot import Red

from .randomtopic import RandomTopic

async def setup(bot: Red):
    await bot.add_cog(RandomTopic(bot))
