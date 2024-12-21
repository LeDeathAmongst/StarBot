# s.otherbot
Otherbot configuration options.<br/>
 - Usage: `s.otherbot`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.otherbot channel
Sets the channel to report in.<br/>

Default to the current one.<br/>
 - Usage: `s.otherbot channel [channel=None]`
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
## s.otherbot pingrole
Sets the role to use for pinging. Leave blank to reset it.<br/>
 - Usage: `s.otherbot pingrole [role_name=None]`
Extended Arg Info
> ### role_name: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.otherbot watch
Watch settings.<br/>
 - Usage: `s.otherbot watch`
 - Aliases: `watching`
### s.otherbot watch online
Manage online notifications.<br/>
 - Usage: `s.otherbot watch online`
#### s.otherbot watch online add
Add a bot that will be tracked when it comes back online.<br/>
 - Usage: `s.otherbot watch online add <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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
#### s.otherbot watch online emoji
Choose which emoji that will be used for online messages.<br/>
 - Usage: `s.otherbot watch online emoji [emoji]`
Extended Arg Info
> ### emoji: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### s.otherbot watch online list
Lists currently tracked bots.<br/>
 - Usage: `s.otherbot watch online list`
#### s.otherbot watch online remove
Removes a bot currently tracked.<br/>
 - Usage: `s.otherbot watch online remove <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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
#### s.otherbot watch online embed
Set wether you want to receive notifications in embed or not.<br/>
 - Usage: `s.otherbot watch online embed`
### s.otherbot watch offline
Manage offline notifications.<br/>
 - Usage: `s.otherbot watch offline`
#### s.otherbot watch offline embed
Set wether you want to receive notifications in embed or not.<br/>
 - Usage: `s.otherbot watch offline embed`
#### s.otherbot watch offline remove
Removes a bot currently tracked.<br/>
 - Usage: `s.otherbot watch offline remove <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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
#### s.otherbot watch offline emoji
Choose which emoji that will be used for offline messages.<br/>
 - Usage: `s.otherbot watch offline emoji [emoji]`
Extended Arg Info
> ### emoji: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### s.otherbot watch offline add
Add a bot that will be tracked when it goes offline.<br/>
 - Usage: `s.otherbot watch offline add <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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
#### s.otherbot watch offline list
Lists currently tracked bots.<br/>
 - Usage: `s.otherbot watch offline list`
