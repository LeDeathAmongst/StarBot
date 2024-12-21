# s.monopoly
Play monopoly with 2-8 people.<br/>

Use the optional parameter "savefile" to load a saved game.<br/>
 - Usage: `s.monopoly [savefile=None]`
 - Checks: `server_only`
Extended Arg Info
> ### savefile: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.monopoly list
List available save files.<br/>
 - Usage: `s.monopoly list`
## s.monopoly delete
Delete one or more save files.<br/>

This cannot be undone.<br/>
 - Usage: `s.monopoly delete <savefiles>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### *savefiles: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.monopolyconvert list
List save files that can be converted.<br/>
 - Usage: `s.monopolyconvert list`
# s.monopolystop
Stop the game of monopoly in this channel.<br/>
 - Usage: `s.monopolystop`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
# s.monopolyset
Config options for monopoly.<br/>
 - Usage: `s.monopolyset`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.monopolyset darkmode
Set if the board should be a darker varient.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset darkmode [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.monopolyset mention
Set if players should be mentioned when their turn begins.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset mention [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.monopolyset auction
Set if properties should be auctioned when passed on.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset auction [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.monopolyset maxjailrolls
Set the maximum number of rolls in jail before bail has to be paid.<br/>

Defaults to 3.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset maxjailrolls [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset luxury
Set how much Luxury Tax should cost.<br/>

Defaults to 100.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset luxury [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset minraise
Set the minimum raise in auctions.<br/>

Defaults to 1.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset minraise [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset bail
Set how much bail should cost.<br/>

Defaults to 50.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset bail [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset income
Set how much Income Tax should cost.<br/>

Defaults to 200.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset income [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset timeout
Set the amount of time before the game times out.<br/>

Value is in seconds.<br/>
Use -1 to disable the timeout.<br/>
Defaults to 60.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset timeout [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset go
Set the base value of passing go.<br/>

Defaults to 200.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset go [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset hotellimit
Set a limit on the number of hotels that can be bought.<br/>

Use -1 to disable the limit.<br/>
Defaults to 12.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset hotellimit [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset houselimit
Set a limit on the number of houses that can be bought.<br/>

Use -1 to disable the limit.<br/>
Defaults to 32.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset houselimit [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset startingcash
Set how much money players should start the game with.<br/>

Defaults to 1500.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset startingcash [value=None]`
Extended Arg Info
> ### value: int = None
> ```
> A number without decimal places.
> ```
## s.monopolyset freeparking
Set the reward for landing on free parking.<br/>

Use an integer to set a static reward.<br/>
Use "none" for no reward.<br/>
Use "tax" to use the sum of taxes and fees as the reward.<br/>
Defaults to none.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset freeparking [value=None]`
Extended Arg Info
> ### value: Union[int, str] = None
> ```
> A number without decimal places.
> ```
## s.monopolyset thread
Set if a thread should be created per-game to contain game messages.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset thread [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.monopolyset doublego
Set if landing on go should double the amount of money given.<br/>

Defaults to False.<br/>
This value is server specific.<br/>
 - Usage: `s.monopolyset doublego [value=None]`
Extended Arg Info
> ### value: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
