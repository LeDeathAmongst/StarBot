# s.rolloutgame (Hybrid Command)
Play a match of Rollout game.<br/>
 - Usage: `s.rolloutgame`
 - Slash Usage: `/rolloutgame`
 - Aliases: `rollout`
 - Checks: `server_only`
# s.rolloutgameleaderboard (Hybrid Command)
Show RollOutGame leaderboard.<br/>
 - Usage: `s.rolloutgameleaderboard`
 - Slash Usage: `/rolloutgameleaderboard`
 - Aliases: `rolloutlb`
# s.setrolloutgame (Hybrid Command)
Group of commands to set RollOutGame.<br/>
 - Usage: `s.setrolloutgame`
 - Slash Usage: `/setrolloutgame`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setrolloutgame showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setrolloutgame showsettings [with_dev=False]`
 - Slash Usage: `/setrolloutgame showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setrolloutgame resetleaderboard (Hybrid Command)
Reset leaderboard in the server.<br/>
 - Usage: `s.setrolloutgame resetleaderboard`
 - Slash Usage: `/setrolloutgame resetleaderboard`
 - Checks: `server_only`
## s.setrolloutgame modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.setrolloutgame modalconfig [confirmation=False]`
 - Slash Usage: `/setrolloutgame modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setrolloutgame prize (Hybrid Command)
Set the prize for Red bank system and cog leaderboard. Default is 5000.<br/>

Default value: `2500`<br/>
Dev: `Range[int, 1000, 50000]`<br/>
 - Usage: `s.setrolloutgame prize <value>`
 - Slash Usage: `/setrolloutgame prize <value>`
 - Checks: `server_only`
## s.setrolloutgame resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.setrolloutgame resetsetting <setting>`
 - Slash Usage: `/setrolloutgame resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setrolloutgame redeconomy (Hybrid Command)
If this option is enabled, the cog will give credits to the user each time the game is won.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setrolloutgame redeconomy <value>`
 - Slash Usage: `/setrolloutgame redeconomy <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
