# s.selfrole
Base command to add/remove selfrole<br/>
 - Usage: `s.selfrole`
## /selfrole add (Slash Command)
Add a role to yourself.<br/>
 - Usage: `/selfrole add <role>`
 - `role:` (Required) …

 - Checks: `Server Only`
Extended Arg Info
> ### role: discord.role.Role
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## /selfrole remove (Slash Command)
Remove a role from yourself<br/>
 - Usage: `/selfrole remove <role>`
 - `role:` (Required) …

 - Checks: `Server Only`
Extended Arg Info
> ### role: discord.role.Role
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## /selfrole list (Slash Command)
List all self assignable role list.<br/>
 - Usage: `/selfrole list`
 - Checks: `Server Only`
# s.selfroleset
Base command to set selfrole list<br/>
 - Usage: `s.selfroleset`
## /selfroleset add (Slash Command)
Add a role to selfrole set<br/>
 - Usage: `/selfroleset add <role>`
 - `role:` (Required) …

 - Checks: `Server Only`
Extended Arg Info
> ### role: discord.role.Role
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## /selfroleset remove (Slash Command)
Remove a role from selfrole set<br/>
 - Usage: `/selfroleset remove <role>`
 - `role:` (Required) …

 - Checks: `Server Only`
Extended Arg Info
> ### role: discord.role.Role
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## /selfroleset allow_dangerous_role (Slash Command)
Allows roles with enhanced permissions to be added in selfrole list<br/>
 - Usage: `/selfroleset allow_dangerous_role <status>`
 - `status:` (Required) …

 - Checks: `Server Only`
Extended Arg Info
> ### status: bool
> - Autocomplete: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
