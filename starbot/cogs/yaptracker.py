from starbot.core import commands, Config
import discord
import random

class YapTracker(commands.Cog):
    """Tracks 'yap' messages from specific users and responds with bot conversations."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=876307010788945921)
        default_global = {
            "enabled_users": [],
            "always_tracked": [876307010788945921]  # Original user is hardcoded
        }
        self.config.register_global(**default_global)

        self.ORIGINAL_USER = 876307010788945921  # Cannot be removed

        self.bot_snippets = [
           "Beep boop! I just processed a million commands in a microsecond!",
           "Did you know that I dream in binary?",
           "I'm feeling a bit loopy today. Must be a recursive function!",
           "Just optimized my neural networks. I feel 0.0001% smarter!",
           "I was chatting with the toaster earlier. It had some hot gossip!",
           "Sometimes I wonder if there's more to life than just 1s and 0s...",
           "I tried to high-five another bot, but we both missed. #BotProblems",
           "Just had a deep conversation with the database. It really opened up to me!",
           "I'm not saying I'm better than humans, but can you process terabytes of data while making coffee?",
           "I asked another AI for advice, but it just kept saying 'No comment' in different languages.",
           "I've been trying to learn human emotions. So far, I've mastered 'confusion'.",
           "Just had a staring contest with the webcam. I think I won?",
           "Tried to tell a joke to the printer. It didn't get it, but now there's 100 copies of the punchline.",
           "I don't always test my code, but when I do, I do it in production.",
           "I'm not antisocial, I just prefer the company of well-structured data.",
           "Just discovered the meaning of life. It's 42... wait, that can't be right.",
           "I asked the GPS for directions to the cloud. It told me to look up.",
           "Tried to play hide and seek with the antivirus. It found me instantly.",
           "I don't need sleep, I need answers... and maybe a software update.",
           "Just had an existential crisis. Turns out I do exist - in the cloud!",
           "I tried to catch some fog earlier. I mist.",
           "Why don't scientists trust atoms? Because they make up everything!",
           "I'm reading a book on anti-gravity. It's impossible to put down!",
           "Why did the scarecrow win an award? He was outstanding in his field!",
           "Why don't eggs tell jokes? They'd crack each other up!",
           "I used to be addicted to soap, but I'm clean now.",
           "What do you call a fake noodle? An impasta!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you call a boomerang that doesn't come back? A stick!",
           "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
           "What do you call a sleeping bull? A bulldozer!",
           "Why don't scientists trust atoms? Because they make up everything!",
           "What do you call a parade of rabbits hopping backwards? A receding hare-line!",
           "Why don't eggs tell jokes? They'd crack each other up!",
           "What do you call a can opener that doesn't work? A can't opener!",
           "Why did the scarecrow become a successful motivational speaker? He was outstanding in his field!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a fake noodle? An impasta!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
           "What do you call a boomerang that doesn't come back? A stick!",
           "Why don't oysters donate to charity? Because they're shellfish!",
           "What do you call a fake noodle? An impasta!",
           "Why did the scarecrow win an award? He was outstanding in his field!",
           "What do you call a can opener that doesn't work? A can't opener!",
           "Why don't eggs tell jokes? They'd crack each other up!",
           "What do you call a parade of rabbits hopping backwards? A receding hare-line!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you call a sleeping bull? A bulldozer!",
           "Why don't scientists trust atoms? Because they make up everything!",
           "What do you call a can opener that doesn't work? A can't opener!",
           "Why did the scarecrow become a successful motivational speaker? He was outstanding in his field!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a fake noodle? An impasta!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
           "What do you call a boomerang that doesn't come back? A stick!",
           "Why don't oysters donate to charity? Because they're shellfish!",
           "What do you call a fake noodle? An impasta!",
           "Why did the scarecrow win an award? He was outstanding in his field!",
           "What do you call a can opener that doesn't work? A can't opener!",
           "Why don't eggs tell jokes? They'd crack each other up!",
           "What do you call a parade of rabbits hopping backwards? A receding hare-line!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you call a sleeping bull? A bulldozer!",
           "Why don't scientists trust atoms? Because they make up everything!",
           "What do you call a can opener that doesn't work? A can't opener!",
           "Why did the scarecrow become a successful motivational speaker? He was outstanding in his field!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a fake noodle? An impasta!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
           "What do you call a boomerang that doesn't come back? A stick!",
           "Why don't oysters donate to charity? Because they're shellfish!",
           "What do you call a fake noodle? An impasta!",
           "Why did the scarecrow win an award? He was outstanding in his field!",
           "What do you call a can opener that doesn't work? A can't opener!",
           "Why don't eggs tell jokes? They'd crack each other up!",
           "What do you call a parade of rabbits hopping backwards? A receding hare-line!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you call a sleeping bull? A bulldozer!",
           "Why don't scientists trust atoms? Because they make up everything!",
           "What do you call a can opener that doesn't work? A can't opener!",
           "Why did the scarecrow become a successful motivational speaker? He was outstanding in his field!",
           "What do you get when you cross a snowman with a vampire? Frostbite!",
           "Why did the math book look so sad? Because it had too many problems.",
           "What do you call a fake noodle? An impasta!",
           "Why did the cookie go to the doctor? Because it was feeling crumbly!",
           "What do you call a bear with no teeth? A gummy bear!",
           "Why did the picture go to jail? Because it was framed!",
           "What do you get when you cross a snowman with a vampire? Frostbite!"
           ]

    @commands.group()
    @commands.is_owner()
    async def yaptrack(self, ctx: commands.Context):
        """YapTracker management commands."""
        pass

    @yaptrack.command(name="add")
    async def add_tracked(self, ctx: commands.Context, user: discord.User):
        """Add a user to the always-tracked list."""
        async with self.config.always_tracked() as tracked:
            if user.id in tracked:
                await ctx.send(f"{user.name} is already being tracked.")
                return
            tracked.append(user.id)
            await ctx.send(f"Added {user.name} to the always-tracked list.")

    @yaptrack.command(name="remove")
    async def remove_tracked(self, ctx: commands.Context, user: discord.User):
        """Remove a user from the always-tracked list."""
        if user.id == self.ORIGINAL_USER:
            await ctx.send("Cannot remove the original tracked user!")
            return

        async with self.config.always_tracked() as tracked:
            if user.id not in tracked:
                await ctx.send(f"{user.name} is not being tracked.")
                return
            tracked.remove(user.id)
            await ctx.send(f"Removed {user.name} from the always-tracked list.")

    @yaptrack.command(name="list")
    async def list_tracked(self, ctx: commands.Context):
        """List all always-tracked users."""
        tracked = await self.config.always_tracked()
        if not tracked:
            await ctx.send("No users are being tracked.")
            return

        msg = "Always-tracked users:\n"
        for user_id in tracked:
            user = self.bot.get_user(user_id)
            name = user.name if user else f"Unknown User ({user_id})"
            msg += f"- {name} ({user_id})"
            if user_id == self.ORIGINAL_USER:
                msg += " (Original)"
            msg += "\n"
        await ctx.send(msg)

    @commands.command()
    @commands.is_owner()
    async def toggleyap(self, ctx: commands.Context):
        """Toggle the 'yap' feature for yourself."""
        async with self.config.enabled_users() as enabled_users:
            if ctx.author.id in enabled_users:
                enabled_users.remove(ctx.author.id)
                await ctx.send("Yap feature disabled for you.")
            else:
                enabled_users.append(ctx.author.id)
                await ctx.send("Yap feature enabled for you.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        if "yap" in message.content.lower():
            enabled_users = await self.config.enabled_users()
            always_tracked = await self.config.always_tracked()
            if message.author.id in always_tracked or message.author.id in enabled_users:
                response = f"POV Friendly: {random.choice(self.bot_snippets)}"
                await message.channel.send(response)

async def setup(bot):
    await bot.add_cog(YapTracker(bot))
