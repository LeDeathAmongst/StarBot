from starbot.core.bot import Red

from .botjoinmessage import BotJoinMessage

async def setup(bot):
    await bot.add_cog(BotJoinMessage(bot))
