# s.uptime
Get my uptime data<br/>
 - Usage: `s.uptime`
## /uptime data (Slash Command)
Get my uptime data in an embed<br/>
 - Usage: `/uptime data [days]`
 - `days:` (Optional) Days of data to show, use 0 for all-time data. Default: 30

Extended Arg Info
> ### days: int
> - Autocomplete: False
> - Default: 30
> 
> Days of data to show, use 0 for all-time data. Default: 30
> 
> ```
> A number without decimal places.
> ```
## /uptime graph (Slash Command)
Get my uptime graph in an embed<br/>
 - Usage: `/uptime graph [days]`
 - `days:` (Optional) Days of data to show, use 0 for all-time data. Default: 30

Extended Arg Info
> ### days: int
> - Autocomplete: False
> - Default: 30
> 
> Days of data to show, use 0 for all-time data. Default: 30
> 
> ```
> A number without decimal places.
> ```
## /uptime downtime (Slash Command)
Get my downtime data in an embed<br/>
 - Usage: `/uptime downtime [days]`
 - `days:` (Optional) Days of data to show, use 0 for all-time data. Default: 30

Extended Arg Info
> ### days: int
> - Autocomplete: False
> - Default: 30
> 
> Days of data to show, use 0 for all-time data. Default: 30
> 
> ```
> A number without decimal places.
> ```
# s.uptime
Get Starfire's uptime percent over the last 30 days, and when I was last restarted.<br/>

The default value for `num_days` is `30`. You can put `0` days for all-time data.<br/>
Otherwise, it needs to be `5` or more.<br/>

Note: embeds must be enabled for this rich data to show<br/>

**Examples:**<br/>
- `s.uptime`<br/>
- `s.uptime 0` (for all-time data)<br/>
- `s.uptime 7`<br/>
 - Usage: `s.uptime [num_days=30]`
Extended Arg Info
> ### num_days: int = 30
> ```
> A number without decimal places.
> ```
# s.downtime
Check Starfire downtime over the last 30 days.<br/>

The default value for `num_days` is `30`. You can put `0` days for all-time data.<br/>
Otherwise, it needs to be `5` or more.<br/>

**Examples:**<br/>
- `s.uptime`<br/>
- `s.uptime 0` (for all-time data)<br/>
- `s.uptime 7`<br/>
 - Usage: `s.downtime [num_days=30]`
Extended Arg Info
> ### num_days: int = 30
> ```
> A number without decimal places.
> ```
# s.uptimegraph
Check Starfire uptime with a graph over the last 30 days.<br/>

The default value for `num_days` is `30`. You can put `0` days for all-time data.<br/>
Otherwise, it needs to be `5` or more.<br/>

**Examples:**<br/>
- `s.uptime` - for the default of 30 days<br/>
- `s.uptime 0` - for all-time data<br/>
-]uptime 7` - 7 days<br/>
 - Usage: `s.uptimegraph [num_days=30]`
Extended Arg Info
> ### num_days: int = 30
> ```
> A number without decimal places.
> ```
