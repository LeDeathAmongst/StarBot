from starbot.core import commands
from starbot.core.bot import Red
from starbot.core.utils.views import SimpleMenu
from Star-Utils import Cog, CogsUtils

from .utils import (
    ValidRoleIndex,
    ValidUserIndex,
    format_embed_pages,
    get_members,
    get_roles,
)

roleboard_perms = commands.bot_has_permissions(embed_links=True, add_reactions=True)


class RoleBoards(Cog):
    """
    Get 'leaderboards' about guild roles, such as the users with the most roles
    and the roles with the most users.
    """

        
    def __init__(self, bot: Red):
        self.bot = bot


    async def red_delete_data_for_user(self, **kwargs):
        return

    @commands.group(aliases=["roleboards", "rb"])
    @commands.guild_only()
    async def roleboard(self, ctx: commands.Context):
        """Get roleboards for this server.."""
        pass

    @roleboard.command(aliases=["topusers"])
    @roleboard_perms
    async def topmembers(self, ctx: commands.Context, index: ValidUserIndex):
        """Get the members with the most roles.

        \u200b
        **Arguments**

        -   ``<index>``: The number of members to get the data for.
        """
        data = get_members(ctx.guild, index=index)
        pages = format_embed_pages(
            ctx, data=data, data_type="members", embed_colour=await ctx.embed_colour()
        )
        menu = SimpleMenu(pages, use_select_menu=True)
        await menu.start(ctx)

    @roleboard.command()
    @roleboard_perms
    async def toproles(self, ctx: commands.Context, index: ValidRoleIndex):
        """Get the roles with the most members.

        \u200b
        **Arguments**

        -   ``<index>``: The number of roles to get the data for.
        """
        data = get_roles(ctx.guild, index=index)
        pages = format_embed_pages(
            ctx, data=data, data_type="roles", embed_colour=await ctx.embed_colour()
        )
        menu = SimpleMenu(pages, use_select_menu=True)
        await menu.start(ctx)
