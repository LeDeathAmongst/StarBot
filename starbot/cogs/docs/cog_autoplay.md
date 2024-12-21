# s.autoplay (Hybrid Command)
Toggle autoplay for a member.<br/>

This will cause the bot to automatically play music that<br/>
the member is listening to on Spotify.<br/>

To stop it, use `s.autoplay` without a member, or<br/>
use a player command like `s.stop` or `s.play`.<br/>
 - Usage: `s.autoplay [member=None]`
 - Slash Usage: `/autoplay [member=None]`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member = None
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
