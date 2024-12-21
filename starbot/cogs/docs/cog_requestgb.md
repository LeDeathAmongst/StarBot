# s.requestgb
Group for global ban request commands.<br/>
 - Usage: `s.requestgb [user_id=None] [proof]`
 - Aliases: `reqgb and rgb`
Extended Arg Info
> ### user_id: int = None
> ```
> A number without decimal places.
> ```
> ### proof: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.requestgb optout
Opt-out the server from the global ban feature.<br/>
 - Usage: `s.requestgb optout`
 - Restricted to: `GUILD_OWNER`
## s.requestgb setlog
Set the log channel for global ban approvals.<br/>
 - Usage: `s.requestgb setlog <channel>`
 - Restricted to: `GUILD_OWNER`
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
## s.requestgb optin
Opt-in the server to the global ban feature.<br/>
 - Usage: `s.requestgb optin`
 - Restricted to: `GUILD_OWNER`
