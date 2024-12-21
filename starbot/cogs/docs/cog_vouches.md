# s.vouches (Hybrid Command)

 - Usage: `s.vouches <user>`
 - Slash Usage: `/vouches <user>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
# s.addvouch (Hybrid Command)

 - Usage: `s.addvouch <user> <number>`
 - Slash Usage: `/addvouch <user> <number>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
> ### number: int
> ```
> A number without decimal places.
> ```
# s.removevouch (Hybrid Command)

 - Usage: `s.removevouch <user> <number>`
 - Slash Usage: `/removevouch <user> <number>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
> ### number: int
> ```
> A number without decimal places.
> ```
# s.vouchleaderboard (Hybrid Command)

 - Usage: `s.vouchleaderboard`
 - Slash Usage: `/vouchleaderboard`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
# s.setvouchchannel (Hybrid Command)

 - Usage: `s.setvouchchannel <channel>`
 - Slash Usage: `/setvouchchannel <channel>`
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
# s.setvouchroles (Hybrid Command)

 - Usage: `s.setvouchroles <role1> [role2=None] [role3=None] [role4=None] [role5=None]`
 - Slash Usage: `/setvouchroles <role1> [role2=None] [role3=None] [role4=None] [role5=None]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### role1: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### role2: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### role3: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### role4: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### role5: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
