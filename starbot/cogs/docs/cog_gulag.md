# s.gulag (Hybrid Command)
Sends a member to the gulag.<br/>

> This will take away all roles of a member and give them the gulag role.<br/>
 - Usage: `s.gulag <member>`
 - Slash Usage: `/gulag <member>`
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
# s.bail (Hybrid Command)
Releases a member from the gulag.<br/>

> This will take away gulag role and give back the roles the member previously had.<br/>
 - Usage: `s.bail <member>`
 - Slash Usage: `/bail <member>`
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
# s.gulagset
Commands for gulag management.<br/>
 - Usage: `s.gulagset`
## s.gulagset channel
Configures the gulag channel.<br/>
 - Usage: `s.gulagset channel <channel>`
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
## s.gulagset clear
Resets the gulag role and channel.<br/>
 - Usage: `s.gulagset clear`
## s.gulagset role
Configures the gulag role.<br/>
 - Usage: `s.gulagset role <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
