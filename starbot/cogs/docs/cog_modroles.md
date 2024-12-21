# s.assignrole
Assign a role to a member.<br/>

NOTE: The role is case sensitive!<br/>
 - Usage: `s.assignrole <role> <member>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
# s.unassignrole
Unassign a role from a member.<br/>

NOTE: The role is case sensitive!<br/>
 - Usage: `s.unassignrole <role> <member>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
# s.modroles
Settings for assignable roles.<br/>
 - Usage: `s.modroles`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.modroles targets
Settings about allowed targets.<br/>
 - Usage: `s.modroles targets`
### s.modroles targets allowbots
Allow to assign roles to bots with `s.assignrole`<br/>

Leave empty to check current settings.<br/>
 - Usage: `s.modroles targets allowbots [enabled=None]`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.modroles targets toprole
Enable/disable top role check.<br/>

When enabled, this will only allow user to assign roles to users<br/>
with lower top role than theirs.<br/>

Leave empty to check current settings.<br/>
 - Usage: `s.modroles targets toprole [enabled=None]`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.modroles remove
Remove assignable role.<br/>
 - Usage: `s.modroles remove <role>`
## s.modroles add
Add assignable role.<br/>
 - Usage: `s.modroles add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.modroles list
List assignable roles.<br/>
 - Usage: `s.modroles list`
