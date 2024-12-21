# s.raffle
Raffle group command<br/>
 - Usage: `s.raffle`
 - Checks: `server_only`
## s.raffle version
Displays the currently installed version of raffle.<br/>
 - Usage: `s.raffle version`
## s.raffle cancel
Cancels an on-going raffle. No winner is chosen.<br/>
 - Usage: `s.raffle cancel [message_id=None]`
Extended Arg Info
> ### message_id: int = None
> ```
> A number without decimal places.
> ```
## s.raffle start
Starts a raffle.<br/>

Timer accepts a integer input that represents seconds or it will<br/>
take the format of HH:MM:SS.<br/>

Example timer inputs:<br/>
`80`       = 1 minute and 20 seconds or 80 seconds<br/>
`30:10`    = 30 minutes and 10 seconds<br/>
`24:00:00` = 1 day or 24 hours<br/>

Title should not be longer than 35 characters.<br/>
 - Usage: `s.raffle start <timer> <title>`
Extended Arg Info
> ### timer
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.raffle end
Ends a raffle early. A winner will still be chosen.<br/>
 - Usage: `s.raffle end [message_id=None]`
Extended Arg Info
> ### message_id: int = None
> ```
> A number without decimal places.
> ```
## s.raffle reroll
Reroll the winner for a raffle. Requires the channel and message id.<br/>
 - Usage: `s.raffle reroll <channel> <messageid>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### messageid: int
> ```
> A number without decimal places.
> ```
# s.setraffle
Set Raffle group command<br/>
 - Usage: `s.setraffle`
 - Checks: `server_only`
## s.setraffle channel
Set the output channel for raffles.<br/>
 - Usage: `s.setraffle channel [channel=None]`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
