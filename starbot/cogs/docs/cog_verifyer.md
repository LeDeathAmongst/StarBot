# s.verify

 - Usage: `s.verify <member>`
 - Checks: `server_only`
Extended Arg Info
> ### member: Optional[discord.member.Member]
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
# s.verifyerset
Settings for verifyer<br/>
 - Usage: `s.verifyerset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.verifyerset memberrole
Set the role to assign to a user when they verify themselves.<br/>

Leave empty to disable this feature.<br/>
 - Usage: `s.verifyerset memberrole <role>`
 - Checks: `server_only`
Extended Arg Info
> ### role: Optional[discord.role.Role]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.verifyerset role
Set the role to assign to a user on server join.<br/>

Leave empty to disable this feature.<br/>
 - Usage: `s.verifyerset role <role>`
 - Checks: `server_only`
Extended Arg Info
> ### role: Optional[discord.role.Role]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.verifyerset disable
Disable verifyer.<br/>
This is per server.<br/>
 - Usage: `s.verifyerset disable`
 - Checks: `server_only`
## s.verifyerset message
Specify what message should be DMed to a user when they join the server.<br/>

Leave empty to disable this feature.<br/>
 - Usage: `s.verifyerset message <text>`
 - Checks: `server_only`
Extended Arg Info
> ### text: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.verifyerset enable
Enable verifyer.<br/>
This is per server.<br/>
 - Usage: `s.verifyerset enable`
 - Checks: `server_only`
## s.verifyerset verifiedmessage
Specify what message should be DMed to a user when they verify themselves.<br/>

Leave empty to disable this feature.<br/>
 - Usage: `s.verifyerset verifiedmessage <text>`
 - Checks: `server_only`
Extended Arg Info
> ### text: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
