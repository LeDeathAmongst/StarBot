# s.mychannel
Control of personal channels.<br/>
 - Usage: `s.mychannel`
 - Aliases: `mychan`
 - Checks: `server_only`
## s.mychannel unassign
Unassign personal text channel from someone.<br/>
 - Usage: `s.mychannel unassign <user>`
 - Restricted to: `ADMIN`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### user: Union[discord.member.Member, discord.user.User, int]
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
## s.mychannel friends
Add or remove friends from your channel.<br/>

`<add_or_remove>` should be either `add` to add or `remove` to remove friends.<br/>
 - Usage: `s.mychannel friends <add_or_remove> [user=None]`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `has_assigned_channel`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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
### s.mychannel friends list
List your added friends.<br/>
 - Usage: `s.mychannel friends list`
## s.mychannel topic
Change the topic of personal channel.<br/>

You can't use blacklisted words.<br/>
 - Usage: `s.mychannel topic <topic>`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `has_assigned_channel`
Extended Arg Info
> ### topic: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.mychannel category
Configure the category every personal text channel should be under.<br/>
 - Usage: `s.mychannel category <category>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### category: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.mychannel perms
Give users permissions on how many users they can to add in their channel.<br/>

Run this command without the `perms` argument to clear the permission config.<br/>
 - Usage: `s.mychannel perms <user> [perms=None]`
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
## s.mychannel pin
Pin a message in the personal channel.<br/>

You can also reply to the message with invoking the command.<br/>
 - Usage: `s.mychannel pin [message=None]`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `has_assigned_channel`
Extended Arg Info
> ### message: Optional[discord.message.Message] = None
> Converts to a :class:`discord.Message`.
> 
>     
## s.mychannel blacklist
Manage blacklisted names.<br/>
 - Usage: `s.mychannel blacklist`
 - Restricted to: `ADMIN`
 - Aliases: `blocklist`
### s.mychannel blacklist add
Add channel name to blacklist.<br/>

Members will not be able to change name to blacklisted names.<br/>
 - Usage: `s.mychannel blacklist add <channel_name>`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.mychannel blacklist list
List of blacklisted channel names.<br/>
 - Usage: `s.mychannel blacklist list`
### s.mychannel blacklist remove
Remove channel name from blacklist.<br/>
 - Usage: `s.mychannel blacklist remove <channel_name>`
Extended Arg Info
> ### channel_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.mychannel position
Edit the channel position for someone's personal channel.<br/>
 - Usage: `s.mychannel position <user> <position>`
 - Restricted to: `ADMIN`
 - Checks: `has_assigned_channel`
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
## s.mychannel list
Assigned channels list.<br/>
 - Usage: `s.mychannel list`
 - Restricted to: `ADMIN`
## s.mychannel create
Create a personal channel and assign it to the user.<br/>

- `<perms>`: give the user permissions on how many users they want to add in their channel.<br/>
 - Usage: `s.mychannel create <user> <perms> <name>`
 - Restricted to: `ADMIN`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `bot_has_server_permissions`
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
## s.mychannel name
Change name of personal channel.<br/>

You cant use blacklisted names.<br/>
 - Usage: `s.mychannel name <name>`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `has_assigned_channel`
## s.mychannel remove
Delete member's personal channel.<br/>
 - Usage: `s.mychannel remove [member]`
 - Restricted to: `ADMIN`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### member: Optional[discord.member.Member] = None
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
## s.mychannel unpin
Unpin a message from the personal channel.<br/>

You can also reply to the message with invoking the command.<br/>
 - Usage: `s.mychannel unpin [message=None]`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `has_assigned_channel`
Extended Arg Info
> ### message: Optional[discord.message.Message] = None
> Converts to a :class:`discord.Message`.
> 
>     
## s.mychannel delete
Delete your personal channel.<br/>
 - Usage: `s.mychannel delete`
 - Cooldown: `1 per 30.0 seconds`
 - Checks: `has_assigned_channel`
## s.mychannel assign
Assign a personal text channel to someone.<br/>
 - Usage: `s.mychannel assign <user> <channel> [perms]`
 - Restricted to: `ADMIN`
 - Checks: `bot_has_server_permissions`
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
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
