# s.globalbanlist (Hybrid Command)
Manage the global ban list.<br/>
 - Usage: `s.globalbanlist`
 - Slash Usage: `/globalbanlist`
 - Aliases: `gbl`
## s.globalbanlist subscribe (Hybrid Command)
Subscribe to a specific ban list.<br/>
 - Usage: `s.globalbanlist subscribe <list_name>`
 - Slash Usage: `/globalbanlist subscribe <list_name>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.globalbanlist setgenerallog (Hybrid Command)
Set the channel for general logging in this server.<br/>
 - Usage: `s.globalbanlist setgenerallog <channel>`
 - Slash Usage: `/globalbanlist setgenerallog <channel>`
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
## s.globalbanlist history (Hybrid Command)
Display the history of a specific ban list.<br/>
 - Usage: `s.globalbanlist history <list_name>`
 - Slash Usage: `/globalbanlist history <list_name>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.globalbanlist remove (Hybrid Command)
Remove a user from a specific ban list.<br/>
 - Usage: `s.globalbanlist remove <list_name> <user>`
 - Slash Usage: `/globalbanlist remove <list_name> <user>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### user: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.globalbanlist add (Hybrid Command)
Add a user to a specific ban list.<br/>
 - Usage: `s.globalbanlist add <list_name> <user> <reason_and_proof>`
 - Slash Usage: `/globalbanlist add <list_name> <user> <reason_and_proof>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason_and_proof: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.globalbanlist appeal (Hybrid Command)
Submit an appeal for a global ban.<br/>
 - Usage: `s.globalbanlist appeal`
 - Slash Usage: `/globalbanlist appeal`
## s.globalbanlist list (Hybrid Command)
List all users in a specific ban list or show available lists.<br/>
 - Usage: `s.globalbanlist list [list_name=None]`
 - Slash Usage: `/globalbanlist list [list_name=None]`
Extended Arg Info
> ### list_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.globalbanlist unsubscribe (Hybrid Command)
Unsubscribe from a specific ban list.<br/>
 - Usage: `s.globalbanlist unsubscribe <list_name>`
 - Slash Usage: `/globalbanlist unsubscribe <list_name>`
Extended Arg Info
> ### list_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
