# s.nick
Forcibly change a user's nickname to a predefined string.<br/>
 - Usage: `s.nick <user> <reason>`
 - Restricted to: `MOD`
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
> ### reason: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.cnick
Forcibly change a user's nickname.<br/>
 - Usage: `s.cnick <user> <nickname> <reason>`
 - Restricted to: `MOD`
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
> ### nickname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.freezenick
Freeze a users nickname.<br/>
 - Usage: `s.freezenick <user> <nickname> [reason]`
 - Restricted to: `MOD`
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
> ### nickname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: Optional[str] = 'Nickname frozen.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.unfreezenick
Unfreeze a user's nickname.<br/>
 - Usage: `s.unfreezenick <user>`
 - Restricted to: `MOD`
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
# s.tempnick
Temporarily rename a user.<br/>
**IMPORTANT**: For better performance, temporary nicknames are checked in a 10 minute intervall.<br/>
 - Usage: `s.tempnick <user> <duration> <nickname> [reason]`
 - Restricted to: `MOD`
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
> ### nickname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: Optional[str] = 'User has been temporarily renamed.'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.nickset
Nicknamer settings<br/>
 - Usage: `s.nickset`
 - Restricted to: `ADMIN`
## s.nickset name
Set the default name that will be applied when using ``s.nick``<br/>
 - Usage: `s.nickset name <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.nickset modlog
Set if you would like to create a modlog entry everytime a nickname is being changed.<br/>
 - Usage: `s.nickset modlog <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.nickset dm
Set if you would like the bot to DM the user who's nickname was changed.<br/>
 - Usage: `s.nickset dm <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.nickpurge
Remove all nicknames in the server.<br/>
 - Usage: `s.nickpurge <are_you_sure>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### are_you_sure: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
