from .aurora import Aurora


async def setup(bot):
    await bot.add_cog(Aurora(bot))
