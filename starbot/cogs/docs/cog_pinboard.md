# s.pinboard
Change the list of active pinned messages<br/>
 - Usage: `s.pinboard`
 - Checks: `server_only`
## s.pinboard remove
Remove your own content to a pinned message<br/>
 - Usage: `s.pinboard remove <pinnedMsgName>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.pinboard add
Add or edit your own content to a pinned message<br/>
 - Usage: `s.pinboard add <pinnedMsgName> <content>`
 - Aliases: `edit`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### content
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.setpinboard
Change the list of active pinned messages<br/>
 - Usage: `s.setpinboard`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setpinboard reset
⚠️ Reset all pinned messages<br/>

Type **`s.setpinboard reset True`** if you're really sure.<br/>
 - Usage: `s.setpinboard reset [areYouSure=False]`
Extended Arg Info
> ### areYouSure=False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setpinboard add
Create a new pinned message<br/>

pinnedMsgName is a label for the pinned message, so that you/others can easily refer back to it later. It should be a single word and short/easy to remember.<br/>
 - Usage: `s.setpinboard add <pinnedMsgName> <channel> <messageDescription>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### messageDescription
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setpinboard update
Update one or all pinned messages<br/>
 - Usage: `s.setpinboard update [pinnedMsgName=None] [repin=False]`
Extended Arg Info
> ### pinnedMsgName=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### repin=False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setpinboard remove
Remove a pinned message<br/>

The message stays behind, but it will be removed from the tracking system, so you can't update it anymore.<br/>
 - Usage: `s.setpinboard remove <pinnedMsgName>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setpinboard list
List all pinned messages<br/>
 - Usage: `s.setpinboard list`
## s.setpinboard edit
Edit description of a pinned message<br/>
 - Usage: `s.setpinboard edit <pinnedMsgName> <description>`
Extended Arg Info
> ### pinnedMsgName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setpinboard import
Import data<br/>
 - Usage: `s.setpinboard import <data>`
Extended Arg Info
> ### data
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
