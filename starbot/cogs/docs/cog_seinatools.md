# s.spotify
View the specified (defaults to author) user's now playing spotify status from their discord activity.<br/>
 - Usage: `s.spotify [user=None]`
 - Checks: `server_only`
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
## s.spotify emoji
Set an emoji to be used with the spotify command.<br/>
 - Usage: `s.spotify emoji <emoji>`
# s.whatplaying
Closer lookup on what the specified user is playing.<br/>
 - Usage: `s.whatplaying [user=None]`
 - Aliases: `whatgame`
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
# s.crates
Get information about a package in Crates.io.<br/>
 - Usage: `s.crates <package_name>`
 - Aliases: `cargo, rustpkg, and crate`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.npm
Get information about a node.js module.<br/>
 - Usage: `s.npm <module_name>`
 - Aliases: `node, npmpkg, and nodepkg`
Extended Arg Info
> ### module_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.ruby
Get information about a rubygem package.<br/>
 - Usage: `s.ruby <package_name>`
 - Aliases: `rubygem, rubypkg, and rubygems`
Extended Arg Info
> ### package_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
