# s.banmessageset
BanMessage settings.<br/>
 - Usage: `s.banmessageset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.banmessageset listmessages
List ban message templates.<br/>
 - Usage: `s.banmessageset listmessages`
## s.banmessageset hackban
Set if hackbans should trigger ban messages.<br/>

INFO: Hackbans are bans of users<br/>
that weren't members of the server (also called preemptive bans).<br/>
 - Usage: `s.banmessageset hackban [enabled=None]`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.banmessageset setimage
Set image for ban message.<br/>
 - Usage: `s.banmessageset setimage`
## s.banmessageset addmessage
Add ban message.<br/>

Those fields will get replaced automatically:<br/>
$username - The banned user's name<br/>
$server - The name of the server<br/>

Note: Ban message can also have image.<br/>
To set it, use `s.banmessageset setimage`<br/>
 - Usage: `s.banmessageset addmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.banmessageset unsetimage
Unset image for ban message.<br/>
 - Usage: `s.banmessageset unsetimage`
## s.banmessageset channel
Set channel for ban messages. Leave empty to disable.<br/>
 - Usage: `s.banmessageset channel [channel=None]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.banmessageset removemessage
Remove ban message.<br/>
 - Usage: `s.banmessageset removemessage`
 - Aliases: `deletemessage`
