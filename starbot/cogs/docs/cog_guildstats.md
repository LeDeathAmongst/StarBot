# s.serverstats (Hybrid Command)
Generate images with messages and voice stats, for members, roles, servers, categories, text channels, voice channels and activities.<br/>
 - Usage: `s.serverstats [members_type=humans] [show_graphic=False] <_object>`
 - Slash Usage: `/serverstats [members_type=humans] [show_graphic=False] <_object>`
 - Checks: `server_only`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.serverstats messages (Hybrid Command)
Display stats for the messages in this server.<br/>
 - Usage: `s.serverstats messages [members_type=humans] [show_graphic=False]`
 - Slash Usage: `/serverstats messages [members_type=humans] [show_graphic=False]`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.serverstats activities (Hybrid Command)
Display stats for activities in this server.<br/>
 - Usage: `s.serverstats activities [members_type=humans]`
 - Slash Usage: `/serverstats activities [members_type=humans]`
## s.serverstats top (Hybrid Command)
Display top stats for voice/messages members/channels.<br/>
 - Usage: `s.serverstats top <members_type> <_type_1> <_type_2>`
 - Slash Usage: `/serverstats top <members_type> <_type_1> <_type_2>`
## s.serverstats voice (Hybrid Command)
Display stats for the voice in this server.<br/>
 - Usage: `s.serverstats voice [members_type=humans] [show_graphic=False]`
 - Slash Usage: `/serverstats voice [members_type=humans] [show_graphic=False]`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.serverstats ignorechannel (Hybrid Command)
Ignore or unignore a specific channel.<br/>
 - Usage: `s.serverstats ignorechannel <channel>`
 - Slash Usage: `/serverstats ignorechannel <channel>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.serverstats ignoreme (Hybrid Command)
Asking GuildStats to ignore your actions.<br/>
 - Usage: `s.serverstats ignoreme`
 - Slash Usage: `/serverstats ignoreme`
## s.serverstats ignorecategory (Hybrid Command)
Ignore or unignore a specific category.<br/>
 - Usage: `s.serverstats ignorecategory <category>`
 - Slash Usage: `/serverstats ignorecategory <category>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### category: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.serverstats role (Hybrid Command)
Display stats for a specified role.<br/>
 - Usage: `s.serverstats role [show_graphic=False] [role]`
 - Slash Usage: `/serverstats role [show_graphic=False] [role]`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.serverstats channel (Hybrid Command)
Display stats for a specified channel.<br/>
 - Usage: `s.serverstats channel [members_type=humans] [show_graphic=False] [channel]`
 - Slash Usage: `/serverstats channel [members_type=humans] [show_graphic=False] [channel]`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.serverstats activity (Hybrid Command)
Display stats for a specific activity in this server.<br/>
 - Usage: `s.serverstats activity [members_type=humans] <activity_name>`
 - Slash Usage: `/serverstats activity [members_type=humans] <activity_name>`
Extended Arg Info
> ### activity_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.serverstats category (Hybrid Command)
Display stats for a specified category.<br/>
 - Usage: `s.serverstats category [members_type=humans] [show_graphic=False] [category]`
 - Slash Usage: `/serverstats category [members_type=humans] [show_graphic=False] [category]`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### category: discord.channel.CategoryChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.serverstats server (Hybrid Command)
Display stats for this server.<br/>
 - Usage: `s.serverstats server [members_type=humans] [show_graphic=False]`
 - Slash Usage: `/serverstats server [members_type=humans] [show_graphic=False]`
 - Aliases: `server`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.serverstats ignoreactivity (Hybrid Command)
Ignore or unignore a specific activity.<br/>
 - Usage: `s.serverstats ignoreactivity <activity_name>`
 - Slash Usage: `/serverstats ignoreactivity <activity_name>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### activity_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.serverstats graphic (Hybrid Command)
Display graphic for members, roles servers, text channels, voice channels and activities.<br/>
 - Usage: `s.serverstats graphic [members_type=humans] [_object]`
 - Slash Usage: `/serverstats graphic [members_type=humans] [_object]`
 - Aliases: `graph`
## s.serverstats enable (Hybrid Command)
Enable the cog in this server/server.<br/>
 - Usage: `s.serverstats enable`
 - Slash Usage: `/serverstats enable`
 - Restricted to: `ADMIN`
## s.serverstats disable (Hybrid Command)
Disable the cog in this server/server.<br/>
 - Usage: `s.serverstats disable`
 - Slash Usage: `/serverstats disable`
 - Restricted to: `ADMIN`
## s.serverstats memberactivities (Hybrid Command)
Display stats for the activities of a specified member.<br/>
 - Usage: `s.serverstats memberactivities [member]`
 - Slash Usage: `/serverstats memberactivities [member]`
 - Aliases: `mactivites and mact`
Extended Arg Info
> ### member: discord.member.Member = operator.attrgetter('author')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
## s.serverstats member (Hybrid Command)
Display stats for a specified member.<br/>
 - Usage: `s.serverstats member [show_graphic=False] [member]`
 - Slash Usage: `/serverstats member [show_graphic=False] [member]`
Extended Arg Info
> ### show_graphic: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### member: discord.member.Member = operator.attrgetter('author')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
