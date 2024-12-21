# s.cmdchannel (Hybrid Command)
Use `s.cmdchannel`, `s.cmduser` and `s.cmduserchannel`.<br/>
 - Usage: `s.cmdchannel <channel> <command>`
 - Slash Usage: `/cmdchannel <channel> <command>`
 - Aliases: `cmdmock`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.cmdchannel channel (Hybrid Command)
Act as if the command had been typed in the channel of your choice.<br/>
The prefix must not be entered if it is a command. It will be a message only, if the command is invalid.<br/>

Use `s.cmdchannel`!<br/>
 - Usage: `s.cmdchannel channel <channel> <command>`
 - Slash Usage: `/cmdchannel channel <channel> <command>`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.cmdchannel testvar (Hybrid Command)
Test variables.<br/>
 - Usage: `s.cmdchannel testvar`
 - Slash Usage: `/cmdchannel testvar`
