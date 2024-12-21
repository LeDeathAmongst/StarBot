# s.rt
Commands to configure Random Topic.<br/>
 - Usage: `s.rt`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.rt setrole
Set the role to be pinged when a new topic is posted.<br/>

Use this command to specify which role should be mentioned whenever a new random topic is generated and sent to the channel.<br/>
 - Usage: `s.rt setrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.rt setinterval
Set the interval for sending random topics (in minutes).<br/>

Use this command to set the interval at which the bot will send random topics.<br/>
 - Usage: `s.rt setinterval <interval>`
Extended Arg Info
> ### interval: int
> ```
> A number without decimal places.
> ```
## s.rt setchannel
Set the channel where random topics will be sent.<br/>

Use this command to specify which text channel the bot should use to send the random topics. Make sure to mention the channel.<br/>
 - Usage: `s.rt setchannel <channel>`
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
## s.rt settitle
Set the title for the Random Topic embed.<br/>

Use this command to customize the title that will appear in the random topic embeds.<br/>
 - Usage: `s.rt settitle <title>`
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
