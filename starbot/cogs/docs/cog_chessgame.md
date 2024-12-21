# s.chess
manage chess games<br/>
 - Usage: `s.chess`
## s.chess move
move the next game piece, using Standard Algebraic Notation<br/>
 - Usage: `s.chess move <game_name> <move>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### move: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.chess start
start a new game<br/>

_Standard is the default when no game type is given_<br/>
__**1**__: Standard, Chess, Classical, Normal, Illegal, From Position<br/>
__**2**__: Suicide, Suicide chess<br/>
__**3**__: Giveaway, Giveaway chess, Give away, Give away chess<br/>
__**4**__: Antichess, Anti chess, Anti<br/>
__**5**__: Atomic, Atom, Atomic chess<br/>
__**6**__: King of the Hill, KOTH, kingOfTheHill<br/>
__**7**__: Racing Kings, Racing, Race, racingkings<br/>
__**8**__: Horde, Horde chess<br/>
__**9**__: Three-check, Three check, Threecheck, Three check chess, 3-check, 3 check, 3check<br/>
__**10**__: Crazyhouse, Crazy House, House, ZH<br/>
 - Usage: `s.chess start <other_player> [game_name=None] [game_type=None]`
Extended Arg Info
> ### other_player: discord.member.Member
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
> ### game_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### game_type: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.chess show
reposts the last gameboard state<br/>
 - Usage: `s.chess show <game_name>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.chess list
list all available games<br/>
 - Usage: `s.chess list`
## s.chess scoreboard
scoreboard related commands<br/>
 - Usage: `s.chess scoreboard`
### s.chess scoreboard find
find a player's score. If none is provided this will look for the requester's score<br/>
 - Usage: `s.chess scoreboard find [player=None]`
Extended Arg Info
> ### player: discord.member.Member = None
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
### s.chess scoreboard list
list users scoreboard from highest to lowest<br/>

Scoreboard can be sorted by elo, wins, losses, or ties.<br/>
Scoreboard is sorted by wins by default.<br/>
 - Usage: `s.chess scoreboard list [sort_by=wins]`
Extended Arg Info
> ### sort_by: str = 'wins'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.chess draw
draw related commands<br/>
 - Usage: `s.chess draw`
### s.chess draw byagreement
Offer draw by agreement<br/>
 - Usage: `s.chess draw byagreement <game_name>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.chess draw claim
if valid claim made to draw the game will end with no victor<br/>
 - Usage: `s.chess draw claim <game_name> <claim_type>`
Extended Arg Info
> ### game_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### claim_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
