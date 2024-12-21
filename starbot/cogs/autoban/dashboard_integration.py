from Star-Utils import CogsUtils  # isort:skip
from starbot.core import commands  # isort:skip
from starbot.core.bot import Red  # isort:skip
from starbot.core.i18n import Translator  # isort:skip
import discord  # isort:skip
import typing  # isort:skip

import os

from starbot.core.utils.chat_formatting import humanize_list

_ = Translator("autoban", __file__)

def dashboard_page(*args, **kwargs):
    def decorator(func: typing.Callable):
        func.__dashboard_decorator_params__ = (args, kwargs)
        return func
    return decorator

class DashboardIntegration:
    bot: Red

    @Cog.listener()
    async def on_dashboard_cog_add(self, dashboard_cog: Cog) -> None:
        dashboard_cog.rpc.third_parties_handler.add_third_party(self)

    @dashboard_page(name=None, description="Manage autoban")
    async def dashboard_main(self, **kwargs) -> None:
        return {"status": 0, "web_content": {"source": '<h1>autoban Dashboard</h1><p>Welcome to the autoban dashboard!</p>'}}

    
