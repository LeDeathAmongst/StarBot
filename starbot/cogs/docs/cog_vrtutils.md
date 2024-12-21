# /latency (Slash Command)
Return the bot's latency.<br/>
 - Usage: `/latency`
# s.todorefresh
Refresh a todo list channel.<br/>

Bring all messages without a ✅ or ❌ to the front of the channel.<br/>

**WARNING**: DO NOT USE THIS COMMAND IN A BUSY CHANNEL.<br/>
 - Usage: `s.todorefresh <confirm>`
 - Restricted to: `MOD`
 - Aliases: `refreshtodo`
Extended Arg Info
> ### confirm: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.text2binary
Convert text to binary<br/>
 - Usage: `s.text2binary <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.binary2text
Convert a binary string to text<br/>
 - Usage: `s.binary2text <binary_string>`
Extended Arg Info
> ### binary_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.randomnum
Generate a random number between the numbers specified<br/>
 - Usage: `s.randomnum [minimum=1] [maximum=100]`
 - Aliases: `rnum`
Extended Arg Info
> ### minimum: int = 1
> ```
> A number without decimal places.
> ```
> ### maximum: int = 100
> ```
> A number without decimal places.
> ```
# s.reactmsg
Add a reaction to a message<br/>
 - Usage: `s.reactmsg <emoji> [message=None]`
 - Restricted to: `MOD`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### message: discord.message.Message = None
> Converts to a :class:`discord.Message`.
> 
>     
# s.closestuser
Find the closest fuzzy match for a user<br/>
 - Usage: `s.closestuser <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.getuser
Find a user by ID<br/>
 - Usage: `s.getuser <user_id>`
 - Aliases: `finduser`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
# s.getbanner
Get a user's banner<br/>
 - Usage: `s.getbanner [user=None]`
Extended Arg Info
> ### user: Union[discord.member.Member, int, NoneType] = None
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
# s.getwebhook
Find a webhook by ID<br/>
 - Usage: `s.getwebhook <webhook_id>`
Extended Arg Info
> ### webhook_id: int
> ```
> A number without decimal places.
> ```
# s.oldestchannels
See which channel is the oldest<br/>
 - Usage: `s.oldestchannels [amount=10]`
 - Checks: `server_only`
Extended Arg Info
> ### amount: int = 10
> ```
> A number without decimal places.
> ```
# s.oldestmembers
See which users have been in the server the longest<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
 - Usage: `s.oldestmembers [amount=10] [include_bots=False]`
 - Aliases: `oldestusers`
 - Checks: `server_only`
Extended Arg Info
> ### amount: Optional[int] = 10
> ```
> A number without decimal places.
> ```
> ### include_bots: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.oldestaccounts
See which users have the oldest Discord accounts<br/>

**Arguments**<br/>
`amount:` how many members to display<br/>
`include_bots:` (True/False) whether to include bots<br/>
 - Usage: `s.oldestaccounts [amount=10] [include_bots=False]`
 - Checks: `server_only`
Extended Arg Info
> ### amount: Optional[int] = 10
> ```
> A number without decimal places.
> ```
> ### include_bots: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.rolemembers
View all members that have a specific role<br/>
 - Usage: `s.rolemembers <role>`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# s.wipevcs
Clear all voice channels from a server<br/>
 - Usage: `s.wipevcs`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
# s.wipethreads
Clear all threads from a server<br/>
 - Usage: `s.wipethreads`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
# s.emojidata
Get info about an emoji<br/>
 - Usage: `s.emojidata <emoji>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, discord.partial_emoji.PartialEmoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
# s.exportchat
Export chat history to an html file<br/>
 - Usage: `s.exportchat [channel=operator.attrgetter('channel')] [limit=50] [tz_info=UTC] [military_time=False]`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### channel: discord.channel.TextChannel = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### limit: int = 50
> ```
> A number without decimal places.
> ```
> ### tz_info: str = 'UTC'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### military_time: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.botinfo
Get info about the bot<br/>
 - Usage: `s.botinfo`
 - Cooldown: `1 per 15.0 seconds`
