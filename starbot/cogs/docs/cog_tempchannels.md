# s.tempchannels
Temporary text-channel creation (only 1 at the moment).<br/>
 - Usage: `s.tempchannels`
 - Restricted to: `MOD`
 - Aliases: `tc`
 - Checks: `server_only`
## s.tempchannels denyadd
Add a role to block sending message to the channel.<br/>

This role should be HIGHER in the role hierarchy than the roles in<br/>
the allowed list! The bot will not check for this.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role<br/>
    The role you wish to deny sending permissions in the temporary channel.<br/>
 - Usage: `s.tempchannels denyadd <role>`
 - Aliases: `da`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.tempchannels denyremove
Remove role from being blocked sending to the channel.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role<br/>
    The role you wish to remove from the deny list.<br/>
 - Usage: `s.tempchannels denyremove <role>`
 - Aliases: `denydelete, dd, and dr`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.tempchannels toggle
Toggle the creation/deletion of the temporary channel.<br/>
 - Usage: `s.tempchannels toggle`
## s.tempchannels start
Set the temp channel creation time. Use 24 hour time.<br/>

Parameters:<br/>
-----------<br/>
hour: int<br/>
    The hour to start the temporary channel.<br/>
minute: int<br/>
    The minute to start the temporary channel.<br/>
 - Usage: `s.tempchannels start <hour> <minute>`
Extended Arg Info
> ### hour: int
> ```
> A number without decimal places.
> ```
> ### minute: int
> ```
> A number without decimal places.
> ```
## s.tempchannels duration
Set the duration of the temp channel. Max 100 hours.<br/>

Parameters:<br/>
-----------<br/>
hours: int<br/>
    Number of hours to make this channel available.<br/>
minutes: int<br/>
    Number of minutes to make this channel available.<br/>

Example:<br/>
If hours = 1, and minutes = 3, then the channel will be available for<br/>
1 hour 3 minutes.<br/>
 - Usage: `s.tempchannels duration <hours> <minutes>`
Extended Arg Info
> ### hours: int
> ```
> A number without decimal places.
> ```
> ### minutes: int
> ```
> A number without decimal places.
> ```
## s.tempchannels archive
Toggle archiving the channel after the fact.<br/>
 - Usage: `s.tempchannels archive`
 - Restricted to: `ADMIN`
## s.tempchannels show
Show current settings.<br/>
 - Usage: `s.tempchannels show`
## s.tempchannels position
Set the position of the text channel in the list.<br/>

Parameters:<br/>
-----------<br/>
position: int<br/>
    The position where you want the temp channel to appear on the channel<br/>
    list.<br/>
 - Usage: `s.tempchannels position <position>`
 - Aliases: `pos`
Extended Arg Info
> ### position: int
> ```
> A number without decimal places.
> ```
## s.tempchannels allowadd
Add a role to allow access to the channel.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role<br/>
    The role you wish to allow access to the temporary channel.<br/>
 - Usage: `s.tempchannels allowadd <role>`
 - Aliases: `aa`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.tempchannels topic
Set the topic of the channel.<br/>

Parameters:<br/>
-----------<br/>
topic: str<br/>
    The topic of the channel.<br/>
 - Usage: `s.tempchannels topic <topic>`
Extended Arg Info
> ### topic: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tempchannels delete
Deletes the temp channel, if it exists.<br/>
 - Usage: `s.tempchannels delete`
 - Aliases: `remove, del, and rm`
## s.tempchannels allowremove
Remove a role from being able access the temporary channel.<br/>

Parameters:<br/>
-----------<br/>
role: discord.Role<br/>
    The role you wish to remove access from.<br/>
 - Usage: `s.tempchannels allowremove <role>`
 - Aliases: `allowdelete, ad, and ar`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.tempchannels name
Set the #name of the channel.<br/>

Parameters:<br/>
-----------<br/>
name: str<br/>
    The #name of the channel, which is shown on the left panel of Discord.<br/>
 - Usage: `s.tempchannels name <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tempchannels nsfw
Toggle NSFW requirements.<br/>
 - Usage: `s.tempchannels nsfw`
## s.tempchannels category
Set the parent category of the text channel.<br/>

Parameters:<br/>
-----------<br/>
category: discord.CategoryChannel<br/>
    The category you wish to nest the temporary channel under.<br/>
 - Usage: `s.tempchannels category [category]`
Extended Arg Info
> ### category: discord.channel.CategoryChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
