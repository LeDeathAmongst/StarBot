from Star_Utils import Cog, CogsUtils
import aiohttp
import discord
from starbot.core import commands, Config
from starbot.core.bot import Red
from starbot.core.utils.chat_formatting import box, humanize_list, pagify

class Zipline(Cog):
    """Cog to interact with Zipline's API."""

    def __init__(self, bot: Red):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.config = Config.get_conf(self, identifier=1234567890)
        self.config.register_global(base_url=None)
        self.config.register_user(api_token=None, is_admin=False)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    async def get_api_token(self, user: discord.User):
        return await self.config.user(user).api_token()

    async def get_base_url(self):
        return await self.config.base_url()

    async def fetch_data(self, endpoint: str, user: discord.User, method: str = 'GET', data: dict = None):
        api_token = await self.get_api_token(user)
        base_url = await self.get_base_url()
        headers = {'Authorization': api_token} if api_token else {}
        url = f'{base_url}/api/{endpoint}'

        if method == 'GET':
            async with self.session.get(url, headers=headers) as response:
                if response.status != 200:
                    return None
                return await response.json()
        elif method == 'POST':
            async with self.session.post(url, headers=headers, json=data) as response:
                if response.status != 200:
                    return None
                return await response.json()
        elif method == 'DELETE':
            async with self.session.delete(url, headers=headers) as response:
                if response.status != 200:
                    return None
                return await response.json()

    @commands.group()
    async def zipline(self, ctx: commands.Context):
        """Commands to interact with Zipline's API."""
        pass

    @zipline.command()
    async def setbaseurl(self, ctx: commands.Context, base_url: str):
        """Set the base URL for Zipline."""
        await self.config.base_url.set(base_url)
        await ctx.send("Base URL set successfully.")

    @zipline.command()
    async def register(self, ctx: commands.Context, api_token: str):
        """Register your account token with your Discord user."""
        await self.config.user(ctx.author).api_token.set(api_token)
        await ctx.send("API token registered successfully.")
        # Check if the token is an admin token
        data = await self.fetch_data('admin/stats', ctx.author)
        if data:
            await self.config.user(ctx.author).is_admin.set(True)
            await ctx.send("Admin token detected. Admin features enabled.")
        else:
            await self.config.user(ctx.author).is_admin.set(False)

    @zipline.command()
    async def listfiles(self, ctx: commands.Context):
        """List all files in your account."""
        data = await self.fetch_data('files', ctx.author)
        if not data:
            return await ctx.send("Failed to fetch data from Zipline.")

        files = [file['name'] for file in data]
        description = humanize_list(files)
        for page in pagify(description, delims=[" ", "\n"], page_length=2000):
            await ctx.send(box(page))

    @zipline.command()
    async def upload(self, ctx: commands.Context, *, url: str = None):
        """Upload a file from a URL or upload a file directly."""
        if url:
            data = await self.fetch_data('upload', ctx.author, method='POST', data={'url': url})
            if not data:
                return await ctx.send("Failed to upload file to Zipline.")
            await ctx.send(f"File uploaded successfully: {data['url']}")
        elif ctx.message.attachments:
            file = ctx.message.attachments[0]
            file_data = await file.read()
            api_token = await self.get_api_token(ctx.author)
            base_url = await self.get_base_url()
            headers = {'Authorization': api_token} if api_token else {}
            async with self.session.post(f'{base_url}/api/upload', headers=headers, data={'file': file_data}) as response:
                if response.status != 200:
                    return await ctx.send("Failed to upload file to Zipline.")
                data = await response.json()
                await ctx.send(f"File uploaded successfully: {data['url']}")
        else:
            await ctx.send("Please provide a URL or attach a file to upload.")

    @zipline.command()
    async def delete(self, ctx: commands.Context, file_id: str):
        """Delete a file by its ID."""
        data = await self.fetch_data(f'files/{file_id}', ctx.author, method='DELETE')
        if not data:
            return await ctx.send("Failed to delete file from Zipline.")

        await ctx.send("File deleted successfully.")

    @zipline.command()
    async def info(self, ctx: commands.Context, file_id: str):
        """Get information about a specific file by ID."""
        data = await self.fetch_data(f'files/{file_id}', ctx.author)
        if not data:
            return await ctx.send("Failed to fetch data from Zipline.")

        embed = discord.Embed(title=data['name'], description=data['url'])
        embed.add_field(name="Uploader", value=data['uploader'])
        embed.add_field(name="Size", value=data['size'])
        embed.add_field(name="Type", value=data['type'])

        await ctx.send(embed=embed)

    @zipline.command()
    async def random(self, ctx: commands.Context):
        """Get a random file."""
        data = await self.fetch_data('files/random', ctx.author)
        if not data:
            return await ctx.send("Failed to fetch data from Zipline.")

        embed = discord.Embed(title=data['name'], description=data['url'])
        embed.add_field(name="Uploader", value=data['uploader'])
        embed.add_field(name="Size", value=data['size'])
        embed.add_field(name="Type", value=data['type'])

        await ctx.send(embed=embed)

    @zipline.command()
    async def stats(self, ctx: commands.Context):
        """Get stats. If the token is admin, show admin stats; otherwise, show user stats."""
        is_admin = await self.config.user(ctx.author).is_admin()
        endpoint = 'admin/stats' if is_admin else 'user/stats'

        data = await self.fetch_data(endpoint, ctx.author)
        if not data:
            return await ctx.send("Failed to fetch stats from Zipline.")

        embed = discord.Embed(title="Stats")
        if is_admin:
            embed.add_field(name="Total Users", value=data['total_users'])
            embed.add_field(name="Total Files", value=data['total_files'])
            embed.add_field(name="Total Size", value=data['total_size'])
        else:
            embed.add_field(name="Total Files", value=data['total_files'])
            embed.add_field(name="Total Size", value=data['total_size'])

        await ctx.send(embed=embed)

    @zipline.command()
    async def auth(self, ctx: commands.Context, endpoint: str):
        """Auth endpoints."""
        data = await self.fetch_data(f'auth/{endpoint}', ctx.author)
        if not data:
            return await ctx.send(f"Failed to fetch data from Zipline endpoint: auth/{endpoint}.")

        await ctx.send(box(str(data)))

    @zipline.command()
    async def user(self, ctx: commands.Context, endpoint: str, user_id: str = None):
        """User endpoints."""
        if user_id:
            data = await self.fetch_data(f'user/{user_id}/{endpoint}', ctx.author)
        else:
            data = await self.fetch_data(f'user/{endpoint}', ctx.author)

        if not data:
            return await ctx.send(f"Failed to fetch data from Zipline endpoint: user/{endpoint}.")

        await ctx.send(box(str(data)))

    @zipline.command()
    async def shorten(self, ctx: commands.Context, url: str):
        """Shorten URL endpoint."""
        data = await self.fetch_data('shorten', ctx.author, method='POST', data={'url': url})
        if not data:
            return await ctx.send("Failed to shorten URL with Zipline.")

        await ctx.send(f"URL shortened successfully: {data['url']}")

    @zipline.command()
    async def version(self, ctx: commands.Context):
        """Version endpoint."""
        data = await self.fetch_data('version', ctx.author)
        if not data:
            return await ctx.send("Failed to fetch version from Zipline.")

        await ctx.send(box(str(data)))

async def setup(bot: Red):
    await bot.add_cog(Zipline(bot))
