# s.ryd
Insert YouTube video url or id as argument to get dislikes count<br/>
 - Usage: `s.ryd <url>`
 - Aliases: `returnyoutubedislike and ytdislikes`
Extended Arg Info
> ### url
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.ryd-config
Change settings of RYD Cog<br/>
 - Usage: `s.ryd-config`
## s.ryd-config me

 - Usage: `s.ryd-config me`
 - Checks: `server_only`
### s.ryd-config me disable
Disable/Enable message scanning for the specific person<br/>
 - Usage: `s.ryd-config me disable`
## s.ryd-config server

 - Usage: `s.ryd-config server`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
### s.ryd-config server disable
Disable/Enable message scanning for server<br/>
 - Usage: `s.ryd-config server disable`
### s.ryd-config server channel
Disable/Enable message scanning for channel. Even in whitelist mode<br/>
 - Usage: `s.ryd-config server channel [channel=None]`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.ryd-config server whitelist
Enable/Disable whitelist mode for server<br/>
 - Usage: `s.ryd-config server whitelist`
