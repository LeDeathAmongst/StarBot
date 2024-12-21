# s.talk
Notification related commands.<br/>
 - Usage: `s.talk`
 - Aliases: `talknotifier`
## s.talk setmessage
Set the notification message for the server.<br/>
 - Usage: `s.talk setmessage <message>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.talk setcooldown
Set the cooldown period for notifications.<br/>
 - Usage: `s.talk setcooldown <cooldown>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### cooldown: int
> ```
> A number without decimal places.
> ```
## s.talk listusers
List all users who are set to receive notifications.<br/>
 - Usage: `s.talk listusers`
 - Restricted to: `ADMIN`
## s.talk clearusers
Clear all target users from the notification list.<br/>
 - Usage: `s.talk clearusers`
 - Restricted to: `ADMIN`
## s.talk removeuser
Remove a user from the target list for notifications.<br/>
 - Usage: `s.talk removeuser <user>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### user: discord.member.Member
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
## s.talk adduser
Add a user to the target list for notifications.<br/>
 - Usage: `s.talk adduser <user>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### user: discord.member.Member
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
## s.talk showmessage
Display the current notification message.<br/>
 - Usage: `s.talk showmessage`
 - Restricted to: `ADMIN`
