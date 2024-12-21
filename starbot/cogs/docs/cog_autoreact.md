# s.autoreact
Reacts to specific text with an emoji.<br/>
 - Usage: `s.autoreact`
 - Checks: `server_only`
## s.autoreact add
Add a new autoreact using regex. Tip: (?i) in a regex makes it case-insensitive.<br/>
 - Usage: `s.autoreact add <emoji> <pattern>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
> ### pattern: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.autoreact list
Shows all autoreacts.<br/>
 - Usage: `s.autoreact list`
## s.autoreact remove
Remove an existing autoreact for an emoji.<br/>
 - Usage: `s.autoreact remove <emoji>`
Extended Arg Info
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
# s.coreact
Copies other people's reactions to recent messages.<br/>
 - Usage: `s.coreact`
## s.coreact chance
The percent chance that the bot will add its own reaction when anyone else reacts.<br/>
 - Usage: `s.coreact chance <chance>`
Extended Arg Info
> ### chance: Optional[float]
> ```
> A number with or without decimal places.
> ```
