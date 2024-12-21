# s.viewpermissions (Hybrid Command)
Display permissions for roles and members, at server level or in a specified channel.<br/>

- You can specify several roles and members, and their permissions will be added together.<br/>
- If you don't provide a channel, only permissions at the server level will be displayed.<br/>
- If you provide permission(s) and a channel, only these permissions will be displayed for this channel.<br/>
- If you provide permission(s) and no channel, all server channels will be displayed, with a tick if all the specified permissions are true in the channel.<br/>
- If you provide permission(s) and no mentionables, the everyone role is used.<br/>
 - Usage: `s.viewpermissions [advanced=False] [channel=None] [permissions=None] [mentionables=None]`
 - Slash Usage: `/viewpermissions [advanced=False] [channel=None] [permissions=None] [mentionables=None]`
 - Aliases: `viewperms and permsview`
 - Checks: `server_only`
Extended Arg Info
> ### advanced: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
