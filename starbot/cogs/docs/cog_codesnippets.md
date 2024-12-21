# s.codesnippets (Hybrid Command)
Send code content from a GitHub/Gist/GitLab/BitBucket/Pastebin/Hastebin URL.<br/>
 - Usage: `s.codesnippets [limit=3] <urls>`
 - Slash Usage: `/codesnippets [limit=3] <urls>`
 - Aliases: `codesnippet`
Extended Arg Info
> ### urls: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.setcodesnippets (Hybrid Command)
Configure CodeSnippets.<br/>
 - Usage: `s.setcodesnippets`
 - Slash Usage: `/setcodesnippets`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setcodesnippets removechannel (Hybrid Command)
Remove a channel where the cog have to send automatically code snippets from URLs.<br/>
 - Usage: `s.setcodesnippets removechannel <channel>`
 - Slash Usage: `/setcodesnippets removechannel <channel>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.setcodesnippets addchannel (Hybrid Command)
Add a channel where the cog have to send automatically code snippets from URLs.<br/>
 - Usage: `s.setcodesnippets addchannel <channel>`
 - Slash Usage: `/setcodesnippets addchannel <channel>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.setcodesnippets showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setcodesnippets showsettings [with_dev=False]`
 - Slash Usage: `/setcodesnippets showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
