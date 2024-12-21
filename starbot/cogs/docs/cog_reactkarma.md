# s.upvote
See this server's upvote emoji.<br/>
 - Usage: `s.upvote`
 - Checks: `server_only`
# s.downvote
See this server's downvote emoji.<br/>
 - Usage: `s.downvote`
 - Checks: `server_only`
# s.karmaboard
Prints out the karma leaderboard.<br/>

Defaults to top 10. Use negative numbers to reverse the leaderboard.<br/>
 - Usage: `s.karmaboard [top=10]`
Extended Arg Info
> ### top: int = 10
> ```
> A number without decimal places.
> ```
# s.karma
Check a user's karma.<br/>

Leave [user] blank to see your own karma.<br/>
 - Usage: `s.karma [user=None]`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member = None
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
# s.setupvote
Set the upvote emoji in this server.<br/>

Only the first reaction from the command author will be added.<br/>
 - Usage: `s.setupvote`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
# s.setdownvote
Add a downvote emoji by reacting to the bot's response.<br/>

Only the first reaction from the command author will be added.<br/>
 - Usage: `s.setdownvote`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
