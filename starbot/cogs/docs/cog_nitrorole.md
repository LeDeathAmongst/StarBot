# s.nitrorole
Settings for NitroRole cog.<br/>
 - Usage: `s.nitrorole`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.nitrorole setimage
Set image for new booster message.<br/>
 - Usage: `s.nitrorole setimage`
## s.nitrorole removemessage
Remove new booster message.<br/>
 - Usage: `s.nitrorole removemessage`
 - Aliases: `deletemessage`
## s.nitrorole unassignonboostend
Set if booster role should be unassigned when someone stops boosting server.<br/>

Leave empty to see current settings.<br/>
 - Usage: `s.nitrorole unassignonboostend [enabled=None]`
Extended Arg Info
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.nitrorole unsetimage
Unset image for new booster message.<br/>
 - Usage: `s.nitrorole unsetimage`
## s.nitrorole listmessages
List new booster message templates.<br/>
 - Usage: `s.nitrorole listmessages`
## s.nitrorole autoassignrole
Set role that will be autoassigned after someone boosts server.<br/>

Leave empty to not assign any role.<br/>
 - Usage: `s.nitrorole autoassignrole [role]`
Extended Arg Info
> ### role: discord.role.Role = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.nitrorole channel
Set channel for new booster messages. Leave empty to disable.<br/>
 - Usage: `s.nitrorole channel [channel=None]`
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
## s.nitrorole addmessage
Add new booster message.<br/>

Those fields will get replaced automatically:<br/>
$mention - Mention the user who boosted<br/>
$username - The user's display name<br/>
$server - The name of the server<br/>
$count - The number of boosts server has<br/>
(this isn't the same as amount of users that boost this server)<br/>
$plural - Empty if count is 1. 's' otherwise<br/>

Note: New booster message can also have image.<br/>
To set it, use `s.nitrorole setimage`<br/>
 - Usage: `s.nitrorole addmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
