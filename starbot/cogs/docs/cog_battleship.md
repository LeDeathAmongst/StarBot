# s.battleship
Start a game of battleship.<br/>
 - Usage: `s.battleship [opponent=None]`
 - Checks: `server_only`
Extended Arg Info
> ### opponent: discord.member.Member = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
# s.battleshipstop
Stop the game of battleship in this channel.<br/>
 - Usage: `s.battleshipstop`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
# s.battleshipboard
View your current board from an ongoing game in your DMs.<br/>

Specify the channel ID of the channel the game is in.<br/>
 - Usage: `s.battleshipboard [channel=None]`
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
# s.battleshipset
Config options for battleship.<br/>
 - Usage: `s.battleshipset`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.battleshipset mention
Set if players should be mentioned when their turn begins.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `s.battleshipset mention [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.battleshipset imgboard
Set if the board should be displayed using an image.<br/>

Defaults to True.<br/>
This value is server specific.<br/>
 - Usage: `s.battleshipset imgboard [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.battleshipset extra
Set if an extra shot should be given after a hit.<br/>

Defaults to True.<br/>
This value is server specific.<br/>
 - Usage: `s.battleshipset extra [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.battleshipset thread
Set if a thread should be created per-game to contain game messages.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `s.battleshipset thread [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
