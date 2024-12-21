# s.race
Race related commands.<br/>
 - Usage: `s.race`
 - Checks: `server_only`
## s.race enter
Allows you to enter the race.<br/>

This command will return silently if a race has already started.<br/>
By not repeatedly telling the user that they can't enter the race, this<br/>
prevents spam.<br/>
 - Usage: `s.race enter`
## s.race start
Begins a new race.<br/>

You cannot start a new race until the active on has ended.<br/>

If you are the only player in the race, you will race against<br/>
your bot.<br/>

The user who started the race is automatically entered into the race.<br/>
 - Usage: `s.race start`
## s.race stats
Display your race stats.<br/>
 - Usage: `s.race stats [user=None]`
Extended Arg Info
> ### user: discord.member.Member = None
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
## s.race wipe
This command will wipe ALL race data.<br/>

You are given a confirmation dialog when using this command.<br/>
If you decide to wipe your data, all stats and settings will be deleted.<br/>
 - Usage: `s.race wipe`
 - Restricted to: `ADMIN`
## s.race bet
Bet on a user in the race.<br/>
 - Usage: `s.race bet <bet> <user>`
Extended Arg Info
> ### bet: int
> ```
> A number without decimal places.
> ```
> ### user: discord.member.Member
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
## s.race version
Displays the version of race.<br/>
 - Usage: `s.race version`
# s.setrace
Race settings commands.<br/>
 - Usage: `s.setrace`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setrace prize
Sets the prize pool for winners.<br/>

Set the prize to 0 if you do not wish any credits to be distributed.<br/>

When prize pooling is enabled (see `s.setrace togglepool`) the prize <br/>
will be distributed as follows:<br/>
    1st place 60%<br/>
    2nd place 30%<br/>
    3rd place 10%<br/>

Example:<br/>
    100 results in 60, 30, 10<br/>
    130 results in 78, 39, 13<br/>

When prize pooling is disabled, only first place will win, and they take<br/>
100% of the winnings.<br/>
 - Usage: `s.setrace prize <prize>`
Extended Arg Info
> ### prize: int
> ```
> A number without decimal places.
> ```
## s.setrace togglepool
Toggles on/off prize pooling.<br/>

Makes it so that prizes are pooled between 1st, 2nd, and 3rd.<br/>
It's a 60/30/10 split rounded to the nearest whole number.<br/>

There must be at least four human players, otherwise, only first<br/>
place wins.<br/>
 - Usage: `s.setrace togglepool`
## s.setrace payoutmin
Sets the number of players needed to payout prizes and bets.<br/>

This sets the required number of players needed to payout prizes.<br/>
If the number of racers aren't met, then nothing is paid out.<br/>

The person starting the race is not counted in this minimum number.<br/>
For example, if you are playing alone vs. the bot and the payout min<br/>
is set to 1, you need 1 human player besides the race starter for a<br/>
payout to occur.<br/>

If you want race to always pay out, then set players to 0.<br/>
 - Usage: `s.setrace payoutmin <players>`
Extended Arg Info
> ### players: int
> ```
> A number without decimal places.
> ```
## s.setrace mode
Changes the race mode.<br/>

Race can either be in normal mode or zoo mode.<br/>

Normal Mode:<br/>
    All racers are turtles.<br/>

Zoo Mode:<br/>
    Racers are randomly selected from a list of animals with<br/>
    different attributes.<br/>
 - Usage: `s.setrace mode <mode>`
Extended Arg Info
> ### mode: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setrace wait
Changes the wait time before a race starts.<br/>

This only affects the period where race is still waiting<br/>
for more participants to join the race.<br/>
 - Usage: `s.setrace wait <wait>`
Extended Arg Info
> ### wait: int
> ```
> A number without decimal places.
> ```
## s.setrace bet
Bet settings for race.<br/>
 - Usage: `s.setrace bet`
### s.setrace bet max
Sets the betting maximum.<br/>
 - Usage: `s.setrace bet max <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
### s.setrace bet toggle
Toggles betting on and off.<br/>
 - Usage: `s.setrace bet toggle`
### s.setrace bet min
Sets the betting minimum.<br/>
 - Usage: `s.setrace bet min <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
### s.setrace bet multiplier
Sets the betting multiplier.<br/>

If the bot's economy mode is set to global instead of server-based, this setting is not available.<br/>
 - Usage: `s.setrace bet multiplier <multiplier>`
Extended Arg Info
> ### multiplier: float
> ```
> A number with or without decimal places.
> ```
