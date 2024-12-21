from starbot.core import commands, Config
import discord
from datetime import datetime
from Star-Utils import Cog, CogsUtils
from discord.ext import tasks

class ThemedChanger(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)

        # Define default themes with nicknames and avatar URLs
        default_themes = {
            "New Year": {
                "nickname": "Happy New Year!",
                "avatar": "https://example.com/newyear_avatar.png"  # Replace with actual URL
            },
            "Valentine's Day": {
                "nickname": "Love is in the air!",
                "avatar": "https://example.com/valentine_avatar.png"
            },
            "St. Patrick's Day": {
                "nickname": "Feeling Lucky!",
                "avatar": "https://example.com/stpat_avatar.png"
            },
            "Fourth of July": {
                "nickname": "Happy Independence Day!",
                "avatar": "https://example.com/fourthofjuly_avatar.png"
            },
            "Halloween": {
                "nickname": "Spooky Bot!",
                "avatar": "https://example.com/halloween_avatar.png"
            },
            "Thanksgiving": {
                "nickname": "Thankful Bot!",
                "avatar": "https://example.com/thanksgiving_avatar.png"
            },
            "Christmas": {
                "nickname": "Merry Christmas!",
                "avatar": "https://example.com/christmas_avatar.png"
            },
            "Test": {
                "nickname": "Starfire Testing",
                "avatar": "http://195.58.58.45:5001/static/avatars/1275521742961508432/2024-10-12_14-10-41.uonkqymtzg.png"
            },
        }

        self.config.register_global(themes=default_themes)
        self.config.register_global(default_nickname=self.bot.user.name)  # Default nickname
        self.config.register_global(default_avatar="http://195.58.58.45:5001/static/avatars/1275521742961508432/2024-10-12_14-20-52.ihncvlixcv.png")  # Default avatar URL

        # Start the theme changer loop
        self.change_theme.start()

    def cog_unload(self):
        self.change_theme.stop()

    @tasks.loop(hours=1)  # Check every hour
    async def change_theme(self):
        current_theme = self.get_current_theme()
        if current_theme:
            await self.update_bot_theme(current_theme)
        else:
            await self.reset_bot_theme()  # Reset to default if no current theme

    def get_current_theme(self):
        """Determine the current theme based on the date."""
        now = datetime.now()

        # Example logic for determining the theme based on the date
        if now.month == 1 and now.day <= 5:  # New Year theme
            return "New Year"
        elif now.month == 2 and now.day == 14:  # Valentine's Day theme
            return "Valentine's Day"
        elif now.month == 3 and now.day == 17:  # St. Patrick's Day theme
            return "St. Patrick's Day"
        elif now.month == 7 and now.day == 4:  # Fourth of July theme
            return "Fourth of July"
        elif now.month == 10 and now.day == 31:  # Halloween theme
            return "Halloween"
        elif now.month == 11 and now.day == 4:  # Thanksgiving (4th Thursday of November)
            if now.weekday() == 3 and (22 <= now.day <= 28):  # Make sure it's the right week
                return "Thanksgiving"
        elif now.month == 12:  # Christmas theme
            return "Christmas"
        elif now.month == 10 and now.day == 
            return "Test"

        return None  # No theme matches

    async def update_bot_theme(self, theme_name):
        """Update the bot's nickname and avatar based on the current theme."""
        themes = await self.config.themes()
        theme = themes.get(theme_name)

        if theme:
            nickname = theme.get("nickname")
            avatar_url = theme.get("avatar")

            # Change nickname
            try:
                await self.bot.user.edit(nick=nickname)
                print(f"Nickname changed to '{nickname}'")
            except discord.Forbidden:
                print(f"Failed to change nickname to '{nickname}': Missing permissions.")

            # Change avatar
            try:
                if avatar_url:
                    async with self.bot.session.get(avatar_url) as response:
                        if response.status == 200:
                            avatar_data = await response.read()
                            await self.bot.user.edit(avatar=avatar_data)
                            print("Avatar updated.")
            except discord.Forbidden:
                print("Failed to change avatar: Missing permissions.")
            except Exception as e:
                print(f"Error updating avatar: {e}")

    async def reset_bot_theme(self):
        """Reset the bot's nickname and avatar to default values."""
        default_nickname = await self.config.default_nickname()
        default_avatar = await self.config.default_avatar()

        # Change nickname to default
        try:
            await self.bot.user.edit(nick=default_nickname)
            print(f"Nickname reset to '{default_nickname}'")
        except discord.Forbidden:
            print(f"Failed to reset nickname to '{default_nickname}': Missing permissions.")

        # Change avatar to default
        try:
            if default_avatar:
                async with self.bot.session.get(default_avatar) as response:
                    if response.status == 200:
                        avatar_data = await response.read()
                        await self.bot.user.edit(avatar=avatar_data)
                        print("Avatar reset to default.")
        except discord.Forbidden:
            print("Failed to reset avatar: Missing permissions.")
        except Exception as e:
            print(f"Error resetting avatar: {e}")

    @commands.command()
    @commands.is_owner()
    async def settheme(self, ctx, holiday: str, nickname: str, avatar_url: str):
        """Set the nickname and avatar for a specific holiday."""
        themes = await self.config.themes()

        if holiday in themes:
            themes[holiday]["nickname"] = nickname
            themes[holiday]["avatar"] = avatar_url
            await self.config.themes.set(themes)
            await ctx.send(f"Updated {holiday} theme: Nickname set to '{nickname}' and avatar updated.")
        else:
            await ctx.send(f"Holiday '{holiday}' not found. Available holidays: {', '.join(themes.keys())}")

    @commands.command()
    @commands.is_owner()
    async def set_default(self, ctx, nickname: str, avatar_url: str):
        """Set the default nickname and avatar for the bot."""
        await self.config.default_nickname.set(nickname)
        await self.config.default_avatar.set(avatar_url)
        await ctx.send(f"Default nickname set to '{nickname}' and default avatar updated.")

async def setup(bot):
    await bot.add_cog(ThemedChanger(bot))
