# s.economytrickle
Configure various settings<br/>
 - Usage: `s.economytrickle`
 - Restricted to: `ADMIN`
 - Aliases: `trickleset`
 - Checks: `is_owner_if_bank_global`
## s.economytrickle settings
Show the current settings<br/>
 - Usage: `s.economytrickle settings`
 - Restricted to: `ADMIN`
 - Aliases: `info and showsettings`
 - Checks: `is_owner_if_bank_global`
## s.economytrickle credits
Set the number of credits to grant<br/>

Set the number to 0 to disable<br/>
Max value is 1000<br/>
 - Usage: `s.economytrickle credits <number>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
## s.economytrickle voice
Set the number of credits to grant every minute<br/>

Set the number to 0 to disable<br/>
Max value is 1000<br/>
 - Usage: `s.economytrickle voice <number>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
## s.economytrickle showblocks
Provide a list of channels that are on the blocklist for this server<br/>
 - Usage: `s.economytrickle showblocks`
 - Restricted to: `ADMIN`
 - Aliases: `showblock`
 - Checks: `server_only`
## s.economytrickle messages
Set the number of messages required to gain credits<br/>

Set the number to 0 to disable<br/>
Max value is 100<br/>
 - Usage: `s.economytrickle messages <number>`
 - Restricted to: `ADMIN`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### number: int
> ```
> A number without decimal places.
> ```
## s.economytrickle blocklist
Add/Remove the current channel (or a specific channel) to the blocklist<br/>

Not passing a channel will add/remove the channel you ran the command in to the blocklist<br/>
 - Usage: `s.economytrickle blocklist [channel=None]`
 - Restricted to: `ADMIN`
 - Aliases: `blacklist`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
