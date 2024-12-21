from Star-Utils import Cog, CogsUtils
import discord
from starbot.core import commands, Config
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import box

class PresenceXP(Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "xp_multipliers": {
                "online": 1.0,
                "idle": 0.8,
                "dnd": 0.6,
                "offline": 0.4
            }
        }
        default_user = {
            "xp": 0,
            "level": 1
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)

    @commands.command()
    async def xp(self, ctx: commands.Context):
        """Check your current XP and level."""
        user_data = await self.config.user(ctx.author).all()
        xp = user_data["xp"]
        level = user_data["level"]
        await ctx.send(f"{ctx.author.mention}, you are level {level} with {xp} XP.")

    @commands.command()
    @commands.is_owner()
    async def setxpmultiplier(self, ctx: commands.Context, status: str, multiplier: float):
        """Set the XP multiplier for a specific status."""
        status = status.lower()
        if status not in ["online", "idle", "dnd", "offline"]:
            await ctx.send("Invalid status. Choose from: online, idle, dnd, offline")
            return

        async with self.config.xp_multipliers() as xp_multipliers:
            xp_multipliers[status] = multiplier

        await ctx.send(f"XP multiplier for {status} status set to {multiplier}")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        status = str(message.author.status)
        xp_multipliers = await self.config.xp_multipliers()
        xp_gain = round(10 * xp_multipliers.get(status, 1.0))

        user_data = await self.config.user(message.author).all()
        user_data["xp"] += xp_gain

        level_up = False
        while user_data["xp"] >= (user_data["level"] * 100):
            user_data["xp"] -= (user_data["level"] * 100)
            user_data["level"] += 1
            level_up = True

        await self.config.user(message.author).set(user_data)

        if level_up:
            await message.channel.send(f"Congratulations {message.author.mention}! You've reached level {user_data['level']}!")
