# s.memberhistory

 - Usage: `s.memberhistory`
 - Aliases: `memhis`
 - Checks: `server_only`
## s.memberhistory avatar
Scroll through the avatar history of a user.<br/>
 - Usage: `s.memberhistory avatar`
### s.memberhistory avatar server

 - Usage: `s.memberhistory avatar server [user=operator.attrgetter('author')] [page=1]`
Extended Arg Info
> ### user: discord.member.Member = operator.attrgetter('author')
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
### s.memberhistory avatar global

 - Usage: `s.memberhistory avatar global [user=operator.attrgetter('author')] [page=1]`
Extended Arg Info
> ### user: discord.member.Member = operator.attrgetter('author')
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
### s.memberhistory avatar decoration

 - Usage: `s.memberhistory avatar decoration [user=operator.attrgetter('author')] [page=1]`
 - Aliases: `deco, decor, and decorations`
Extended Arg Info
> ### user: discord.member.Member = operator.attrgetter('author')
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
## s.memberhistory ignore
Add a user or role to the ignore list.<br/>
 - Usage: `s.memberhistory ignore`
 - Restricted to: `ADMIN`
### s.memberhistory ignore server
Add a user or role to the ignore list.<br/>
 - Usage: `s.memberhistory ignore server <user_or_role>`
 - Restricted to: `ADMIN`
 - Aliases: `server`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
## s.memberhistory unignore
Remove a user or role from the ignore list.<br/>
 - Usage: `s.memberhistory unignore`
 - Restricted to: `ADMIN`
### s.memberhistory unignore server
Remove a user or role from the ignore list.<br/>
 - Usage: `s.memberhistory unignore server <user_or_role>`
 - Restricted to: `ADMIN`
 - Aliases: `server`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
## s.memberhistory toggle
Toggle the current state of member history.<br/>
 - Usage: `s.memberhistory toggle`
 - Restricted to: `GUILD_OWNER`
## s.memberhistory showsettings
See the configured settings and additional data about MemberHistory.<br/>
 - Usage: `s.memberhistory showsettings`
 - Restricted to: `ADMIN`
 - Aliases: `ss`
