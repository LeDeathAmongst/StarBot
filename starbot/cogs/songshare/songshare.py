import discord
from Star-Utils import Cog, CogsUtils

from starbot.core import commands, Config, utils

import aiohttp

import logging
import asyncio
import urllib.parse
import re

log = logging.getLogger("red.jak-cogs.songshare")


class SongShare (Cog):

    
    def __init__(self, bot):
        self.bot = bot
        #  ^
        # /!\  the regex is AI generated so there might be problems. I don't have the ressources to check every matching link, I just hope it works…
        #/___\
        self.REGEX = r"https?://(?:open\.spotify\.com/(?:track|album)/[^\s\n]+|" \
                    r"itunes\.apple\.com/[a-z]{2}/album/[^\s\n]+|" \
                    r"music\.apple\.com/[a-z]{2}/(?:album|playlist)/[^\s\n]+|" \
                    r"(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=[^\s&]+|youtu\.be/[^\s&]+|"\
                    r"music\.youtube\.com/watch\?v=[^\s&]+)|"\
                    r"play\.google\.com/store/music/album/[^\s\n]+|" \
                    r"www\.pandora\.com/artist/[\w-]+/[\w-]+/[^\s\n]+|" \
                    r"www\.deezer\.com/[a-z]{2}/(?:track|album)/[^\s\n]+|" \
                    r"deezer\.page\.link/[a-zA-Z0-9]+|"\
                    r"tidal\.com/browse/(?:track|album)/[^\s\n]+|" \
                    r"music\.amazon\.com/(?:albums|tracks)/[^\s\n]+|" \
                    r"www\.amazon\.com/[a-z]{2}/dp/[^\s\n]+|" \
                    r"soundcloud\.com/[\w-]+/[^\s\n]+|" \
                    r"[a-z]{2}\.napster\.com/artist/[\w-]+/album/[\w-]+/track/[^\s\n]+|" \
                    r"music\.yandex\.[a-z]{2}/album/[\w-]+/track/[^\s\n]+|" \
                    r"spinrilla\.com/(?:songs|mixtapes)/[^\s\n]+|" \
                    r"audius\.co/[\w-]+/[^\s\n]+|" \
                    r"play\.anghami\.com/(?:song|album)/[^\s\n]+|" \
                    r"www\.boomplaymusic\.com/share/music/[^\s\n]+|" \
                    r"audiomack\.com/[\w-]+/song/[^\s\n]+)"
        self.COMPILED_REGEX = re.compile(self.REGEX, re.IGNORECASE)
        self.use_api = False
        self.api_key = ""
        self.channel_ids = []
        self.not_channel_ids = []
        self.guild_ids = []
        self.config = Config.get_conf(self, identifier=6268506813, force_registration=True)
        default_guild = {"all_guild": False,
                         "except_channels": [],
                         "specify_channels": []
                         }
        self.config.register_guild(**default_guild)

        asyncio.create_task(self.load())

    async def load(self):
        await self.bot.wait_until_ready()
        api_key = await self.bot.get_shared_api_tokens("songlink")
        if api_key == {}:
            self.use_api = False
        else:
            self.api_key = api_key
            self.use_api = True
        guilds = self.config._get_base_group(self.config.GUILD)
        async with guilds.all() as all_guilds:
            for guid, guild_data in all_guilds.items():
                guild = self.bot.get_guild(int(guid))
                if not guild:
                    continue
                if guild_data.get("all_guild"):
                    self.guild_ids.append(int(guid))
                if guild_data.get("except_channels"):
                    for i in guild_data.get("except_channels"):
                        self.not_channel_ids.append(int(i))
                if guild_data.get("specify_channels"):
                    for i in guild_data.get("specify_channels"):
                        self.channel_ids.append(int(i))


    async def rewrite_services_names(self, name:str):
        if name == "spotify":
            return "Spotify"
        elif name == "itunes":
            return "iTunes"
        elif name == "appleMusic":
            return "Apple Music"
        elif name == "youtube":
            return "YouTube"
        elif name == "youtubeMusic":
            return "YouTube Music"
        elif name == "google":
                return "Google"
        elif name == "googleStore":
            return "Google Play"
        elif name == "pandora":
            return "Pandora"
        elif name == "deezer":
            return "Deezer"
        elif name == "tidal":
            return "Tidal"
        elif name == "amazonStore":
            return "Amazon Store"
        elif name == "amazonMusic":
            return "Amazon Music"
        elif name == "soundcloud":
                return "SoundCloud"
        elif name == "napster":
            return "Napster"
        elif name == "yandex":
            return "Yandex Music"
        elif name == "spinrilla":
            return "Spinrilla"
        elif name == "audius":
            return "Audius"
        elif name == "audiomack":
            return "Audiomack"
        elif name == "anghami":
            return "Anghami"
        elif name == "boomplay":
            return "Boomplay"
        else:
            return name
    
    @commands.commands.Cog.listener()
    async def on_message_without_command(self, message: discord.Message):
        if message.author.bot:
            return
        if message.guild:
            if not((message.guild.id in self.guild_ids) or (message.channel.id in self.channel_ids)):
                return
            if message.channel.id in self.not_channel_ids:
                return
            if await self.bot.cog_disabled_in_guild(SongShare, message.guild):
                return
            channel_perms = message.channel.permissions_for(message.guild)
            if not channel_perms.send_messages:
                return
        #if not await self.bot.ignored_channel_or_guild(message): #causes problems with media channels where commands aren't allowed… So I commented out unless better option
        #    return
        #if not await self.bot.allowed_by_whitelist_blacklist(message.author):
         #   return
          # I think this should still trigger even if the user is blacklisted. Leaving this in just in case some might think otherwise or whatever.
        urls = self.COMPILED_REGEX.findall(message.content)
        if not urls:
            return
        for i in urls:
            data = {"url": i
                    }
            if self.use_api:
                data["key"] = self.api_key
            encoded_params = urllib.parse.urlencode(data)
            url = "https://api.song.link/v1-alpha.1/links?" + encoded_params
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        response = await resp.json()
                        view = discord.ui.View()
                        for i, body in response["linksByPlatform"].items():
                            button = discord.ui.Button(style=discord.ButtonStyle.link, label= await self.rewrite_services_names(i), url=body["url"])
                            view.add_item(button)
                        found = False
                        for key, value in response["entitiesByUniqueId"].items():
                            if key.startswith("SPOTIFY_SONG"):
                                song_infos = value
                                found = True
                                break
                        if not found:
                            song_infos = next(iter(response["entitiesByUniqueId"].values()))
                        if await self.bot.embed_requested(message.channel):
                            embed = discord.Embed(title=song_infos['title'], url=response["pageUrl"])
                            embed.set_author(name = song_infos["artistName"])
                            try:
                                embed.set_thumbnail(url=song_infos["thumbnailUrl"])
                            except KeyError:
                                pass
                            embed.set_footer(text="Powered by Songlink/Odesli", icon_url="https://songlink-public.s3-us-west-1.amazonaws.com/icon-auth0.png")
                            embed.color = await self.bot.get_embed_color(message.channel)
                            await message.reply(embed=embed, view=view, mention_author = False)
                        else:
                            await message.reply(f"#### {song_infos['artistName']}\n # {song_infos['title']}\n{response['pageUrl']}", view = view, mention_author = False)# if it should not use embeds fallback to this
                    else:
                        try:
                            response = await resp.json()
                        except: #doesn't matter what, does not get handled differently (ik you shouldn't use that but)
                            response = None
                        await message.reply(f"Failed to connect with song.link with `{resp.status}: {resp.reason}`")
                        log.error(f"Failed to connect with song.link with {resp.status}: {resp.reason} requesting url: {url}; {response}")

    @commands.admin()
    @commands.bot_in_a_guild()
    @commands.group(aliases=["setsongshare"])
    async def songshareset(self, ctx):
        """Set up the songshare cog"""
        pass

    @songshareset.command(aliases=["everywhere", "guild"])
    async def allguild(self, ctx, toggle:bool = None):
        """Toggle between complete guild or only a single channel
        
        Set True to activate it in the entire guild, False if only in selected channels. Leave emtpy totoggle"""

        set_to:bool
        if toggle is None:
            current_setting = await self.config.guild(ctx.guild).all_guild()
            set_to = not current_setting
        elif toggle:
            set_to = True
        else:
            set_to = False
        await self.config.guild(ctx.guild).all_guild.set(set_to)

        if set_to:
            await ctx.send("The songshare will now be active in the entire guild. If you want to blacklist channels, use `[p]songshareset channel blacklist`")

    async def get_if_balcklist_append(self, is_blacklist:bool):
        if is_blacklist:
            return " blacklist "
        else:
            return " "

    async def get_config_path (self, ctx, is_blacklist:bool):
        if is_blacklist:
            return self.config.guild(ctx.guild).except_channels()
        else:
            return self.config.guild(ctx.guild).specify_channels()
        
    async def get_channel_var(self, is_blacklist:bool):
        if is_blacklist:
            return self.not_channel_ids
        else:
            return self.channel_ids
        

    async def add_channel(self, ctx, channel:discord.TextChannel, is_blacklist:bool = False):
        append = await self.get_if_balcklist_append(is_blacklist)
        channel_var = await self.get_channel_var(is_blacklist)
        async with await self.get_config_path(ctx, is_blacklist) as channels:
            if channel.id not in channels:
                channels.append(channel.id)
                channel_var.append(channel.id)
                await ctx.send(f"Added {channel.mention} to the songshare{append}channels.")
            else:
                await ctx.send(f"{channel.mention} is already in the songshare{append}channels. To remove it run `[p]songshareset channel{append}remove <channel>`")

    async def remove_channel(self, ctx, channel:discord.TextChannel, is_blacklist:bool = False):
        append = await self.get_if_balcklist_append(is_blacklist)
        channel_var = await self.get_channel_var(is_blacklist)
        async with await self.get_config_path(ctx, is_blacklist) as channels:
            if channel.id in channels:
                channels.remove(channel.id)
                channel_var.remove(channel.id)
                await ctx.send(f"Removed {channel.mention} from the songshare{append}channels.")
            else:
                await ctx.send(f"{channel.mention} is not in the songshare{append}channels. If you want to add it instead, run `[p]songshareset channel{append}add <channel>`")
    
    async def reset_channels(self, ctx, is_blacklist:bool = False):
        append = await self.get_if_balcklist_append(is_blacklist)
        channel_var = await self.get_channel_var(is_blacklist)
        view = utils.views.ConfirmView(ctx.author)
        view.message = await ctx.send(f"Are you sure you want to reset the songshare{append}channels to the entire guild?", view=view)
        await view.wait()
        if view.result:
            async with await self.get_config_path(ctx, is_blacklist) as channels:
                for channel in channels:
                    channel_var.remove(channel)
                channels.clear()
            await view.message.edit(f"Reset the songshare{append}channels to the entire guild.")
        else:
            await view.message.edit("Cancelled")

    @songshareset.group()
    async def channel(self, ctx):
        """Select channels for the songshare"""
        pass

    @channel.command()
    async def add(self, ctx, channel:discord.TextChannel):
        """Add a channel to the songshare"""
        await self.add_channel(ctx, channel)

    @channel.command()
    async def remove(self, ctx, channel:discord.TextChannel):
        """Remove a channel from the songshare"""
        await self.remove_channel(ctx, channel)

    @channel.command()
    async def reset(self, ctx):
        """Reset the songshare channels to the entire guild"""
        await self.reset_channels(ctx)

    @songshareset.group()
    async def blacklist(self, ctx):
        """Blacklist channels from the songshare
        
        Overrides all set channels"""

    @blacklist.command(name = "add")
    async def b_add(self, ctx, channel:discord.TextChannel):
        """Add a channel to the songshare blacklist"""
        await self.add_channel(ctx, channel, True)

    @blacklist.command(name = "remove")
    async def b_remove(self, ctx, channel:discord.TextChannel):
        """Remove a channel from the songshare blacklist"""
        await self.remove_channel(ctx, channel, True)

    @blacklist.command(name = "reset")
    async def b_reset(self, ctx):
        """Reset the songshare blacklist channels to the entire guild"""
        await self.reset_channels(ctx, True)