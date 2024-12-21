# s.sesh
Group command for managing smoking sessions.<br/>
 - Usage: `s.sesh`
 - Checks: `server_only`
## s.sesh setchannel
Set the channel where sesh announcements will be made.<br/>
 - Usage: `s.sesh setchannel <channel>`
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
## s.sesh leave
Leave the current smoking session.<br/>
 - Usage: `s.sesh leave`
 - Checks: `server_only`
## s.sesh list
List all upcoming smoking sessions.<br/>
 - Usage: `s.sesh list`
 - Checks: `server_only`
## s.sesh start
Start a new smoking session using interactive components.<br/>
 - Usage: `s.sesh start`
 - Checks: `server_only`
## s.sesh cancel
Cancel a smoking session you created.<br/>

Provide the session ID to cancel the session.<br/>
 - Usage: `s.sesh cancel <session_id>`
 - Checks: `server_only`
Extended Arg Info
> ### session_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sesh end
Manually end a smoking session.<br/>

Provide the session ID or the voice channel ID to end the session.<br/>
 - Usage: `s.sesh end <identifier>`
 - Checks: `server_only`
Extended Arg Info
> ### identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sesh join
Join the currently active smoking session.<br/>
 - Usage: `s.sesh join`
 - Checks: `server_only`
## s.sesh setrole
Set a role to be mentioned when a sesh is announced or starts.<br/>
 - Usage: `s.sesh setrole <role>`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.sesh setcategory
Set the category where sesh voice channels will be created.<br/>
 - Usage: `s.sesh setcategory <category>`
 - Checks: `server_only`
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
