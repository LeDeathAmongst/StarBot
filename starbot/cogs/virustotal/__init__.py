from starbot.core.bot import Red #type: ignore

from .virustotal import VirusTotal


async def setup(bot: Red):
    cog = VirusTotal(bot)
    await bot.add_cog(cog)


__red_end_user_data_statement__ = "The VirusTotal cog by BeeHive does not store any user data. VirusTotal stores submitted file information subject to their own Terms of Service and Privacy Policy."
