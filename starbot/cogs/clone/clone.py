from Star-Utils import Cog, CogsUtils
import discord
from starbot.core import commands, checks
from typing import List

class Clone(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logs = CogsUtils.get_logger("Clone")

    @commands.command()
    @checks.mod()
    async def clone(self, ctx, user: discord.Member):
        """
        Clones specified user
        """
        new_nick = user.display_name
        my_role = [r for r in user.guild.roles if "snek color" == r.name.lower()]
        if len(my_role) != 1:
            await ctx.send("Error finding role, aborting!")
            return
        my_role = my_role[0]
        avatar = await user.display_avatar.replace(static_format='png', format='png').read()
        me = ctx.message.guild.me

        # await ctx.send(file=discord.File(avatar, filename='profile.png'))
        await me.edit(nick=new_nick)
        await self.bot.user.edit(avatar=avatar)
        await my_role.edit(color=user.color)
        await ctx.send("Done")

    @commands.command()
    @checks.mod()
    async def set_color(self, ctx: commands.Context, color: str):
        if color.startswith("#"):
            color = color[1:]

        if len(color) != 6:
            await ctx.send("Invalid Color!")
            return

        my_role: List[discord.Role] = [
            r for r in ctx.message.guild.roles if "snek color" == r.name.lower()
        ]
        if len(my_role) != 1:
            await ctx.send("Error finding role, aborting!")
            return
        my_role: discord.Role = my_role[0]

        red = int(color[:2], 16)
        green = int(color[2:4], 16)
        blue = int(color[4:], 16)
        print(f"New rgb color is {red}, {green}, {blue}")

        color = discord.Color.from_rgb(red, green, blue)

        await my_role.edit(color=color)
