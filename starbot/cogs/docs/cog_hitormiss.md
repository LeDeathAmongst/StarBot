# s.throw
Throw an item you own at a user<br/>

`item` is the name of the item you want to throw<br/>
`target` is the user you want to throw the item at<br/>
 - Usage: `s.throw <target> <item>`
 - Cooldown: `1 per 5.0 seconds`
# s.heal
Heal yourself.<br/>

Use a medkit if you own one, to increase your hp from anywhere near 1 to 40.<br/>
 - Usage: `s.heal`
 - Cooldown: `1 per 60.0 seconds`
# s.hitormiss
Hit or Miss<br/>
 - Usage: `s.hitormiss`
 - Aliases: `hom`
 - Cooldown: `2 per 5.0 seconds`
## s.hitormiss stats
See yours or others Hit Or Miss stats.<br/>
 - Usage: `s.hitormiss stats [user=None]`
 - Aliases: `profile`
## s.hitormiss leaderboard
Show the top players in the Hit Or Miss leaderboard.<br/>

There are 6 ways learderboards can be sorted:<br/>
- **Throws**: The leaderboard shows the top players who threw the most items.<br/>
- **Kills**: The amount of kills users have. (default)<br/>
- **Deaths**: The amount of times users have died.<br/>
- **Hits**: The amount of times users have hit others.<br/>
- **Misses**: The amount of times users have missed a throw.<br/>
- **KDR**: The K/D ratio of user's kills to their deaths.<br/>
- **All**: TO see all of the above at once. (This type won't be sorted and randomly placed.)<br/>

Pass any of the above exactly to the `type` parameter.<br/>

The leaderboard is `local` by default (only for the current server).<br/>
To show the global leaderboard, pass `true` to the `global_or_local` argument.<br/>
 - Usage: `s.hitormiss leaderboard [_type=kills] [global_or_local=False]`
 - Aliases: `lb and top`
## s.hitormiss inventory
See all the items that you currently own in Hit Or Miss.<br/>
 - Usage: `s.hitormiss inventory`
 - Aliases: `inv`
## s.hitormiss buy
Buy a Hit Or Miss item for your inventory.<br/>

`s.buy <item>` to buy 1 of the item.<br/>
`s.buy <amount> <item>` to buy a specific amount of the item.<br/>

where,<br/>
`<item>` is the name of the item you want to buy.<br/>
 - Usage: `s.hitormiss buy [amount=None] <item>`
 - Aliases: `purchase`
Extended Arg Info
> ### amount: Optional[int] = None
> ```
> A number without decimal places.
> ```
## s.hitormiss shop
See items available to buy for Hit Or Miss.<br/>

User `s.buy <item>` to buy an item.<br/>
 - Usage: `s.hitormiss shop`
 - Aliases: `items`
