# s.jpset
Adjust the settings for the cog.<br/>
 - Usage: `s.jpset`
 - Restricted to: `ADMIN`
 - Aliases: `joinpingset`
 - Checks: `server_only`
## s.jpset message
Set the message that will be sent when a user joins.<br/>

Usable placeholders include:<br/>
- {member} (the member that joined)<br/>
    - {member(mention)} (the mention)<br/>
    - {member(id)} (the id)<br/>
    - {member(name)} (the name)<br/>
    - {member(discriminator)} (the discriminator)<br/>

- {server} (the server the member joined)<br/>

This messsage uses tagscript and allows embed<br/>
 - Usage: `s.jpset message <message>`
 - Aliases: `m`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.jpset deleteafter
Set the time in seconds after which the ping message will be deleted.<br/>
 - Usage: `s.jpset deleteafter <seconds>`
 - Aliases: `da`
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```
## s.jpset channel
Set the channels where the pings will be sent on member join.<br/>
 - Usage: `s.jpset channel`
 - Aliases: `c and channels`
### s.jpset channel add
Remove the channels from the list of channels where the pings will be sent on member join.<br/>
 - Usage: `s.jpset channel add <channels>`
 - Aliases: `a`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.jpset channel remove
Add the channels to the list of channels where the pings will be sent on member join.<br/>
 - Usage: `s.jpset channel remove <channels>`
 - Aliases: `r`
Extended Arg Info
> ### *channels: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.jpset show
Show the current joinping settings.<br/>
 - Usage: `s.jpset show`
 - Aliases: `showsettings, settings, and setting`
