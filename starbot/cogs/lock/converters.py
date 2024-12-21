"""
MIT License

Copyright (c) 2020-2023 PhenoM4n4n
Copyright (c) 2023-present japandotorg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Optional, Union

import discord
from rapidfuzz import process
from starbot.core import commands
from unidecode import unidecode


class ChannelToggle(commands.Converter):
    async def convert(
        self,
        ctx: commands.Context,
        argument: str,
    ) -> Union[bool, None]:
        argument = argument.lower()
        if argument not in ["true", "default", "neutral"]:
            raise commands.BadArgument(
                f"`{argument}` is not a valid channel state. You use provide `true` or `default`."
            )
        ret = None
        if argument in ["neutral", "default"]:
            ret = None
        elif argument == "true":
            ret = True
        return ret


class LockableChannel(commands.TextChannelConverter):
    async def convert(
        self,
        ctx: commands.Context,
        argument: str,
    ) -> Optional[discord.TextChannel]:
        channel = await super().convert(ctx, argument)
        if not channel.permissions_for(ctx.me).manage_roles:  # type: ignore
            raise commands.BadArgument(
                f"I do not have permissions to edit permissions in {channel.mention}.",
            )
        if not await ctx.bot.is_owner(ctx.author):
            author_perms = channel.permissions_for(ctx.author)  # type: ignore
            if not author_perms.read_messages:
                raise commands.BadArgument(
                    f"You do not have permissions to view or edit {channel.mention}."
                )
        return channel


# original converter from https://github.com/TrustyJAID/Trusty-cogs/blob/master/serverstats/converters.py#L19
class FuzzyRole(commands.RoleConverter):
    """
    This will accept role ID's, mentions, and perform a fuzzy search for
    roles within the guild and return a list of role objects
    matching partial names
    Guidance code on how to do this from:
    https://github.com/Rapptz/discord.py/blob/rewrite/discord/ext/commands/converter.py#L85
    https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/starbot/cogs/mod/mod.py#L24
    """

    def __init__(self, response: bool = True):
        self.response: bool = response
        super().__init__()

    async def convert(
        self,
        ctx: commands.Context,
        argument: str,
    ) -> discord.Role:
        try:
            basic_role = await super().convert(ctx, argument)
        except commands.BadArgument:
            pass
        else:
            return basic_role
        guild = ctx.guild
        result = [
            (r[2], r[1])
            for r in process.extract(
                argument,
                {r: unidecode(r.name) for r in guild.roles},  # type: ignore
                limit=None,
                score_cutoff=75,
            )
        ]
        if not result:
            raise commands.BadArgument(f'Role "{argument}" not found.' if self.response else None)

        sorted_result = sorted(result, key=lambda r: r[1], reverse=True)
        return sorted_result[0][0]  # type: ignore


class LockableRole(FuzzyRole):
    async def convert(self, ctx: commands.Context, argument: str) -> discord.Role:
        role = await super().convert(ctx, argument)
        if not await ctx.bot.is_owner(ctx.author) and role >= ctx.author.top_role:  # type: ignore
            raise commands.BadArgument(
                f"You do not have permissions to edit **{role}**'s permissions."
            )
        return role
