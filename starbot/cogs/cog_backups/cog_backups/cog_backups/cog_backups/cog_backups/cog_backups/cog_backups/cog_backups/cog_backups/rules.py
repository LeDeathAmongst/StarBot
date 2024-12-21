import discord
from starbot.core import commands, Config
import sqlite3

class RuleManager(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        self.config.register_guild(rules_channel=None)
        self.db_path = "rules.db"
        self._create_db()

    def _create_db(self):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS rules (
                        guild_id INTEGER,
                        rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        rule_text TEXT)""")
            conn.commit()

    @commands.guild_only()
    @commands.command(name="addrule")
    async def add_rule(self, ctx, *, rule_text: str):
        """Add a rule to the server's rule list."""
        guild_id = ctx.guild.id
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO rules (guild_id, rule_text) VALUES (?, ?)", (guild_id, rule_text))
            conn.commit()

        await ctx.send(embed=discord.Embed(title="Rule Added", description=f"Rule added: {rule_text}", color=discord.Color.green()))
        await self.update_rules_channel(ctx.guild)

    @commands.guild_only()
    @commands.command(name="resetrules")
    @commands.has_permissions(administrator=True)
    async def reset_rules(self, ctx):
        """Reset all rules for the server."""
        guild_id = ctx.guild.id
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM rules WHERE guild_id = ?", (guild_id,))
            conn.commit()

        await ctx.send(embed=discord.Embed(title="Rules Reset", description="All rules have been reset.", color=discord.Color.red()))
        await self.update_rules_channel(ctx.guild)

    @commands.guild_only()
    @commands.command(name="removerule")
    async def remove_rule(self, ctx, rule_id: int):
        """Remove a rule by its ID."""
        guild_id = ctx.guild.id
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM rules WHERE guild_id = ? AND rule_id = ?", (guild_id, rule_id))
            conn.commit()

        await ctx.send(embed=discord.Embed(title="Rule Removed", description=f"Rule with ID {rule_id} has been removed.", color=discord.Color.red()))
        await self.update_rules_channel(ctx.guild)

    @commands.guild_only()
    @commands.command(name="editrule")
    async def edit_rule(self, ctx, rule_id: int, *, new_text: str):
        """Edit a rule by its ID."""
        guild_id = ctx.guild.id
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("UPDATE rules SET rule_text = ? WHERE guild_id = ? AND rule_id = ?", (new_text, guild_id, rule_id))
            conn.commit()

        await ctx.send(embed=discord.Embed(title="Rule Edited", description=f"Rule with ID {rule_id} has been updated.", color=discord.Color.green()))
        await self.update_rules_channel(ctx.guild)

    @commands.guild_only()
    @commands.command(name="showrules")
    async def show_rules(self, ctx):
        """Show all rules for the server."""
        guild_id = ctx.guild.id
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT rule_id, rule_text FROM rules WHERE guild_id = ?", (guild_id,))
            rules = c.fetchall()

        if not rules:
            await ctx.send(embed=discord.Embed(title="No Rules", description="No rules have been set for this server.", color=discord.Color.orange()))
        else:
            embed = discord.Embed(title="Server Rules", color=discord.Color.blue())
            for rule_id, rule_text in rules:
                embed.add_field(name=f"Rule {rule_id}", value=rule_text, inline=False)
            await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command(name="postrules")
    @commands.has_permissions(administrator=True)
    async def post_rules(self, ctx, channel: discord.TextChannel):
        """Post the rules to a specific channel and set it for dynamic updates."""
        await self.config.guild(ctx.guild).rules_channel.set(channel.id)
        await self.update_rules_channel(ctx.guild)
        await ctx.send(embed=discord.Embed(title="Rules Channel Set", description=f"Rules will now be posted in {channel.mention}.", color=discord.Color.green()))

    async def update_rules_channel(self, guild: discord.Guild):
        rules_channel_id = await self.config.guild(guild).rules_channel()
        if rules_channel_id:
            channel = guild.get_channel(rules_channel_id)
            if channel:
                await channel.purge()
                guild_id = guild.id
                with sqlite3.connect(self.db_path) as conn:
                    c = conn.cursor()
                    c.execute("SELECT rule_id, rule_text FROM rules WHERE guild_id = ?", (guild_id,))
                    rules = c.fetchall()

                if rules:
                    embed = discord.Embed(title="Server Rules", color=discord.Color.blue())
                    for rule_id, rule_text in rules:
                        embed.add_field(name=f"Rule {rule_id}", value=rule_text, inline=False)
                    await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RuleManager(bot))
