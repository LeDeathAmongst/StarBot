import discord
from starbot.core import commands, Config
from datetime import datetime
import sqlite3
import asyncio
from Star-Utils import Cog, CogsUtils

class MentionTracker(Cog):
    """Tracks and displays mentions a user has received."""
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=323046932922879151042652259913293516239, force_registration=True)
        self.db_path = "mention_tracker.db"
        self.init_db()
        self.logs = CogsUtils.get_logger(cog=self)

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS mentions
                     (user_id INTEGER, content TEXT, jump_url TEXT, author TEXT, time_unix INTEGER)''')
        conn.commit()
        conn.close()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        mentions = message.mentions
        if not mentions:
            return

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        current_time_unix = int(datetime.utcnow().timestamp())

        for mention in mentions:
            mention_data = (
                mention.id,
                message.content,
                message.jump_url,
                message.author.display_name,
                current_time_unix
            )
            c.execute("INSERT INTO mentions VALUES (?, ?, ?, ?, ?)", mention_data)

        conn.commit()
        conn.close()

    @commands.group()
    async def pinged(self, ctx: commands.Context):
        """Manage snippets."""
        pass

    @commands.guild_only()
    @pinged.command(aliases=['mentions', 'mention'])
    async def who(self, ctx, limit: int = 10):
        """Display the last X mentions you have received (default 10, max 50)"""
        if limit > 50:
            limit = 50
        elif limit < 1:
            limit = 1

        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM mentions WHERE user_id=? ORDER BY time_unix DESC LIMIT ?", (ctx.author.id, limit))
        mention_list = c.fetchall()
        conn.close()

        if not mention_list:
            await ctx.send("No mentions tracked.")
            return

        embeds = []
        for i in range(0, len(mention_list), 5):
            embed = discord.Embed(title=f"Your last {limit} mentions", color=await ctx.embed_color())
            for mention_data in mention_list[i:i+5]:
                mention_content = f"Content: {mention_data[1]}\n[Jump to message]({mention_data[2]})"
                mention_content += f"\nTimestamp: <t:{mention_data[4]}:R>"
                embed.add_field(name=f"Mentioned by: {mention_data[3]}", value=mention_content, inline=False)
            embeds.append(embed)

        if len(embeds) == 1:
            await ctx.send(embed=embeds[0])
        else:
            await self.menu_pages(ctx, embeds)

    @commands.guild_only()
    @pinged.command()
    async def clear(self, ctx):
        """Clear all your tracked mentions"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("DELETE FROM mentions WHERE user_id=?", (ctx.author.id,))
        conn.commit()
        conn.close()
        await ctx.send("All your tracked mentions have been cleared.")

    @commands.guild_only()
    @pinged.command()
    async def stats(self, ctx):
        """Display mention statistics"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM mentions WHERE user_id=?", (ctx.author.id,))
        total_mentions = c.fetchone()[0]
        c.execute("SELECT author, COUNT(*) FROM mentions WHERE user_id=? GROUP BY author ORDER BY COUNT(*) DESC LIMIT 5", (ctx.author.id,))
        top_mentioners = c.fetchall()
        conn.close()

        embed = discord.Embed(title="Mention Statistics", color=await ctx.embed_color())
        embed.add_field(name="Total Mentions", value=str(total_mentions), inline=False)
        if top_mentioners:
            embed.add_field(name="Top Mentioners", value="\n".join([f"{author}: {count}" for author, count in top_mentioners]), inline=False)
        await ctx.send(embed=embed)

    async def menu_pages(self, ctx, embeds):
        def react_check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        current_page = 0
        msg = await ctx.send(embed=embeds[current_page])
        await msg.add_reaction("◀️")
        await msg.add_reaction("▶️")

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=react_check)
                if str(reaction.emoji) == "▶️" and current_page < len(embeds) - 1:
                    current_page += 1
                    await msg.edit(embed=embeds[current_page])
                    await msg.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "◀️" and current_page > 0:
                    current_page -= 1
                    await msg.edit(embed=embeds[current_page])
                    await msg.remove_reaction(reaction, user)
                else:
                    await msg.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await msg.clear_reactions()
                break
