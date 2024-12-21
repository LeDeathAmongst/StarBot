# s.rep
Check a user's reputation in your server.<br/>

If no user is specified, the user who invoked the command will be used.<br/>
 - Usage: `s.rep [member=None]`
 - Aliases: `reputation`
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
## s.rep reset
Reset a user's reputation to 0.<br/>

If no user is specified, the user who invoked the command will be used.<br/>
 - Usage: `s.rep reset <members> <reason>`
 - Checks: `is_staff`
Extended Arg Info
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rep add
Add a certain amount of reputation to a user.<br/>
 - Usage: `s.rep add <amount> <members_or_voice> <reason>`
 - Checks: `is_staff`
Extended Arg Info
> ### amount: float
> ```
> A number with or without decimal places.
> ```
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rep remove
Remove a certain amount of reputation from a user.<br/>
 - Usage: `s.rep remove <amount> <members> <reason>`
 - Checks: `is_staff`
Extended Arg Info
> ### amount: float
> ```
> A number with or without decimal places.
> ```
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rep leaderboard
See a ranked list of users with the most/least reputation.<br/>

The amount if the number of users to show on the leaderboard. (defaults to 10)<br/>

If the reversed argument is not used, it defaults to True<br/>
which shows the leaderboard from highest to lowest.<br/>
Pass False/0 to show the leaderboard from lowest to highest instead.<br/>
 - Usage: `s.rep leaderboard [amount=None] [reversed=True]`
 - Aliases: `lb`
Extended Arg Info
> ### amount: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### reversed=True
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.repset
Set the settings for the reputation system.<br/>
 - Usage: `s.repset`
 - Restricted to: `ADMIN`
## s.repset logchannel
Set the log channel for the reputation system.<br/>

This channel will be used to log all reputation changes.<br/>
 - Usage: `s.repset logchannel <channel>`
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
## s.repset staffrole
Set the staff role for the reputation system.<br/>

This role will be able to use the reputation commands.<br/>
 - Usage: `s.repset staffrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.repset showsettings
Show the current settings for the reputation system.<br/>
 - Usage: `s.repset showsettings`
 - Aliases: `show and ss`
