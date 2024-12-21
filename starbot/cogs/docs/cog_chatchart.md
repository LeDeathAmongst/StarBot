# s.chatchart
Generates a pie chart, representing the last 5000 messages in the specified channel.<br/>
 - Usage: `s.chatchart [channel=None] [messages=5000]`
 - Cooldown: `1 per 10.0 seconds`
 - Checks: `server_only`
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
> ### messages: int = 5000
> ```
> A number without decimal places.
> ```
# s.serverchart
Generates a pie chart, representing the last 1000 messages from every allowed channel in the server.<br/>

As example:<br/>
For each channel that the bot is allowed to scan. It will take the last 1000 messages from each channel.<br/>
And proceed to build a chart out of that.<br/>
 - Usage: `s.serverchart [messages=1000]`
 - Restricted to: `MOD`
 - Aliases: `serverchart`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### messages: int = 1000
> ```
> A number without decimal places.
> ```
# s.ccdeny
Add a channel to deny chatchart use.<br/>
 - Usage: `s.ccdeny <channel>`
 - Restricted to: `MOD`
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
# s.ccdenylist
List the channels that are denied.<br/>
 - Usage: `s.ccdenylist`
 - Restricted to: `MOD`
 - Checks: `server_only`
# s.ccallow
Remove a channel from the deny list to allow chatchart use.<br/>
 - Usage: `s.ccallow <channel>`
 - Restricted to: `MOD`
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
