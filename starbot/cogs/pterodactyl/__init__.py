from .pterodactyl import Pterodactyl


async def setup(bot):
    await bot.add_cog(Pterodactyl(bot))
