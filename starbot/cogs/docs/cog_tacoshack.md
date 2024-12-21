# s.tacoshack
Various TacoShack commands.<br/>
 - Usage: `s.tacoshack`
 - Aliases: `ts, shack, and taco`
## s.tacoshack found
Found your shack.<br/>
 - Usage: `s.tacoshack found`
 - Aliases: `create`
## s.tacoshack work
Work your shack.<br/>
 - Usage: `s.tacoshack work`
 - Aliases: `w`
 - Cooldown: `1 per 600.0 seconds`
## s.tacoshack daily
Collect daily reward.<br/>
 - Usage: `s.tacoshack daily`
 - Aliases: `d`
 - Cooldown: `1 per 86400.0 seconds`
## s.tacoshack reset
Reset your shack.<br/>
 - Usage: `s.tacoshack reset`
 - Aliases: `restart`
 - Cooldown: `1 per 3600.0 seconds`
## s.tacoshack shacks
List of all shacks.<br/>
 - Usage: `s.tacoshack shacks`
 - Checks: `server_only`
## s.tacoshack hire
Hire employees for your shack.<br/>
 - Usage: `s.tacoshack hire [id=None]`
Extended Arg Info
> ### id: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tacoshack tips
Collect tips from your shack.<br/>
 - Usage: `s.tacoshack tips`
 - Aliases: `t`
 - Cooldown: `1 per 300.0 seconds`
## s.tacoshack help
View all commands and their descriptions.<br/>
 - Usage: `s.tacoshack help`
## s.tacoshack buy
Buy upgrades for your shack.<br/>
 - Usage: `s.tacoshack buy <id>`
Extended Arg Info
> ### id
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tacoshack slogan
Set your shack slogan.<br/>
 - Usage: `s.tacoshack slogan <str>`
Extended Arg Info
> ### str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tacoshack deposit
Deposit bank currency into shack balance.<br/>
 - Usage: `s.tacoshack deposit <amount>`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## s.tacoshack withdraw
Withdraw shack balance into bank currency.<br/>
 - Usage: `s.tacoshack withdraw <amount>`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## s.tacoshack leaderboard
View the scoreboard.<br/>
 - Usage: `s.tacoshack leaderboard [show_global=False]`
 - Aliases: `scoreboard and top`
 - Checks: `server_only`
Extended Arg Info
> ### show_global: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.tacoshack balance
View your shack balance.<br/>
 - Usage: `s.tacoshack balance <user>`
Extended Arg Info
> ### user: Optional[discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
## s.tacoshack name
Name/rename your shack.<br/>
 - Usage: `s.tacoshack name <str>`
 - Aliases: `rename`
Extended Arg Info
> ### str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tacoshack shack
View your shack.<br/>
 - Usage: `s.tacoshack shack <user>`
 - Aliases: `myshack`
Extended Arg Info
> ### user: Optional[discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
## s.tacoshack upgrades
View upgrades for your shack.<br/>
 - Usage: `s.tacoshack upgrades`
 - Aliases: `upgrade and up`
