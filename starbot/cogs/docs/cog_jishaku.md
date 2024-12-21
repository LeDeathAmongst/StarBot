# s.jishaku
The Jishaku debug and diagnostic commands.<br/>

This command on its own gives a status brief.<br/>
All other functionality is within its subcommands.<br/>
 - Usage: `s.jishaku`
 - Aliases: `jsk`
## s.jishaku repeat
Runs a command multiple times in a row.<br/>

This acts like the command was invoked several times manually, so it obeys cooldowns.<br/>
You can use this in conjunction with `jsk sudo` to bypass this.<br/>
 - Usage: `s.jishaku repeat <times> <command_string>`
Extended Arg Info
> ### times: int
> ```
> A number without decimal places.
> ```
> ### command_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.jishaku shutdown
Logs this bot out.<br/>
 - Usage: `s.jishaku shutdown`
 - Aliases: `logout`
## s.jishaku py_inspect
Evaluation of Python code with inspect information.<br/>
 - Usage: `s.jishaku py_inspect <argument>`
 - Aliases: `pyi, python_inspect, and pythoninspect`
## s.jishaku source
Displays the source code for a command.<br/>
 - Usage: `s.jishaku source <command_name>`
 - Aliases: `src`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.jishaku retain
Turn variable retention for REPL on or off.<br/>

Provide no argument for current status.<br/>
 - Usage: `s.jishaku retain [toggle]`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.jishaku git
Shortcut for 'jsk sh git'. Invokes the system shell.<br/>
 - Usage: `s.jishaku git <argument>`
## s.jishaku hide
Hides Jishaku from the help command.<br/>
 - Usage: `s.jishaku hide`
## s.jishaku show
Shows Jishaku in the help command.<br/>
 - Usage: `s.jishaku show`
## s.jishaku cancel
Cancels a task with the given index.<br/>

If the index passed is -1, will cancel the last task instead.<br/>
 - Usage: `s.jishaku cancel <index>`
Extended Arg Info
> ### index: Union[int, str]
> ```
> A number without decimal places.
> ```
## s.jishaku load
Loads or reloads the given extension names.<br/>

Reports any extensions that failed to load.<br/>
 - Usage: `s.jishaku load <extensions>`
 - Aliases: `reload`
## s.jishaku tasks
Shows the currently running jishaku tasks.<br/>
 - Usage: `s.jishaku tasks`
## s.jishaku dis
Disassemble Python code into bytecode.<br/>
 - Usage: `s.jishaku dis <argument>`
 - Aliases: `disassemble`
## s.jishaku invite
Retrieve the invite URL for this bot.<br/>

If the names of permissions are provided, they are requested as part of the invite.<br/>
 - Usage: `s.jishaku invite <perms>`
Extended Arg Info
> ### *perms: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.jishaku cat
Read out a file, using syntax highlighting if detected.<br/>

Lines and linespans are supported by adding '#L12' or '#L12-14' etc to the end of the filename.<br/>
 - Usage: `s.jishaku cat <argument>`
Extended Arg Info
> ### argument: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.jishaku pip
Shortcut for 'jsk sh pip'. Invokes the system shell.<br/>
 - Usage: `s.jishaku pip <argument>`
## s.jishaku debug
Run a command timing execution and catching exceptions.<br/>
 - Usage: `s.jishaku debug <command_string>`
 - Aliases: `dbg`
Extended Arg Info
> ### command_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.jishaku curl
Download and display a text file from the internet.<br/>

This command is similar to jsk cat, but accepts a URL.<br/>
 - Usage: `s.jishaku curl <url>`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.jishaku py
Direct evaluation of Python code.<br/>
 - Usage: `s.jishaku py <argument>`
 - Aliases: `python`
## s.jishaku shell
Executes statements in the system shell.<br/>

This uses the system shell as defined in $SHELL, or `/bin/bash` otherwise.<br/>
Execution can be cancelled by closing the paginator.<br/>
 - Usage: `s.jishaku shell <argument>`
 - Aliases: `bash, sh, powershell, ps1, ps, and cmd`
## s.jishaku rtt
Calculates Round-Trip Time to the API.<br/>
 - Usage: `s.jishaku rtt`
 - Aliases: `ping`
## s.jishaku voice
Voice-related commands.<br/>

If invoked without subcommand, relays current voice state.<br/>
 - Usage: `s.jishaku voice`
 - Aliases: `vc`
### s.jishaku voice resume
Resumes a running audio source, if there is one.<br/>
 - Usage: `s.jishaku voice resume`
### s.jishaku voice disconnect
Disconnects from the voice channel in this server, if there is one.<br/>
 - Usage: `s.jishaku voice disconnect`
 - Aliases: `dc`
### s.jishaku voice play
Plays audio direct from a URI.<br/>

Can be either a local file or an audio resource on the internet.<br/>
 - Usage: `s.jishaku voice play <uri>`
 - Aliases: `play_local`
Extended Arg Info
> ### uri: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.jishaku voice stop
Stops running an audio source, if there is one.<br/>
 - Usage: `s.jishaku voice stop`
### s.jishaku voice pause
Pauses a running audio source, if there is one.<br/>
 - Usage: `s.jishaku voice pause`
### s.jishaku voice volume
Adjusts the volume of an audio source if it is supported.<br/>
 - Usage: `s.jishaku voice volume <percentage>`
Extended Arg Info
> ### percentage: float
> ```
> A number with or without decimal places.
> ```
### s.jishaku voice join
Joins a voice channel, or moves to it if already connected.<br/>

Passing a voice channel uses that voice channel.<br/>
Passing a member will use that member's current voice channel.<br/>
Passing nothing will use the author's voice channel.<br/>
 - Usage: `s.jishaku voice join [destination]`
 - Aliases: `connect`
Extended Arg Info
> ### destination: Union[discord.channel.VoiceChannel, discord.member.Member] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.jishaku permtrace
Calculates the source of granted or rejected permissions.<br/>

This accepts a channel, and either a member or a list of roles.<br/>
It calculates permissions the same way Discord does, while keeping track of the source.<br/>
 - Usage: `s.jishaku permtrace <channel> <targets>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### *targets: Union[discord.member.Member, discord.role.Role]
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
## s.jishaku unload
Unloads the given extension names.<br/>

Reports any extensions that failed to unload.<br/>
 - Usage: `s.jishaku unload <extensions>`
## s.jishaku override
Run a command with a different user, channel, or thread, optionally bypassing checks and cooldowns.<br/>

Users will try to resolve to a Member, but will use a User if it can't find one.<br/>
 - Usage: `s.jishaku override <overrides> <command_string>`
 - Aliases: `execute, exec, override!, execute!, and exec!`
Extended Arg Info
> ### command_string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
