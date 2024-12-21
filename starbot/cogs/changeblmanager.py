import discord
import json
import asyncio
from datetime import datetime
from pathlib import Path
from starbot.core import commands, checks
from starbot.core.bot import Red
from starbot.core.data_manager import cog_data_path

class BotListManager(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot
        self.data_path = cog_data_path(self)
        self.changelogs_file = self.data_path / "changelogs.json"
        self.botlist_file = self.data_path / "botlist.json"
        self.ensure_data_files()
        self.changelog_message_id = None
        self.changelog_channel_id = None  # You'll need to set this to your desired channel ID
        self.bot.loop.create_task(self.update_changelog_loop())

    def ensure_data_files(self):
        self.data_path.mkdir(parents=True, exist_ok=True)
        if not self.changelogs_file.exists():
            with open(self.changelogs_file, 'w') as f:
                json.dump([], f)
        if not self.botlist_file.exists():
            with open(self.botlist_file, 'w') as f:
                json.dump([], f)

    def save_changelogs(self, changelogs):
        with open(self.changelogs_file, 'w') as f:
            json.dump(changelogs, f, indent=2)

    def load_changelogs(self):
        with open(self.changelogs_file, 'r') as f:
            return json.load(f)

    def save_botlist(self, botlist):
        with open(self.botlist_file, 'w') as f:
            json.dump(botlist, f, indent=2)

    def load_botlist(self):
        with open(self.botlist_file, 'r') as f:
            return json.load(f)

    @commands.group()
    @checks.is_owner()
    async def changelog(self, ctx):
        """Manage changelogs"""
        pass

    @changelog.command(name="set")
    async def set_dynamic_changelog(self, ctx):
        """Set the current channel for the dynamic changelog"""
        self.changelog_channel_id = ctx.channel.id
        await ctx.send(f"Dynamic changelog will be updated in this channel.")
        await self.update_dynamic_changelog()

    async def update_dynamic_changelog(self):
        if not self.changelog_channel_id:
            return

        channel = self.bot.get_channel(self.changelog_channel_id)
        if not channel:
            return

        changelogs = self.load_changelogs()
        if not changelogs:
            content = "No changelog entries found."
        else:
            embeds = self.create_changelog_embeds(changelogs)

            if self.changelog_message_id:
                try:
                    message = await channel.fetch_message(self.changelog_message_id)
                    await message.edit(content=None, embeds=embeds)
                    return
                except discord.NotFound:
                    pass  # Message was deleted, we'll send a new one

            message = await channel.send(embeds=embeds)
            self.changelog_message_id = message.id

    def create_changelog_embeds(self, changelogs):
        embeds = []
        current_embed = discord.Embed(title="Changelogs", color=discord.Color.blue())
        field_count = 0

        for log in changelogs:
            version = log['version']
            date = log['date']
            changes = "\n".join(f"• {change}" for change in log['changes'])

            field_value = f"**Date:** {date}\n**Changes:**\n{changes}"

            if field_count >= 25:
                embeds.append(current_embed)
                current_embed = discord.Embed(title="Changelogs (Continued)", color=discord.Color.blue())
                field_count = 0

            current_embed.add_field(name=version, value=field_value, inline=False)
            field_count += 1

        if current_embed.fields:
            embeds.append(current_embed)

        return embeds

    async def update_changelog_loop(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            await self.update_dynamic_changelog()
            await asyncio.sleep(300)  # Update every 5 minutes

    @changelog.command(name="add")
    async def changelog_add(self, ctx, version: str, *, changes: str):
        """Add a new changelog entry"""
        changes_list = [change.strip() for change in changes.split(',')]
        new_entry = {
            "version": version,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "changes": changes_list
        }

        await ctx.send(f"Preview of the changelog:\n```json\n{json.dumps(new_entry, indent=2)}\n```\nDo you want to add this? (yes/no)")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["yes", "no"]

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            return await ctx.send("Timed out. Changelog not added.")

        if msg.content.lower() == "yes":
            changelogs = self.load_changelogs()
            changelogs.append(new_entry)
            self.save_changelogs(changelogs)
            await ctx.send("Changelog added successfully.")
        else:
            await ctx.send("Changelog not added.")

        # After adding the changelog
        await self.update_dynamic_changelog()
        await ctx.send("Changelog added and dynamic message updated.")

    @changelog.command(name="remove")
    async def changelog_remove(self, ctx, version: str):
        """Remove a changelog entry by version"""
        changelogs = self.load_changelogs()
        initial_length = len(changelogs)
        changelogs = [log for log in changelogs if log["version"] != version]
        removed_count = initial_length - len(changelogs)

        if removed_count > 0:
            self.save_changelogs(changelogs)
            await ctx.send(f"Removed changelog entry for version {version}.")
        else:
            await ctx.send(f"No changelog entry found for version {version}.")

    @changelog.command(name="list")
    async def changelog_list(self, ctx):
        """List all changelog entries"""
        changelogs = self.load_changelogs()
        if not changelogs:
            await ctx.send("No changelog entries found.")
            return

        embeds = []
        current_embed = discord.Embed(title="Changelogs", color=discord.Color.blue())
        field_count = 0

        for log in changelogs:
            version = log['version']
            date = log['date']
            changes = "\n".join(f"• {change}" for change in log['changes'])

            field_value = f"**Date:** {date}\n**Changes:**\n{changes}"

            if field_count >= 25:
                embeds.append(current_embed)
                current_embed = discord.Embed(title="Changelogs (Continued)", color=discord.Color.blue())
                field_count = 0

            current_embed.add_field(name=version, value=field_value, inline=False)
            field_count += 1

        if current_embed.fields:
            embeds.append(current_embed)

        for embed in embeds:
            await ctx.send(embed=embed)

    @commands.group()
    @checks.is_owner()
    async def botlists(self, ctx):
        """Manage changelogs"""
        pass

    @botlists.command(aliases=["+"])
    async def add(self, ctx, name: str, site: str, link: str):
        """Add a new bot list entry"""
        entry = {"name": name, "site": site, "link": link}
        botlist = self.load_botlist()
        botlist.append(entry)
        self.save_botlist(botlist)
        await ctx.send("Bot list entry added successfully.")

    @botlists.command(aliases=["-"])
    async def remove(self, ctx, *, name: str):
        """Remove a bot list entry by name"""
        botlist = self.load_botlist()
        initial_length = len(botlist)
        botlist = [entry for entry in botlist if entry["name"].lower() != name.lower()]
        removed_count = initial_length - len(botlist)

        if removed_count > 0:
            self.save_botlist(botlist)
            await ctx.send(f"Removed {removed_count} bot list entry(ies) with the name '{name}'.")
        else:
            await ctx.send(f"No bot list entries found with the name '{name}'.")

    @botlists.command()
    async def list(self, ctx):
        """List all bot list entries"""
        botlist = self.load_botlist()
        if not botlist:
            await ctx.send("No bot list entries found.")
            return

        message = json.dumps(botlist, indent=2)
        for page in [message[i:i+1990] for i in range(0, len(message), 1990)]:
            await ctx.send(f"```json\n{page}\n```")

async def setup(bot: Red):
    bot_list_manager = BotListManager(bot)
    await bot.add_cog(bot_list_manager)
