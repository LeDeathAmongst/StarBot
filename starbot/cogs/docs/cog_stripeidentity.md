# s.setverificationchannel
Set the channel where verification results will be sent.<br/>
 - Usage: `s.setverificationchannel <channel>`
 - Restricted to: `ADMIN`
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
# s.setageverifiedrole
Set the role to give to users who are verified as 18 or older.<br/>
 - Usage: `s.setageverifiedrole <role>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# s.setidverifiedrole
Set the role to give to users who have been completely ID verified.<br/>
 - Usage: `s.setidverifiedrole <role>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# s.cancelverification
Cancel a pending verification session for a user and remove it from the list of sessions.<br/>
 - Usage: `s.cancelverification <user>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
# s.agecheck
Perform an age check on a user using Stripe Identity.<br/>
 - Usage: `s.agecheck <user>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
# s.idcheck
Perform a biometric verification of a Discord user's real-life identity.<br/>
 - Usage: `s.idcheck <user>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
# s.pending
Show all pending verifications for users in the server.<br/>
 - Usage: `s.pending`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
# s.attest
Allows a user to self-attest their government issued ID for analysis<br/>
 - Usage: `s.attest`
 - Checks: `server_only`
