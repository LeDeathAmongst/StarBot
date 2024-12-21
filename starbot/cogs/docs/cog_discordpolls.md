# s.discordpolls
Base command to manage polls.<br/>
 - Usage: `s.discordpolls`
 - Aliases: `discordpoll and dpoll`
 - Checks: `server_only`
## s.discordpolls log
Logging Configuration Commands For Polls.<br/>
 - Usage: `s.discordpolls log`
 - Restricted to: `ADMIN`
 - Aliases: `logging`
### s.discordpolls log settings
View the settings for poll logging.<br/>
 - Usage: `s.discordpolls log settings`
 - Aliases: `showsettings, show, and ss`
### s.discordpolls log message
Configure the poll logging message.<br/>

[Docs WIP]<br/>
 - Usage: `s.discordpolls log message <type> [message]`
### s.discordpolls log toggle
Toggle poll logging in this server.<br/>
 - Usage: `s.discordpolls log toggle <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.discordpolls log channel
Configure the logging channel.<br/>
 - Usage: `s.discordpolls log channel [channel=None]`
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
## s.discordpolls answer
View info a specific answer of a poll.<br/>

**Arguments**:<br/>
- `poll   :` the message with a poll attached.<br/>
- `number :` the answer number/id.<br/>
 - Usage: `s.discordpolls answer <poll> <number>`
 - Aliases: `option`
## s.discordpolls create
Create a poll.<br/>

Answers containing spaces must be enclosed in "double quotes".<br/>

**Argument**:<br/>
- `question :` question for the poll.<br/>
- `answers  :` poll answers, separated by spaces, text and emoji must be<br/>
split using `|`, `;` or `-`.<br/>
- `duration :` duration for the poll in hours, if not provided defaults to 12.<br/>
- `multiple :` whether users are allowed to select more than one answer,<br/>
defaults to false.<br/>

**Examples**:<br/>
- `s.dpoll create "New Poll" answer1 answer2 10 true`<br/>
- `s.dpoll create "New Poll" answer1|<:cogsred:594238096934043658> answer2 10 true`<br/>
- `s.dpoll create "New Poll" "Answer 1|<:cogsred:594238096934043658>" "Answer 2" 10 true`<br/>
 - Usage: `s.discordpolls create <question> <answers> [duration=12] [multiple=False]`
 - Cooldown: `1 per 30.0 seconds`
Extended Arg Info
> ### multiple: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.discordpolls end
End a poll owned by Starfire.<br/>

**Arguments**:<br/>
- `poll :` the message with a poll attached (must be owned by Starfire).<br/>
 - Usage: `s.discordpolls end <poll>`
 - Aliases: `stop`
## s.discordpolls giveroles
Mass apply role to all the voters of a specific answer in a poll.<br/>

**Arguments**:<br/>
- `poll   :` the message with a poll attached.<br/>
- `number :` the answer number/id.<br/>
- `roles  :` roles to be applied.<br/>
 - Usage: `s.discordpolls giveroles <poll> <number> <roles>`
 - Restricted to: `ADMIN`
 - Aliases: `roles and role`
 - Cooldown: `1 per 120.0 seconds`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.discordpolls answers
View all the answers of a poll.<br/>

**Arguments**:<br/>
- `poll :` the message with a poll attached.<br/>
 - Usage: `s.discordpolls answers <poll>`
 - Aliases: `options`
