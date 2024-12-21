# s.purge (Hybrid Command)
Removes messages that meet a criteria.<br/>

Messages older than 14 days cannot be deleted.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Example:**<br/>
- `s.purge 10`<br/>
- `s.purge 2000`<br/>
 - Usage: `s.purge <number> [channel=None]`
 - Slash Usage: `/purge <number> [channel=None]`
 - Aliases: `clean and cleanup`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge bot (Hybrid Command)
Removes bot messages, optionally takes a prefix argument.<br/>

**Arguments:**<br/>
- `<prefix>`: The bot's prefix you want to remove.<br/>
- `<number`: The number of messages you want to delete. (Defaults to 100)<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge bot`<br/>
- `s.purge bot ? 2000`<br/>
 - Usage: `s.purge bot [prefix=None] [number=100] [channel=None]`
 - Slash Usage: `/purge bot [prefix=None] [number=100] [channel=None]`
 - Aliases: `bots`
Extended Arg Info
> ### prefix: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge user (Hybrid Command)
Removes all messages by the member.<br/>

**Arguments:**<br/>
- `<member>`: The user to delete messages for.<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge user @member`<br/>
- `s.purge user @member 2000`<br/>
 - Usage: `s.purge user <member> <number> [channel=None]`
 - Slash Usage: `/purge user <member> <number> [channel=None]`
 - Aliases: `member`
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
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge mine (Hybrid Command)
Removes my messages from the channel.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge mine 10`<br/>
- `s.purge mine 2000`<br/>
 - Usage: `s.purge mine <number> [channel=None]`
 - Slash Usage: `/purge mine <number> [channel=None]`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge emoji (Hybrid Command)
Removes all messages containing custom emoji.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge emoji 10`<br/>
- `s.purge emoji 200`<br/>
 - Usage: `s.purge emoji <number> [channel=None]`
 - Slash Usage: `/purge emoji <number> [channel=None]`
 - Aliases: `emojis`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge contains (Hybrid Command)
Removes all messages containing a text.<br/>
The text must be at least 3 characters long.<br/>

**Arguments:**<br/>
- `<text>`: the text to be removed.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge contains hi`<br/>
- `s.purge contains bye`<br/>
 - Usage: `s.purge contains <text> [channel]`
 - Slash Usage: `/purge contains <text> [channel]`
 - Aliases: `contain`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge links (Hybrid Command)
Removes all messages containing a link.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge links 10`<br/>
- `s.purge links 2000`<br/>
 - Usage: `s.purge links <number> [channel=None]`
 - Slash Usage: `/purge links <number> [channel=None]`
 - Aliases: `link`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge files (Hybrid Command)
Removes messages that have attachments in them.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge files 10`<br/>
- `s.purge files 2000`<br/>
 - Usage: `s.purge files <number> [channel=None]`
 - Slash Usage: `/purge files <number> [channel=None]`
 - Aliases: `file`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge after (Hybrid Command)
Delete all messages after a specified message.<br/>

To get a message id, enable developer mode in Discord's<br/>
settings, 'appearance' tab. Then right click a message<br/>
and copy its id.<br/>
Replying to a message will cleanup all messages after it.<br/>

**Arguments:**<br/>
- `<message_id>` The id of the message to cleanup after. This message won't be deleted.<br/>
- `<delete_pinned>` Whether to delete pinned messages or not. Defaults to False<br/>
 - Usage: `s.purge after <message_id> [delete_pinned=False]`
 - Slash Usage: `/purge after <message_id> [delete_pinned=False]`
Extended Arg Info
> ### delete_pinned: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.purge custom (Hybrid Command)
Remove messages that meet a criteria from the flags.<br/>

The following flags are valid.<br/>

`user:` Remove messages from the given user.<br/>
`contains:` Remove messages that contain a substring.<br/>
`prefix:` Remove messages that start with a string.<br/>
`suffix:` Remove messages that end with a string.<br/>
`after:` Search for messages that come after this message ID.<br/>
`before:` Search for messages that come before this message ID.<br/>
`bot: yes` Remove messages from bots. (not webhooks!)<br/>
`webhooks: yes` Remove messages from webhooks.<br/>
`embeds: yes` Remove messages that have embeds.<br/>
`files: yes` Remove messages that have attachments.<br/>
`emoji: yes` Remove messages that have custom emoji.<br/>
`reactions: yes` Remove messages that have reactions.<br/>
`require: any or all` Whether any or all flags should be met before deleting messages.<br/>
 - Usage: `s.purge custom [number=None] <flags>`
 - Slash Usage: `/purge custom [number=None] <flags>`
## s.purge reactions (Hybrid Command)
Removes all reactions from messages that have them.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge reactions 10`<br/>
- `s.purge reactions 200`<br/>
 - Usage: `s.purge reactions <number> [channel=None]`
 - Slash Usage: `/purge reactions <number> [channel=None]`
 - Aliases: `reaction`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge regex (Hybrid Command)
Removes messages that matches the regex pattern.<br/>

**Arguments:**<br/>
- `<pattern>`: The regex pattern to match.<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge regex (?i)(h(?:appy) 1`<br/>
- `s.purge regex (?i)(h(?:appy) 10`<br/>
 - Usage: `s.purge regex <pattern> <number> [channel=None]`
 - Slash Usage: `/purge regex <pattern> <number> [channel=None]`
Extended Arg Info
> ### pattern: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge embeds (Hybrid Command)
Removes messages that have embeds in them.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge embeds 10`<br/>
- `s.purge embeds 2000`<br/>
 - Usage: `s.purge embeds <number> [channel=None]`
 - Slash Usage: `/purge embeds <number> [channel=None]`
 - Aliases: `embed`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge between (Hybrid Command)
Delete the messages between Message One and Message Two, providing the messages IDs.<br/>

The first message ID should be the older message and the second one the newer.<br/>

**Arguments:**<br/>
- `<one>` The id of the message to cleanup after. This message won't be deleted.<br/>
- `<two>` The id of the message to cleanup before. This message won't be deleted.<br/>
- `<delete_pinned>` Whether to delete pinned messages or not. Defaults to False.<br/>

**Example:**<br/>
- `s.cleanup between 123456789123456789 987654321987654321`<br/>
 - Usage: `s.purge between <one> <two> [delete_pinned=None]`
 - Slash Usage: `/purge between <one> <two> [delete_pinned=None]`
Extended Arg Info
> ### delete_pinned: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.purge duplicates (Hybrid Command)
Deletes duplicate messages in the channel from the last X messages and keeps only one copy.<br/>

**Arguments:**<br/>
- `<number>` The number of messages to check for duplicates. Must be a positive integer.<br/>
 - Usage: `s.purge duplicates <number>`
 - Slash Usage: `/purge duplicates <number>`
 - Aliases: `duplicate and spam`
## s.purge self (Hybrid Command)
Removes your messages from the channel.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge self 10`<br/>
- `s.purge self 2000`<br/>
 - Usage: `s.purge self <number> [channel=None]`
 - Slash Usage: `/purge self <number> [channel=None]`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge images (Hybrid Command)
Removes messages that have embeds or attachments.<br/>

**Arguments:**<br/>
- `<number`: The number of messages you want to delete.<br/>
- `<channel>`: The channel you want to delete messages in. (Defaults to current channel)<br/>

**Examples:**<br/>
- `s.purge images 10`<br/>
- `s.purge images 2000`<br/>
 - Usage: `s.purge images <number> [channel=None]`
 - Slash Usage: `/purge images <number> [channel=None]`
 - Aliases: `image`
Extended Arg Info
> ### channel: Union[discord.threads.Thread, discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.purge before (Hybrid Command)
Deletes X messages before the specified message.<br/>

To get a message id, enable developer mode in Discord's<br/>
settings, 'appearance' tab. Then right click a message<br/>
and copy its id.<br/>
Replying to a message will cleanup all messages before it.<br/>

**Arguments:**<br/>
- `<message_id>` The id of the message to cleanup before. This message won't be deleted.<br/>
- `<number>` The max number of messages to cleanup. Must be a positive integer.<br/>
- `<delete_pinned>` Whether to delete pinned messages or not. Defaults to False<br/>
 - Usage: `s.purge before <message_id> <number> [delete_pinned=False]`
 - Slash Usage: `/purge before <message_id> <number> [delete_pinned=False]`
Extended Arg Info
> ### delete_pinned: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
