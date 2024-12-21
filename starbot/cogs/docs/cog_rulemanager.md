# s.addrule
Add a rule to the server's rule list.<br/>
 - Usage: `s.addrule <rule_text>`
 - Checks: `server_only`
Extended Arg Info
> ### rule_text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.resetrules
Reset all rules for the server.<br/>
 - Usage: `s.resetrules`
 - Checks: `server_only`
# s.removerule
Remove a rule by its ID.<br/>
 - Usage: `s.removerule <rule_id>`
 - Checks: `server_only`
Extended Arg Info
> ### rule_id: int
> ```
> A number without decimal places.
> ```
# s.editrule
Edit a rule by its ID.<br/>
 - Usage: `s.editrule <rule_id> <new_text>`
 - Checks: `server_only`
Extended Arg Info
> ### rule_id: int
> ```
> A number without decimal places.
> ```
> ### new_text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.showrules
Show all rules for the server.<br/>
 - Usage: `s.showrules`
 - Checks: `server_only`
# s.postrules
Post the rules to a specific channel and set it for dynamic updates.<br/>
 - Usage: `s.postrules <channel>`
 - Checks: `server_only`
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
