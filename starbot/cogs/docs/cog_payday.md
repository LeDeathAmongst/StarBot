# s.freecredits
More options to get free credits<br/>
 - Usage: `s.freecredits`
 - Checks: `server_only_check`
## s.freecredits times
Display remaining time for all options<br/>
 - Usage: `s.freecredits times`
 - Checks: `cmd_all`
## s.freecredits monthly
Get some free currency every month (30 days)<br/>
 - Usage: `s.freecredits monthly`
 - Checks: `cmd_check`
## s.freecredits yearly
Get some free currency every year (365 days)<br/>
 - Usage: `s.freecredits yearly`
 - Checks: `cmd_check`
## s.freecredits hourly
Get some free currency every hour<br/>
 - Usage: `s.freecredits hourly`
 - Checks: `cmd_check`
## s.freecredits all
Claim all available freecredits<br/>
 - Usage: `s.freecredits all`
 - Checks: `cmd_all`
## s.freecredits quarterly
Get some free currency every quarter (122 days)<br/>
 - Usage: `s.freecredits quarterly`
 - Checks: `cmd_check`
## s.freecredits weekly
Get some free currency every week (7 days)<br/>
 - Usage: `s.freecredits weekly`
 - Checks: `cmd_check`
## s.freecredits daily
Get some free currency every day<br/>
 - Usage: `s.freecredits daily`
 - Checks: `cmd_check`
# s.pdconfig
Configure the `freecredits` options<br/>

More detailed docs: <https://cogs.yamikaitou.dev/payday.html#pdconfig><br/>
 - Usage: `s.pdconfig`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
## s.pdconfig daily
Configure the `daily` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `s.pdconfig daily <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `day`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.pdconfig quarterly
Configure the `quarterly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `s.pdconfig quarterly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `quarter`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.pdconfig yearly
Configure the `yearly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `s.pdconfig yearly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `year`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.pdconfig hourly
Configure the `hourly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `s.pdconfig hourly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `hour`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.pdconfig monthly
Configure the `monthly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `s.pdconfig monthly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `month`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.pdconfig settings
Print the `freecredits` options<br/>
 - Usage: `s.pdconfig settings`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
## s.pdconfig weekly
Configure the `weekly` options<br/>

Setting this to 0 will disable the command<br/>
 - Usage: `s.pdconfig weekly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `week`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.pdconfig streaks
Configure the `streaks` options<br/>
 - Usage: `s.pdconfig streaks`
 - Restricted to: `GUILD_OWNER`
 - Checks: `is_owner_if_bank_global`
### s.pdconfig streaks weekly
Configure the `weekly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `s.pdconfig streaks weekly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `week`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
### s.pdconfig streaks percent
Configure streaks to be a percentage or flat amount<br/>

<state> should be any of these combinations, `on/off`, `yes/no`, `1/0`, `true/false`<br/>
 - Usage: `s.pdconfig streaks percent <state>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `percentage`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### state: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.pdconfig streaks daily
Configure the `daily` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `s.pdconfig streaks daily <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `day`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
### s.pdconfig streaks hourly
Configure the `hourly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `s.pdconfig streaks hourly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `hour`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
### s.pdconfig streaks yearly
Configure the `yearly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `s.pdconfig streaks yearly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `year`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
### s.pdconfig streaks quarterly
Configure the `quarterly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `s.pdconfig streaks quarterly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `quarter`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
### s.pdconfig streaks monthly
Configure the `monthly` streaks value<br/>

Setting this to 0 will disable the streak bonus<br/>
 - Usage: `s.pdconfig streaks monthly <value>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `month`
 - Checks: `is_owner_if_bank_global`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
