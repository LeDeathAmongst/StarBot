from .emojiinfo import EmojiInfo


async def setup(bot):
    await bot.add_cog(EmojiInfo(bot))
