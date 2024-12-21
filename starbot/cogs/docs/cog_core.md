# s.ping (Hybrid Command)
Shows my ping/latency.<br/>

This data can't be considered an actual latency and as matter of fact, affected by many factors.<br/>

Discord WS: WebSocket latency. This is how fast bot will receive events from Discord.<br/>
Message: Difference between your command message and message with ping.<br/>
Typing: Time that bot taken to send message with ping.<br/>
 - Usage: `s.ping [show_shards=False]`
 - Slash Usage: `/ping [show_shards=False]`
 - Aliases: `oing, ling, ipng, pnig, and pign`
Extended Arg Info
> ### show_shards: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.info (Hybrid Command)
Shows info about something<br/>
 - Usage: `s.info`
 - Slash Usage: `/info`
## s.info bot (Hybrid Command)
Shows info about me.<br/>
 - Usage: `s.info bot`
 - Slash Usage: `/info bot`
## s.info credits (Hybrid Command)
Shows my credits.<br/>
 - Usage: `s.info credits`
 - Slash Usage: `/info credits`
# s.uptime (Hybrid Command)
Shows my uptime.<br/>
 - Usage: `s.uptime`
 - Slash Usage: `/uptime`
# s.mydata
Commands which interact with the data Starfire has about you.<br/>

More information can be found in the [End User Data Documentation.](https://docs.discord.red/en/stable/red_core_data_statement.html)<br/>
 - Usage: `s.mydata`
## s.mydata whatdata
Find out what type of data Starfire stores and why.<br/>

**Example:**<br/>
- `s.mydata whatdata`<br/>
 - Usage: `s.mydata whatdata`
 - Cooldown: `1 per 600.0 seconds`
## s.mydata 3rdparty
View the End User Data statements of each 3rd-party module.<br/>

This will send an attachment with the End User Data statements of all loaded 3rd party cogs.<br/>

**Example:**<br/>
- `s.mydata 3rdparty`<br/>
 - Usage: `s.mydata 3rdparty`
 - Cooldown: `1 per 1800.0 seconds`
## s.mydata getmydata
[Coming Soon] Get what data Starfire has about you.<br/>
 - Usage: `s.mydata getmydata`
 - Cooldown: `1 per 7200.0 seconds`
## s.mydata forgetme
Have Starfire forget what it knows about you.<br/>

This may not remove all data about you, data needed for operation,<br/>
such as command cooldowns will be kept until no longer necessary.<br/>

Further interactions with Starfire may cause it to learn about you again.<br/>

**Example:**<br/>
- `s.mydata forgetme`<br/>
 - Usage: `s.mydata forgetme`
 - Cooldown: `1 per 86400.0 seconds`
# s.embedset
Commands for toggling embeds on or off.<br/>

This setting determines whether or not to use embeds as a response to a command (for commands that support it).<br/>
The default is to use embeds.<br/>

The embed settings are checked until the first True/False in this order:<br/>

- In server context:<br/>
  1. Channel override - `s.embedset channel`<br/>
  2. Server command override - `s.embedset command server`<br/>
  3. Server override - `s.embedset server`<br/>
  4. Global command override - `s.embedset command global`<br/>
  5. Global setting  -`s.embedset global`<br/>

- In DM context:<br/>
  1. User override - `s.embedset user`<br/>
  2. Global command override - `s.embedset command global`<br/>
  3. Global setting - `s.embedset global`<br/>
 - Usage: `s.embedset`
## s.embedset command
Sets a command's embed setting.<br/>

If you're the bot owner, this will try to change the command's embed setting globally by default.<br/>
Otherwise, this will try to change embed settings on the current server.<br/>

If enabled is left blank, the setting will be unset.<br/>

To see full evaluation order of embed settings, run `s.help embedset`.<br/>

**Examples:**<br/>
- `s.embedset command info` - Clears command specific embed settings for 'info'.<br/>
- `s.embedset command info False` - Disables embeds for 'info'.<br/>
- `s.embedset command "ignore list" True` - Quotes are needed for subcommands.<br/>

**Arguments:**<br/>
- `[enabled]` - Whether to use embeds for this command. Leave blank to reset to default.<br/>
 - Usage: `s.embedset command <command> [enabled=None]`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.embedset command server
Sets a command's embed setting for the current server.<br/>

If set, this is used instead of the server default to determine whether or not to use embeds.<br/>

If enabled is left blank, the setting will be unset and the server default will be used instead.<br/>

To see full evaluation order of embed settings, run `s.help embedset`.<br/>

**Examples:**<br/>
- `s.embedset command server info` - Clears command specific embed settings for 'info'.<br/>
- `s.embedset command server info False` - Disables embeds for 'info'.<br/>
- `s.embedset command server "ignore list" True` - Quotes are needed for subcommands.<br/>

**Arguments:**<br/>
- `[enabled]` - Whether to use embeds for this command. Leave blank to reset to default.<br/>
 - Usage: `s.embedset command server <command> [enabled=None]`
 - Aliases: `server`
 - Checks: `server_only`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.embedset channel
Set's a channel's embed setting.<br/>

If set, this is used instead of the server and command defaults to determine whether or not to use embeds.<br/>
This is used for all commands done in a channel.<br/>

If enabled is left blank, the setting will be unset and the server default will be used instead.<br/>

To see full evaluation order of embed settings, run `s.help embedset`.<br/>

**Examples:**<br/>
- `s.embedset channel #text-channel False` - Disables embeds in the #text-channel.<br/>
- `s.embedset channel #forum-channel disable` - Disables embeds in the #forum-channel.<br/>
- `s.embedset channel #text-channel` - Resets value to use server default in the #text-channel.<br/>

**Arguments:**<br/>
    - `<channel>` - The text, voice, stage, or forum channel to set embed setting for.<br/>
    - `[enabled]` - Whether to use embeds in this channel. Leave blank to reset to default.<br/>
 - Usage: `s.embedset channel <channel> [enabled=None]`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.embedset showsettings
Show the current embed settings.<br/>

Provide a command name to check for command specific embed settings.<br/>

**Examples:**<br/>
- `s.embedset showsettings` - Shows embed settings.<br/>
- `s.embedset showsettings info` - Also shows embed settings for the 'info' command.<br/>
- `s.embedset showsettings "ignore list"` - Checking subcommands requires quotes.<br/>

**Arguments:**<br/>
- `[command]` - Checks this command for command specific embed settings.<br/>
 - Usage: `s.embedset showsettings [command=None]`
## s.embedset server
Set the server's embed setting.<br/>

If set, this is used instead of the global default to determine whether or not to use embeds.<br/>
This is used for all commands done in a server.<br/>

If enabled is left blank, the setting will be unset and the global default will be used instead.<br/>

To see full evaluation order of embed settings, run `s.help embedset`.<br/>

**Examples:**<br/>
- `s.embedset server False` - Disables embeds on this server.<br/>
- `s.embedset server` - Resets value to use global default.<br/>

**Arguments:**<br/>
- `[enabled]` - Whether to use embeds on this server. Leave blank to reset to default.<br/>
 - Usage: `s.embedset server [enabled=None]`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `server`
 - Checks: `server_only`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.embedset user
Sets personal embed setting for DMs.<br/>

If set, this is used instead of the global default to determine whether or not to use embeds.<br/>
This is used for all commands executed in a DM with the bot.<br/>

If enabled is left blank, the setting will be unset and the global default will be used instead.<br/>

To see full evaluation order of embed settings, run `s.help embedset`.<br/>

**Examples:**<br/>
- `s.embedset user False` - Disables embeds in your DMs.<br/>
- `s.embedset user` - Resets value to use global default.<br/>

**Arguments:**<br/>
- `[enabled]` - Whether to use embeds in your DMs. Leave blank to reset to default.<br/>
 - Usage: `s.embedset user [enabled=None]`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.invite
Shows Starfire's invite url.<br/>

This will always send the invite to DMs to keep it private.<br/>

This command is locked to the owner unless `s.inviteset public` is set to True.<br/>

**Example:**<br/>
- `s.invite`<br/>
 - Usage: `s.invite`
 - Checks: `CoreLogic`
# s.bankset
Base command for bank settings.<br/>
 - Usage: `s.bankset`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
## s.bankset bankname
Set the bank's name.<br/>
 - Usage: `s.bankset bankname <name>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.bankset creditsname
Set the name for the bank's currency.<br/>
 - Usage: `s.bankset creditsname <name>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.bankset registeramount
Set the initial balance for new bank accounts.<br/>

Example:<br/>
- `s.bankset registeramount 5000`<br/>

**Arguments**<br/>

- `<creds>` The new initial balance amount. Default is 0.<br/>
 - Usage: `s.bankset registeramount <creds>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### creds: int
> ```
> A number without decimal places.
> ```
## s.bankset reset
Delete all bank accounts.<br/>

Examples:<br/>
- `s.bankset reset` - Did not confirm. Shows the help message.<br/>
- `s.bankset reset yes`<br/>

**Arguments**<br/>

- `<confirmation>` This will default to false unless specified.<br/>
 - Usage: `s.bankset reset [confirmation=False]`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.bankset prune
Base command for pruning bank accounts.<br/>
 - Usage: `s.bankset prune`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
### s.bankset prune server
Prune bank accounts for users no longer in the server.<br/>

Cannot be used with a global bank. See `s.bankset prune global`.<br/>

Examples:<br/>
- `s.bankset prune server` - Did not confirm. Shows the help message.<br/>
- `s.bankset prune server yes`<br/>

**Arguments**<br/>

- `<confirmation>` This will default to false unless specified.<br/>
 - Usage: `s.bankset prune server [confirmation=False]`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `server and local`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.bankset prune user
Delete the bank account of a specified user.<br/>

Examples:<br/>
- `s.bankset prune user @Twentysix` - Did not confirm. Shows the help message.<br/>
- `s.bankset prune user @Twentysix yes`<br/>

**Arguments**<br/>

- `<user>` The user to delete the bank of. Takes mentions, names, and user ids.<br/>
- `<confirmation>` This will default to false unless specified.<br/>
 - Usage: `s.bankset prune user <member_or_id> [confirmation=False]`
Extended Arg Info
> ### member_or_id: Union[discord.member.Member, starbot.core.commands.converter.RawUserIdConverter]
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
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.bankset maxbal
Set the maximum balance a user can get.<br/>
 - Usage: `s.bankset maxbal <amount>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## s.bankset showsettings
Show the current bank settings.<br/>
 - Usage: `s.bankset showsettings`
# s.modlogset
Manage modlog settings.<br/>
 - Usage: `s.modlogset`
 - Restricted to: `GUILD_OWNER`
## s.modlogset cases
Enable or disable case creation for a mod action.<br/>

An action can be enabling or disabling specific cases. (Ban, kick, mute, etc.)<br/>

Example: `s.modlogset cases kick enabled`<br/>
 - Usage: `s.modlogset cases [action=None]`
 - Checks: `server_only`
Extended Arg Info
> ### action: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.modlogset modlog
Set a channel as the modlog.<br/>

Omit `[channel]` to disable the modlog.<br/>
 - Usage: `s.modlogset modlog [channel=None]`
 - Aliases: `channel`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.modlogset resetcases
Reset all modlog cases in this server.<br/>
 - Usage: `s.modlogset resetcases`
 - Checks: `server_only`
# s.set
Commands for changing Starfire's settings.<br/>
 - Usage: `s.set`
## s.set roles
Set server's admin and mod roles for Starfire.<br/>
 - Usage: `s.set roles`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
### s.set roles addmodrole
Adds a moderator role for this server.<br/>

This grants access to moderator level commands like:<br/>
 - `s.mute`<br/>
 - `s.cleanup`<br/>
 - `s.customcommand create`<br/>

 And more.<br/>

**Examples:**<br/>
- `s.set roles addmodrole @Mods`<br/>
- `s.set roles addmodrole Loyal Helpers`<br/>

**Arguments:**<br/>
- `<role>` - The role to add as a moderator.<br/>
 - Usage: `s.set roles addmodrole <role>`
 - Restricted to: `GUILD_OWNER`
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
### s.set roles removemodrole
Removes a mod role for this server.<br/>

**Examples:**<br/>
- `s.set roles removemodrole @Mods`<br/>
- `s.set roles removemodrole Loyal Helpers`<br/>

**Arguments:**<br/>
- `<role>` - The role to remove from being a moderator.<br/>
 - Usage: `s.set roles removemodrole <role>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `remmodrole, delmodrole, and deletemodrole`
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
### s.set roles removeadminrole
Removes an admin role for this server.<br/>

**Examples:**<br/>
- `s.set roles removeadminrole @Admins`<br/>
- `s.set roles removeadminrole Super Admins`<br/>

**Arguments:**<br/>
- `<role>` - The role to remove from being an admin.<br/>
 - Usage: `s.set roles removeadminrole <role>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `remadmindrole, deladminrole, and deleteadminrole`
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
### s.set roles addadminrole
Adds an admin role for this server.<br/>

Admins have the same access as Mods, plus additional admin level commands like:<br/>
 - `s.set serverprefix`<br/>
 - `s.addrole`<br/>
 - `s.ban`<br/>
 - `s.ignore server`<br/>

 And more.<br/>

**Examples:**<br/>
- `s.set roles addadminrole @Admins`<br/>
- `s.set roles addadminrole Super Admins`<br/>

**Arguments:**<br/>
- `<role>` - The role to add as an admin.<br/>
 - Usage: `s.set roles addadminrole <role>`
 - Restricted to: `GUILD_OWNER`
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
## s.set showsettings
Show the current settings for Starfire.<br/>

Accepts optional server parameter to allow prefix recovery.<br/>
 - Usage: `s.set showsettings [server=None]`
Extended Arg Info
> ### server: discord.server.Guild = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## s.set usebotcolour
Toggle whether to use the bot owner-configured colour for embeds.<br/>

Default is to use the bot's configured colour.<br/>
Otherwise, the colour used will be the colour of the bot's top role.<br/>

**Example:**<br/>
- `s.set usebotcolour`<br/>
 - Usage: `s.set usebotcolour`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `usebotcolor`
 - Checks: `server_only`
## s.set bot
Commands for changing Starfire's metadata.<br/>
 - Usage: `s.set bot`
 - Restricted to: `ADMIN`
 - Aliases: `metadata`
### s.set bot nickname
Sets Starfire's nickname for the current server.<br/>

Maximum length for a nickname is 32 characters.<br/>

**Example:**<br/>
- `s.set bot nickname 🎃 SpookyBot 🎃`<br/>

**Arguments:**<br/>
- `[nickname]` - The nickname to give the bot. Leave blank to clear the current nickname.<br/>
 - Usage: `s.set bot nickname [nickname]`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### nickname: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.set deletedelay
Set the delay until the bot removes the command message.<br/>

Must be between -1 and 60.<br/>

Set to -1 to disable this feature.<br/>

This is only applied to the current server and not globally.<br/>

**Examples:**<br/>
- `s.set deletedelay` - Shows the current delete delay setting.<br/>
- `s.set deletedelay 60` - Sets the delete delay to the max of 60 seconds.<br/>
- `s.set deletedelay -1` - Disables deleting command messages.<br/>

**Arguments:**<br/>
- `[time]` - The seconds to wait before deleting the command message. Use -1 to disable.<br/>
 - Usage: `s.set deletedelay [time=None]`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### time: int = None
> ```
> A number without decimal places.
> ```
## s.set serverprefix
Sets Starfire's server prefix(es).<br/>

Warning: This will override global prefixes, the bot will not respond to any global prefixes in this server.<br/>
    This is not additive. It will replace all current server prefixes.<br/>
    A prefix cannot have more than 25 characters.<br/>

**Examples:**<br/>
- `s.set serverprefix !`<br/>
- `s.set serverprefix "! "` - Quotes are needed to use spaces in prefixes.<br/>
- `s.set serverprefix "@Starfire "` - This uses a mention as the prefix.<br/>
- `s.set serverprefix ! ? .` - Sets multiple prefixes.<br/>
- `s.set serverprefix "Red - Discord Bot" ?` - Sets the prefix for a specific server. Quotes are needed to use spaces in the server name.<br/>

**Arguments:**<br/>
- `[server]` - The server to set the prefix for. Defaults to current server.<br/>
- `[prefixes...]` - The prefixes the bot will respond to on this server. Leave blank to clear server prefixes.<br/>
 - Usage: `s.set serverprefix <server> <prefixes>`
 - Restricted to: `ADMIN`
 - Aliases: `serverprefixes`
Extended Arg Info
> ### server: Optional[discord.server.Guild]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
> ### *prefixes: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.set regionalformat
Changes the bot's regional format in this server. This is used for formatting date, time and numbers.<br/>

`language_code` can be any language code with country code included, e.g. `en-US`, `de-DE`, `fr-FR`, `pl-PL`, etc.<br/>
Pass "reset" to `language_code` to base regional formatting on bot's locale in this server.<br/>

If you want to change bot's global regional format, see `s.set regionalformat global` command.<br/>

**Examples:**<br/>
- `s.set regionalformat en-US`<br/>
- `s.set region de-DE`<br/>
- `s.set regionalformat reset` - Resets to the locale.<br/>

**Arguments:**<br/>
- `[language_code]` - The region format to use for the bot in this server.<br/>
 - Usage: `s.set regionalformat <language_code>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `region`
Extended Arg Info
> ### language_code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.set regionalformat server
Changes the bot's regional format in this server. This is used for formatting date, time and numbers.<br/>

`language_code` can be any language code with country code included, e.g. `en-US`, `de-DE`, `fr-FR`, `pl-PL`, etc.<br/>
Pass "reset" to `language_code` to base regional formatting on bot's locale in this server.<br/>

**Examples:**<br/>
- `s.set regionalformat server en-US`<br/>
- `s.set region local de-DE`<br/>
- `s.set regionalformat server reset` - Resets to the locale.<br/>

**Arguments:**<br/>
- `[language_code]` - The region format to use for the bot in this server.<br/>
 - Usage: `s.set regionalformat server <language_code>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `local and server`
 - Checks: `server_only`
Extended Arg Info
> ### language_code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.set serverfuzzy
Toggle whether to enable fuzzy command search for the server.<br/>

This allows the bot to identify potential misspelled commands and offer corrections.<br/>

Note: This can be processor intensive and may be unsuitable for larger servers.<br/>

Default is for fuzzy command search to be disabled.<br/>

**Example:**<br/>
- `s.set serverfuzzy`<br/>
 - Usage: `s.set serverfuzzy`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.set locale
Changes Starfire's locale in this server.<br/>

Go to [Red's Crowdin page](https://translate.discord.red) to see locales that are available with translations.<br/>

Use "default" to return to the bot's default set language.<br/>

If you want to change bot's global locale, see `s.set locale global` command.<br/>

**Examples:**<br/>
- `s.set locale en-US`<br/>
- `s.set locale de-DE`<br/>
- `s.set locale fr-FR`<br/>
- `s.set locale pl-PL`<br/>
- `s.set locale default` - Resets to the global default locale.<br/>

**Arguments:**<br/>
- `<language_code>` - The default locale to use for the bot. This can be any language code with country code included.<br/>
 - Usage: `s.set locale <language_code>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### language_code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.set locale server
Changes Starfire's locale in this server.<br/>

Go to [Red's Crowdin page](https://translate.discord.red) to see locales that are available with translations.<br/>

Use "default" to return to the bot's default set language.<br/>

**Examples:**<br/>
- `s.set locale server en-US`<br/>
- `s.set locale server de-DE`<br/>
- `s.set locale server fr-FR`<br/>
- `s.set locale server pl-PL`<br/>
- `s.set locale server default` - Resets to the global default locale.<br/>

**Arguments:**<br/>
- `<language_code>` - The default locale to use for the bot. This can be any language code with country code included.<br/>
 - Usage: `s.set locale server <language_code>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `local and server`
 - Checks: `server_only`
Extended Arg Info
> ### language_code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.contact
Sends a message to the owner.<br/>

This is limited to one message every 60 seconds per person.<br/>

**Example:**<br/>
- `s.contact Help! The bot has become sentient!`<br/>

**Arguments:**<br/>
- `[message]` - The message to send to the owner.<br/>
 - Usage: `s.contact <message>`
 - Cooldown: `1 per 60.0 seconds`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.command
Commands to enable and disable commands and cogs.<br/>
 - Usage: `s.command`
 - Restricted to: `GUILD_OWNER`
## s.command disablecog
Disable a cog in this server.<br/>

Note: This will only work on loaded cogs, and must reference the title-case cog name.<br/>

**Examples:**<br/>
- `s.command disablecog Economy`<br/>
- `s.command disablecog ModLog`<br/>

**Arguments:**<br/>
- `<cog>` - The name of the cog to disable on this server. Must be title-case.<br/>
 - Usage: `s.command disablecog <cog>`
 - Checks: `server_only`
## s.command listdisabledcogs
List the cogs which are disabled in this server.<br/>

**Example:**<br/>
- `s.command listdisabledcogs`<br/>
 - Usage: `s.command listdisabledcogs`
 - Checks: `server_only`
## s.command listdisabled
List disabled commands.<br/>

If you're the bot owner, this will show global disabled commands by default.<br/>
Otherwise, this will show disabled commands on the current server.<br/>

**Example:**<br/>
- `s.command listdisabled`<br/>
 - Usage: `s.command listdisabled`
### s.command listdisabled global
List disabled commands globally.<br/>

**Example:**<br/>
- `s.command listdisabled global`<br/>
 - Usage: `s.command listdisabled global`
### s.command listdisabled server
List disabled commands in this server.<br/>

**Example:**<br/>
- `s.command listdisabled server`<br/>
 - Usage: `s.command listdisabled server`
 - Checks: `server_only`
## s.command enablecog
Enable a cog in this server.<br/>

Note: This will only work on loaded cogs, and must reference the title-case cog name.<br/>

**Examples:**<br/>
- `s.command enablecog Economy`<br/>
- `s.command enablecog ModLog`<br/>

**Arguments:**<br/>
- `<cog>` - The name of the cog to enable on this server. Must be title-case.<br/>
 - Usage: `s.command enablecog <cogname>`
 - Checks: `server_only`
Extended Arg Info
> ### cogname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.command enable
Enable a command.<br/>

If you're the bot owner, this will try to enable a globally disabled command by default.<br/>
Otherwise, this will try to enable a command disabled on the current server.<br/>

**Examples:**<br/>
- `s.command enable userinfo` - Enables the `userinfo` command in the Mod cog.<br/>
- `s.command enable urban` - Enables the `urban` command in the General cog.<br/>

**Arguments:**<br/>
- `<command>` - The command to enable.<br/>
 - Usage: `s.command enable <command>`
### s.command enable server
Enable a command in this server.<br/>

**Examples:**<br/>
- `s.command enable server userinfo` - Enables the `userinfo` command in the Mod cog.<br/>
- `s.command enable server urban` - Enables the `urban` command in the General cog.<br/>

**Arguments:**<br/>
- `<command>` - The command to enable for the current server.<br/>
 - Usage: `s.command enable server <command>`
 - Aliases: `server`
 - Checks: `server_only`
## s.command disable
Disable a command.<br/>

If you're the bot owner, this will disable commands globally by default.<br/>
Otherwise, this will disable commands on the current server.<br/>

**Examples:**<br/>
- `s.command disable userinfo` - Disables the `userinfo` command in the Mod cog.<br/>
- `s.command disable urban` - Disables the `urban` command in the General cog.<br/>

**Arguments:**<br/>
- `<command>` - The command to disable.<br/>
 - Usage: `s.command disable <command>`
### s.command disable server
Disable a command in this server only.<br/>

**Examples:**<br/>
- `s.command disable server userinfo` - Disables the `userinfo` command in the Mod cog.<br/>
- `s.command disable server urban` - Disables the `urban` command in the General cog.<br/>

**Arguments:**<br/>
- `<command>` - The command to disable for the current server.<br/>
 - Usage: `s.command disable server <command>`
 - Aliases: `server`
 - Checks: `server_only`
# s.autoimmune
Commands to manage server settings for immunity from automated actions.<br/>

This includes duplicate message deletion and mention spam from the Mod cog, and filters from the Filter cog.<br/>
 - Usage: `s.autoimmune`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.autoimmune remove
Remove a user or role from being immune to automated moderation actions.<br/>

**Examples:**<br/>
- `s.autoimmune remove @Twentysix` - Removes a user.<br/>
- `s.autoimmune remove @Mods` - Removes a role.<br/>

**Arguments:**<br/>
- `<user_or_role>` - The user or role to remove immunity from.<br/>
 - Usage: `s.autoimmune remove <user_or_role>`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
## s.autoimmune isimmune
Checks if a user or role would be considered immune from automated actions.<br/>

**Examples:**<br/>
- `s.autoimmune isimmune @Twentysix`<br/>
- `s.autoimmune isimmune @Mods`<br/>

**Arguments:**<br/>
- `<user_or_role>` - The user or role to check the immunity of.<br/>
 - Usage: `s.autoimmune isimmune <user_or_role>`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
## s.autoimmune list
Gets the current members and roles configured for automatic moderation action immunity.<br/>

**Example:**<br/>
- `s.autoimmune list`<br/>
 - Usage: `s.autoimmune list`
## s.autoimmune add
Makes a user or role immune from automated moderation actions.<br/>

**Examples:**<br/>
- `s.autoimmune add @Twentysix` - Adds a user.<br/>
- `s.autoimmune add @Mods` - Adds a role.<br/>

**Arguments:**<br/>
- `<user_or_role>` - The user or role to add immunity to.<br/>
 - Usage: `s.autoimmune add <user_or_role>`
Extended Arg Info
> ### user_or_role: Union[discord.member.Member, discord.role.Role]
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
# s.ignore
Commands to add servers or channels to the ignore list.<br/>

The ignore list will prevent the bot from responding to commands in the configured locations.<br/>

Note: Owners and Admins override the ignore list.<br/>
 - Usage: `s.ignore`
 - Checks: `server_only`
## s.ignore list
List the currently ignored servers and channels.<br/>

**Example:**<br/>
- `s.ignore list`<br/>
 - Usage: `s.ignore list`
## s.ignore server
Ignore commands in this server.<br/>

Note: Owners, Admins, and those with Manage Server permissions override ignored servers.<br/>

**Example:**<br/>
- `s.ignore server` - Ignores the current server<br/>
 - Usage: `s.ignore server`
 - Restricted to: `ADMIN`
 - Aliases: `server`
## s.ignore channel
Ignore commands in the channel, thread, or category.<br/>

Defaults to the current thread or channel.<br/>

Note: Owners, Admins, and those with Manage Channel permissions override ignored channels.<br/>

**Examples:**<br/>
- `s.ignore channel #general` - Ignores commands in the #general channel.<br/>
- `s.ignore channel` - Ignores commands in the current channel.<br/>
- `s.ignore channel "General Channels"` - Use quotes for categories with spaces.<br/>
- `s.ignore channel 356236713347252226` - Also accepts IDs.<br/>

**Arguments:**<br/>
- `<channel>` - The channel to ignore. This can also be a thread or category channel.<br/>
 - Usage: `s.ignore channel [channel=operator.attrgetter('channel')]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel, discord.channel.CategoryChannel, discord.threads.Thread] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.unignore
Commands to remove servers or channels from the ignore list.<br/>
 - Usage: `s.unignore`
 - Checks: `server_only`
## s.unignore channel
Remove a channel, thread, or category from the ignore list.<br/>

Defaults to the current thread or channel.<br/>

**Examples:**<br/>
- `s.unignore channel #general` - Unignores commands in the #general channel.<br/>
- `s.unignore channel` - Unignores commands in the current channel.<br/>
- `s.unignore channel "General Channels"` - Use quotes for categories with spaces.<br/>
- `s.unignore channel 356236713347252226` - Also accepts IDs. Use this method to unignore categories.<br/>

**Arguments:**<br/>
- `<channel>` - The channel to unignore. This can also be a thread or category channel.<br/>
 - Usage: `s.unignore channel [channel=operator.attrgetter('channel')]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.channel.ForumChannel, discord.channel.CategoryChannel, discord.threads.Thread] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.unignore server
Remove this server from the ignore list.<br/>

**Example:**<br/>
- `s.unignore server` - Stops ignoring the current server<br/>
 - Usage: `s.unignore server`
 - Restricted to: `ADMIN`
 - Aliases: `server`
