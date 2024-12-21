# s.theme
Play, view, or configure a user's set theme song(s).<br/>
 - Usage: `s.theme [user]`
 - Aliases: `themes`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.user.User = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## s.theme clear
Clear your list of themes.<br/>

⚠ This action cannot be undone.<br/>
 - Usage: `s.theme clear`
## s.theme add
Adds the specified themes to your theme list.<br/>

Comma-seperated list.<br/>
 - Usage: `s.theme add <new_themes>`
## s.theme list
Lists your currently set themes.<br/>
 - Usage: `s.theme list [user]`
Extended Arg Info
> ### user: discord.user.User = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## s.theme play
Play a user's set theme song(s).<br/>
 - Usage: `s.theme play [user]`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.user.User = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## s.theme remove
Removes the specified themes from your theme list.<br/>

Comma-seperated list.<br/>
 - Usage: `s.theme remove <themes_to_remove>`
