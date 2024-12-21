# s.fastclickgame (Hybrid Command)
Play to click on the right button as fast as you can!<br/>
 - Usage: `s.fastclickgame`
 - Slash Usage: `/fastclickgame`
 - Aliases: `fastclick and fcg`
 - Checks: `server_only`
## s.fastclickgame leaderboard (Hybrid Command)
Show Fast Click Game leaderboard.<br/>
 - Usage: `s.fastclickgame leaderboard`
 - Slash Usage: `/fastclickgame leaderboard`
 - Aliases: `lb`
 - Checks: `server_only`
## s.fastclickgame duel (Hybrid Command)
Play Fast Click Game with another player.<br/>
 - Usage: `s.fastclickgame duel <player>`
 - Slash Usage: `/fastclickgame duel <player>`
 - Aliases: `single`
 - Checks: `server_only`
Extended Arg Info
> ### player: discord.member.Member
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
## s.fastclickgame multi (Hybrid Command)
Play Fast Click Game with multiple rounds.<br/>
 - Usage: `s.fastclickgame multi [rounds=3] [buttons=25]`
 - Slash Usage: `/fastclickgame multi [rounds=3] [buttons=25]`
 - Checks: `server_only`
# s.setfastclickgame (Hybrid Command)
Group of commands to set FastClickGame.<br/>
 - Usage: `s.setfastclickgame`
 - Slash Usage: `/setfastclickgame`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setfastclickgame resetleaderboard (Hybrid Command)
Reset leaderboard in the server.<br/>
 - Usage: `s.setfastclickgame resetleaderboard`
 - Slash Usage: `/setfastclickgame resetleaderboard`
 - Checks: `server_only`
## s.setfastclickgame prize (Hybrid Command)
Set the prize for Red bank system and cog leaderboard. Default is 5000.<br/>

Default value: `2500`<br/>
Dev: `Range[int, 1000, 50000]`<br/>
 - Usage: `s.setfastclickgame prize <value>`
 - Slash Usage: `/setfastclickgame prize <value>`
 - Checks: `server_only`
## s.setfastclickgame redeconomy (Hybrid Command)
If this option is enabled, the cog will give credits to the user each time the game is won.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setfastclickgame redeconomy <value>`
 - Slash Usage: `/setfastclickgame redeconomy <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setfastclickgame modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.setfastclickgame modalconfig [confirmation=False]`
 - Slash Usage: `/setfastclickgame modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setfastclickgame resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.setfastclickgame resetsetting <setting>`
 - Slash Usage: `/setfastclickgame resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setfastclickgame showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setfastclickgame showsettings [with_dev=False]`
 - Slash Usage: `/setfastclickgame showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
