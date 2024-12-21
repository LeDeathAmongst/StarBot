# s.sethoneypot (Hybrid Command)
Set the honeypot settings. Only the server owner can use this command for security reasons.<br/>
 - Usage: `s.sethoneypot`
 - Slash Usage: `/sethoneypot`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.sethoneypot logschannel (Hybrid Command)
The channel to send the logs to.<br/>

Default value: `None`<br/>
Dev: `typing.Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]`<br/>
 - Usage: `s.sethoneypot logschannel <value>`
 - Slash Usage: `/sethoneypot logschannel <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.sethoneypot resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.sethoneypot resetsetting <setting>`
 - Slash Usage: `/sethoneypot resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sethoneypot action (Hybrid Command)
The action to take when a self bot/scammer is detected.<br/>

Default value: `None`<br/>
Dev: `typing.Literal['mute', 'kick', 'ban']`<br/>
 - Usage: `s.sethoneypot action <value>`
 - Slash Usage: `/sethoneypot action <value>`
 - Checks: `server_only`
## s.sethoneypot pingrole (Hybrid Command)
The role to ping when a self bot/scammer is detected.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.role.Role'>`<br/>
 - Usage: `s.sethoneypot pingrole <value>`
 - Slash Usage: `/sethoneypot pingrole <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.sethoneypot bandeletemessagedays (Hybrid Command)
The number of days of messages to delete when banning a self bot/scammer.<br/>

Default value: `3`<br/>
Dev: `Range[int, 0, 7]`<br/>
 - Usage: `s.sethoneypot bandeletemessagedays <value>`
 - Slash Usage: `/sethoneypot bandeletemessagedays <value>`
 - Checks: `server_only`
## s.sethoneypot createchannel (Hybrid Command)
Create the honeypot channel.<br/>
 - Usage: `s.sethoneypot createchannel`
 - Slash Usage: `/sethoneypot createchannel`
 - Aliases: `makechannel`
 - Checks: `bot_has_server_permissions and server_only`
## s.sethoneypot muterole (Hybrid Command)
The mute role to assign to the self bots/scammers, if the action is `mute`.<br/>

Default value: `None`<br/>
Dev: `<class 'discord.role.Role'>`<br/>
 - Usage: `s.sethoneypot muterole <value>`
 - Slash Usage: `/sethoneypot muterole <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.sethoneypot enabled (Hybrid Command)
Toggle the cog.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.sethoneypot enabled <value>`
 - Slash Usage: `/sethoneypot enabled <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.sethoneypot modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.sethoneypot modalconfig [confirmation=False]`
 - Slash Usage: `/sethoneypot modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.sethoneypot showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.sethoneypot showsettings [with_dev=False]`
 - Slash Usage: `/sethoneypot showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
