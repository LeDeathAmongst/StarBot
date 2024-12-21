# s.bl
Commands to manage the blacklist.<br/>
 - Usage: `s.bl`
 - Checks: `server_only`
## s.bl addtrustedrole
Add a role to the trusted roles list.<br/>
 - Usage: `s.bl addtrustedrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.bl check
Check if a user is in the blacklist.<br/>
 - Usage: `s.bl check <user>`
Extended Arg Info
> ### user: discord.user.User
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
## s.bl add
Add a user to the blacklist with a link.<br/>
 - Usage: `s.bl add <user> <link>`
Extended Arg Info
> ### user: discord.user.User
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
> ### link: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.bl remove
Remove a user from the blacklist.<br/>
 - Usage: `s.bl remove <user>`
Extended Arg Info
> ### user: discord.user.User
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
## s.bl removetrustedrole
Remove a role from the trusted roles list.<br/>
 - Usage: `s.bl removetrustedrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.bl list
List all blacklisted users.<br/>
 - Usage: `s.bl list`
