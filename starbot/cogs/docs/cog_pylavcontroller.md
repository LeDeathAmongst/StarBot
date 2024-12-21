# s.plcontrollerset
Configure the PyLav Controller.<br/>
 - Usage: `s.plcontrollerset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.plcontrollerset channel
Set the channel to create the controller in.<br/>
 - Usage: `s.plcontrollerset channel <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.VoiceChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.plcontrollerset acceptrequests
Toggle whether the controller should listen for requests.<br/>
 - Usage: `s.plcontrollerset acceptrequests`
 - Aliases: `ar and listen`
## s.plcontrollerset slowmode
Toggle whether the controller should use slowmode.<br/>
 - Usage: `s.plcontrollerset slowmode`
 - Aliases: `sm`
## s.plcontrollerset acceptsearches
Toggle whether the controller should listen for searches.<br/>
 - Usage: `s.plcontrollerset acceptsearches`
 - Aliases: `as and search`
## s.plcontrollerset antispam
Toggle whether the controller enable the antispam check.<br/>
 - Usage: `s.plcontrollerset antispam`
 - Aliases: `spam`
