# s.infocontrol
Manage info enforcement settings.<br/>
 - Usage: `s.infocontrol`
 - Checks: `server_only`
## s.infocontrol disable
Disable info enforcement<br/>
 - Usage: `s.infocontrol disable`
 - Restricted to: `ADMIN`
## s.infocontrol toggle
Toggle blocking of a specific data type.<br/>
 - Usage: `s.infocontrol toggle <data_type>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### data_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.infocontrol settings
List current settings for blocking data types.<br/>
 - Usage: `s.infocontrol settings`
## s.infocontrol reset
Reset the info control settings to default for this server.<br/>
 - Usage: `s.infocontrol reset`
 - Restricted to: `ADMIN`
## s.infocontrol removemodrole
Remove a role from the list of roles to mention in alerts.<br/>
 - Usage: `s.infocontrol removemodrole <role>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.infocontrol alerts
Set the log channel for info control deletions.<br/>
 - Usage: `s.infocontrol alerts <channel>`
 - Restricted to: `ADMIN`
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
## s.infocontrol addmodrole
Add a role to the list of roles to mention in alerts.<br/>
 - Usage: `s.infocontrol addmodrole <role>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.infocontrol enable
Enable info enforcement<br/>
 - Usage: `s.infocontrol enable`
 - Restricted to: `ADMIN`
