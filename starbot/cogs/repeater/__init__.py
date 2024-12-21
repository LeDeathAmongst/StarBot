from .repeater import Repeater

async def setup(bot):
    await bot.add_cog(Repeater(bot))
