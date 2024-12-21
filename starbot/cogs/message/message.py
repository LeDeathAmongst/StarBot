import discord
from starbot.core import Config, commands, checks
from Star-Utils import Cog, CogsUtils

class Message(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command
    @commands.guild_only()
    @commands.mod()
    async def message(self, ctx, user: discord.User, embed: bool = True, *, message_content):
        """
        Send a message to a user via DM through the bot.
        Usage: [p]message <user (@user or user id)> <embed true/false> <message>
        """
        try:
            # Remove the invoking user's name from the message content
            message_content = message_content.replace(ctx.author.mention, '').strip()

            # Find the mentioned user (you can also use user IDs)
            if user:
                if embed:
                    # If embed=True, send the message as an embed
                    embed = discord.Embed(description=message_content, color=await ctx.embed_color())
                    await user.send(embed=embed)
                else:
                    # If embed=False, send the message as plain text
                    await user.send(message_content)

                await ctx.send(f"Message sent to {user.name} successfully.")
            else:
                await ctx.send("You need to mention a user to send a message to.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")