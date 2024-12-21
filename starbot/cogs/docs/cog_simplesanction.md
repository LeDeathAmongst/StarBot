# s.setsimplesanction (Hybrid Command)
Configure SimpleSanction for your server.<br/>
 - Usage: `s.setsimplesanction`
 - Slash Usage: `/setsimplesanction`
 - Restricted to: `ADMIN`
 - Aliases: `simplesanctionset`
 - Checks: `server_only`
## s.setsimplesanction resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.setsimplesanction resetsetting <setting>`
 - Slash Usage: `/setsimplesanction resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setsimplesanction showauthor (Hybrid Command)
Show the command author in embeds.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setsimplesanction showauthor <value>`
 - Slash Usage: `/setsimplesanction showauthor <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsimplesanction actionconfirmation (Hybrid Command)
Require a confirmation for each sanction (except userinfo).<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setsimplesanction actionconfirmation <value>`
 - Slash Usage: `/setsimplesanction actionconfirmation <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsimplesanction finishmessage (Hybrid Command)
Send an embed after a sanction command execution.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setsimplesanction finishmessage <value>`
 - Slash Usage: `/setsimplesanction finishmessage <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsimplesanction showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setsimplesanction showsettings [with_dev=False]`
 - Slash Usage: `/setsimplesanction showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsimplesanction reasonrequired (Hybrid Command)
Require a reason for each sanction (except userinfo).<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setsimplesanction reasonrequired <value>`
 - Slash Usage: `/setsimplesanction reasonrequired <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsimplesanction thumbnail (Hybrid Command)
Set the embed thumbnail.<br/>

Default value: `https://i.imgur.com/Bl62rGd.png`<br/>
Dev: `<class 'str'>`<br/>
 - Usage: `s.setsimplesanction thumbnail <value>`
 - Slash Usage: `/setsimplesanction thumbnail <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setsimplesanction modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.setsimplesanction modalconfig [confirmation=False]`
 - Slash Usage: `/setsimplesanction modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setsimplesanction usewarnsystem (Hybrid Command)
Use WarnSystem by Laggron for the sanctions.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setsimplesanction usewarnsystem <value>`
 - Slash Usage: `/setsimplesanction usewarnsystem <value>`
 - Aliases: `warnsystemuse`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.sanction (Hybrid Command)
Sanction a member quickly and easily.<br/>

All arguments are optional and will be requested during the action if necessary. You must specify the parameters in this order.<br/>

Parameters:<br/>
- `user`: Server member.                            Who is the user concerned?<br/>
- `confirmation`: True or False.                Confirm the action directly. (Default is the recorded value)<br/>
- `show_author`: True or False.                 Do you want the bot to show in its embeds who is the author of the command/sanction? (Default is the recorded value)<br/>
- `finish_message`: True or False.              Do you want the bot to show an embed just before the action summarising the action and giving the sanctioned user and the reason? (Default is the recorded value)<br/>
- `fake_action`: True or False.             Do you want the command to do everything as usual, but (unintentionally) forget to execute the action?<br/>
- `duration`: Duration. (5d, 8h, 1m...) If you choose a TempBan, TempMute or TempMuteChanne, this value will be used for the duration of that action.<br/>
- `reason`: Text.                                       The reason for this action. (`not` to not specify one, unless the reason has been made falcutative in the parameters)<br/>

Short version: s.sanction<br/>
Long version:  s.sanction 10 @member true true true true true true 3d Spam.<br/>
 - Usage: `s.sanction [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Slash Usage: `/sanction [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Restricted to: `MOD`
 - Aliases: `punishmember and punishuser`
 - Checks: `server_only`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 03 (Hybrid Command)
- 🔨 Ban a member from this server.<br/>

It won't delete messages by default.<br/>

Examples:<br/>
- `s.sanction 3 @member not`: Ban for no reason.<br/>
- `s.sanction 3 @member Insults`: Ban for the reason "Insults".<br/>
- `s.sanction 3 012345678987654321 Advertising`: Ban the user with the ID provided.<br/>
 - Usage: `s.sanction 03 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Slash Usage: `/sanction 03 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Aliases: `3 and ban`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 10 (Hybrid Command)
- ⌛ TempMute a member in this channel.<br/>

You can set a timed mute by providing a valid time before the reason.<br/>

Examples:<br/>
- `s.sanction 10 @member 30m not`: 30 minutes mute for no reason.<br/>
- `s.sanction 10 @member 5h Spam`: 5 hours mute for the reason "Spam".<br/>
- `s.sanction 10 @member 3d Advertising`: 3 days mute for the reason "Advertising".<br/>
 - Usage: `s.sanction 10 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Slash Usage: `/sanction 10 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Aliases: `tempmutechannel`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 07 (Hybrid Command)
- 🔇 Mute a member in all channels, including voice channels.<br/>

Examples:<br/>
- `s.sanction 7 @member not`: Infinite mute for no reason.<br/>
- `s.sanction 7 @member Spam`:Infinite  mute for the reason "Spam".<br/>
- `s.sanction 7 @member Advertising`: Infinite mute for the reason "Advertising".<br/>
 - Usage: `s.sanction 07 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Slash Usage: `/sanction 07 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Aliases: `7 and mute`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 00 (Hybrid Command)
- Sanction a member quickly and easily.<br/>

Examples:<br/>
- `s.sanction 0 @member`<br/>
- `s.sanction 0 @member What are these roles?`<br/>
- `s.sanction 0 012345678987654321`<br/>
 - Usage: `s.sanction 00 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Slash Usage: `/sanction 00 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Aliases: `0 and sanction`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 02 (Hybrid Command)
- ⚠️ Add a simple warning on a member.<br/>

Examples:<br/>
- `s.sanction 2 @member not`: Warn for no reason.<br/>
- `s.sanction 2 @member Insults`: Warn for the reason "Insults".<br/>
- `s.sanction 2 012345678987654321 Advertising`: Warn the user with the ID provided.<br/>
 - Usage: `s.sanction 02 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Slash Usage: `/sanction 02 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Aliases: `2 and warn`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 06 (Hybrid Command)
- 👢 Kick a member from this server.<br/>

Examples:<br/>
- `s.sanction 6 @member not`: Kick for no reason.<br/>
- `s.sanction 6 @member Insults`: Kick for the reason "Insults".<br/>
- `s.sanction 6 012345678987654321 Advertising`: Kick the user with the ID provided.<br/>
 - Usage: `s.sanction 06 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Slash Usage: `/sanction 06 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Aliases: `6 and kick`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 09 (Hybrid Command)
- ⏳ TempMute a member in all channels, including voice channels.<br/>

You can set a timed mute by providing a valid time before the reason.<br/>

Examples:<br/>
- `s.sanction 9 @member 30m not`: 30 minutes mute for no reason.<br/>
- `s.sanction 9 @member 5h Spam`: 5 hours mute for the reason "Spam".<br/>
- `s.sanction 9 @member 3d Advertising`: 3 days mute for the reason "Advertising".<br/>
 - Usage: `s.sanction 09 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Slash Usage: `/sanction 09 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Aliases: `9 and tempmute`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 05 (Hybrid Command)
- 💨 TempBan a member from this server.<br/>

It won't delete messages by default.<br/>
If you want to perform a temporary ban, provide the time before the reason.<br/>

Examples:<br/>
- `s.sanction 5 @member not`: Ban for no reason.<br/>
- `s.sanction 5 @member 7d Insults`: 7 days ban for the reason "Insults".<br/>
- `s.sanction 5 012345678987654321 Advertising`: Ban the user with the ID provided.<br/>
 - Usage: `s.sanction 05 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Slash Usage: `/sanction 05 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [duration_for_mute_or_ban=None] [reason]`
 - Aliases: `5 and tempban`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 08 (Hybrid Command)
- 👊 Mute a member in this channel.<br/>

Examples:<br/>
- `s.sanction 8 @member not`: Infinite mute for no reason.<br/>
- `s.sanction 8 @member Spam`: Infinite mute for the reason "Spam".<br/>
- `s.sanction 8 @member Advertising`: Infinite mute for the reason "Advertising".<br/>
 - Usage: `s.sanction 08 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Slash Usage: `/sanction 08 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Aliases: `8 and mutechannel`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 04 (Hybrid Command)
- 🔂 SoftBan a member from this server.<br/>

This means that the user will be banned and immediately unbanned, so it will purge their messages in a period, in all channels.<br/>

Examples:<br/>
- `s.sanction 4 @member not`: SoftBan for no reason<br/>
- `s.sanction 4 @member Insults`: SoftBan for the reason "Insults"<br/>
- `s.sanction 4 012345678987654321 Advertising`: SoftBan the user with the ID provided.<br/>
 - Usage: `s.sanction 04 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Slash Usage: `/sanction 04 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Aliases: `4 and softban`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.sanction 01 (Hybrid Command)
- ℹ️ Show informations about a member.<br/>

Examples:<br/>
- `s.sanction 1 @member`: UserInfo for no reason.<br/>
- `s.sanction 1 @member What are these roles?`: UserInfo for the reason "What are these roles?".<br/>
- `s.sanction 1 012345678987654321`: UserInfo with the ID provided.<br/>
 - Usage: `s.sanction 01 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Slash Usage: `/sanction 01 [member=None] [confirmation=None] [show_author=None] [finish_message=None] [fake_action=False] [reason]`
 - Aliases: `1, userinfo, memberinfo, and info`
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
> ### confirmation: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_author: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### finish_message: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### fake_action: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### reason: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
