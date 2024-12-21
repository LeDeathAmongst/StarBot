# s.away
Tell the bot you're away or back.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
 - Usage: `s.away [delete_after=None] [message]`
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.idle
Set an automatic reply when you're idle.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
 - Usage: `s.idle [delete_after=None] [message]`
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.offline
Set an automatic reply when you're offline.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
 - Usage: `s.offline [delete_after=None] [message]`
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.dnd
Set an automatic reply when you're dnd.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
 - Usage: `s.dnd [delete_after=None] [message]`
 - Aliases: `donotdisturb`
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.streaming
Set an automatic reply when you're streaming.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
 - Usage: `s.streaming [delete_after=None] [message]`
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.listening
Set an automatic reply when you're listening to Spotify.<br/>

`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>
 - Usage: `s.listening [delete_after=None] [message]`
Extended Arg Info
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = ' '
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.gaming
Set an automatic reply when you're playing a specified game.<br/>

`game` The game you would like automatic responses for<br/>
`delete_after` Optional seconds to delete the automatic reply. Must be minimum 5 seconds<br/>
`message` The custom message to display when you're mentioned<br/>

Use "double quotes" around a game's name if it is more than one word.<br/>
 - Usage: `s.gaming <game> [delete_after=None] [message]`
Extended Arg Info
> ### game: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### delete_after: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.toggleaway
Toggle away messages on the whole server or a specific server member.<br/>

Mods, Admins and Bot Owner are immune to this.<br/>
 - Usage: `s.toggleaway [member=None]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member = None
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
# s.awaytextonly
Toggle forcing the server's away messages to be text only.<br/>

This overrides the embed_links check this cog uses for message sending.<br/>
 - Usage: `s.awaytextonly`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
# s.awaysettings
View your current away settings<br/>
 - Usage: `s.awaysettings`
 - Aliases: `awayset`
