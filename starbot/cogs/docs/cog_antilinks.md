# s.antilinks
Configuration options.<br/>
 - Usage: `s.antilinks`
 - Restricted to: `MOD`
 - Aliases: `nolinks, nolink, antilink, and alset`
 - Checks: `server_only`
## s.antilinks watch
Add/remove/list channels to watch.<br/>

- If added, links will be removed in these channels.<br/>
 - Usage: `s.antilinks watch <add_or_remove> [channels=None]`
### s.antilinks watch list
List the channels being watched.<br/>
 - Usage: `s.antilinks watch list`
## s.antilinks whitelist
Whitelist options.<br/>
 - Usage: `s.antilinks whitelist`
### s.antilinks whitelist role
Add or remove roles from the whitelist.<br/>
 - Usage: `s.antilinks whitelist role <add_or_remove> [roles=None]`
#### s.antilinks whitelist role list
List whitelisted roles.<br/>
 - Usage: `s.antilinks whitelist role list`
 - Aliases: `view`
### s.antilinks whitelist user
Add or remove users from the whitelist.<br/>
 - Usage: `s.antilinks whitelist user <add_or_remove> [members=None]`
#### s.antilinks whitelist user list
List whitelisted users.<br/>
 - Usage: `s.antilinks whitelist user list`
## s.antilinks channel
Set the message transfer channel.<br/>

Leave the channel blank to turn it off.<br/>
 - Usage: `s.antilinks channel [channel=None]`
 - Aliases: `chan`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
