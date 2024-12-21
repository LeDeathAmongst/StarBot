# s.adwarn (Hybrid Command)
Warn a user and send an embed to the default warning channel.<br/>
 - Usage: `s.adwarn <user> <reason>`
 - Slash Usage: `/adwarn <user> <reason>`
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
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.removewarn
Remove a specific warning from a user by its UUID.<br/>
 - Usage: `s.removewarn <user> <warning_id>`
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
> ### warning_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.warncount (Hybrid Command)
Get the total number of warnings a user has.<br/>
 - Usage: `s.warncount <user>`
 - Slash Usage: `/warncount <user>`
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
# s.clearwarns (Hybrid Command)
Clear all warnings for a user.<br/>
 - Usage: `s.clearwarns <user>`
 - Slash Usage: `/clearwarns <user>`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
# s.unadwarn (Hybrid Command)
Clear the most recent warning for a user.<br/>
 - Usage: `s.unadwarn <user>`
 - Slash Usage: `/unadwarn <user>`
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
# s.editaw
Edit a specific warning by its UUID.<br/>
 - Usage: `s.editaw <user> <warning_id> <new_reason>`
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
> ### warning_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### new_reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.topwarners
Show the top 5 users who have issued the most warnings in the current server.<br/>
 - Usage: `s.topwarners`
# s.modwarns
Show the number of warnings issued by a moderator and who they have warned in the current server.<br/>
 - Usage: `s.modwarns <moderator>`
Extended Arg Info
> ### moderator: discord.member.Member
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
# s.adboard
Show all users who have issued warnings and how many they have issued.<br/>
 - Usage: `s.adboard`
# s.warnset
Settings for the warning system.<br/>
 - Usage: `s.warnset`
 - Checks: `server_only`
## s.warnset timeoutduration
Set the duration (in minutes) for timeouts.<br/>
 - Usage: `s.warnset timeoutduration <minutes>`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```
## s.warnset show
Show the current warning channel and thresholds.<br/>
 - Usage: `s.warnset show`
## s.warnset threshold
Set an action for a specific warning count threshold.<br/>
 - Usage: `s.warnset threshold <warning_count> <action>`
Extended Arg Info
> ### warning_count: int
> ```
> A number without decimal places.
> ```
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.warnset delthreshold
Delete a specific warning count threshold by its UUID.<br/>
 - Usage: `s.warnset delthreshold <threshold_id>`
Extended Arg Info
> ### threshold_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.warnset channel
Set the default channel for warnings.<br/>
 - Usage: `s.warnset channel <channel>`
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
## s.warnset softbanduration
Set the duration (in days) for message deletion during a softban.<br/>
 - Usage: `s.warnset softbanduration <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
# s.adrace
Start an adwarn race that lasts for a configurable amount of time.<br/>
 - Usage: `s.adrace <duration>`
Extended Arg Info
> ### duration: int
> ```
> A number without decimal places.
> ```
