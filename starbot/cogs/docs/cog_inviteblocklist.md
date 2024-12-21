# s.inviteblock
Settings for managing invite link blocking<br/>
 - Usage: `s.inviteblock`
 - Restricted to: `MOD`
 - Aliases: `ibl and inviteblocklist`
## s.inviteblock immunity
Commands for fine tuning allowed channels, users, or roles<br/>
 - Usage: `s.inviteblock immunity`
 - Aliases: `immune`
### s.inviteblock immunity remove
Add a server ID to the allowlist, providing an invite link will also work<br/>

`[channel_user_role...]` is the channel, user or role to remove from the whitelist<br/>
(You can supply more than one of any at a time)<br/>
 - Usage: `s.inviteblock immunity remove <channel_user_role>`
 - Aliases: `del and rem`
### s.inviteblock immunity info
Show what channels, users, and roles are in the invite link allowlist<br/>
 - Usage: `s.inviteblock immunity info`
### s.inviteblock immunity add
Add a server ID to the allowlist, providing an invite link will also work<br/>

`[channel_user_role...]` is the channel, user or role to whitelist<br/>
(You can supply more than one of any at a time)<br/>
 - Usage: `s.inviteblock immunity add <channel_user_role>`
## s.inviteblock blocklist
Commands for setting the blocklist<br/>
 - Usage: `s.inviteblock blocklist`
 - Aliases: `blacklist, bl, and block`
### s.inviteblock blocklist add
Add a server ID to the blocklist, providing an invite link will also work<br/>

`[invite_or_server_id]` The server ID or invite to the server you want to have<br/>
invite links blocked from.<br/>
 - Usage: `s.inviteblock blocklist add <invite_or_server_id>`
Extended Arg Info
> ### *invite_or_server_id: Union[discord.invite.Invite, discord.server.Guild, int]
> Converts to a :class:`~discord.Invite`.
> 
>     This is done via an HTTP request using :meth:`.Bot.fetch_invite`.
> 
>     
### s.inviteblock blocklist list
Show which servers were added to the blocklist and who added them<br/>
 - Usage: `s.inviteblock blocklist list`
### s.inviteblock blocklist info
Show what server ID's are in the invite link blocklist<br/>
 - Usage: `s.inviteblock blocklist info`
### s.inviteblock blocklist remove
Add a server ID to the blocklist, providing an invite link will also work<br/>

`[invite_or_server_id]` The server ID or invite to the server you not longer want to have<br/>
invite links blocked from.<br/>
 - Usage: `s.inviteblock blocklist remove <thing_to_block>`
 - Aliases: `del and rem`
Extended Arg Info
> ### *thing_to_block: Union[discord.invite.Invite, discord.server.Guild, int]
> Converts to a :class:`~discord.Invite`.
> 
>     This is done via an HTTP request using :meth:`.Bot.fetch_invite`.
> 
>     
## s.inviteblock blockall
Automatically remove all invites regardless of their destination<br/>
 - Usage: `s.inviteblock blockall <set_to>`
 - Restricted to: `MOD`
Extended Arg Info
> ### set_to: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.inviteblock allowlist
Commands for setting the blocklist<br/>
 - Usage: `s.inviteblock allowlist`
 - Aliases: `whitelist, wl, al, and allow`
### s.inviteblock allowlist info
Show what server ID's are in the invite link allowlist<br/>
 - Usage: `s.inviteblock allowlist info`
### s.inviteblock allowlist add
Add a server ID to the allowlist, providing an invite link will also work<br/>

`[invite_or_server_id]` The server ID or invite to the server you want to have<br/>
invites allowed from.<br/>
 - Usage: `s.inviteblock allowlist add <invite_or_server_id>`
Extended Arg Info
> ### *invite_or_server_id: Union[discord.invite.Invite, discord.server.Guild, int]
> Converts to a :class:`~discord.Invite`.
> 
>     This is done via an HTTP request using :meth:`.Bot.fetch_invite`.
> 
>     
### s.inviteblock allowlist remove
Add a server ID to the allowlist, providing an invite link will also work<br/>

`[invite_or_server_id]` The server ID or invite to the server you not longer want to have<br/>
invites allowed from.<br/>
 - Usage: `s.inviteblock allowlist remove <invite_or_server_id>`
 - Aliases: `del and rem`
Extended Arg Info
> ### *invite_or_server_id: Union[discord.invite.Invite, discord.server.Guild, int]
> Converts to a :class:`~discord.Invite`.
> 
>     This is done via an HTTP request using :meth:`.Bot.fetch_invite`.
> 
>     
