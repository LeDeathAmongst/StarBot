# s.pets
Manage your pet.<br/>
 - Usage: `s.pets`
 - Restricted to: `MOD`
 - Aliases: `pupper`
 - Checks: `server_only`
## s.pets toggle
Toggle pets on the server.<br/>
 - Usage: `s.pets toggle`
## s.pets credits
Set the pet credits range on successful petting.<br/>
 - Usage: `s.pets credits <min_amt> <max_amt>`
Extended Arg Info
> ### min_amt: int
> ```
> A number without decimal places.
> ```
> ### max_amt: int
> ```
> A number without decimal places.
> ```
## s.pets delete
Set how long to wait before deleting the thanks message.<br/>
To leave the thanks message with no deletion, use 0 as the amount.<br/>
10 is the default.<br/>
Max is 5 minutes (300).<br/>
 - Usage: `s.pets delete [amount=0]`
Extended Arg Info
> ### amount: int = 0
> ```
> A number without decimal places.
> ```
## s.pets cooldown
Set the pet appearance cooldown in seconds.<br/>

300s/5 minute minimum. Default is 3600s/1 hour.<br/>
 - Usage: `s.pets cooldown [seconds=None]`
Extended Arg Info
> ### seconds: int = None
> ```
> A number without decimal places.
> ```
## s.pets channel
Channel management for pet appearance.<br/>
 - Usage: `s.pets channel`
 - Restricted to: `MOD`
 - Checks: `server_only`
### s.pets channel removeall
Remove all petting channels from the list.<br/>
 - Usage: `s.pets channel removeall`
### s.pets channel add
Add a text channel for pets.<br/>
 - Usage: `s.pets channel add <channel>`
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
### s.pets channel remove
Remove a text channel from petting.<br/>
 - Usage: `s.pets channel remove <channel>`
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
### s.pets channel addall
Add all valid channels for the server that the bot can speak in.<br/>
 - Usage: `s.pets channel addall`
## s.pets hello
Set the pet greeting message.<br/>
 - Usage: `s.pets hello [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.pets thanks
Set the pet thanks message.<br/>
 - Usage: `s.pets thanks [message]`
Extended Arg Info
> ### message: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
