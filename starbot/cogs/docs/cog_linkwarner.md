# s.linkwarner
Settings for LinkWarner cog.<br/>
 - Usage: `s.linkwarner`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.linkwarner deletedelay
Set the delete delay (in seconds) for the warning message.<br/>

Use `s.linkwarner deletedelay disable` to disable auto-deletion.<br/>

Note: This does not work when the warning messages are sent through DMs.<br/>
 - Usage: `s.linkwarner deletedelay <new_value>`
Extended Arg Info
> ### new_value: int
> ```
> A number without decimal places.
> ```
### s.linkwarner deletedelay disable
Disable auto-deletion of the warning messages.<br/>
 - Usage: `s.linkwarner deletedelay disable`
## s.linkwarner unsetmessage
Unset link warning message.<br/>
 - Usage: `s.linkwarner unsetmessage`
## s.linkwarner usedms
Set if LinkWarner should use DMs for warning messages.<br/>

Note: This is NOT recommended as the user might block the bot or all DMs<br/>
from the server and the warning might not get sent to the offender at all.<br/>
This also means that the bot is more likely to get ratelimited for repeatedly<br/>
trying to DM the user when they spam links.<br/>

If you're trying to minimize spam that the warning messages cause,<br/>
you should consider enabling delete delay instead.<br/>
 - Usage: `s.linkwarner usedms <new_state>`
Extended Arg Info
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.linkwarner channel
Channel-specific settings for LinkWarner.<br/>
 - Usage: `s.linkwarner channel`
### s.linkwarner channel ignore
Set if LinkWarner should ignore links in provided channel.<br/>
 - Usage: `s.linkwarner channel ignore <channel> <new_state>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.linkwarner channel unsetmessage
Unset link warning message for provided channel.<br/>
 - Usage: `s.linkwarner channel unsetmessage <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.linkwarner channel showsettings
Show settings for the given channel.<br/>
 - Usage: `s.linkwarner channel showsettings <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.linkwarner channel domains
Configuration for allowed/disallowed domains in the specific channel.<br/>
 - Usage: `s.linkwarner channel domains`
#### s.linkwarner channel domains add
Add domains to the domains list of the provided channel.<br/>

Note: The cog is using exact matching for domain names<br/>
which means that domain names like youtube.com and www.youtube.com<br/>
are treated as 2 different domains.<br/>

Example:<br/>
`s.linkwarner channel domains add #channel youtube.com discord.com`<br/>
 - Usage: `s.linkwarner channel domains add <channel> <domains>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.linkwarner channel domains remove
Remove domains from the domains list of the provided channel.<br/>

Example:<br/>
`s.linkwarner channel domains remove #channel youtube.com discord.com`<br/>
 - Usage: `s.linkwarner channel domains remove <channel> <domains>`
 - Aliases: `delete`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.linkwarner channel domains clear
Clear domains from the domains list of the provided channel.<br/>
 - Usage: `s.linkwarner channel domains clear <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.linkwarner channel domains setmode
Change current domains list mode.<br/>

Available modes:<br/>
`0` - Inherit the server setting and use domains<br/>
      from both server's and channel's domain list.<br/>
`1` - Only domains on the channel's domains list can be sent.<br/>
`2` - All domains can be sent except the ones on the channel's domains list.<br/>
 - Usage: `s.linkwarner channel domains setmode <channel> <new_mode>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.linkwarner channel setmessage
Set link warning message for provided channel.<br/>

Those fields will get replaced automatically:<br/>
$mention - Mention the user who sent the message with a link<br/>
$username - The user's display name<br/>
$server - The name of the server<br/>
 - Usage: `s.linkwarner channel setmessage <channel> <message>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.linkwarner state
Set if LinkWarner should be enabled for this server.<br/>

If used without a setting, this will show the current state.<br/>
 - Usage: `s.linkwarner state <new_state>`
Extended Arg Info
> ### new_state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.linkwarner domains
Configuration for allowed/disallowed domains in the server.<br/>
 - Usage: `s.linkwarner domains`
### s.linkwarner domains add
Add domains to the domains list.<br/>

Note: The cog is using exact matching for domain names<br/>
which means that domain names like youtube.com and www.youtube.com<br/>
are treated as 2 different domains.<br/>

Example:<br/>
`s.linkwarner domains add google.com youtube.com`<br/>
 - Usage: `s.linkwarner domains add <domains>`
### s.linkwarner domains remove
Remove domains from the domains list.<br/>

Example:<br/>
`s.linkwarner domains remove youtube.com discord.com`<br/>
 - Usage: `s.linkwarner domains remove <domains>`
 - Aliases: `delete`
### s.linkwarner domains setmode
Change current domains list mode.<br/>

Available modes:<br/>
`1` - Only domains on the domains list can be sent.<br/>
`2` - All domains can be sent except the ones on the domains list.<br/>
 - Usage: `s.linkwarner domains setmode <new_mode>`
### s.linkwarner domains clear
Clear domains from the domains list.<br/>
 - Usage: `s.linkwarner domains clear`
## s.linkwarner showsettings
Show settings for the current server.<br/>
 - Usage: `s.linkwarner showsettings`
## s.linkwarner excludedroles
Settings for roles that are excluded from getting filtered.<br/>
 - Usage: `s.linkwarner excludedroles`
### s.linkwarner excludedroles add
Add roles that will be excluded from getting filtered.<br/>
 - Usage: `s.linkwarner excludedroles add <roles>`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.linkwarner excludedroles remove
Remove roles that will be excluded from getting filtered.<br/>
 - Usage: `s.linkwarner excludedroles remove <roles>`
 - Aliases: `delete`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.linkwarner setmessage
Set link warning message.<br/>

Those fields will get replaced automatically:<br/>
$mention - Mention the user who sent the message with a link<br/>
$username - The user's display name<br/>
$server - The name of the server<br/>
 - Usage: `s.linkwarner setmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
