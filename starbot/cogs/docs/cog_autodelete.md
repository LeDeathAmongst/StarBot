# s.autodelete
Manage the AutoDelete settings.<br/>
 - Usage: `s.autodelete`
## s.autodelete toggle
Toggle the auto-delete feature for this server.<br/>
 - Usage: `s.autodelete toggle`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.autodelete logchannel
Set the log channel for auto-delete messages.<br/>
 - Usage: `s.autodelete logchannel <channel>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
