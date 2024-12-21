# s.editvoicechannel (Hybrid Command)
Commands for edit a voice channel.<br/>
 - Usage: `s.editvoicechannel`
 - Slash Usage: `/editvoicechannel`
 - Aliases: `editvoiceroom`
 - Checks: `server_only`
## s.editvoicechannel list (Hybrid Command)
List all voice channels in the current server.<br/>
 - Usage: `s.editvoicechannel list`
 - Slash Usage: `/editvoicechannel list`
 - Checks: `server_only`
## s.editvoicechannel view (Hybrid Command)
View and edit voice channel.<br/>
 - Usage: `s.editvoicechannel view <channel>`
 - Slash Usage: `/editvoicechannel view <channel>`
 - Aliases: `-`
 - Checks: `server_only`
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
## s.editvoicechannel slowmodedelay (Hybrid Command)
Edit voice channel slowmode delay.<br/>

Specifies the slowmode rate limit for user in this channel. A value of 0s disables slowmode. The maximum value possible is 21600s.<br/>
 - Usage: `s.editvoicechannel slowmodedelay <channel> <slowmode_delay>`
 - Slash Usage: `/editvoicechannel slowmodedelay <channel> <slowmode_delay>`
 - Aliases: `slowmode_delay`
 - Checks: `server_only`
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
## s.editvoicechannel position (Hybrid Command)
Edit voice channel position.<br/>

Warning: Only voice channels are taken into account. Channel 1 is the highest positioned voice channel.<br/>
Channels cannot be moved to a position that takes them out of their current category.<br/>
 - Usage: `s.editvoicechannel position <channel> <position>`
 - Slash Usage: `/editvoicechannel position <channel> <position>`
 - Checks: `server_only`
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
## s.editvoicechannel syncpermissions (Hybrid Command)
Edit voice channel sync permissions.<br/>
 - Usage: `s.editvoicechannel syncpermissions <channel> [sync_permissions=None]`
 - Slash Usage: `/editvoicechannel syncpermissions <channel> [sync_permissions=None]`
 - Aliases: `sync_permissions`
 - Checks: `server_only`
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
> ### sync_permissions: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editvoicechannel overwrites (Hybrid Command)
Edit voice channel overwrites/permissions.<br/>

You may not specify `True` or `False` to reset the overwrite(s).<br/>
You must possess the permissions you wish to modify.<br/>

• `create_instant_invite`<br/>
• `manage_channels`<br/>
• `add_reactions`<br/>
• `priority_speaker`<br/>
• `stream`<br/>
• `read_messages`<br/>
• `send_messages`<br/>
• `send_tts_messages`<br/>
• `manage_messages`<br/>
• `embed_links`<br/>
• `attach_files`<br/>
• `read_message_history`<br/>
• `mention_everyone`<br/>
• `external_emojis`<br/>
• `connect`<br/>
• `speak`<br/>
• `mute_members`<br/>
• `deafen_members`<br/>
• `move_members`<br/>
• `use_voice_activation`<br/>
• `manage_roles`<br/>
• `manage_webhooks`<br/>
• `use_application_commands`<br/>
• `request_to_speak`<br/>
• `manage_threads`<br/>
• `create_public_threads`<br/>
• `create_private_threads`<br/>
• `external_stickers`<br/>
• `send_messages_in_threads`<br/>
 - Usage: `s.editvoicechannel overwrites <channel> <roles_or_users> <true_or_false> <permissions>`
 - Slash Usage: `/editvoicechannel overwrites <channel> <roles_or_users> <true_or_false> <permissions>`
 - Aliases: `permissions and perms`
 - Checks: `server_only`
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
> ### true_or_false: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editvoicechannel name (Hybrid Command)
Edit voice channel name.<br/>
 - Usage: `s.editvoicechannel name <channel> <name>`
 - Slash Usage: `/editvoicechannel name <channel> <name>`
 - Checks: `server_only`
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
## s.editvoicechannel videoqualitymode (Hybrid Command)
Edit voice channel video quality mode.<br/>

auto = 1<br/>
full = 2<br/>
 - Usage: `s.editvoicechannel videoqualitymode <channel> <video_quality_mode>`
 - Slash Usage: `/editvoicechannel videoqualitymode <channel> <video_quality_mode>`
 - Aliases: `video_quality_mode`
 - Checks: `server_only`
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
## s.editvoicechannel delete (Hybrid Command)
Delete voice channel.<br/>
 - Usage: `s.editvoicechannel delete <channel> [confirmation=False]`
 - Slash Usage: `/editvoicechannel delete <channel> [confirmation=False]`
 - Checks: `server_only`
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
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editvoicechannel bitrate (Hybrid Command)
Edit voice channel bitrate.<br/>

It must be a number between 8000 and<br/>
Level 1: 128000<br/>
Level 2: 256000<br/>
Level 3: 384000<br/>
 - Usage: `s.editvoicechannel bitrate <channel> <bitrate>`
 - Slash Usage: `/editvoicechannel bitrate <channel> <bitrate>`
 - Checks: `server_only`
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
## s.editvoicechannel create (Hybrid Command)
Create a voice channel.<br/>
 - Usage: `s.editvoicechannel create [category=None] <name>`
 - Slash Usage: `/editvoicechannel create [category=None] <name>`
 - Aliases: `new and +`
 - Checks: `server_only`
Extended Arg Info
> ### category: Optional[discord.channel.CategoryChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.editvoicechannel nsfw (Hybrid Command)
Edit voice channel nsfw.<br/>
 - Usage: `s.editvoicechannel nsfw <channel> [nsfw=None]`
 - Slash Usage: `/editvoicechannel nsfw <channel> [nsfw=None]`
 - Checks: `server_only`
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
> ### nsfw: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editvoicechannel category (Hybrid Command)
Edit voice channel category.<br/>
 - Usage: `s.editvoicechannel category <channel> <category>`
 - Slash Usage: `/editvoicechannel category <channel> <category>`
 - Checks: `server_only`
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
> ### category: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.editvoicechannel userlimit (Hybrid Command)
Edit voice channel user limit.<br/>

It must be a number between 0 and 99.<br/>
 - Usage: `s.editvoicechannel userlimit <channel> <user_limit>`
 - Slash Usage: `/editvoicechannel userlimit <channel> <user_limit>`
 - Aliases: `user_limit`
 - Checks: `server_only`
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
## s.editvoicechannel clone (Hybrid Command)
Clone a voice channel.<br/>
 - Usage: `s.editvoicechannel clone <channel> <name>`
 - Slash Usage: `/editvoicechannel clone <channel> <name>`
 - Checks: `server_only`
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
## s.editvoicechannel invite (Hybrid Command)
Create an invite for a voice channel.<br/>

`max_age`: How long the invite should last in days. If it's 0 then the invite doesn't expire.<br/>
`max_uses`: How many uses the invite could be used for. If it's 0 then there are unlimited uses.<br/>
`temporary`: Denotes that the invite grants temporary membership (i.e. they get kicked after they disconnect).<br/>
`unique`: Indicates if a unique invite URL should be created. Defaults to True. If this is set to False then it will return a previously created invite.<br/>
 - Usage: `s.editvoicechannel invite <channel> [max_age=None] [max_uses=None] [temporary=False] [unique=True]`
 - Slash Usage: `/editvoicechannel invite <channel> [max_age=None] [max_uses=None] [temporary=False] [unique=True]`
 - Checks: `server_only`
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
> ### max_age: Optional[float] = None
> ```
> A number with or without decimal places.
> ```
> ### max_uses: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### temporary: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### unique: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.editthread (Hybrid Command)
Commands for edit a text channel.<br/>
 - Usage: `s.editthread`
 - Slash Usage: `/editthread`
 - Checks: `server_only`
## s.editthread locked (Hybrid Command)
Edit thread locked.<br/>
 - Usage: `s.editthread locked <thread> [locked=None]`
 - Slash Usage: `/editthread locked <thread> [locked=None]`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
> ### locked: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editthread autoarchiveduration (Hybrid Command)
Edit thread auto archive duration.<br/>
 - Usage: `s.editthread autoarchiveduration <thread> <auto_archive_duration>`
 - Slash Usage: `/editthread autoarchiveduration <thread> <auto_archive_duration>`
 - Aliases: `auto_archive_duration`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.editthread view (Hybrid Command)
View and edit thread.<br/>
 - Usage: `s.editthread view [thread=None]`
 - Slash Usage: `/editthread view [thread=None]`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### thread: discord.threads.Thread = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.editthread pinned (Hybrid Command)
Edit thread pinned.<br/>
 - Usage: `s.editthread pinned <thread> <pinned>`
 - Slash Usage: `/editthread pinned <thread> <pinned>`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
> ### pinned: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editthread invitable (Hybrid Command)
Edit thread invitable.<br/>
 - Usage: `s.editthread invitable <thread> [invitable=None]`
 - Slash Usage: `/editthread invitable <thread> [invitable=None]`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
> ### invitable: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editthread slowmodedelay (Hybrid Command)
Edit thread slowmode delay.<br/>
 - Usage: `s.editthread slowmodedelay <thread> <slowmode_delay>`
 - Slash Usage: `/editthread slowmodedelay <thread> <slowmode_delay>`
 - Aliases: `slowmode_delay`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.editthread delete (Hybrid Command)
Delete a thread.<br/>
 - Usage: `s.editthread delete <thread> [confirmation=False]`
 - Slash Usage: `/editthread delete <thread> [confirmation=False]`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editthread create (Hybrid Command)
Create a thread.<br/>

You'll join it automatically.<br/>
 - Usage: `s.editthread create [channel=None] [message=None] <name>`
 - Slash Usage: `/editthread create [channel=None] [message=None] <name>`
 - Aliases: `new and +`
 - Checks: `server_only`
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
## s.editthread archived (Hybrid Command)
Edit thread archived.<br/>
 - Usage: `s.editthread archived <thread> [archived=None]`
 - Slash Usage: `/editthread archived <thread> [archived=None]`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
> ### archived: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editthread name (Hybrid Command)
Edit thread name.<br/>
 - Usage: `s.editthread name <thread> <name>`
 - Slash Usage: `/editthread name <thread> <name>`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.editthread appliedtags (Hybrid Command)
Edit thread applied tags.<br/>

```
s.editthread appliedtags "<name>|<emoji>|[moderated]"
s.editthread appliedtags "Reporting|⚠️|True" "Bug|🐛"
```
 - Usage: `s.editthread appliedtags <thread> <applied_tags>`
 - Slash Usage: `/editthread appliedtags <thread> <applied_tags>`
 - Aliases: `applied_tags`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
## s.editthread list (Hybrid Command)
List all threads in the current server.<br/>
 - Usage: `s.editthread list`
 - Slash Usage: `/editthread list`
 - Checks: `server_only`
## s.editthread removeuser (Hybrid Command)
Remove member from thread.<br/>
 - Usage: `s.editthread removeuser <thread> <member>`
 - Slash Usage: `/editthread removeuser <thread> <member>`
 - Aliases: `removemember, remove_user, and remove_member`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
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
## s.editthread adduser (Hybrid Command)
Add member to thread.<br/>
 - Usage: `s.editthread adduser <thread> <member>`
 - Slash Usage: `/editthread adduser <thread> <member>`
 - Aliases: `addmember, add_user, and add_member`
 - Checks: `server_only`
Extended Arg Info
> ### thread: Optional[discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name.
> 
>     
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
# s.edittextchannel (Hybrid Command)
Commands for edit a text channel.<br/>
 - Usage: `s.edittextchannel`
 - Slash Usage: `/edittextchannel`
 - Checks: `server_only`
## s.edittextchannel topic (Hybrid Command)
Edit text channel topic.<br/>
 - Usage: `s.edittextchannel topic <channel> <topic>`
 - Slash Usage: `/edittextchannel topic <channel> <topic>`
 - Checks: `server_only`
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
## s.edittextchannel nsfw (Hybrid Command)
Edit text channel nsfw.<br/>
 - Usage: `s.edittextchannel nsfw <channel> [nsfw=None]`
 - Slash Usage: `/edittextchannel nsfw <channel> [nsfw=None]`
 - Checks: `server_only`
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
> ### nsfw: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.edittextchannel defaultthreadslowmodedelay (Hybrid Command)
Edit text channel default thread slowmode delay.<br/>

The new default thread slowmode delay in seconds for threads created in this channel. Must be between 0 and 21600 (6 hours) seconds.<br/>
 - Usage: `s.edittextchannel defaultthreadslowmodedelay <channel> <default_thread_slowmode_delay>`
 - Slash Usage: `/edittextchannel defaultthreadslowmodedelay <channel> <default_thread_slowmode_delay>`
 - Aliases: `default_thread_slowmode_delay`
 - Checks: `server_only`
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
## s.edittextchannel overwrites (Hybrid Command)
Edit text channel overwrites/permissions.<br/>

You may not specify `True` or `False` to reset the permission(s).<br/>
You must possess the permissions you wish to modify.<br/>

• `create_instant_invite`<br/>
• `manage_channels`<br/>
• `add_reactions`<br/>
• `priority_speaker`<br/>
• `stream`<br/>
• `read_messages`<br/>
• `send_messages`<br/>
• `send_tts_messages`<br/>
• `manage_messages`<br/>
• `embed_links`<br/>
• `attach_files`<br/>
• `read_message_history`<br/>
• `mention_everyone`<br/>
• `external_emojis`<br/>
• `connect`<br/>
• `speak`<br/>
• `mute_members`<br/>
• `deafen_members`<br/>
• `move_members`<br/>
• `use_voice_activation`<br/>
• `manage_roles`<br/>
• `manage_webhooks`<br/>
• `use_application_commands`<br/>
• `request_to_speak`<br/>
• `manage_threads`<br/>
• `create_public_threads`<br/>
• `create_private_threads`<br/>
• `external_stickers`<br/>
• `send_messages_in_threads`<br/>
 - Usage: `s.edittextchannel overwrites <channel> <roles_or_users> <true_or_false> <permissions>`
 - Slash Usage: `/edittextchannel overwrites <channel> <roles_or_users> <true_or_false> <permissions>`
 - Aliases: `permissions and perms`
 - Checks: `server_only`
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
> ### true_or_false: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.edittextchannel create (Hybrid Command)
Create a text channel.<br/>
 - Usage: `s.edittextchannel create [category=None] <name>`
 - Slash Usage: `/edittextchannel create [category=None] <name>`
 - Aliases: `new and +`
 - Checks: `server_only`
Extended Arg Info
> ### category: Optional[discord.channel.CategoryChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.edittextchannel syncpermissions (Hybrid Command)
Edit text channel syncpermissions with category.<br/>
 - Usage: `s.edittextchannel syncpermissions <channel> [sync_permissions=None]`
 - Slash Usage: `/edittextchannel syncpermissions <channel> [sync_permissions=None]`
 - Aliases: `sync_permissions`
 - Checks: `server_only`
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
> ### sync_permissions: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.edittextchannel delete (Hybrid Command)
Delete a text channel.<br/>
 - Usage: `s.edittextchannel delete <channel> [confirmation=False]`
 - Slash Usage: `/edittextchannel delete <channel> [confirmation=False]`
 - Aliases: `-`
 - Checks: `server_only`
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
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.edittextchannel view (Hybrid Command)
View and edit text channel.<br/>
 - Usage: `s.edittextchannel view [channel=None]`
 - Slash Usage: `/edittextchannel view [channel=None]`
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
## s.edittextchannel position (Hybrid Command)
Edit text channel position.<br/>

Warning: Only text channels are taken into account. Channel 1 is the highest positioned text channel.<br/>
Channels cannot be moved to a position that takes them out of their current category.<br/>
 - Usage: `s.edittextchannel position <channel> <position>`
 - Slash Usage: `/edittextchannel position <channel> <position>`
 - Checks: `server_only`
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
## s.edittextchannel invite (Hybrid Command)
Create an invite for a text channel.<br/>

`max_age`: How long the invite should last in days. If it's 0 then the invite doesn't expire.<br/>
`max_uses`: How many uses the invite could be used for. If it's 0 then there are unlimited uses.<br/>
`temporary`: Denotes that the invite grants temporary membership (i.e. they get kicked after they disconnect).<br/>
`unique`: Indicates if a unique invite URL should be created. Defaults to True. If this is set to False then it will return a previously created invite.<br/>
 - Usage: `s.edittextchannel invite <channel> [max_age=None] [max_uses=None] [temporary=False] [unique=True]`
 - Slash Usage: `/edittextchannel invite <channel> [max_age=None] [max_uses=None] [temporary=False] [unique=True]`
 - Checks: `server_only`
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
> ### max_age: Optional[float] = None
> ```
> A number with or without decimal places.
> ```
> ### max_uses: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### temporary: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### unique: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.edittextchannel clone (Hybrid Command)
Clone a text channel.<br/>
 - Usage: `s.edittextchannel clone <channel> <name>`
 - Slash Usage: `/edittextchannel clone <channel> <name>`
 - Checks: `server_only`
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
## s.edittextchannel name (Hybrid Command)
Edit text channel name.<br/>
 - Usage: `s.edittextchannel name <channel> <name>`
 - Slash Usage: `/edittextchannel name <channel> <name>`
 - Checks: `server_only`
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
## s.edittextchannel slowmodedelay (Hybrid Command)
Edit text channel slowmode delay.<br/>

Specifies the slowmode rate limit for user in this channel. A value of 0s disables slowmode. The maximum value possible is 21600s.<br/>
 - Usage: `s.edittextchannel slowmodedelay <channel> <slowmode_delay>`
 - Slash Usage: `/edittextchannel slowmodedelay <channel> <slowmode_delay>`
 - Aliases: `slowmode_delay`
 - Checks: `server_only`
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
## s.edittextchannel category (Hybrid Command)
Edit text channel category.<br/>
 - Usage: `s.edittextchannel category <channel> <category>`
 - Slash Usage: `/edittextchannel category <channel> <category>`
 - Checks: `server_only`
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
> ### category: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.edittextchannel defaultautoarchiveduration (Hybrid Command)
Edit text channel default auto archive duration.<br/>

The new default auto archive duration in minutes for threads created in this channel. Must be one of `60`, `1440`, `4320`, or `10080`.<br/>
 - Usage: `s.edittextchannel defaultautoarchiveduration <channel> <default_auto_archive_duration>`
 - Slash Usage: `/edittextchannel defaultautoarchiveduration <channel> <default_auto_archive_duration>`
 - Aliases: `default_auto_archive_duration`
 - Checks: `server_only`
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
## s.edittextchannel type (Hybrid Command)
Edit text channel type.<br/>

`text`: 0<br/>
`news`: 5<br/>
Currently, only conversion between ChannelType.text and ChannelType.news is supported. This is only available to servers that contain NEWS in Guild.features.<br/>
 - Usage: `s.edittextchannel type <channel> <_type>`
 - Slash Usage: `/edittextchannel type <channel> <_type>`
 - Checks: `server_only`
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
## s.edittextchannel list (Hybrid Command)
List all text channels in the current server.<br/>
 - Usage: `s.edittextchannel list`
 - Slash Usage: `/edittextchannel list`
 - Checks: `server_only`
# s.editrole (Hybrid Command)
Commands for edit a role.<br/>
 - Usage: `s.editrole`
 - Slash Usage: `/editrole`
 - Checks: `server_only`
## s.editrole color (Hybrid Command)
Edit role color.<br/>
 - Usage: `s.editrole color <role> <color>`
 - Slash Usage: `/editrole color <role> <color>`
 - Aliases: `colour`
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
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
## s.editrole mentionable (Hybrid Command)
Edit role mentionable.<br/>
 - Usage: `s.editrole mentionable <role> [mentionable=None]`
 - Slash Usage: `/editrole mentionable <role> [mentionable=None]`
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
> ### mentionable: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editrole position (Hybrid Command)
Edit role position.<br/>

Warning: The role with a position 1 is the highest role in the Discord hierarchy.<br/>
 - Usage: `s.editrole position <role> <position>`
 - Slash Usage: `/editrole position <role> <position>`
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
## s.editrole view (Hybrid Command)
View and edit role.<br/>
 - Usage: `s.editrole view <role>`
 - Slash Usage: `/editrole view <role>`
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
## s.editrole name (Hybrid Command)
Edit role name.<br/>
 - Usage: `s.editrole name <role> <name>`
 - Slash Usage: `/editrole name <role> <name>`
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
## s.editrole hoist (Hybrid Command)
Edit role hoist.<br/>
 - Usage: `s.editrole hoist <role> [hoist=None]`
 - Slash Usage: `/editrole hoist <role> [hoist=None]`
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
> ### hoist: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editrole displayicon (Hybrid Command)
Edit role display icon.<br/>

`display_icon` can be an Unicode emoji, a custom emoji or an url. You can also upload an attachment.<br/>
 - Usage: `s.editrole displayicon <role> [display_icon=None]`
 - Slash Usage: `/editrole displayicon <role> [display_icon=None]`
 - Aliases: `icon and display_icon`
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
## s.editrole delete (Hybrid Command)
Delete a role.<br/>
 - Usage: `s.editrole delete <role> [confirmation=False]`
 - Slash Usage: `/editrole delete <role> [confirmation=False]`
 - Aliases: `-`
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
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editrole permissions (Hybrid Command)
Edit role permissions.<br/>

You must possess the permissions you wish to modify.<br/>

• `create_instant_invite`<br/>
• `manage_channels`<br/>
• `add_reactions`<br/>
• `priority_speaker`<br/>
• `stream`<br/>
• `read_messages`<br/>
• `send_messages`<br/>
• `send_tts_messages`<br/>
• `manage_messages`<br/>
• `embed_links`<br/>
• `attach_files`<br/>
• `read_message_history`<br/>
• `mention_everyone`<br/>
• `external_emojis`<br/>
• `connect`<br/>
• `speak`<br/>
• `mute_members`<br/>
• `deafen_members`<br/>
• `move_members`<br/>
• `use_voice_activation`<br/>
• `manage_roles`<br/>
• `manage_webhooks`<br/>
• `use_application_commands`<br/>
• `request_to_speak`<br/>
• `manage_threads`<br/>
• `create_public_threads`<br/>
• `create_private_threads`<br/>
• `external_stickers`<br/>
• `send_messages_in_threads`<br/>
 - Usage: `s.editrole permissions <role> <true_or_false> <permissions>`
 - Slash Usage: `/editrole permissions <role> <true_or_false> <permissions>`
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
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editrole create (Hybrid Command)
Create a role.<br/>
 - Usage: `s.editrole create [color=None] <name>`
 - Slash Usage: `/editrole create [color=None] <name>`
 - Aliases: `new and +`
 - Checks: `server_only`
## s.editrole list (Hybrid Command)
List all roles in the current server.<br/>
 - Usage: `s.editrole list`
 - Slash Usage: `/editrole list`
 - Checks: `server_only`
# s.editserver (Hybrid Command)
Commands for edit a server.<br/>
 - Usage: `s.editserver`
 - Slash Usage: `/editserver`
 - Checks: `server_only`
## s.editserver raidalertsdisabled (Hybrid Command)
Edit server invites raid alerts disabled state.<br/>
 - Usage: `s.editserver raidalertsdisabled <raid_alerts_disabled>`
 - Slash Usage: `/editserver raidalertsdisabled <raid_alerts_disabled>`
 - Aliases: `raid_alerts_disabled`
 - Checks: `server_only`
Extended Arg Info
> ### raid_alerts_disabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editserver safetyalertschannel (Hybrid Command)
Edit server invites safety alerts channel.<br/>
 - Usage: `s.editserver safetyalertschannel [safety_alerts_channel=None]`
 - Slash Usage: `/editserver safetyalertschannel [safety_alerts_channel=None]`
 - Aliases: `safety_alerts_channel`
 - Checks: `server_only`
Extended Arg Info
> ### safety_alerts_channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.editserver name (Hybrid Command)
Edit server name.<br/>
 - Usage: `s.editserver name <name>`
 - Slash Usage: `/editserver name <name>`
 - Checks: `server_only`
## s.editserver afkchannel (Hybrid Command)
Edit server afkchannel.<br/>
 - Usage: `s.editserver afkchannel [afk_channel]`
 - Slash Usage: `/editserver afkchannel [afk_channel]`
 - Aliases: `afk_channel`
 - Checks: `server_only`
Extended Arg Info
> ### afk_channel: Optional[discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.editserver publicupdateschannel (Hybrid Command)
Edit server public updates channel.<br/>
 - Usage: `s.editserver publicupdateschannel [public_updates_channel=None]`
 - Slash Usage: `/editserver publicupdateschannel [public_updates_channel=None]`
 - Aliases: `public_updates_channel`
 - Checks: `server_only`
Extended Arg Info
> ### public_updates_channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.editserver view (Hybrid Command)
View and edit server.<br/>
 - Usage: `s.editserver view`
 - Slash Usage: `/editserver view`
 - Checks: `server_only`
## s.editserver explicitcontentfilter (Hybrid Command)
Edit server explicit content filter.<br/>
 - Usage: `s.editserver explicitcontentfilter <explicit_content_filter>`
 - Slash Usage: `/editserver explicitcontentfilter <explicit_content_filter>`
 - Aliases: `explicit_content_filter`
 - Checks: `server_only`
## s.editserver icon (Hybrid Command)
Edit server icon.<br/>

You can use an URL or upload an attachment.<br/>
 - Usage: `s.editserver icon [icon=None]`
 - Slash Usage: `/editserver icon [icon=None]`
 - Checks: `server_only`
## s.editserver community (Hybrid Command)
Edit server community state.<br/>
 - Usage: `s.editserver community <community>`
 - Slash Usage: `/editserver community <community>`
 - Checks: `server_only`
Extended Arg Info
> ### community: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editserver afktimeout (Hybrid Command)
Edit server afk timeout.<br/>
 - Usage: `s.editserver afktimeout <afk_timeout>`
 - Slash Usage: `/editserver afktimeout <afk_timeout>`
 - Aliases: `afk_timeout`
 - Checks: `server_only`
Extended Arg Info
> ### afk_timeout: int
> ```
> A number without decimal places.
> ```
## s.editserver systemchannelflags (Hybrid Command)
Edit server system channel flags.<br/>
 - Usage: `s.editserver systemchannelflags <system_channel_flags>`
 - Slash Usage: `/editserver systemchannelflags <system_channel_flags>`
 - Aliases: `system_channel_flags`
 - Checks: `server_only`
## s.editserver widgetchannel (Hybrid Command)
Edit server invites widget channel.<br/>
 - Usage: `s.editserver widgetchannel [widget_channel=None]`
 - Slash Usage: `/editserver widgetchannel [widget_channel=None]`
 - Aliases: `widget_channel`
 - Checks: `server_only`
## s.editserver invitesdisabled (Hybrid Command)
Edit server invites disabled state.<br/>
 - Usage: `s.editserver invitesdisabled <invites_disabled>`
 - Slash Usage: `/editserver invitesdisabled <invites_disabled>`
 - Aliases: `invites_disabled`
 - Checks: `server_only`
Extended Arg Info
> ### invites_disabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editserver verificationlevel (Hybrid Command)
Edit server verification level.<br/>
 - Usage: `s.editserver verificationlevel <verification_level>`
 - Slash Usage: `/editserver verificationlevel <verification_level>`
 - Aliases: `verification_level`
 - Checks: `server_only`
## s.editserver ruleschannel (Hybrid Command)
Edit server rules channel.<br/>
 - Usage: `s.editserver ruleschannel [rules_channel=None]`
 - Slash Usage: `/editserver ruleschannel [rules_channel=None]`
 - Aliases: `rules_channel`
 - Checks: `server_only`
Extended Arg Info
> ### rules_channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.editserver description (Hybrid Command)
Edit server description.<br/>
 - Usage: `s.editserver description [description]`
 - Slash Usage: `/editserver description [description]`
 - Checks: `server_only`
Extended Arg Info
> ### description: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.editserver splash (Hybrid Command)
Edit server splash.<br/>

You can use an URL or upload an attachment.<br/>
 - Usage: `s.editserver splash [splash=None]`
 - Slash Usage: `/editserver splash [splash=None]`
 - Aliases: `invite_splash`
 - Checks: `server_only`
## s.editserver banner (Hybrid Command)
Edit server banner.<br/>

You can use an URL or upload an attachment.<br/>
 - Usage: `s.editserver banner [banner=None]`
 - Slash Usage: `/editserver banner [banner=None]`
 - Checks: `server_only`
## s.editserver discoverysplash (Hybrid Command)
Edit server discovery splash.<br/>

You can use an URL or upload an attachment.<br/>
 - Usage: `s.editserver discoverysplash [discovery_splash=None]`
 - Slash Usage: `/editserver discoverysplash [discovery_splash=None]`
 - Aliases: `discovery_splash`
 - Checks: `server_only`
## s.editserver discoverable (Hybrid Command)
Edit server discoverable state.<br/>
 - Usage: `s.editserver discoverable <discoverable>`
 - Slash Usage: `/editserver discoverable <discoverable>`
 - Checks: `server_only`
Extended Arg Info
> ### discoverable: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editserver defaultnotifications (Hybrid Command)
Edit server notification level.<br/>
 - Usage: `s.editserver defaultnotifications <default_notifications>`
 - Slash Usage: `/editserver defaultnotifications <default_notifications>`
 - Aliases: `notificationslevel and default_notifications`
 - Checks: `server_only`
## s.editserver preferredlocale (Hybrid Command)
Edit server preferred locale.<br/>

american_english = 'en-US'<br/>
british_english = 'en-GB'<br/>
bulgarian = 'bg'<br/>
chinese = 'zh-CN'<br/>
taiwan_chinese = 'zh-TW'<br/>
croatian = 'hr'<br/>
czech = 'cs'<br/>
danish = 'da'<br/>
dutch = 'nl'<br/>
finnish = 'fi'<br/>
french = 'fr'<br/>
german = 'de'<br/>
greek = 'el'<br/>
hindi = 'hi'<br/>
hungarian = 'hu'<br/>
italian = 'it'<br/>
japanese = 'ja'<br/>
korean = 'ko'<br/>
lithuanian = 'lt'<br/>
norwegian = 'no'<br/>
polish = 'pl'<br/>
brazil_portuguese = 'pt-BR'<br/>
romanian = 'ro'<br/>
russian = 'ru'<br/>
spain_spanish = 'es-ES'<br/>
swedish = 'sv-SE'<br/>
thai = 'th'<br/>
turkish = 'tr'<br/>
ukrainian = 'uk'<br/>
vietnamese = 'vi'<br/>
 - Usage: `s.editserver preferredlocale <preferred_locale>`
 - Slash Usage: `/editserver preferredlocale <preferred_locale>`
 - Aliases: `preferred_locale`
 - Checks: `server_only`
## s.editserver premiumprogressbarenabled (Hybrid Command)
Edit server premium progress bar enabled.<br/>
 - Usage: `s.editserver premiumprogressbarenabled [premium_progress_bar_enabled=None]`
 - Slash Usage: `/editserver premiumprogressbarenabled [premium_progress_bar_enabled=None]`
 - Aliases: `premium_progress_bar_enabled`
 - Checks: `server_only`
Extended Arg Info
> ### premium_progress_bar_enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editserver widgetenabled (Hybrid Command)
Edit server invites widget enabled state.<br/>
 - Usage: `s.editserver widgetenabled <widget_enabled>`
 - Slash Usage: `/editserver widgetenabled <widget_enabled>`
 - Aliases: `widget_enabled`
 - Checks: `server_only`
Extended Arg Info
> ### widget_enabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.editserver systemchannel (Hybrid Command)
Edit server system channel.<br/>
 - Usage: `s.editserver systemchannel [system_channel=None]`
 - Slash Usage: `/editserver systemchannel [system_channel=None]`
 - Aliases: `system_channel`
 - Checks: `server_only`
Extended Arg Info
> ### system_channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.editserver vanitycode (Hybrid Command)
Edit server vanity code.<br/>
 - Usage: `s.editserver vanitycode <vanity_code>`
 - Slash Usage: `/editserver vanitycode <vanity_code>`
 - Aliases: `vanity_code`
 - Checks: `server_only`
Extended Arg Info
> ### vanity_code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
