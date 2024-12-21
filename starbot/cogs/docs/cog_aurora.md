# /note (Slash Command)
Add a note to a user.<br/>
 - Usage: `/note <target> <reason> [silent]`
 - `target:` (Required) Who are you noting?
 - `reason:` (Required) Why are you noting this user?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you noting?
> 
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
> - Autocomplete: False
> 
> Why are you noting this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /warn (Slash Command)
Warn a user.<br/>
 - Usage: `/warn <target> <reason> [silent]`
 - `target:` (Required) Who are you warning?
 - `reason:` (Required) Why are you warning this user?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you warning?
> 
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
> - Autocomplete: False
> 
> Why are you warning this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /addrole (Slash Command)
Add a role to a user.<br/>
 - Usage: `/addrole <target> <role> <reason> [duration] [silent]`
 - `target:` (Required) Who are you adding a role to?
 - `role:` (Required) What role are you adding to the target?
 - `reason:` (Required) Why are you adding a role to this user?
 - `duration:` (Optional) How long are you adding this role for?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you adding a role to?
> 
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
> ### role: discord.role.Role
> - Autocomplete: False
> 
> What role are you adding to the target?
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### reason: str
> - Autocomplete: False
> 
> Why are you adding a role to this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### duration: str
> - Autocomplete: False
> - Default: None
> 
> How long are you adding this role for?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /removerole (Slash Command)
Remove a role from a user.<br/>
 - Usage: `/removerole <target> <role> <reason> [duration] [silent]`
 - `target:` (Required) Who are you removing a role from?
 - `role:` (Required) What role are you removing from the target?
 - `reason:` (Required) Why are you removing a role from this user?
 - `duration:` (Optional) How long are you removing this role for?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you removing a role from?
> 
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
> ### role: discord.role.Role
> - Autocomplete: False
> 
> What role are you removing from the target?
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### reason: str
> - Autocomplete: False
> 
> Why are you removing a role from this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### duration: str
> - Autocomplete: False
> - Default: None
> 
> How long are you removing this role for?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /mute (Slash Command)
Mute a user.<br/>
 - Usage: `/mute <target> <duration> <reason> [silent]`
 - `target:` (Required) Who are you unbanning?
 - `duration:` (Required) How long are you muting this user for?
 - `reason:` (Required) Why are you unbanning this user?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you unbanning?
> 
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
> ### duration: str
> - Autocomplete: False
> 
> How long are you muting this user for?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reason: str
> - Autocomplete: False
> 
> Why are you unbanning this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /unmute (Slash Command)
Unmute a user.<br/>
 - Usage: `/unmute <target> [reason] [silent]`
 - `target:` (Required) Who are you unmuting?
 - `reason:` (Optional) Why are you unmuting this user?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you unmuting?
> 
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
> - Autocomplete: False
> - Default: None
> 
> Why are you unmuting this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /kick (Slash Command)
Kick a user.<br/>
 - Usage: `/kick <target> <reason> [silent]`
 - `target:` (Required) Who are you kicking?
 - `reason:` (Required) Why are you kicking this user?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you kicking?
> 
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
> - Autocomplete: False
> 
> Why are you kicking this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /ban (Slash Command)
Ban a user.<br/>
 - Usage: `/ban <target> <reason> [duration] [delete_messages] [silent]`
 - `target:` (Required) Who are you banning?
 - `reason:` (Required) Why are you banning this user?
 - `duration:` (Optional) How long are you banning this user for?
 - `delete_messages:` (Optional) How many days of messages to delete?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you banning?
> 
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
> - Autocomplete: False
> 
> Why are you banning this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### duration: str
> - Autocomplete: False
> - Default: None
> 
> How long are you banning this user for?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### delete_messages: int
> - Autocomplete: False
> - Default: None
> - Choices: ['None', '1 Hour', '12 Hours', '1 Day', '3 Days', '7 Days']
> 
> How many days of messages to delete?
> 
> ```
> A number without decimal places.
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /unban (Slash Command)
Unban a user.<br/>
 - Usage: `/unban <target> [reason] [silent]`
 - `target:` (Required) Who are you unbanning?
 - `reason:` (Optional) Why are you unbanning this user?
 - `silent:` (Optional) Should the user be messaged?

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> 
> Who are you unbanning?
> 
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
> - Autocomplete: False
> - Default: None
> 
> Why are you unbanning this user?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### silent: bool
> - Autocomplete: False
> - Default: None
> 
> Should the user be messaged?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /history (Slash Command)
List previous infractions.<br/>
 - Usage: `/history [target] [moderator] [pagesize] [page] [ephemeral] [inline] [export]`
 - `target:` (Optional) User whose infractions to query, overrides moderator if both are given
 - `moderator:` (Optional) Query by moderator
 - `pagesize:` (Optional) Amount of infractions to list per page
 - `page:` (Optional) Page to select
 - `ephemeral:` (Optional) Hide the command response
 - `inline:` (Optional) Display infractions in a grid arrangement (does not look very good)
 - `export:` (Optional) Exports the server's entire moderation history to a JSON file

Extended Arg Info
> ### target: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> User whose infractions to query, overrides moderator if both are given
> 
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
> ### moderator: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> Query by moderator
> 
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
> ### pagesize: int
> - Autocomplete: False
> - Default: None
> 
> Amount of infractions to list per page
> 
> ```
> A number without decimal places.
> ```
> ### page: int
> - Autocomplete: False
> - Default: 1
> 
> Page to select
> 
> ```
> A number without decimal places.
> ```
> ### ephemeral: bool
> - Autocomplete: False
> - Default: None
> 
> Hide the command response
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### inline: bool
> - Autocomplete: False
> - Default: None
> 
> Display infractions in a grid arrangement (does not look very good)
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### export: bool
> - Autocomplete: False
> - Default: False
> 
> Exports the server's entire moderation history to a JSON file
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
# /resolve (Slash Command)
Resolve a specific case.<br/>
 - Usage: `/resolve <case> [reason]`
 - `case:` (Required) Case number of the case you're trying to resolve
 - `reason:` (Optional) Reason for resolving case

Extended Arg Info
> ### case: int
> - Autocomplete: False
> 
> Case number of the case you're trying to resolve
> 
> ```
> A number without decimal places.
> ```
> ### reason: str
> - Autocomplete: False
> - Default: None
> 
> Reason for resolving case
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# /case (Slash Command)
Check the details of a specific case.<br/>
 - Usage: `/case <case> [ephemeral] [evidenceformat] [changes] [export]`
 - `case:` (Required) What case are you looking up?
 - `ephemeral:` (Optional) Hide the command response
 - `evidenceformat:` (Optional) …
 - `changes:` (Optional) List the changes made to the case
 - `export:` (Optional) Export the case to a JSON file or codeblock

Extended Arg Info
> ### case: int
> - Autocomplete: False
> 
> What case are you looking up?
> 
> ```
> A number without decimal places.
> ```
> ### ephemeral: bool
> - Autocomplete: False
> - Default: None
> 
> Hide the command response
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### evidenceformat: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### changes: bool
> - Autocomplete: False
> - Default: False
> 
> List the changes made to the case
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### export: str
> - Autocomplete: False
> - Default: None
> - Choices: ['Export as File', 'Export as Codeblock']
> 
> Export the case to a JSON file or codeblock
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# /edit (Slash Command)
Edit the reason of a specific case.<br/>
 - Usage: `/edit <case> <reason> [duration]`
 - `case:` (Required) What case are you editing?
 - `reason:` (Required) What is the new reason?
 - `duration:` (Optional) What is the new duration? Does not reapply the moderation if it has already expired.

Extended Arg Info
> ### case: int
> - Autocomplete: False
> 
> What case are you editing?
> 
> ```
> A number without decimal places.
> ```
> ### reason: str
> - Autocomplete: False
> 
> What is the new reason?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### duration: str
> - Autocomplete: False
> - Default: None
> 
> What is the new duration? Does not reapply the moderation if it has already expired.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.aurora
Settings and miscellaneous commands for Aurora.<br/>
 - Usage: `s.aurora`
 - Aliases: `moderation and mod`
## s.aurora settings
Configure Aurora's settings.<br/>
 - Usage: `s.aurora settings`
 - Aliases: `config, options, and set`
### s.aurora settings immunity
Manage the immunity whitelist.<br/>
 - Usage: `s.aurora settings immunity`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
### s.aurora settings overrides
Manage Aurora's user overriddable settings.<br/>
 - Usage: `s.aurora settings overrides`
 - Aliases: `override and user`
### s.aurora settings addrole
Manage the addrole whitelist.<br/>

Roles added to this list are also applied to `/removerole`.<br/>
 - Usage: `s.aurora settings addrole`
 - Restricted to: `ADMIN`
 - Aliases: `removerole`
 - Checks: `server_only`
### s.aurora settings server
Manage Aurora's server settings.<br/>
 - Usage: `s.aurora settings server`
 - Restricted to: `ADMIN`
 - Aliases: `server`
 - Checks: `server_only`
## s.aurora timedelta
Convert a string to a timedelta.<br/>

This command converts a duration to a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta) Python object.<br/>
You cannot convert years or months as they are not fixed units. Use `s.aurora relativedelta` for that.<br/>

**Example usage**<br/>
`s.aurora timedelta 1 day 15hr 82 minutes 52s`<br/>
**Output**<br/>
`1 day, 16:22:52`<br/>
 - Usage: `s.aurora timedelta <duration>`
 - Aliases: `tdc, td, and timedeltaconvert`
Extended Arg Info
> ### duration: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.aurora relativedelta
Convert a string to a relativedelta.<br/>

This command converts a duration to a [`relativedelta`](https://dateutil.readthedocs.io/en/stable/relativedelta.html) Python object.<br/>

**Example usage**<br/>
`s.aurora relativedelta 3 years 1 day 15hr 82 minutes 52s`<br/>
**Output**<br/>
`relativedelta(years=+3, days=+1, hours=+15, minutes=+82, seconds=+52)`<br/>
 - Usage: `s.aurora relativedelta <duration>`
 - Aliases: `rdc, rd, and relativedeltaconvert`
Extended Arg Info
> ### duration: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.aurora import
Import moderation history from other bots.<br/>
 - Usage: `s.aurora import`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
### s.aurora import aurora
Import moderation history from another bot using Aurora.<br/>
 - Usage: `s.aurora import aurora`
 - Restricted to: `ADMIN`
### s.aurora import galacticbot
Import moderation history from GalacticBot.<br/>
 - Usage: `s.aurora import galacticbot`
 - Restricted to: `ADMIN`
