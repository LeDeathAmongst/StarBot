from starbot.core import commands  # isort:skip
from starbot.core.bot import Red  # isort:skip
from Star-Utils import Cog

class DashboardIntegration:
    bot: Red

    @commands.Cog.listener()
    async def on_dashboard_cog_add(self, dashboard_cog: Cog) -> None:
        if hasattr(self, "settings") and hasattr(self.settings, "commands_added"):
            await self.settings.commands_added.wait()
        dashboard_cog.rpc.third_parties_handler.add_third_party(self)
