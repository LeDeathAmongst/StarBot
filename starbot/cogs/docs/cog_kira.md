# s.kira
Remind people to only post relevant links.<br/>
 - Usage: `s.kira`
## s.kira watch
Add a channel to be monitored.<br/>
 - Usage: `s.kira watch <channel>`
 - Restricted to: `ADMIN`
 - Aliases: `w`
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
## s.kira unwatch
Remove a channel from the watchlist.<br/>
 - Usage: `s.kira unwatch <channel>`
 - Restricted to: `ADMIN`
 - Aliases: `u`
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
## s.kira domain
Configure which domains to look out for.<br/>

This function doesn't do anything at the moment, but will be expanded later.<br/>
 - Usage: `s.kira domain <channel>`
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
## s.kira question
Change the question the sender will be required to answer.<br/>
 - Usage: `s.kira question <channel> <question>`
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
> ### question: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.kira timeout
Set the timeout for questioning the sender. 0 will disable the questioning and deletes the message immediately.<br/>

Default is 10 seconds.<br/>
 - Usage: `s.kira timeout <channel> <timeout>`
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
> ### timeout: Optional[int]
> ```
> A number without decimal places.
> ```
