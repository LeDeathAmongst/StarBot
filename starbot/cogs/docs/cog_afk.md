# s.afk
Set your AFK status with an optional reason.<br/>
 - Usage: `s.afk [reason]`
Extended Arg Info
> ### reason: str = 'No reason provided'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.setafknick
Set a custom nickname template for AFK users. Use {displayname} as a placeholder for the user's display name.<br/>
 - Usage: `s.setafknick [template]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### template: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.setafkcolor
Set the embed color for AFK messages.<br/>
 - Usage: `s.setafkcolor <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
