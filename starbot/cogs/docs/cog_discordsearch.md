# s.discordsearch (Hybrid Command)
Search for a message on Discord in a channel.<br/>

Warning: The bot uses the api for each search.<br/>
Arguments:<br/>
`--author @user1 --author user2#1234 --author 0123456789`<br/>
`--mention @user1 --mention user2#1234 --mention 0123456789`<br/>
`--before now`<br/>
`--after "25/12/2000 00h00"`<br/>
`--pinned true`<br/>
`--content "AAA3A-cogs"`<br/>
`--regex "\[p\]"`<br/>
`--contain link --contain embed --contain file`<br/>
`--limit 100` (It's the limit of the number of messages taken into account in the search, not the number of results.)<br/>
 - Usage: `s.discordsearch <channel> <args>`
 - Slash Usage: `/discordsearch <channel> <args>`
 - Restricted to: `ADMIN`
 - Aliases: `dsearch`
 - Cooldown: `3 per 30.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
