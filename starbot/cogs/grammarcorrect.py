from Star_Utils import Co, CogsUtils
import discord
from starbot.core import commands, Config
from better_profanity import profanity
import requests
import tempfile
import re
import difflib
from PIL import Image, ImageDraw, ImageFont

class GrammarCorrector(Cog):
    """Cog to correct a user's grammar and filter inappropriate content while maintaining the original style"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        # Initialize the profanity filter
        profanity.load_censor_words()

    def correct_grammar(self, text):
        url = "https://api.languagetool.org/v2/check"
        data = {
            'text': text,
            'language': 'en-US'
        }
        response = requests.post(url, data=data)
        result = response.json()
        matches = result['matches']

        corrected_text = text
        offset_correction = 0

        for match in matches:
            start = match['offset'] + offset_correction
            end = start + match['length']
            replacement = match['replacements'][0]['value'] if match['replacements'] else ''
            corrected_text = corrected_text[:start] + replacement + corrected_text[end:]
            offset_correction += len(replacement) - match['length']

        return corrected_text

    def contains_inappropriate_content(self, text):
        return profanity.contains_profanity(text)

    def filter_profanity(self, text):
        return profanity.censor(text)

    def generate_correction_summary(self, original_text, corrected_text):
        diff = difflib.ndiff(original_text.splitlines(), corrected_text.splitlines())
        corrections = [line for line in diff if line.startswith('- ') or line.startswith('+ ')]
        return corrections

    def generate_correction_image(self, corrections):
        # Create a blank image with black background
        font = ImageFont.load_default()
        max_width = 800
        padding = 10
        line_height = font.getbbox("A")[3] - font.getbbox("A")[1]
        image_height = (line_height + padding) * len(corrections) + padding

        image = Image.new('RGB', (max_width, image_height), color='black')
        draw = ImageDraw.Draw(image)

        y_text = padding
        for line in corrections:
            color = 'red' if line.startswith('- ') else 'green' if line.startswith('+ ') else 'white'
            draw.text((padding, y_text), line, font=font, fill=color)
            y_text += line_height + padding

        return image

    @commands.command()
    async def grammar(self, ctx, *, text: str):
        """Correct the grammar of the provided text and remove profanity while maintaining the original style."""
        if self.contains_inappropriate_content(text):
            text = self.filter_profanity(text)

        # Extract links and discord usernames and replace them with placeholders
        links = re.findall(r'(https?://\S+)', text)
        usernames = re.findall(r'(@\S+)', text)
        text_without_links_usernames = re.sub(r'(https?://\S+)', '<<LINK>>', text)
        text_without_links_usernames = re.sub(r'(@\S+)', '<<USER>>', text_without_links_usernames)

        # Correct grammar while maintaining the original formatting
        corrected_text = self.correct_grammar(text_without_links_usernames)

        # Reinsert links and usernames into the corrected text
        for link in links:
            corrected_text = corrected_text.replace('<<LINK>>', link, 1)
        for username in usernames:
            corrected_text = corrected_text.replace('<<USER>>', username, 1)

        # Generate correction summary
        corrections = self.generate_correction_summary(text, corrected_text)

        if corrections:
            # Generate correction image
            correction_image = self.generate_correction_image(corrections)

            # Save the image to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
                correction_image.save(temp_file, format='PNG')
                temp_file_path_image = temp_file.name

            # Send the correction image
            await ctx.send(file=discord.File(temp_file_path_image, filename="corrections.png"))

            # Clean up the temporary file
            temp_file.close()

            # Save the corrected text to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.txt') as temp_file:
                temp_file.write(corrected_text)
                temp_file_path_text = temp_file.name

            # Send the corrected text as a .txt file
            await ctx.send(file=discord.File(temp_file_path_text, filename="corrected_text.txt"))

            # Clean up the temporary file
            temp_file.close()
        else:
            await ctx.send(f"{ctx.author.mention}, your text does not require any corrections.")

async def setup(bot):
    await bot.add_cog(GrammarCorrector(bot))
