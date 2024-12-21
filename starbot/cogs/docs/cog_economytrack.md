# s.economytrack
Configure EconomyTrack<br/>
 - Usage: `s.economytrack`
 - Aliases: `ecotrack`
 - Checks: `server_only`
## s.economytrack togglemembertrack
Enable/Disable member tracking for this server<br/>
 - Usage: `s.economytrack togglemembertrack`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.economytrack view
View EconomyTrack Settings<br/>
 - Usage: `s.economytrack view`
## s.economytrack togglebanktrack
Enable/Disable economy tracking for this server<br/>
 - Usage: `s.economytrack togglebanktrack`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.economytrack timezone
Set your desired timezone for the graph<br/>

**Arguments**<br/>
`<timezone>` A string representing a valid timezone<br/>

**Example:** `s.ecotrack timezone US/Eastern`<br/>

Use this command without the argument to get a huge list of valid timezones.<br/>
 - Usage: `s.economytrack timezone <timezone>`
Extended Arg Info
> ### timezone: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.remoutliers
Cleanup data above a certain total economy balance<br/>

**Arguments**<br/>
datatype: either `bank` or `member`<br/>
 - Usage: `s.remoutliers <max_value> [datatype=bank]`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### max_value: int
> ```
> A number without decimal places.
> ```
> ### datatype: str = 'bank'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.bankgraph
View bank status over a period of time.<br/>
**Arguments**<br/>
`<timespan>` How long to look for, or `all` for all-time data. Defaults to 1 day.<br/>
Must be at least 1 hour.<br/>
**Examples:**<br/>
    - `s.bankgraph 3w2d`<br/>
    - `s.bankgraph 5d`<br/>
    - `s.bankgraph all`<br/>
 - Usage: `s.bankgraph [timespan=1d]`
 - Aliases: `bgraph`
 - Cooldown: `5 per 60.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### timespan: str = '1d'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.membergraph
View member count over a period of time.<br/>
**Arguments**<br/>
`<timespan>` How long to look for, or `all` for all-time data. Defaults to 1 day.<br/>
Must be at least 1 hour.<br/>
**Examples:**<br/>
    - `s.membergraph 3w2d`<br/>
    - `s.membergraph 5d`<br/>
    - `s.membergraph all`<br/>
 - Usage: `s.membergraph [timespan=1d]`
 - Aliases: `memgraph`
 - Cooldown: `5 per 60.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### timespan: str = '1d'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
