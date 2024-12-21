# s.wouldyourather (Hybrid Command)
Would you rather?<br/>
 - Usage: `s.wouldyourather`
 - Slash Usage: `/wouldyourather`
 - Aliases: `wyr`
 - Cooldown: `1 per 3.0 seconds`
 - Checks: `server_only and is_restricted`
# s.neverhaveiever (Hybrid Command)
Never have I ever.<br/>
 - Usage: `s.neverhaveiever`
 - Slash Usage: `/neverhaveiever`
 - Aliases: `nhie`
 - Cooldown: `1 per 3.0 seconds`
 - Checks: `server_only and is_restricted`
# s.paranoia (Hybrid Command)
Paranoia questions.<br/>
 - Usage: `s.paranoia`
 - Slash Usage: `/paranoia`
 - Cooldown: `1 per 3.0 seconds`
 - Checks: `server_only and is_restricted`
# s.truth (Hybrid Command)
Truth questions, optionally ask truth questions to members!<br/>
 - Usage: `s.truth [member]`
 - Slash Usage: `/truth [member]`
 - Cooldown: `1 per 3.0 seconds`
 - Checks: `server_only and is_restricted`
Extended Arg Info
> ### member: Optional[discord.member.Member] = None
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
# s.dare (Hybrid Command)
Dare questions, optionally ask dare questions to members!<br/>
 - Usage: `s.dare [member]`
 - Slash Usage: `/dare [member]`
 - Cooldown: `1 per 3.0 seconds`
 - Checks: `server_only and is_restricted`
Extended Arg Info
> ### member: Optional[discord.member.Member] = None
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
# s.cgset
Configurating options for Conversation Games.<br/>
 - Usage: `s.cgset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.cgset rating
Set rating for the games.<br/>

Converting to R-Rating will disallow the commands from working in<br/>
non-nsfw channels.<br/>
 - Usage: `s.cgset rating <rating>`
