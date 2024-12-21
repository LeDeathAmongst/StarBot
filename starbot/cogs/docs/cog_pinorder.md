# s.pinorder
Group of commands to set some messages to be always pinned on top in a specified order.<br/>
 - Usage: `s.pinorder`
## s.pinorder list
Lists message pins managed by this cog in this channel or a given channel.<br/>
 - Usage: `s.pinorder list <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.pinorder unpin
Unpins a message and removes it from the message pins managed by this cog.<br/>
 - Usage: `s.pinorder unpin <message>`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
## s.pinorder refresh
Manually triggers a reshuffle of pins to keep the set order.<br/>
 - Usage: `s.pinorder refresh`
## s.pinorder pin
Pins a message and sets its position in the messages managed by this cog.<br/>
Any manual pins will trigger a reshuffle of pins to keep these messages on top in the given order.<br/>
 - Usage: `s.pinorder pin <message> <position>`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
> ### position: int
> ```
> A number without decimal places.
> ```
