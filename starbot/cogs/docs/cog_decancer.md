# s.decancer
Remove special/cancerous characters from user nicknames<br/>

Parameters:<br/>
    ctx (commands.Context): The command invocation context.<br/>
    member (discord.Member): The user who's nickname is being modified.<br/>

Returns:<br/>
    None<br/>
 - Usage: `s.decancer <member>`
 - Restricted to: `MOD`
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
# s.decancerset
Settings for Decancer<br/>
 - Usage: `s.decancerset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.decancerset defaultname
Set the default name for new users.<br/>

Args:<br/>
    name (str): The name to use for new users.<br/>
 - Usage: `s.decancerset defaultname <name>`
 - Checks: `server_only`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.decancerset modlog
Set the modlog channel for Decancer.<br/>

Args:<br/>
    channel (discord.TextChannel | None): The channel to log to. If `None`, the current channel will be used.<br/>
 - Usage: `s.decancerset modlog [channel=None]`
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
## s.decancerset auto
Toggle automatically decancering new users.<br/>

Args:<br/>
    status (bool | None): If True, then new users will be decancered. If False, they will not.<br/>
        If None, then the current setting will be toggled.<br/>
 - Usage: `s.decancerset auto [status=None]`
 - Checks: `server_only`
Extended Arg Info
> ### status: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.decancerset showsettings
Shows the current settings for Decancer.<br/>

Args:<br/>
    ctx (commands.Context): The invocation context.<br/>

Returns:<br/>
    discord.Message: The sent message with the settings.<br/>
 - Usage: `s.decancerset showsettings`
 - Aliases: `settings and ss`
 - Checks: `server_only`
# s.dehoist
Decancer all members of the targeted role.<br/>

Role defaults to all members of the server.<br/>
 - Usage: `s.dehoist [role]`
 - Restricted to: `MOD`
 - Cooldown: `1 per 36000.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
