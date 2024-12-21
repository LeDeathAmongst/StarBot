import discord
from starbot.core import commands, Config
import aiohttp
import asyncio
import json
from datetime import datetime
import os

class StatsPusher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "push_url": "http://your-flask-site.com/push_stats",
            "push_interval": 300  # 5 minutes
        }
        self.config.register_global(**default_global)
        self.push_task = self.bot.loop.create_task(self.push_stats_loop())

    def cog_unload(self):
        self.push_task.cancel()

    @commands.command()
    @commands.is_owner()
    async def setpushurl(self, ctx, url: str):
        """Set the URL to push stats to."""
        await self.config.push_url.set(url)
        await ctx.send(f"Push URL set to {url}")

    @commands.command()
    @commands.is_owner()
    async def setpushinterval(self, ctx, interval: int):
        """Set the interval (in seconds) for pushing stats."""
        await self.config.push_interval.set(interval)
        await ctx.send(f"Push interval set to {interval} seconds")
        self.push_task.cancel()
        self.push_task = self.bot.loop.create_task(self.push_stats_loop())

    @commands.command()
    @commands.is_owner()
    async def pushstats(self, ctx):
        """Manually push stats and update the stats file."""
        success = await self.push_stats()
        if success:
            await ctx.send("Stats pushed successfully and file updated.")
        else:
            await ctx.send("Failed to push stats, but the file has been updated.")

    async def push_stats_loop(self):
        while True:
            await self.push_stats()
            await asyncio.sleep(await self.config.push_interval())

    async def push_stats(self):
        url = await self.config.push_url()
        stats = {
            "user_count": sum(guild.member_count for guild in self.bot.guilds),
            "server_count": len(self.bot.guilds),
            "command_count": len(set(self.bot.walk_commands())),
            "avatar_url": str(self.bot.user.avatar.url if self.bot.user.avatar else ""),
            "timestamp": datetime.utcnow().isoformat()
        }

        # Always save stats to a file
        self.save_stats_to_file(stats)

        # Attempt to push stats to URL
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=stats) as resp:
                    if resp.status == 200:
                        print("Stats pushed successfully")
                        return True
                    else:
                        print(f"Failed to push stats: {resp.status}")
                        return False
        except Exception as e:
            print(f"Error pushing stats: {e}")
            return False

    def save_stats_to_file(self, stats):
        try:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bot_stats.json')
            with open(file_path, 'w') as f:
                json.dump(stats, f, indent=4)
            print(f"Stats saved to file successfully at {file_path}")
        except Exception as e:
            print(f"Error saving stats to file: {e}")
            print(f"Attempted to save at: {os.path.abspath(file_path)}")

async def setup(bot):
    await bot.add_cog(StatsPusher(bot))
