from Star-Utils import CogsUtils  # isort:skip
from starbot.core import commands  # isort:skip
from starbot.core.bot import Red  # isort:skip
from starbot.core.i18n import Translator  # isort:skip
import discord  # isort:skip
import typing  # isort:skip

import os

from starbot.core.utils.chat_formatting import humanize_list

_ = Translator("application", __file__)

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

    @dashboard_page(name=None, description="Manage application")
    async def dashboard_main(self, **kwargs) -> None:
        return {"status": 0, "web_content": {"source": '<h1>application Dashboard</h1><p>Welcome to the application dashboard!</p>'}}

    @dashboard_page(
        name="guild",
        description="Manage application for a specific guild",
        methods=("GET", "POST"),
    )
    async def dashboard_guild(self, user: discord.User, guild: discord.Guild, **kwargs) -> None:
        is_owner = user.id in self.bot.owner_ids
        member = guild.get_member(user.id)
        if not is_owner and not await self.bot.is_mod(member):
            return {
                "status": 0,
                "error_code": 403,
                "message": _("You don't have permissions to access this page."),
            }

        # Add your guild-specific dashboard logic here
        return {
            "status": 0,
            "web_content": {"source": f'<h2>application Settings for {guild.name}</h2><p>Guild-specific settings and controls go here.</p>'}
        }

    # Add more dashboard_page methods as needed for your cog's functionality
