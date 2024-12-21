from starbot.core import commands
from collections import deque, defaultdict
from Star-Utils import Cog, CogsUtils

class Repeater(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.enabled = True
        self.recent_messages = defaultdict(lambda: deque(maxlen=3))

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        if message.author.bot:
            return
        
        words = message.content.split()
        if len(words) != 1:
            return
        
        word = words[0].lower()  # Convert to lowercase for case-insensitive comparison
        channel = message.channel

        self.recent_messages[channel].append(word)

        # Check if the last three messages in the channel contain the same word and no other words
        if len(self.recent_messages[channel]) == 3:
            repeated_word = self.recent_messages[channel][0]  # Get the word from the first message
            if all(msg.lower() == repeated_word for msg in self.recent_messages[channel]) and all(len(msg.split()) == 1 for msg in self.recent_messages[channel]):
                await channel.send(f"{repeated_word}")
                self.recent_messages[channel].clear()  # Clear the recent messages for the channel