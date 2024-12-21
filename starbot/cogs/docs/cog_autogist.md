# s.autogistset
AutoGist settings.<br/>
 - Usage: `s.autogistset`
 - Restricted to: `ADMIN`
## s.autogistset blockchannels
Block the bot from listening to the given channels.<br/>
 - Usage: `s.autogistset blockchannels <channels>`
 - Aliases: `blockchannel`
 - Checks: `server_only`
Extended Arg Info
> ### *channels: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.autogistset allowchannels
Allow the bot to listen to the given channels.<br/>
 - Usage: `s.autogistset allowchannels <channels>`
 - Aliases: `allowchannel`
 - Checks: `server_only`
Extended Arg Info
> ### *channels: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.autogistset extensions
Settings for file extensions<br/>
that are required for AutoGist to upload file to Gist.<br/>

By default AutoGist will look for files with `.txt` and `.log` extensions.<br/>
 - Usage: `s.autogistset extensions`
 - Aliases: `ext and exts`
 - Checks: `server_only`
### s.autogistset extensions remove
Remove file extensions from the list.<br/>

Example:<br/>
`s.autogist extensions remove txt .log` - removes `.txt` and `.log` extensions.<br/>
 - Usage: `s.autogistset extensions remove <extensions>`
 - Aliases: `delete`
Extended Arg Info
> ### *extensions: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.autogistset extensions list
List file extensions that are required for AutoGist to upload file to Gist.<br/>
 - Usage: `s.autogistset extensions list`
### s.autogistset extensions add
Add file extensions to the list.<br/>

Example:<br/>
`s.autogist extensions add txt .log` - adds `.txt` and `.log` extensions.<br/>
 - Usage: `s.autogistset extensions add <extensions>`
Extended Arg Info
> ### *extensions: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.autogistset listoverridden
List server channels that don't use the default setting.<br/>
 - Usage: `s.autogistset listoverridden`
 - Checks: `server_only`
## s.autogistset listentobots
Make AutoGist listen to messages from other bots in this server.<br/>

NOTE: To make bot listen to messages from itself,<br/>
you need to use `s.autogistset listentoself` command.<br/>
 - Usage: `s.autogistset listentobots [state=None]`
 - Checks: `server_only`
Extended Arg Info
> ### state: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.autogistset listentohumans
Make AutoGist listen to messages from humans in this server.<br/>
 - Usage: `s.autogistset listentohumans [state=None]`
 - Checks: `server_only`
Extended Arg Info
> ### state: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.autogistset listentoself
Make the bot listen to messages from itself in this server.<br/>

See also: `s.autogistset listentobots` command,<br/>
that makes the bot listen to other bots.<br/>
 - Usage: `s.autogistset listentoself [state=None]`
 - Checks: `server_only`
Extended Arg Info
> ### state: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.autogistset channeldefault
Set whether AutoGist should by default listen to channels.<br/>

If default is set to True, bot will only listen to channels it was explicitly<br/>
allowed to listen to with `s.autogistset allowchannels` command.<br/>

If default is set to False, bot will listen to all channels except the ones<br/>
it was explicitly blocked from listening to<br/>
with `s.autogistset denychannels` command.<br/>

By default, servers will not listen to any channel.<br/>
Use `s.autogist channeldefault` without a setting to see current mode.<br/>
 - Usage: `s.autogistset channeldefault [allow=None]`
 - Checks: `server_only`
Extended Arg Info
> ### allow: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
