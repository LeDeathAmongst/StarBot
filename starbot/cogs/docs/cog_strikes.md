# s.strike
Strike a user.<br/>
 - Usage: `s.strike <member> <reason>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.delstrike
Remove a single strike by its ID.<br/>
 - Usage: `s.delstrike <strike_id>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### strike_id: int
> ```
> A number without decimal places.
> ```
# s.delstrikes
Remove all strikes from a member.<br/>
 - Usage: `s.delstrikes <member>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
# s.strikes
Show all previous strikes for a user.<br/>
 - Usage: `s.strikes <member>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member
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
# s.allstrikes
Show all recent individual strikes.<br/>

`[num_days]` is the number of past days of strikes to display.<br/>
Defaults to 30. When 0, all strikes from the beginning of time<br/>
will be counted shown.<br/>
 - Usage: `s.allstrikes [num_days=30]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### num_days: int = 30
> ```
> A number without decimal places.
> ```
# s.strikecounts
Show the strike count for multiple users.<br/>

`[num_days]` is the number of past days of strikes to count.<br/>
Defaults to 0, which means all strikes from the beginning of<br/>
time will be counted.<br/>

`[limit]` is the maximum amount of members to show the<br/>
strike count for. Defaults to 100.<br/>

`[sort_by]` is the column to sort the table by. May be one of<br/>
either *count* or *date*. Defaults to *count*.<br/>

`[sort_order]` is the order to sort in. It may be one of either<br/>
*desc* for descending or *asc* for ascending. Defaults to<br/>
*desc*.<br/>
 - Usage: `s.strikecounts [num_days=0] [limit=100] [sort_by=count] [sort_order=desc]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### num_days: int = 0
> ```
> A number without decimal places.
> ```
> ### limit: int = 100
> ```
> A number without decimal places.
> ```
> ### sort_by: str = 'count'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### sort_order: str = 'desc'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
