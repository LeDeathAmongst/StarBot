from .message import Message

async def setup(bot):
    cog = Message(bot)
    await bot.add_cog(cog)