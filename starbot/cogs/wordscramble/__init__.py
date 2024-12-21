from .wordscramble import WordScramble

async def setup(bot):
    await bot.add_cog(WordScramble(bot))
