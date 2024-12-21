import discord
from starbot.core import commands
from starbot.core import Config
from starbot.core import bank
import random
import aiohttp
import asyncio
from datetime import datetime, timedelta
from Star-Utils import Cog, CogsUtils

class WordScramble(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=123456578438267890, force_registration=True)

        default_settings = {
            "base_amount": 100,
            "time_limits": {}  # Store time limits for guilds
        }
        self.config.register_global(**default_settings)

        self.api_url = 'https://random-word-api.herokuapp.com/word'
        self.games_in_progress = {}
        self.time_messages = {}
        self.tasks = {}

    @commands.group()
    async def wordscrambleset(self, ctx):
        """Set options for Word Scramble"""

    @wordscrambleset.command()
    async def timelimit(self, ctx, seconds: int):
        """Set the time limit for Word Scramble games in this guild."""
        if seconds <= 0:
            await ctx.send("Time limit must be greater than 0 seconds.")
            return
        async with self.config.time_limits() as time_limits:
            time_limits[ctx.guild.id] = seconds
        await ctx.send(f"Time limit set to {seconds} seconds for Word Scramble games in this guild.")

    @wordscrambleset.command()
    async def baseamount(self, ctx, amount: int):
        """Set the base amount of credits received per unscrambled word, this amount gets multiplied by the amount of letters in the scrambled word."""
        if amount <= 0:
            await ctx.send("Base amount must be greater than 0.")
            return
        await self.config.base_amount.set(amount)
        await ctx.send(f"Base amount set to {amount} credits per unscrambled word.")

    @commands.command()
    async def wordscramble(self, ctx, length: int = None):
        """Start a game of WordScramble"""
        try:
            if ctx.guild.id in self.games_in_progress:
                await ctx.send("A game is already in progress in this guild. Please wait for it to finish.")
                return

            self.games_in_progress[ctx.guild.id] = True

            if length is None:
                length = random.randint(4, 7)
            elif length < 3 or length > 12:
                await ctx.send("Word length must be between 3 and 12.")
                del self.games_in_progress[ctx.guild.id]
                return
            
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{self.api_url}?length={length}') as response:
                    if response.status == 200:
                        data = await response.json()
                        word = random.choice(data)
                        scrambled_word = ''.join(random.sample(word, len(word)))
                        scramble_msg = await ctx.send(f"Unscramble the word: `{scrambled_word}`")

                        base_amount = await self.config.base_amount()
                        time_limits = await self.config.time_limits()

                        time_limit = time_limits.get(ctx.guild.id, 120)  # Default to 2 minutes if not set
                        end_time = datetime.utcnow() + timedelta(seconds=time_limit)
                        end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
                        time_msg = await ctx.send(f"You have until <t:{int(end_time.timestamp())}:R> to guess the word!")
                        self.time_messages[ctx.guild.id] = time_msg

                        def check(msg):
                            return msg.guild == ctx.guild  # Allow any message in the guild

                        while datetime.utcnow() < end_time:
                            try:
                                answer = await self.bot.wait_for('message', check=check, timeout=5.0)
                                if answer.content.lower() == word.lower():
                                    currency = await bank.get_currency_name(ctx.guild)
                                    credits_won = len(word) * base_amount
                                    await self.reward_player(ctx.author, credits_won)
                                    await ctx.send(f"Congratulations {answer.author.mention}! You've unscrambled the word `{word}` correctly and won {credits_won} {currency}!")
                                    del self.games_in_progress[ctx.guild.id]
                                    return
                            except asyncio.TimeoutError:
                                pass

                        await ctx.send(f"Time's up! The word was: `{word}`")
                        await self.time_messages[ctx.guild.id].delete()
                        del self.time_messages[ctx.guild.id]
                        del self.games_in_progress[ctx.guild.id]
                    else:
                        await ctx.send("Failed to fetch word from the API.")
                        del self.games_in_progress[ctx.guild.id]
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")
            del self.games_in_progress[ctx.guild.id]

    async def reward_player(self, member, amount):
        try:
            await bank.deposit_credits(member, amount)
        except (ValueError, TypeError) as e:
            print(f"Failed to deposit credits: {e}")

    async def on_cog_unload(self):
        for task in self.tasks.values():
            task.cancel()

        for guild_id in self.games_in_progress.keys():
            del self.games_in_progress[guild_id]
            del self.time_messages[guild_id]
