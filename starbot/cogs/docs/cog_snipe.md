# s.snipe (Hybrid Command)
Bulk snipe deleted messages.<br/>
 - Usage: `s.snipe <channel> [index=0]`
 - Slash Usage: `/snipe <channel> [index=0]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### index: int = 0
> ```
> A number without decimal places.
> ```
## s.snipe index (Hybrid Command)
Snipe a deleted message.<br/>
 - Usage: `s.snipe index <channel> [index=0]`
 - Slash Usage: `/snipe index <channel> [index=0]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### index: int = 0
> ```
> A number without decimal places.
> ```
## s.snipe mentions (Hybrid Command)
Bulk snipe deleted messages with roles/users mentions.<br/>
 - Usage: `s.snipe mentions <channel>`
 - Slash Usage: `/snipe mentions <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.snipe embeds (Hybrid Command)
Bulk snipe deleted messages with embeds.<br/>
 - Usage: `s.snipe embeds <channel>`
 - Slash Usage: `/snipe embeds <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.snipe list (Hybrid Command)
List deleted messages.<br/>
 - Usage: `s.snipe list <channel> [member]`
 - Slash Usage: `/snipe list <channel> [member]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### member: Union[discord.member.Member, discord.user.User] = None
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
## s.snipe bulk (Hybrid Command)
Bulk snipe deleted messages.<br/>
 - Usage: `s.snipe bulk <channel>`
 - Slash Usage: `/snipe bulk <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.snipe membersmentions (Hybrid Command)
Bulk snipe deleted messages with members mentions.<br/>
 - Usage: `s.snipe membersmentions <channel>`
 - Slash Usage: `/snipe membersmentions <channel>`
 - Aliases: `usersmentions`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.snipe rolesmentions (Hybrid Command)
Bulk snipe deleted messages with roles mentions.<br/>
 - Usage: `s.snipe rolesmentions <channel>`
 - Slash Usage: `/snipe rolesmentions <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.snipe member (Hybrid Command)
Bulk snipe deleted messages for the specified member.<br/>
 - Usage: `s.snipe member <channel> <member>`
 - Slash Usage: `/snipe member <channel> <member>`
 - Aliases: `user`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### member: Union[discord.member.Member, discord.user.User]
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
# s.esnipe (Hybrid Command)
Bulk snipe edited messages.<br/>
 - Usage: `s.esnipe <channel> [index=0]`
 - Slash Usage: `/esnipe <channel> [index=0]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### index: int = 0
> ```
> A number without decimal places.
> ```
## s.esnipe rolesmentions (Hybrid Command)
Bulk snipe edited messages with roles mentions.<br/>
 - Usage: `s.esnipe rolesmentions <channel>`
 - Slash Usage: `/esnipe rolesmentions <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.esnipe membersmentions (Hybrid Command)
Bulk snipe edited messages with members mentions.<br/>
 - Usage: `s.esnipe membersmentions <channel>`
 - Slash Usage: `/esnipe membersmentions <channel>`
 - Aliases: `usersmentions`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.esnipe index (Hybrid Command)
Snipe an edited message.<br/>
 - Usage: `s.esnipe index <channel> [index=0]`
 - Slash Usage: `/esnipe index <channel> [index=0]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### index: int = 0
> ```
> A number without decimal places.
> ```
## s.esnipe mentions (Hybrid Command)
Bulk snipe edited messages with roles/users mentions.<br/>
 - Usage: `s.esnipe mentions <channel>`
 - Slash Usage: `/esnipe mentions <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.esnipe embeds (Hybrid Command)
Bulk snipe edited messages with embeds.<br/>
 - Usage: `s.esnipe embeds <channel>`
 - Slash Usage: `/esnipe embeds <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.esnipe list (Hybrid Command)
List edited messages.<br/>
 - Usage: `s.esnipe list <channel> [member]`
 - Slash Usage: `/esnipe list <channel> [member]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### member: Union[discord.member.Member, discord.user.User] = None
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
## s.esnipe member (Hybrid Command)
Bulk snipe edited messages for the specified member.<br/>
 - Usage: `s.esnipe member <channel> <member>`
 - Slash Usage: `/esnipe member <channel> <member>`
 - Aliases: `user`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### member: Union[discord.member.Member, discord.user.User]
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
## s.esnipe bulk (Hybrid Command)
Bulk snipe edited messages.<br/>
 - Usage: `s.esnipe bulk <channel>`
 - Slash Usage: `/esnipe bulk <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.setsnipe (Hybrid Command)
Commands to configure Snipe.<br/>
 - Usage: `s.setsnipe`
 - Slash Usage: `/setsnipe`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setsnipe ignoredchannels (Hybrid Command)
Set the channels in which deleted and edited messages will be ignored.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
 - Usage: `s.setsnipe ignoredchannels <value>`
 - Slash Usage: `/setsnipe ignoredchannels <value>`
 - Checks: `server_only`
## s.setsnipe ignored (Hybrid Command)
Set if the deleted and edited messages in this server will be ignored.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setsnipe ignored <value>`
 - Slash Usage: `/setsnipe ignored <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsnipe showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setsnipe showsettings [with_dev=False]`
 - Slash Usage: `/setsnipe showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsnipe modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.setsnipe modalconfig [confirmation=False]`
 - Slash Usage: `/setsnipe modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsnipe resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.setsnipe resetsetting <setting>`
 - Slash Usage: `/setsnipe resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
