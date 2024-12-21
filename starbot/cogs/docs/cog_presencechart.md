# s.presencechart (Hybrid Command)
Make a chart with the different Discord statuses (presence) of a Discord member, in the previous x days (last 100 days maximum).<br/>
 - Usage: `s.presencechart [days_number=30] [frame_mode=True] [member]`
 - Slash Usage: `/presencechart [days_number=30] [frame_mode=True] [member]`
 - Aliases: `statuschart and statuseschart`
Extended Arg Info
> ### frame_mode: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### member: discord.member.Member = operator.attrgetter('author')
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
## s.presencechart member (Hybrid Command)
Make a chart with the different Discord statuses (presence) of a Discord member, in the previous x days (last 100 days maximum).<br/>
 - Usage: `s.presencechart member [days_number=30] [frame_mode=True] [member]`
 - Slash Usage: `/presencechart member [days_number=30] [frame_mode=True] [member]`
 - Aliases: `user`
Extended Arg Info
> ### frame_mode: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### member: discord.member.Member = operator.attrgetter('author')
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
## s.presencechart role (Hybrid Command)
Make a chart with the different Discord statuses (presence) of all members of the specfied role.<br/>
 - Usage: `s.presencechart role [frame_mode=True] <role>`
 - Slash Usage: `/presencechart role [frame_mode=True] <role>`
Extended Arg Info
> ### frame_mode: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.presencechart ignoreme (Hybrid Command)
Asking PresenceChart to ignore your statuses (presence).<br/>
 - Usage: `s.presencechart ignoreme`
 - Slash Usage: `/presencechart ignoreme`
## s.presencechart server (Hybrid Command)
Make a chart with the different Discord statuses (presence) of all members of the server/server.<br/>
 - Usage: `s.presencechart server [frame_mode=True]`
 - Slash Usage: `/presencechart server [frame_mode=True]`
 - Aliases: `server`
Extended Arg Info
> ### frame_mode: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```
