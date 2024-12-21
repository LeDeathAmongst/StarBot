# s.uttt
Play a game of ultimate tic tac toe.<br/>

You may only play in the sub board that corresponds to the last<br/>
spot your opponent played. If you are sent to a sub board that<br/>
has been finished, you can choose any sub board. First to win<br/>
three sub boards in a row wins.<br/>
 - Usage: `s.uttt [opponent=None]`
 - Checks: `server_only`
Extended Arg Info
> ### opponent: discord.member.Member = None
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
# s.utttstop
Stop the game of ultimate tic tac toe in this channel.<br/>
 - Usage: `s.utttstop`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
