from .songshare import SongShare

async def setup(bot):
    await bot.add_cog(SongShare(bot))