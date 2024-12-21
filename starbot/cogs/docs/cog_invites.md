# s.invites
Settings for the invite tracker.<br/>
 - Usage: `s.invites`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.invites growthchart
Show the overall member growth of the server as a graph.<br/>
 - Usage: `s.invites growthchart`
## s.invites stats
Fetch and show invite stats for the server.<br/>
 - Usage: `s.invites stats`
## s.invites addreward
Add a reward for a specific number of invites.<br/>
 - Usage: `s.invites addreward <invite_count> <role>`
Extended Arg Info
> ### invite_count: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.invites leaderboard
Show the leaderboard of top inviting users.<br/>
 - Usage: `s.invites leaderboard`
## s.invites announcechannel
Set the announcement channel for invites.<br/>
 - Usage: `s.invites announcechannel <channel>`
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
## s.invites removereward
Remove a reward for a specific number of invites.<br/>
 - Usage: `s.invites removereward <invite_count>`
Extended Arg Info
> ### invite_count: int
> ```
> A number without decimal places.
> ```
