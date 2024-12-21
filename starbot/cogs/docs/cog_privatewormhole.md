# s.privatewormhole
Manage private wormhole connections.<br/>
 - Usage: `s.privatewormhole`
## s.privatewormhole unglobalblacklist
Command to remove a user from the global private wormhole blacklist (Bot Owner Only).<br/>
 - Usage: `s.privatewormhole unglobalblacklist <user>`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## s.privatewormhole removewordfilter
Remove a word from the private wormhole word filter.<br/>
 - Usage: `s.privatewormhole removewordfilter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.privatewormhole globalblacklist
Prevent specific members from sending messages through the private wormhole globally.<br/>
 - Usage: `s.privatewormhole globalblacklist <user>`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## s.privatewormhole addwordfilter
Add a word to the private wormhole word filter.<br/>
 - Usage: `s.privatewormhole addwordfilter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.privatewormhole leave
Leave a private wormhole.<br/>
 - Usage: `s.privatewormhole leave <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.privatewormhole create
Create a private wormhole with a name and password.<br/>
 - Usage: `s.privatewormhole create <name> <password>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### password: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.privatewormhole join
Join an existing private wormhole with the correct name and password.<br/>
 - Usage: `s.privatewormhole join <name> <password>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### password: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
