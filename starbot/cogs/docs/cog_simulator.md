# s.simulator
Main simulator command. Use me!<br/>
 - Usage: `s.simulator`
 - Aliases: `sim`
## s.simulator count
Count instances of a word, globally or for a user<br/>
 - Usage: `s.simulator count <word> [user=None]`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### user: Optional[discord.member.Member] = None
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
## s.simulator info
How this works<br/>
 - Usage: `s.simulator info`
 - Aliases: `help`
## s.simulator stats
Statistics about the simulator, globally or for a user<br/>
 - Usage: `s.simulator stats [user=None]`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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
## s.simulator set
Set up your simulator.<br/>
 - Usage: `s.simulator set`
### s.simulator set showsettings
Show the current simulator settings<br/>
 - Usage: `s.simulator set showsettings`
# s.dontsimulateme
Excludes you from your messages being read and analyzed by the simulator.<br/>
 - Usage: `s.dontsimulateme`
