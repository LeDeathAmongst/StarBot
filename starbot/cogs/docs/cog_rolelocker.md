# s.rolelock
Base command for locking commands or cogs.<br/>
 - Usage: `s.rolelock`
 - Restricted to: `ADMIN`
## s.rolelock command
Lock a specific command behind roles.<br/>
 - Usage: `s.rolelock command <command_name> <roles>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.rolelock removecommand
Remove a command from being locked.<br/>
 - Usage: `s.rolelock removecommand <command_name>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rolelock tierinfo
Display detailed information about a specific tier.<br/>
 - Usage: `s.rolelock tierinfo <tier_name>`
Extended Arg Info
> ### tier_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rolelock cleartier
Clear all roles from the specified tier.<br/>
 - Usage: `s.rolelock cleartier <tier_name>`
Extended Arg Info
> ### tier_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rolelock tierlist
List all tiers and the roles in them.<br/>
 - Usage: `s.rolelock tierlist`
## s.rolelock removecog
Remove a cog from being locked.<br/>
 - Usage: `s.rolelock removecog <cog_name>`
Extended Arg Info
> ### cog_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rolelock cog
Lock an entire cog behind roles.<br/>
 - Usage: `s.rolelock cog <cog_name> <roles>`
Extended Arg Info
> ### cog_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
