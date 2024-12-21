## /server-stats avatar (Slash Command)
Display a users avatar in chat<br/>
 - Usage: `/server-stats avatar [member]`
 - `member:` (Optional) …

Extended Arg Info
> ### member: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> …
> 
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
## /server-stats emoji (Slash Command)
Post a large size emojis in chat<br/>
 - Usage: `/server-stats emoji <emoji>`
 - `emoji:` (Required) …

Extended Arg Info
> ### emoji: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /server-stats botstats (Slash Command)
Display stats about the bot<br/>
 - Usage: `/server-stats botstats`
## s.server-stats channeledit
Modify channel options<br/>
 - Usage: `s.server-stats channeledit`
### /server-stats channeledit name (Slash Command)
Edit a channels name<br/>
 - Usage: `/server-stats channeledit name <channel> <name>`
 - `channel:` (Required) …
 - `name:` (Required) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /server-stats channeledit position (Slash Command)
Edit a channels position<br/>
 - Usage: `/server-stats channeledit position <channel> <position>`
 - `channel:` (Required) …
 - `position:` (Required) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### position: int
> - Autocomplete: False
> 
> …
> 
> ```
> A number without decimal places.
> ```
### /server-stats channeledit sync (Slash Command)
Set whether or not to sync permissions with the channels Category<br/>
 - Usage: `/server-stats channeledit sync <channel> <toggle>`
 - `channel:` (Required) …
 - `toggle:` (Required) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### toggle: bool
> - Autocomplete: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
### /server-stats channeledit nsfw (Slash Command)
Set whether or not a channel is NSFW<br/>
 - Usage: `/server-stats channeledit nsfw <toggle> [channel]`
 - `toggle:` (Required) …
 - `channel:` (Optional) …

Extended Arg Info
> ### toggle: bool
> - Autocomplete: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### /server-stats channeledit topic (Slash Command)
Edit a channels topic<br/>
 - Usage: `/server-stats channeledit topic <topic> [channel]`
 - `topic:` (Required) …
 - `channel:` (Optional) …

Extended Arg Info
> ### topic: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### /server-stats channeledit bitrate (Slash Command)
Edit a voice channels bitrate<br/>
 - Usage: `/server-stats channeledit bitrate <channel> <bitrate>`
 - `channel:` (Required) …
 - `bitrate:` (Required) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### bitrate: int
> - Autocomplete: False
> 
> …
> 
> ```
> A number without decimal places.
> ```
### /server-stats channeledit userlimit (Slash Command)
Edit a voice channels user limit<br/>
 - Usage: `/server-stats channeledit userlimit <channel> <limit>`
 - `channel:` (Required) …
 - `limit:` (Required) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### limit: int
> - Autocomplete: False
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /server-stats whois (Slash Command)
Display servers a user shares with the bot<br/>
 - Usage: `/server-stats whois <user_id>`
 - `user_id:` (Required) …

Extended Arg Info
> ### user_id: discord.member.Member
> - Autocomplete: False
> 
> …
> 
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
## s.server-stats serveredit
Edit various server settings<br/>
 - Usage: `s.server-stats serveredit`
### /server-stats serveredit name (Slash Command)
Change the server name<br/>
 - Usage: `/server-stats serveredit name <name>`
 - `name:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /server-stats serveredit verificationlevel (Slash Command)
Modify the servers verification level<br/>
 - Usage: `/server-stats serveredit verificationlevel <level>`
 - `level:` (Required) …

Extended Arg Info
> ### level: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /server-stats serveredit systemchannel (Slash Command)
Change the system channel<br/>
 - Usage: `/server-stats serveredit systemchannel [channel]`
 - `channel:` (Optional) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### /server-stats serveredit afkchannel (Slash Command)
Change the servers AFK voice channel<br/>
 - Usage: `/server-stats serveredit afkchannel [channel]`
 - `channel:` (Optional) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### /server-stats serveredit afktimeout (Slash Command)
Change the servers AFK timeout<br/>
 - Usage: `/server-stats serveredit afktimeout <timeout>`
 - `timeout:` (Required) …

Extended Arg Info
> ### timeout: int
> - Autocomplete: False
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /server-stats topmembers (Slash Command)
Lists top members on the server by join date<br/>
 - Usage: `/server-stats topmembers [include_bots] [server]`
 - `include_bots:` (Optional) …
 - `server:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### include_bots: bool
> - Autocomplete: False
> - Default: None
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### server: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /server-stats getserver (Slash Command)
Display info about servers the bot is on<br/>
 - Usage: `/server-stats getserver [server]`
 - `server:` (Optional) …

Extended Arg Info
> ### server: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /server-stats getservers (Slash Command)
Display info about multiple servers<br/>
 - Usage: `/server-stats getservers <servers>`
 - `servers:` (Required) …

Extended Arg Info
> ### servers: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /server-stats nummembers (Slash Command)
Display number of users on a server<br/>
 - Usage: `/server-stats nummembers [server]`
 - `server:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### server: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /server-stats getroles (Slash Command)
Displays all roles their ID and number of members in order of<br/>
 - Usage: `/server-stats getroles [server]`
 - `server:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### server: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /server-stats getreactions (Slash Command)
Gets a list of all reactions from specified message and displays the user ID,<br/>
 - Usage: `/server-stats getreactions <message>`
 - `message:` (Required) …

Extended Arg Info
> ### message: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /server-stats serverstats (Slash Command)
Gets total messages on the server and displays each channel<br/>
 - Usage: `/server-stats serverstats`
 - Checks: `Server Only`
## /server-stats channelstats (Slash Command)
Gets total messages in a specific channel as well as the user who<br/>
 - Usage: `/server-stats channelstats [channel]`
 - `channel:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## /server-stats serveremojis (Slash Command)
Display all server emojis in a menu that can be scrolled through<br/>
 - Usage: `/server-stats serveremojis [id_emojis] [server]`
 - `id_emojis:` (Optional) …
 - `server:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### id_emojis: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### server: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.avatar (Hybrid Command)
Display a users avatar in chat<br/>
 - Usage: `s.avatar <member>`
 - Slash Usage: `/avatar <member>`
Extended Arg Info
> ### member: Union[discord.member.Member, discord.user.User, NoneType]
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
# s.emoji (Hybrid Command)
Post a large size emojis in chat<br/>
 - Usage: `s.emoji <emoji>`
 - Slash Usage: `/emoji <emoji>`
Extended Arg Info
> ### emoji: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.botstats (Hybrid Command)
Display stats about the bot<br/>
 - Usage: `s.botstats`
 - Slash Usage: `/botstats`
 - Aliases: `bs`
# s.channeledit (Hybrid Command)
Modify channel options<br/>
 - Usage: `s.channeledit`
 - Slash Usage: `/channeledit`
 - Restricted to: `MOD`
## s.channeledit bitrate (Hybrid Command)
Edit a voice channels bitrate<br/>

- `<channel>` The voice channel you want to change.<br/>
- `<bitrate>` The new bitrate between 8000 and 96000.<br/>
 - Usage: `s.channeledit bitrate <channel> <bitrate>`
 - Slash Usage: `/channeledit bitrate <channel> <bitrate>`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### bitrate: int
> ```
> A number without decimal places.
> ```
## s.channeledit userlimit (Hybrid Command)
Edit a voice channels user limit<br/>

- `<channel>` The voice channel you want to change the limit on.<br/>
- `<limit>` The limt on number of users between 0 and 99.<br/>
 - Usage: `s.channeledit userlimit <channel> <limit>`
 - Slash Usage: `/channeledit userlimit <channel> <limit>`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### limit: int
> ```
> A number without decimal places.
> ```
## s.channeledit name (Hybrid Command)
Edit a channels name<br/>
 - Usage: `s.channeledit name <channel> <name>`
 - Slash Usage: `/channeledit name <channel> <name>`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.channeledit topic (Hybrid Command)
Edit a channels topic<br/>
 - Usage: `s.channeledit topic <channel> <topic>`
 - Slash Usage: `/channeledit topic <channel> <topic>`
 - Restricted to: `MOD`
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
> ### topic: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.channeledit position (Hybrid Command)
Edit a channels position<br/>
 - Usage: `s.channeledit position <channel> <position>`
 - Slash Usage: `/channeledit position <channel> <position>`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### position: int
> ```
> A number without decimal places.
> ```
## s.channeledit permissions (Hybrid Command)
Edit channel read permissions for designated role<br/>

`[channel]` The channel you would like to edit. If no channel is provided<br/>
the channel this command is run in will be used.<br/>
`[true_or_false]` `True` or `False` to set the permission level. If this is not<br/>
provided `None` will be used instead which signifies the default state of the permission.<br/>
`[roles_or_users...]` the roles or users you want to edit this setting for.<br/>

`<permission>` Must be one of the following:<br/>
 - create_instant_invite<br/>
 - manage_channels<br/>
 - add_reactions<br/>
 - priority_speaker<br/>
 - stream<br/>
 - read_messages<br/>
 - send_messages<br/>
 - send_tts_messages<br/>
 - manage_messages<br/>
 - embed_links<br/>
 - attach_files<br/>
 - read_message_history<br/>
 - mention_everyone<br/>
 - external_emojis<br/>
 - connect<br/>
 - speak<br/>
 - mute_members<br/>
 - deafen_members<br/>
 - move_members<br/>
 - use_voice_activation<br/>
 - manage_roles<br/>
 - manage_webhooks<br/>
 - use_application_commands<br/>
 - request_to_speak<br/>
 - manage_threads<br/>
 - create_public_threads<br/>
 - create_private_threads<br/>
 - external_stickers<br/>
 - send_messages_in_threads<br/>
 - use_soundboard<br/>
 - Usage: `s.channeledit permissions <permission> <channel> <true_or_false> <roles_or_users>`
 - Slash Usage: `/channeledit permissions <permission> <channel> <true_or_false> <roles_or_users>`
 - Restricted to: `MOD`
 - Aliases: `perms and permission`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### true_or_false: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### *roles_or_users: Union[discord.member.Member, discord.role.Role, str]
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
## s.channeledit nsfw (Hybrid Command)
Set whether or not a channel is NSFW<br/>
 - Usage: `s.channeledit nsfw <toggle> [channel=None]`
 - Slash Usage: `/channeledit nsfw <toggle> [channel=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.channeledit sync (Hybrid Command)
Set whether or not to sync permissions with the channels Category<br/>
 - Usage: `s.channeledit sync <channel> <toggle>`
 - Slash Usage: `/channeledit sync <channel> <toggle>`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.pruneroles
Perform various actions on users who haven't spoken in x days<br/>

Note: This will only check if a user has talked in the past x days whereas<br/>
discords built in Prune checks online status<br/>
 - Usage: `s.pruneroles`
 - Checks: `server_only`
## s.pruneroles list
List the users who have not talked in x days.<br/>

- `<days>` The days you want to search for.<br/>
- `[role]` The role you want to check.<br/>
 - Usage: `s.pruneroles list <days> [role=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.pruneroles remove
Remove roles from users who haven't spoken in x days.<br/>

- `<days>` is the number of days since last seen talking on the server.<br/>
- `[removed_roles...]` the roles to remove from inactive users.<br/>
 - Usage: `s.pruneroles remove <days> <removed_roles>`
 - Restricted to: `MOD`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
> ### *removed_roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.pruneroles add
Give roles to users who haven't spoken in x days<br/>

- `<days>` is the number of days since last seen talking on the server<br/>
- `[new_roles...]` The new roles to apply to a user who is inactive<br/>
 - Usage: `s.pruneroles add <days> <new_roles>`
 - Restricted to: `MOD`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
> ### *new_roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.pruneroles kick
Kick users from the server who have been inactive for x days<br/>

- `<days>` is the number of days since last seen talking on the server<br/>
- `[role]` is the specified role you would like to kick defaults to everyone<br/>
- `[reinvite=True]` True/False whether to try to send the user a message before kicking<br/>
 - Usage: `s.pruneroles kick <days> [role=None] [reinvite=True]`
 - Restricted to: `MOD`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### reinvite: bool = True
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.whois (Hybrid Command)
Display servers a user shares with the bot<br/>

- `<user_id>` The user you want to search for, ID's are preferred but some name lookup works.<br/>
 - Note: This will only show shared servers between you and the bot.<br/>
 - Usage: `s.whois <user_id>`
 - Slash Usage: `/whois <user_id>`
Extended Arg Info
> ### user_id: discord.user.User
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
# s.serveredit (Hybrid Command)
Edit various server settings<br/>
 - Usage: `s.serveredit`
 - Slash Usage: `/serveredit`
 - Restricted to: `ADMIN`
## s.serveredit systemchannel (Hybrid Command)
Change the system channel<br/>

This is the default discord welcome channel.<br/>
- `[channel]` The channel you want to set as the system channel.<br/>
 - If not provided will be set to `None`.<br/>
 - Usage: `s.serveredit systemchannel [channel=None]`
 - Slash Usage: `/serveredit systemchannel [channel=None]`
 - Restricted to: `ADMIN`
 - Aliases: `welcomechannel`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.serveredit name (Hybrid Command)
Change the server name<br/>

- `<name>` The new name of the server.<br/>
 - Usage: `s.serveredit name <name>`
 - Slash Usage: `/serveredit name <name>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.serveredit verificationlevel (Hybrid Command)
Modify the servers verification level<br/>

- `<level>` must be one of:<br/>
 - `none`<br/>
 - `low`<br/>
 - `medium`<br/>
 - `table flip`<br/>
 - `high`<br/>
 - `double table flip`<br/>
 - `extreme`<br/>
 - Usage: `s.serveredit verificationlevel <level>`
 - Slash Usage: `/serveredit verificationlevel <level>`
 - Restricted to: `ADMIN`
 - Aliases: `verification`
Extended Arg Info
> ### level: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.serveredit afktimeout (Hybrid Command)
Change the servers AFK timeout<br/>

- `<timeout>` must be a value of 60, 300, 900, 1800, or 3600.<br/>
 - Usage: `s.serveredit afktimeout <timeout>`
 - Slash Usage: `/serveredit afktimeout <timeout>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### timeout: int
> ```
> A number without decimal places.
> ```
## s.serveredit afkchannel (Hybrid Command)
Change the servers AFK voice channel<br/>

- `[channel]` The channel you want to set as the system channel.<br/>
 - If not provided will be set to `None`.<br/>
 - Usage: `s.serveredit afkchannel [channel=None]`
 - Slash Usage: `/serveredit afkchannel [channel=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### channel: Optional[discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.topmembers (Hybrid Command)
Lists top members on the server by join date<br/>

- `[include_bots]` whether or not to display bots or members. By default this will show everyone.<br/>
- `[server]` can be either the server ID or name.<br/>
 - Note: You must share the server with the bot for this to work.<br/>
 - Usage: `s.topmembers [include_bots=None] [server=None]`
 - Slash Usage: `/topmembers [include_bots=None] [server=None]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### include_bots: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.getserver (Hybrid Command)
Display info about servers the bot is on<br/>

- `[server]` can be either the server ID or name.<br/>
 - Note: You must share the server with the bot for this to work.<br/>
 - Usage: `s.getserver [server]`
 - Slash Usage: `/getserver [server]`
# s.getservers (Hybrid Command)
Display info about multiple servers<br/>

- `[servers]` can be multiple either the server ID or name.<br/>
 - Note: You must share the server with the bot for this to work.<br/>
 - Usage: `s.getservers <servers>`
 - Slash Usage: `/getservers <servers>`
 - Restricted to: `ADMIN`
# s.nummembers (Hybrid Command)
Display number of users on a server<br/>

- `[server]` can be either the server ID or name.<br/>
 - Note: You must share the server with the bot for this to work.<br/>
 - Usage: `s.nummembers [server]`
 - Slash Usage: `/nummembers [server]`
 - Restricted to: `MOD`
 - Checks: `server_only`
# s.getroles (Hybrid Command)
Displays all roles their ID and number of members in order of<br/>
hierarchy<br/>

- `[server]` can be either the server ID or name.<br/>
 - Note: You must share the server with the bot for this to work.<br/>
 - Usage: `s.getroles [server]`
 - Slash Usage: `/getroles [server]`
 - Restricted to: `MOD`
 - Aliases: `rolestats`
 - Checks: `server_only`
# s.getreactions (Hybrid Command)
Gets a list of all reactions from specified message and displays the user ID,<br/>
Username, and Discriminator and the emoji name.<br/>
 - Usage: `s.getreactions <message>`
 - Slash Usage: `/getreactions <message>`
 - Restricted to: `MOD`
 - Aliases: `getreaction`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
# s.serverstats (Hybrid Command)
Gets total messages on the server and displays each channel<br/>
separately as well as the user who has posted the most in each channel<br/>

Note: This is a very slow function and may take some time to complete<br/>
 - Usage: `s.serverstats`
 - Slash Usage: `/serverstats`
 - Restricted to: `MOD`
 - Checks: `server_only`
# s.channelstats (Hybrid Command)
Gets total messages in a specific channel as well as the user who<br/>
has posted the most in that channel<br/>

`limit` must be a number of messages to check, defaults to all messages<br/>
Note: This can be a very slow function and may take some time to complete<br/>
 - Usage: `s.channelstats [channel=None]`
 - Slash Usage: `/channelstats [channel=None]`
 - Checks: `server_only`
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
# s.serveremojis (Hybrid Command)
Display all server emojis in a menu that can be scrolled through<br/>

`id_emojis` return the id of emojis. Default to False, set True<br/>
 if you want to see emojis ID's.<br/>
- `[server]` can be either the server ID or name.<br/>
 - Note: You must share the server with the bot for this to work.<br/>
 - Usage: `s.serveremojis [id_emojis=False] [server]`
 - Slash Usage: `/serveremojis [id_emojis=False] [server]`
 - Aliases: `serveremojis`
 - Checks: `server_only`
Extended Arg Info
> ### id_emojis: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
