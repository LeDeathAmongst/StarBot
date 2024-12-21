# s.dynamicchannellist
Group command for DynamicChannelList.<br/>
 - Usage: `s.dynamicchannellist`
 - Restricted to: `MOD`
 - Aliases: `dcl`
## s.dynamicchannellist categoryblacklist
Toggle if a category is blacklisted from appearing on channel lists.<br/>

If no category is provided, the currently blacklisted categories will be listed.<br/>
 - Usage: `s.dynamicchannellist categoryblacklist [cat=None]`
 - Aliases: `categoryignore`
Extended Arg Info
> ### cat: discord.channel.CategoryChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.dynamicchannellist reloadauto
Reload all automatically updating channel lists.<br/>
 - Usage: `s.dynamicchannellist reloadauto`
## s.dynamicchannellist removeauto
Remove an automatically updating channel list.<br/>

This will not delete the message, only stop it from updating.<br/>
`message` should be a link to the message.<br/>
 - Usage: `s.dynamicchannellist removeauto <message>`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
## s.dynamicchannellist color
Set the color to use for embeds.<br/>
 - Usage: `s.dynamicchannellist color <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
## s.dynamicchannellist header
Set the header for all embed messages.<br/>
 - Usage: `s.dynamicchannellist header [text]`
Extended Arg Info
> ### text=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.dynamicchannellist generate
Generate a one-time channel list.<br/>
 - Usage: `s.dynamicchannellist generate [channel=None] [ignoreBlacklist=False] [role=None]`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### ignoreBlacklist: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.dynamicchannellist channelblacklist
Toggle if a channel is blacklisted from appearing on channel lists.<br/>

If no channel is provided, the currently blacklisted categories will be listed.<br/>
 - Usage: `s.dynamicchannellist channelblacklist [chan=None]`
 - Aliases: `channelignore`
Extended Arg Info
> ### chan: Union[discord.channel.TextChannel, discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.dynamicchannellist createauto
Create an automatically updating channel list.<br/>
 - Usage: `s.dynamicchannellist createauto [channel=None] [ignoreBlacklist=False] [role=None]`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### ignoreBlacklist: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
