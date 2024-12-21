from .ext import RYD

__red_end_user_data_statement__ = "RYD stores preferences about turning off links scanner"


async def setup(bot):
    await bot.add_cog(RYD(bot))
