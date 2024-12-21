from .fact import UselessFacts

async def setup(bot):
    await bot.add_cog(UselessFacts(bot))
