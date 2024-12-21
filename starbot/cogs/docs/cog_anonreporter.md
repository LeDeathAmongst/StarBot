# s.anonreporter
Anonreporter settings<br/>
 - Usage: `s.anonreporter`
 - Restricted to: `ADMIN`
## s.anonreporter channel
Set the channel used for server reports.<br/>
 - Usage: `s.anonreporter channel <channel>`
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
# s.anonreport
Report something anonymously (don't include text to report via DM)<br/>
 - Usage: `s.anonreport <server> <text>`
Extended Arg Info
> ### server: Optional[discord.server.Guild]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
> ### text: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.botreport
Report something to the bot owner anonymously.<br/>
 - Usage: `s.botreport <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
