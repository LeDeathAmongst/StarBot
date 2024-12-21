import discord
from starbot.core import commands, Config
from starbot.core.bot import Red
import sqlite3
import os
from datetime import datetime
from Star_Utils import Cog, CogsUtils

class BlacklistCentral(commands.Cog):
    """A cog for storing blacklist data."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_global(authorized_users=[])

        self.lists = ['difficult', 'n_r', 'nsfw', 'abusive', 's_u_s']
        self.databases = {}
        self.cursors = {}
        self.setup_databases()
        self.logs = CogsUtils.get_logger("BlacklistCentral")
    def setup_databases(self):
        for list_name in self.lists:
            db_path = f"data/blacklistcentral/{list_name}.db"
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
            self.databases[list_name] = sqlite3.connect(db_path)
            self.cursors[list_name] = self.databases[list_name].cursor()
            self.setup_table(list_name)

    def setup_table(self, list_name):
        self.cursors[list_name].execute('''CREATE TABLE IF NOT EXISTS blacklisted_users
                                          (user_id INTEGER PRIMARY KEY,
                                           username TEXT,
                                           link TEXT,
                                           reason TEXT,
                                           extra TEXT,
                                           added_at TIMESTAMP)''')
        self.databases[list_name].commit()

    @commands.group(name="blcentral", aliases=["blc"])
    async def blcentral(self, ctx: commands.Context):
        """Manage the blacklist central."""
        pass

    @blcentral.command(name="add")
    async def add(self, ctx: commands.Context, list_name: str, user_id: int, username: str, link: str, reason: str, *, extra: str = "None"):
        """Add a user to a specific blacklist."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Available lists: {', '.join(self.lists)}")
            return

        cursor = self.cursors[list_name]
        cursor.execute("INSERT OR REPLACE INTO blacklisted_users (user_id, username, link, reason, extra, added_at) VALUES (?, ?, ?, ?, ?, ?)",
                        (user_id, username, link, reason, extra, datetime.utcnow()))
        self.databases[list_name].commit()

        await ctx.send(f"User {username} (ID: {user_id}) has been added to the {list_name} list.")

    @blcentral.command(name="remove")
    async def remove(self, ctx: commands.Context, list_name: str, user_id: int):
        """Remove a user from a specific blacklist."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Available lists: {', '.join(self.lists)}")
            return

        cursor = self.cursors[list_name]
        cursor.execute("DELETE FROM blacklisted_users WHERE user_id = ?", (user_id,))
        self.databases[list_name].commit()

        await ctx.send(f"User with ID {user_id} has been removed from the {list_name} list.")

    @blcentral.command(name="list")
    async def list(self, ctx: commands.Context, list_name: str = None):
        """List all users in a specific blacklist or show available lists."""
        if not await self.is_authorized(ctx.author):
            await ctx.send("You are not authorized to use this command.")
            return

        if list_name is None:
            await ctx.send(f"Available lists: {', '.join(self.lists)}")
            return

        if list_name not in self.lists:
            await ctx.send(f"The list '{list_name}' does not exist. Available lists: {', '.join(self.lists)}")
            return

        cursor = self.cursors[list_name]
        cursor.execute("SELECT user_id, username, link, reason, extra, added_at FROM blacklisted_users ORDER BY added_at DESC")
        users = cursor.fetchall()

        if not users:
            await ctx.send(f"No users found in the {list_name} list.")
            return

        message = f"Users in {list_name} list:\n\n"
        for user in users:
            message += f"User ID: {user[0]}, Username: {user[1]}\nLink: {user[2]}\nReason: {user[3]}\nExtra: {user[4]}\nAdded at: {user[5]}\n\n"

        for chunk in [message[i:i+1900] for i in range(0, len(message), 1900)]:
            await ctx.send(chunk)

    @commands.group(name="blcadmin", aliases=["blca"])
    @commands.is_owner()
    async def blcadmin(self, ctx: commands.Context):
        """Admin commands for BlacklistCentral."""
        pass

    @blcadmin.command(name="addauth")
    async def add_authorized(self, ctx: commands.Context, user: discord.User):
        """Add a user to the list of authorized users."""
        async with self.config.authorized_users() as auth_users:
            if user.id not in auth_users:
                auth_users.append(user.id)
                await ctx.send(f"{user.name} has been added to the list of authorized users.")
            else:
                await ctx.send(f"{user.name} is already an authorized user.")

    @blcadmin.command(name="removeauth")
    async def remove_authorized(self, ctx: commands.Context, user: discord.User):
        """Remove a user from the list of authorized users."""
        async with self.config.authorized_users() as auth_users:
            if user.id in auth_users:
                auth_users.remove(user.id)
                await ctx.send(f"{user.name} has been removed from the list of authorized users.")
            else:
                await ctx.send(f"{user.name} is not an authorized user.")

    @blcadmin.command(name="listauth")
    async def list_authorized(self, ctx: commands.Context):
        """List all authorized users."""
        auth_users = await self.config.authorized_users()
        if not auth_users:
            await ctx.send("There are no authorized users.")
        else:
            user_list = []
            for user_id in auth_users:
                user = self.bot.get_user(user_id)
                user_list.append(f"{user.name} (ID: {user.id})" if user else f"Unknown User (ID: {user_id})")
            await ctx.send("Authorized users:\n" + "\n".join(user_list))

    async def is_authorized(self, user: discord.User) -> bool:
        """Check if a user is authorized to manage the blacklist."""
        authorized_users = await self.config.authorized_users()
        return user.id in authorized_users or await self.bot.is_owner(user)

    def cog_unload(self):
        for db in self.databases.values():
            db.close()

async def setup(bot):
    await bot.add_cog(BlacklistCentral(bot))
