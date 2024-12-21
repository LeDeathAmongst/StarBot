# s.roleassigner
Role assigner, one role per user from a list of roles.<br/>
 - Usage: `s.roleassigner`
 - Restricted to: `MOD`
 - Aliases: `ra`
 - Checks: `server_only`
## s.roleassigner unassign
Remove roles on the list from users.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role (optional)<br/>
    Remove roles from members with a certain role. If this is not specified,<br/>
    then it will remove all roles on the list from ALL members of the server.<br/>
 - Usage: `s.roleassigner unassign [role=None]`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.roleassigner list
List roles for random assignment.<br/>
 - Usage: `s.roleassigner list`
 - Aliases: `ls`
## s.roleassigner assign
Randomly assign roles to members of the server.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role (optional)<br/>
    Apply to a subset of users with a certain role. If this is not specified,<br/>
    then it will apply one of the roles to ALL members of the server.<br/>
 - Usage: `s.roleassigner assign [role=None]`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.roleassigner remove
Remove a role to be randomly assigned.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role<br/>
    The role you wish to remove from the role assigner list.<br/>
 - Usage: `s.roleassigner remove <role>`
 - Aliases: `delete, del, and rm`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.roleassigner add
Add a role to be randomly assigned.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role<br/>
    The role you wish to add to the role assigner list.<br/>
 - Usage: `s.roleassigner add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.roleassigner random
Assign a role to some users from a certain role.<br/>

Pick `number` of users from fromRole at random, and assign assignRole to<br/>
those users.<br/>

Parameters:<br/>
-----------<br/>
assignRole: discord.Role<br/>
    The role you wish to assign to those members you just picked.<br/>
number: int<br/>
    The number of members you wish to randomly pick.<br/>
fromRole: discord.Role (optional)<br/>
    The role you wish to pick server members from. If this is not given,<br/>
    then it will pick from ALL server members.<br/>
excludeFromRole: discord.Role (optional)<br/>
    Any member with this role will not be considered for picking.<br/>
 - Usage: `s.roleassigner random <assignRole> <number> [fromRole=None] [excludeFromRole=None]`
Extended Arg Info
> ### assignRole: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### number: int
> ```
> A number without decimal places.
> ```
> ### fromRole: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### excludeFromRole: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
