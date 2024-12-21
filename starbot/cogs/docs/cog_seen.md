# s.seen (Hybrid Command)
Check when a member/role/channel/category was last active!<br/>
 - Usage: `s.seen <_type> <show_details> <_object>`
 - Slash Usage: `/seen <_type> <show_details> <_object>`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### _object: Union[discord.member.Member, discord.role.Role, discord.channel.TextChannel, discord.channel.CategoryChannel]
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
## s.seen ignoreme (Hybrid Command)
Asking Seen to ignore your actions.<br/>
 - Usage: `s.seen ignoreme`
 - Slash Usage: `/seen ignoreme`
## s.seen category (Hybrid Command)
Check when a category was last active!<br/>
 - Usage: `s.seen category <_type> <show_details> [category=None]`
 - Slash Usage: `/seen category <_type> <show_details> [category=None]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### category: Optional[discord.channel.CategoryChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.seen member (Hybrid Command)
Check when a member was last active!<br/>
 - Usage: `s.seen member <_type> <show_details> [member]`
 - Slash Usage: `/seen member <_type> <show_details> [member]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### member: Optional[discord.member.Member] = None
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
## s.seen role (Hybrid Command)
Check when a role was last active!<br/>
 - Usage: `s.seen role <_type> <show_details> [role]`
 - Slash Usage: `/seen role <_type> <show_details> [role]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.seen server (Hybrid Command)
Check when a server was last active!<br/>
 - Usage: `s.seen server <_type> <show_details> [server]`
 - Slash Usage: `/seen server <_type> <show_details> [server]`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.seen board (Hybrid Command)
View a Seen Board for members/roles/channels/categories/servers/users!<br/>

`bots` is a parameter for `members` and `users`. `include_role` and `exclude_role` are parameters for only `members`.<br/>
 - Usage: `s.seen board <_type> [_object=members] [reverse=False] [bots=None] [include_role=None] [exclude_role=None]`
 - Slash Usage: `/seen board <_type> [_object=members] [reverse=False] [bots=None] [include_role=None] [exclude_role=None]`
 - Checks: `server_only`
Extended Arg Info
> ### reverse: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### bots: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### include_role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### exclude_role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.seen channel (Hybrid Command)
Check when a channel was last active!<br/>
 - Usage: `s.seen channel <_type> <show_details> [channel=None]`
 - Slash Usage: `/seen channel <_type> <show_details> [channel=None]`
 - Checks: `server_only`
Extended Arg Info
> ### show_details: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
