# s.spam
Spam a message in a channel a specified number of times.<br/>
 - Usage: `s.spam <channel> <amount> <message>`
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
> ### amount: int
> ```
> A number without decimal places.
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.ghostping
Ghostping a member in a specified channel.<br/>
 - Usage: `s.ghostping <member> <channel> [amount=1] [interval=1]`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### amount: int = 1
> ```
> A number without decimal places.
> ```
> ### interval: int = 1
> ```
> A number without decimal places.
> ```
# s.stopghostping
Stop the ghostping task.<br/>
 - Usage: `s.stopghostping`
 - Checks: `server_only`
