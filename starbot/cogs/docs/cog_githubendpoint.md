# s.githubendpoint
Manage messages sent from GitHub.<br/>
 - Usage: `s.githubendpoint`
 - Restricted to: `ADMIN`
## s.githubendpoint registerself

 - Usage: `s.githubendpoint registerself <git_name>`
Extended Arg Info
> ### git_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.githubendpoint removechannel

 - Usage: `s.githubendpoint removechannel <repo> <channel>`
Extended Arg Info
> ### repo: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.githubendpoint addchannel

 - Usage: `s.githubendpoint addchannel <repo> <channel>`
Extended Arg Info
> ### repo: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.githubendpoint checkchannels

 - Usage: `s.githubendpoint checkchannels <repo>`
Extended Arg Info
> ### repo: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
