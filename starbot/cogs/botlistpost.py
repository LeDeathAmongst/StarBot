import aiohttp
from starbot.core import commands, Config
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import box

class DiscordBotListAPI(commands.Cog):
    """Interact with the Discord Bot List API"""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        default_global = {"api_token": None}
        self.config.register_global(**default_global)
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    @commands.group()
    @commands.is_owner()
    async def dblapi(self, ctx):
        """Discord Bot List API commands"""
        pass

    @dblapi.command()
    async def settoken(self, ctx, token: str):
        """Set the Discord Bot List API token"""
        await self.config.api_token.set(token)
        await ctx.send("API token set successfully.")

    @dblapi.command()
    async def postcommands(self, ctx):
        """Post bot commands to Discord Bot List"""
        token = await self.config.api_token()
        if not token:
            return await ctx.send("API token not set. Use `[p]dblapi settoken` to set it.")

        commands_list = []
        for command in self.bot.commands:
            if not command.hidden:
                commands_list.append({
                    "name": command.name,
                    "description": command.help or "No description provided.",
                    "type": 1
                })

        url = f"https://discordbotlist.com/api/v1/bots/{self.bot.user.id}/commands"
        headers = {"Authorization": f"Bot {token}"}

        async with self.session.post(url, json=commands_list, headers=headers) as resp:
            if resp.status == 200:
                await ctx.send("Commands posted successfully to Discord Bot List.")
            else:
                await ctx.send(f"Failed to post commands. Status code: {resp.status}")

    @dblapi.command()
    async def poststats(self, ctx):
        """Post bot statistics to Discord Bot List"""
        token = await self.config.api_token()
        if not token:
            return await ctx.send("API token not set. Use `[p]dblapi settoken` to set it.")

        stats = {
            "guilds": len(self.bot.guilds),
            "users": len(self.bot.users),
            "voice_connections": len(self.bot.voice_clients)
        }

        url = f"https://discordbotlist.com/api/v1/bots/{self.bot.user.id}/stats"
        headers = {"Authorization": f"Bot {token}"}

        async with self.session.post(url, json=stats, headers=headers) as resp:
            if resp.status == 200:
                await ctx.send("Statistics posted successfully to Discord Bot List.")
            else:
                await ctx.send(f"Failed to post statistics. Status code: {resp.status}")

    @commands.command()
    async def infobot(self, ctx):
        """Display bot information"""
        embed = discord.Embed(title=f"{self.bot.user.name} Information", color=discord.Color.blue())
        embed.add_field(name="Servers", value=str(len(self.bot.guilds)), inline=True)
        embed.add_field(name="Users", value=str(len(self.bot.users)), inline=True)
        embed.add_field(name="Commands", value=str(len(self.bot.commands)), inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(DiscordBotListAPI(bot))
