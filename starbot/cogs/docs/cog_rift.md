# s.send
Send a message to the specified destinations.<br/>

Editing or deleting the message you send will still forward<br/>
to the bot's reposts, as in normal rifts.<br/>
 - Usage: `s.send <rifts>`
# s.rift
Communicate with other channels through Red.<br/>
 - Usage: `s.rift`
## s.rift close
Closes all rifts that lead to this channel.<br/>
 - Usage: `s.rift close`
### s.rift close server
Closes all rifts that lead to this server.<br/>
 - Usage: `s.rift close server`
 - Aliases: `server`
 - Checks: `server_only`
## s.rift info
Provides info about rifts opened in the specified scope.<br/>
 - Usage: `s.rift info [scope]`
Extended Arg Info
> ### scope: str = 'channel'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rift blocklist
Configures blocklists.<br/>

Blocklisted destinations cannot have rifts opened to them.<br/>
 - Usage: `s.rift blocklist`
 - Aliases: `denylist and blacklist`
### s.rift blocklist channel
Blocklists the current channel or the specified channel.<br/>

Can also blocklist DM channels.<br/>
 - Usage: `s.rift blocklist channel [channel]`
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
### s.rift blocklist server
Blocklists the current server.<br/>

All channels and members in a server are considered blocklisted if the server is blocklisted.<br/>
Members can still be reached if they are in another, non-blocklisted server.<br/>
 - Usage: `s.rift blocklist server`
 - Restricted to: `ADMIN`
 - Aliases: `server`
 - Checks: `server_only`
## s.rift link
Links this channel to the specified destination(s).<br/>

Anything anyone says in this channel will be forwarded.<br/>
All replies will be relayed back here.<br/>
 - Usage: `s.rift link [one_way=None] <rifts>`
Extended Arg Info
> ### one_way: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.rift open
Opens a rift to the specified destination(s).<br/>

Only your messages will be forwarded to the specified destinations,<br/>
and all replies will be sent back to you.<br/>
 - Usage: `s.rift open [one_way=None] <rifts>`
Extended Arg Info
> ### one_way: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
