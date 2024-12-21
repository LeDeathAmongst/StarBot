from starbot.core import commands
from starbot.core.bot import Red
import typing
from Star-Utils import Cog

def dashboard_page(*args, **kwargs):
    def decorator(func: typing.Callable):
        func.__dashboard_decorator_params__ = (args, kwargs)
        return func
    return decorator

class DashboardIntegration:
    bot: Red

    @commands.Cog.listener()
    async def on_dashboard_cog_add(self, dashboard_cog: Cog) -> None:
        dashboard_cog.rpc.third_parties_handler.add_third_party(self)

    @dashboard_page(name="example")
    async def example_page(self, **kwargs) -> typing.Dict[str, typing.Any]:
        return {"status": 0, "web_content": {"source": "<h1>Example Page</h1>"}}
