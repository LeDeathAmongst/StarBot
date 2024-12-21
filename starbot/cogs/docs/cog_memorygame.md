# s.memorygame (Hybrid Command)
Play to Memory game. Choose between `3x3`, `4x4` and `5x5` versions.<br/>
 - Usage: `s.memorygame [difficulty=5x5]`
 - Slash Usage: `/memorygame [difficulty=5x5]`
# s.memorygameleaderboard (Hybrid Command)
Show MemoryGame leaderboard.<br/>
 - Usage: `s.memorygameleaderboard`
 - Slash Usage: `/memorygameleaderboard`
 - Aliases: `memorygamelb`
# s.setmemorygame (Hybrid Command)
Group of commands to set MemoryGame.<br/>
 - Usage: `s.setmemorygame`
 - Slash Usage: `/setmemorygame`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setmemorygame resetleaderboard (Hybrid Command)
Reset leaderboard in the server.<br/>
 - Usage: `s.setmemorygame resetleaderboard`
 - Slash Usage: `/setmemorygame resetleaderboard`
 - Checks: `server_only`
## s.setmemorygame maxprize (Hybrid Command)
Set the max prize for Red bank system and cog leaderboard. Default is 5000.<br/>

Default value: `5000`<br/>
Dev: `Range[int, 1000, 50000]`<br/>
 - Usage: `s.setmemorygame maxprize <value>`
 - Slash Usage: `/setmemorygame maxprize <value>`
 - Checks: `server_only`
## s.setmemorygame redeconomy (Hybrid Command)
If this option is enabled, the cog will give credits to the user each time the game is won.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setmemorygame redeconomy <value>`
 - Slash Usage: `/setmemorygame redeconomy <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setmemorygame reductionpersecond (Hybrid Command)
Set the reduction per second of prize for Red bank system and cog leaderboard. Default is 5.<br/>

Default value: `5`<br/>
Dev: `Range[int, 0, 30]`<br/>
 - Usage: `s.setmemorygame reductionpersecond <value>`
 - Slash Usage: `/setmemorygame reductionpersecond <value>`
 - Checks: `server_only`
## s.setmemorygame showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setmemorygame showsettings [with_dev=False]`
 - Slash Usage: `/setmemorygame showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setmemorygame resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.setmemorygame resetsetting <setting>`
 - Slash Usage: `/setmemorygame resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setmemorygame reductionperwrongmatch (Hybrid Command)
Set the reduction per wrong match of prize for Red bank system and cog leaderboard. Default is 15.<br/>

Default value: `15`<br/>
Dev: `Range[int, 0, 30]`<br/>
 - Usage: `s.setmemorygame reductionperwrongmatch <value>`
 - Slash Usage: `/setmemorygame reductionperwrongmatch <value>`
 - Checks: `server_only`
## s.setmemorygame modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.setmemorygame modalconfig [confirmation=False]`
 - Slash Usage: `/setmemorygame modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setmemorygame maxwrongmatches (Hybrid Command)
Set the maximum tries for each game. Use `0` for no limit.<br/>

Default value: `None`<br/>
Dev: `Range[int, 0, 50]`<br/>
 - Usage: `s.setmemorygame maxwrongmatches <value>`
 - Slash Usage: `/setmemorygame maxwrongmatches <value>`
 - Checks: `server_only`
