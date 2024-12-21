# s.evolution
EVOLVE THE GREATEST ANIMALS OF ALL TIME!!!!<br/>
 - Usage: `s.evolution`
 - Aliases: `e and evo`
## s.evolution start
Start your adventure...<br/>
 - Usage: `s.evolution start`
## s.evolution evolve
Evolve them animals to get more of da economy credits<br/>
 - Usage: `s.evolution evolve <level> [amount=1]`
Extended Arg Info
> ### level: int
> ```
> A number without decimal places.
> ```
> ### amount: int = 1
> ```
> A number without decimal places.
> ```
## s.evolution market
Buy or sell animals from different sellers<br/>
 - Usage: `s.evolution market`
### s.evolution market daily
View the daily deals.<br/>

These will come at a lower price than the store, but can only be bought once per day.<br/>

Status guide:<br/>
    A: Available to be bought and put in backyard<br/>
    B: Already purchased<br/>
    S: Available to be bought, but will be put in stash because you either do not have the space for the, or above your level threshold<br/>
 - Usage: `s.evolution market daily`
### s.evolution market store
Buy animals from the always in-stock store.<br/>

While the store will always have animals for sale, you cannot buy above a certain level,<br/>
and they will be for a higher price.<br/>
 - Usage: `s.evolution market store [level=None] [amount=1] [skip_confirmation=False]`
 - Aliases: `shop`
Extended Arg Info
> ### level: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### amount: Optional[int] = 1
> ```
> A number without decimal places.
> ```
> ### skip_confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.evolution deletemydata
Delete your game data.<br/>

WARNING!  Your data *will not be able to be recovered*!<br/>
 - Usage: `s.evolution deletemydata [check=False]`
Extended Arg Info
> ### check: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.evolution stash
Where your special animals are put if you cannot hold them in your backyard<br/>
 - Usage: `s.evolution stash`
### s.evolution stash claim
Claim animals or perks from your stash.<br/>
 - Usage: `s.evolution stash claim`
#### s.evolution stash claim animal
Claim animals from your stash<br/>
 - Usage: `s.evolution stash claim animal <level>`
Extended Arg Info
> ### level: int
> ```
> A number without decimal places.
> ```
### s.evolution stash view
View the animals and perks you have in your stash<br/>
 - Usage: `s.evolution stash view`
## s.evolution backyard
Where ya animals live!  Pass 1 or true to put it in a menu.<br/>
 - Usage: `s.evolution backyard [use_menu=False]`
 - Aliases: `by`
Extended Arg Info
> ### use_menu: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
