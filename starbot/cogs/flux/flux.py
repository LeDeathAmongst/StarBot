import io
import re
import random
from typing import Final, List, Optional
import aiohttp
import discord
from starbot.core import commands
from starbot.core.bot import Red
from starbot.core.utils.views import SetApiView
from Star_Utils import Cog

class DiffusionError(discord.errors.DiscordException):
    pass

class fluximggen(Cog):
    def __init__(self, bot: Red) -> None:
        self.bot: Red = bot
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.model_mapping = {
            "base": "flux",
            "realism": "flux-realism",
            "3d": "flux-3d",
            "anime": "flux-anime",
            "disney": "flux-disney",
            "pixel": "flux-pixel",
            "4o": "flux-4o",
            "anydark": "any-dark"
        }
        self.tokens = None  # Initialize tokens as None

    async def initialize_tokens(self):
        self.tokens = await self.bot.get_shared_api_tokens("flux")
        if not self.tokens.get("model") or not self.tokens.get("size") or not self.tokens.get("endpoint"):
            raise DiffusionError("Setup not done. Use `set api flux model <default_model>`, `set api flux size <default_size>`, and `set api endpoint <baseUrl for api>`.")

    async def cog_load(self) -> None:
        try:
            await self.initialize_tokens()
        except DiffusionError as e:
            # Log the error or take other actions if needed
            pass

    async def cog_unload(self) -> None:
        if self.session:
            await self.session.close()

    async def _request(self, baseUrl: str, prompt: str, model: str, size: Optional[str], seed: int) -> bytes:
        sizeParam = "16:9"
        if size is not None:
            sizeParam = size
        url = f"{baseUrl}?prompt={prompt}&model={model}&size={sizeParam}&seed={seed}"
        async with self.session.get(url) as response:
            content = await response.read()

            if response.status != 200:
                raise DiffusionError(f"Error?: {response.status}")
            if content.startswith(b"NSFW detected"):
                raise DiffusionError("NSFW")

            return content

    async def _generate_image(self, prompt: str, model: Optional[str], size: Optional[str], seed: int) -> bytes:
        default_model = self.tokens["model"]
        default_size = self.tokens["size"]
        baseUrl = self.tokens["endpoint"]

        size = size or default_size
        model = model or default_model
        if model.lower() not in self.model_mapping:
            raise DiffusionError(f"Model `{model}` does not exist.")
        model = self.model_mapping.get(model.lower(), model)
        return await self._request(baseUrl, prompt, model, size, seed)

    async def _image_to_file(self, image_data: bytes, prompt: str) -> discord.File:
        return discord.File(
            io.BytesIO(image_data),
            filename=f"{prompt.replace(' ', '_')}.png"
        )

    @commands.hybrid_command(name="flux", aliases=["f"])
    async def _gen(self, ctx: commands.Context, *, args: str) -> None:
        """Generate Images using Flux!

        **Examples:**
        - `[p]flux cyberpunk cat`
        - `[p]f kermit --model=realism`

        **Arguments:**
        - `<prompt>` - A detailed description of the image you want to create.
        - `--model` - Choose the specific model to use for image generation.
        - `--size` - Aspect Ratio for the generated image.
        - `--seed` - Specific seed value for randomization.

        **Models:**
        - `base` - Base flux model.
        - `realism` - Flux model with a LORa fine tuned for realism.
        - `3d` - Flux model with a LORa fine tuned for 3d images.
        - `anime` - Flux model with a LORa fine tuned for anime.
        - `disney` - Flux model with a LORa fine tuned for disney.
        """
        await ctx.typing()

        # Check if tokens are initialized
        if not self.tokens or not self.tokens.get("model") or not self.tokens.get("size") or not self.tokens.get("endpoint"):
            await ctx.send(
                "Setup not done. Please configure the API settings using the following commands:\n"
                "`set api flux model <default_model>`\n"
                "`set api flux size <default_size>`\n"
                "`set api endpoint <baseUrl for api>`"
            )
            return

        args_list = args.split(" ")
        model = None
        size = None
        seed = random.randint(1, 100000)
        prompt_parts = []

        for arg in args_list:
            if arg.startswith("--model="):
                model = arg.split("=")[1]
            elif arg.startswith("--size="):
                size = arg.split("=")[1]
                if not re.match(r"^\d+:\d+$", size):
                    await ctx.send("Invalid size value. Please provide a valid aspect ratio in the format 'width:height' (e.g., '16:9').")
                    return
            elif arg.startswith("--seed="):
                seed = int(arg.split("=")[1])
            else:
                prompt_parts.append(arg)

        prompt = " ".join(prompt_parts)

        try:
            image_data = await self._generate_image(prompt, model, size, seed)
        except DiffusionError as e:
            await ctx.send(
                f"Something went wrong...\n{e}",
                reference=ctx.message.to_reference(fail_if_not_exists=False),
                allowed_mentions=discord.AllowedMentions(replied_user=False),
            )
            return
        except aiohttp.ClientResponseError as e:
            await ctx.send(
                f"Error?: `{e.status}`\n{e.message}",
                reference=ctx.message.to_reference(fail_if_not_exists=False),
                allowed_mentions=discord.AllowedMentions(replied_user=False),
            )
            return
        file: discord.File = await self._image_to_file(image_data, prompt)
        await ctx.send(
            embed=discord.Embed(
                description=f"Prompt: {prompt}; Model: {model if model else self.tokens.get('model')}; Seed: {seed}",
                color=await ctx.embed_color(),
            ),
            file=file,
        )
