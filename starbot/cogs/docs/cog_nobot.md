# s.nobot
Main setup command for NoBot<br/>
 - Usage: `s.nobot`
## s.nobot delfilter
Delete a filter<br/>
 - Usage: `s.nobot delfilter`
## s.nobot view
View NoBot settings<br/>
 - Usage: `s.nobot view`
## s.nobot delbot
Remove a bot from the filter list<br/>

If bot is no longer in the server, use its ID<br/>
 - Usage: `s.nobot delbot <bot>`
Extended Arg Info
> ### bot: Union[discord.member.Member, int]
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
## s.nobot addbot
Add a bot to the filter list<br/>
 - Usage: `s.nobot addbot <bot>`
Extended Arg Info
> ### bot: discord.member.Member
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
## s.nobot addfilter
Add text context to match against the bot filter list, use phrases that match what the bot sends exactly<br/>
 - Usage: `s.nobot addfilter <message>`
Extended Arg Info
> ### message
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
