# s.songshareset
Set up the songshare cog<br/>
 - Usage: `s.songshareset`
 - Restricted to: `ADMIN`
 - Aliases: `setsongshare`
 - Checks: `bot_in_a_server`
## s.songshareset allserver
Toggle between complete server or only a single channel<br/>

Set True to activate it in the entire server, False if only in selected channels. Leave emtpy totoggle<br/>
 - Usage: `s.songshareset allserver [toggle=None]`
 - Aliases: `everywhere and server`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.songshareset blacklist
Blacklist channels from the songshare<br/>

Overrides all set channels<br/>
 - Usage: `s.songshareset blacklist`
### s.songshareset blacklist add
Add a channel to the songshare blacklist<br/>
 - Usage: `s.songshareset blacklist add <channel>`
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
### s.songshareset blacklist reset
Reset the songshare blacklist channels to the entire server<br/>
 - Usage: `s.songshareset blacklist reset`
### s.songshareset blacklist remove
Remove a channel from the songshare blacklist<br/>
 - Usage: `s.songshareset blacklist remove <channel>`
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
## s.songshareset channel
Select channels for the songshare<br/>
 - Usage: `s.songshareset channel`
### s.songshareset channel add
Add a channel to the songshare<br/>
 - Usage: `s.songshareset channel add <channel>`
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
### s.songshareset channel reset
Reset the songshare channels to the entire server<br/>
 - Usage: `s.songshareset channel reset`
### s.songshareset channel remove
Remove a channel from the songshare<br/>
 - Usage: `s.songshareset channel remove <channel>`
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
