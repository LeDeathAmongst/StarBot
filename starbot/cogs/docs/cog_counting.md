# s.counting (Hybrid Command)
Counting commands<br/>
 - Usage: `s.counting`
 - Slash Usage: `/counting`
 - Checks: `server_only`
## s.counting countstats (Hybrid Command)
Get your current counting statistics.<br/>
 - Usage: `s.counting countstats [user=None]`
 - Slash Usage: `/counting countstats [user=None]`
 - Aliases: `stats`
 - Cooldown: `1 per 10.0 seconds`
 - Checks: `server_only`
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
## s.counting resetme (Hybrid Command)
Reset your counting stats.<br/>
 - Usage: `s.counting resetme`
 - Slash Usage: `/counting resetme`
 - Checks: `server_only`
# s.countingset
Counting settings commands.<br/>
 - Usage: `s.countingset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.countingset channel
Set the counting channel<br/>
 - Usage: `s.countingset channel <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.countingset togglemessage
Toggle to show a message for a specific setting.<br/>

Available settings: edit, count<br/>

`count` - Show the next number message when a user sends an incorrect number. Default is disabled<br/>
`edit` - Shows a message when a user edits their message in the counting channel. Default is disabled<br/>
 - Usage: `s.countingset togglemessage <setting>`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.countingset togglereact
Toggle the reactions for correct numbers.<br/>
 - Usage: `s.countingset togglereact`
## s.countingset deleteafter
Set the number of seconds to delete the incorrect message<br/>

Default is 5 seconds<br/>
 - Usage: `s.countingset deleteafter <seconds>`
## s.countingset settings
Show the current counting settings.<br/>
 - Usage: `s.countingset settings`
## s.countingset togglesilent
Toggle silent mode for counting messages.<br/>

Silent is discords new feature.<br/>
 - Usage: `s.countingset togglesilent`
## s.countingset reset
Reset the settings for the counting.<br/>
 - Usage: `s.countingset reset`
## s.countingset togglesameuser
Toggle whether the same user can count more than once consecutively.<br/>

Users cannot count consecutively if this is enabled meaning they have to wait for someone else to count.<br/>
 - Usage: `s.countingset togglesameuser`
## s.countingset setmessage
Set the default message for a specific type.<br/>

Available message types: edit, count<br/>

`edit` - The message to show when a user edits their message in the counting channel.<br/>
`count` - The message to show when a user sends an incorrect number in the counting channel.<br/>

**Examples:**<br/>
- `s.countingset setmessage edit You can't edit your messages here.`<br/>
- `s.countingset setmessage count Next number should be {next_count}`<br/>

**Arguments:**<br/>
- `<message_type>` The type of message to set (edit or count).<br/>
- `<message>` The message to set.<br/>
 - Usage: `s.countingset setmessage <message_type> <message>`
Extended Arg Info
> ### message_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.countingset setreaction
Set the reaction for correct numbers.<br/>
 - Usage: `s.countingset setreaction <emoji_input>`
Extended Arg Info
> ### emoji_input: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.countingset toggle
Toggle counting in the channel<br/>
 - Usage: `s.countingset toggle`
