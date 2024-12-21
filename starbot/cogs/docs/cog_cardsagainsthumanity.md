# s.cah (Hybrid Command)
Cards Against Humanity®️ commands<br/>

Cards Against Humanity®️ is licened under Creative Commons BY-NC-SA 4.0<br/>
https://creativecommons.org/licenses/by-nc-sa/4.0/<br/>
 - Usage: `s.cah`
 - Slash Usage: `/cah`
## s.cah list (Hybrid Command)
List all the available set names.<br/>
 - Usage: `s.cah list`
 - Slash Usage: `/cah list`
## s.cah start (Hybrid Command)
Start a game of Cards Against Humanity®️<br/>

`[rounds=10]` The number of rounds you wish to play.<br/>
`[card_set]` The name of the card set(s) you want to use.<br/>
By default all official cards are used but you can customize this<br/>
by `|` separating card sets.<br/>
e.g. `s.cah start 10 CAH Base Set|2012 Holiday Pack`<br/>
 - Usage: `s.cah start [rounds=10] <card_set>`
 - Slash Usage: `/cah start [rounds=10] <card_set>`
 - Checks: `server_only`
Extended Arg Info
> ### rounds: Optional[int] = 10
> ```
> A number without decimal places.
> ```
