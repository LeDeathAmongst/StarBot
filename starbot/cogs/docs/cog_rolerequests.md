# s.request
Requests access to a role.<br/>
 - Usage: `s.request <role_name>`
 - Aliases: `iam and req`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.request clear
Clears all requestable roles.<br/>
 - Usage: `s.request clear`
 - Aliases: `clr`
 - Checks: `server_only`
## s.request postlist
Lists the roles that can be requested and posts them permanently to the specified channel.<br/>
 - Usage: `s.request postlist <channel>`
 - Restricted to: `MOD`
 - Aliases: `post_list`
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
## s.request add
Gives you a requestable role.<br/>
 - Usage: `s.request add <role_name>`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.request rem
Takes a requestable role.<br/>
 - Usage: `s.request rem <role_name>`
 - Aliases: `remove`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.request remrole
Removes a role from being requestable.<br/>
 - Usage: `s.request remrole <role_name>`
 - Restricted to: `MOD`
 - Aliases: `removerole`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.request massadd
Adds roles to all users who have participated in a channel within the last X messages.<br/>
 - Usage: `s.request massadd [limit=1000] [channel=None] <role_name>`
 - Restricted to: `MOD`
 - Aliases: `massapplyrole and massapply`
 - Checks: `server_only`
Extended Arg Info
> ### limit: int = 1000
> ```
> A number without decimal places.
> ```
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.request addrole
Adds a role to be requestable.<br/>
 - Usage: `s.request addrole <role_name>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### role_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.request list
Lists the roles that can be requested.<br/>
 - Usage: `s.request list`
 - Checks: `server_only`
# s.reqset
Adjust s.request command settings.<br/>
 - Usage: `s.reqset`
 - Restricted to: `MOD`
 - Checks: `server_only`
## s.reqset show_member_count
Whether to show or hide the number of users who currently have the role in successful s.request commands and the role list.<br/>

For value, pass in "true" or "false".<br/>
Omit the value to toggle.<br/>
Using the aliases with "hide" at the start inverts the value passed in.<br/>
 - Usage: `s.reqset show_member_count [value=None]`
 - Restricted to: `MOD`
 - Aliases: `hide_member_count, show_stats, and hide_stats`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.reqset request_channel
Where `s.request list` commands say to use the `s.request` command. Use the command without a channel argument to set to no channel.<br/>
 - Usage: `s.reqset request_channel [channel=None]`
 - Restricted to: `MOD`
 - Aliases: `req_channel and channel`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.reqset max_requestable
Maximum number of roles that users can request.<br/>

If set to -1, there is no limit.<br/>
 - Usage: `s.reqset max_requestable <count>`
 - Restricted to: `MOD`
 - Aliases: `max_req and max`
 - Checks: `server_only`
Extended Arg Info
> ### count: int
> ```
> A number without decimal places.
> ```
## s.reqset auto_post_list
Whether to automatically update existing post_list posts when roles or counts change.<br/>

For value, pass in "true" or "false".<br/>
Omit the value to toggle.<br/>
 - Usage: `s.reqset auto_post_list [value=None]`
 - Restricted to: `MOD`
 - Aliases: `auto_postlist`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
