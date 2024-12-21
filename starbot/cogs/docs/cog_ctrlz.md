# s.ctrlz (Hybrid Command)
Revert some actions in servers, from the audit logs.<br/>
 - Usage: `s.ctrlz`
 - Slash Usage: `/ctrlz`
 - Restricted to: `GUILD_OWNER`
 - Checks: `bot_has_server_permissions and server_only`
## s.ctrlz view (Hybrid Command)
View the audit logs that can be reverted.<br/>
 - Usage: `s.ctrlz view [include_already_reverted=True] [displayed_actions=None] [user=None] [after=None] [before=None]`
 - Slash Usage: `/ctrlz view [include_already_reverted=True] [displayed_actions=None] [user=None] [after=None] [before=None]`
 - Checks: `bot_has_server_permissions and server_only`
Extended Arg Info
> ### include_already_reverted: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### user: Optional[discord.user.User] = None
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
## s.ctrlz mass (Hybrid Command)
Revert all the audit logs that can be reverted.<br/>

You can choose the audit logs to ignore.<br/>
 - Usage: `s.ctrlz mass [displayed_actions=None] [user=None] [after=None] [before=None]`
 - Slash Usage: `/ctrlz mass [displayed_actions=None] [user=None] [after=None] [before=None]`
 - Checks: `bot_has_server_permissions and server_only`
Extended Arg Info
> ### user: Optional[discord.user.User] = None
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
