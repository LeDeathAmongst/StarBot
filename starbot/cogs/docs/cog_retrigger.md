## s.re-trigger modlog
Set which events to record in the modlog.<br/>
 - Usage: `s.re-trigger modlog`
### /re-trigger modlog settings (Slash Command)
Show retrigger's modlog settings for this server.<br/>
 - Usage: `/re-trigger modlog settings`
### /re-trigger modlog bans (Slash Command)
Toggle custom ban messages in the modlog<br/>
 - Usage: `/re-trigger modlog bans`
### /re-trigger modlog kicks (Slash Command)
Toggle custom kick messages in the modlog<br/>
 - Usage: `/re-trigger modlog kicks`
### /re-trigger modlog filter (Slash Command)
Toggle custom filter messages in the modlog<br/>
 - Usage: `/re-trigger modlog filter`
### /re-trigger modlog addroles (Slash Command)
Toggle custom add role messages in the modlog<br/>
 - Usage: `/re-trigger modlog addroles`
### /re-trigger modlog removeroles (Slash Command)
Toggle custom remove role messages in the modlog<br/>
 - Usage: `/re-trigger modlog removeroles`
### /re-trigger modlog channel (Slash Command)
Set the modlog channel for filtered words<br/>
 - Usage: `/re-trigger modlog channel [channel]`
 - `channel:` (Optional) …

Extended Arg Info
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.re-trigger allowlist
Set allowlist options for ReTrigger.<br/>
 - Usage: `s.re-trigger allowlist`
### /re-trigger allowlist add (Slash Command)
Add a channel, user, or role to a triggers allowlist<br/>
 - Usage: `/re-trigger allowlist add <trigger> [channel] [user] [role]`
 - `trigger:` (Required) …
 - `channel:` (Optional) …
 - `user:` (Optional) …
 - `role:` (Optional) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### user: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> …
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
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### /re-trigger allowlist remove (Slash Command)
Remove a channel, user, or role from a triggers allowlist<br/>
 - Usage: `/re-trigger allowlist remove <trigger> [channel] [user] [role]`
 - `trigger:` (Required) …
 - `channel:` (Optional) …
 - `user:` (Optional) …
 - `role:` (Optional) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### user: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> …
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
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.re-trigger blocklist
Set blocklist options for ReTrigger.<br/>
 - Usage: `s.re-trigger blocklist`
### /re-trigger blocklist add (Slash Command)
Add a channel, user, or role to a triggers blocklist<br/>
 - Usage: `/re-trigger blocklist add <trigger> [channel] [user] [role]`
 - `trigger:` (Required) …
 - `channel:` (Optional) …
 - `user:` (Optional) …
 - `role:` (Optional) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### user: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> …
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
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### /re-trigger blocklist remove (Slash Command)
Remove a channel, user, or role from a triggers blocklist<br/>
 - Usage: `/re-trigger blocklist remove <trigger> [channel] [user] [role]`
 - `trigger:` (Required) …
 - `channel:` (Optional) …
 - `user:` (Optional) …
 - `role:` (Optional) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel
> - Autocomplete: False
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### user: discord.member.Member
> - Autocomplete: False
> - Default: None
> 
> …
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
> - Default: None
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.re-trigger edit
Edit various settings in a set trigger.<br/>
 - Usage: `s.re-trigger edit`
### /re-trigger edit cooldown (Slash Command)
Set cooldown options for ReTrigger<br/>
 - Usage: `/re-trigger edit cooldown <trigger> <time> [style]`
 - `trigger:` (Required) …
 - `time:` (Required) …
 - `style:` (Optional) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### time: int
> - Autocomplete: False
> 
> …
> 
> ```
> A number without decimal places.
> ```
> ### style: str
> - Autocomplete: False
> - Default: server
> - Choices: ['server', 'channel', 'member']
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit regex (Slash Command)
Edit the regex of a saved trigger.<br/>
 - Usage: `/re-trigger edit regex <trigger> <regex>`
 - `trigger:` (Required) …
 - `regex:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit nsfw (Slash Command)
Toggle whether a trigger is considered age-restricted.<br/>
 - Usage: `/re-trigger edit nsfw <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit readembeds (Slash Command)
Toggle whether to include embed contents in searched text.<br/>
 - Usage: `/re-trigger edit readembeds <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit readfilenames (Slash Command)
Toggle whether to search message attachment filenames.<br/>
 - Usage: `/re-trigger edit readfilenames <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit reply (Slash Command)
Set whether or not to reply to the triggered message.<br/>
 - Usage: `/re-trigger edit reply <trigger> [set_to]`
 - `trigger:` (Required) …
 - `set_to:` (Optional) True will reply with mention, False will reply without mention, blank will not use a reply.

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### set_to: bool
> - Autocomplete: False
> - Default: None
> 
> True will reply with mention, False will reply without mention, blank will not use a reply.
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
### /re-trigger edit thread (Slash Command)
Set whether or not to create a thread from the trigger.<br/>
 - Usage: `/re-trigger edit thread <trigger> [set_to] [thread_name]`
 - `trigger:` (Required) …
 - `set_to:` (Optional) True will create a Public Thread, False will create a Private Thread, blank will not create a…
 - `thread_name:` (Optional) The name of the thread created. You can use replacements like in text responses.

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### set_to: bool
> - Autocomplete: False
> - Default: None
> 
> True will create a Public Thread, False will create a Private Thread, blank will not create a…
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### thread_name: str
> - Autocomplete: False
> - Default: None
> 
> The name of the thread created. You can use replacements like in text responses.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit tts (Slash Command)
Set whether or not to send the message with text-to-speech.<br/>
 - Usage: `/re-trigger edit tts <trigger> <set_to>`
 - `trigger:` (Required) …
 - `set_to:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### set_to: bool
> - Autocomplete: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
### /re-trigger edit mention (Slash Command)
Set whether or not this trigger can mention roles<br/>
 - Usage: `/re-trigger edit mention <style> <trigger> <set_to>`
 - `style:` (Required) …
 - `trigger:` (Required) …
 - `set_to:` (Required) …

Extended Arg Info
> ### style: int
> - Autocomplete: False
> - Choices: ['everyone', 'role', 'user']
> 
> …
> 
> ```
> A number without decimal places.
> ```
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### set_to: bool
> - Autocomplete: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
### /re-trigger edit edited (Slash Command)
Toggle whether to search message edits.<br/>
 - Usage: `/re-trigger edit edited <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit ignorecommands (Slash Command)
Toggle whether a trigger will ignore commands.<br/>
 - Usage: `/re-trigger edit ignorecommands <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit text (Slash Command)
Edit the text of a saved trigger.<br/>
 - Usage: `/re-trigger edit text <trigger> <text>`
 - `trigger:` (Required) …
 - `text:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit chance (Slash Command)
Edit the chance a trigger will execute.<br/>
 - Usage: `/re-trigger edit chance <trigger> <chance>`
 - `trigger:` (Required) …
 - `chance:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### chance: int
> - Autocomplete: False
> 
> …
> 
> ```
> A number without decimal places.
> ```
### /re-trigger edit command (Slash Command)
Edit the command a trigger runs.<br/>
 - Usage: `/re-trigger edit command <trigger> <command>`
 - `trigger:` (Required) …
 - `command:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### command: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit role (Slash Command)
Edit the added or removed role of a saved trigger.<br/>
 - Usage: `/re-trigger edit role <trigger> <role>`
 - `trigger:` (Required) …
 - `role:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### role: discord.role.Role
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### /re-trigger edit reaction (Slash Command)
Edit the emoji reaction of a saved trigger.<br/>
 - Usage: `/re-trigger edit reaction <trigger> <emoji>`
 - `trigger:` (Required) …
 - `emoji:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### emoji: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit enable (Slash Command)
Enable a trigger<br/>
 - Usage: `/re-trigger edit enable <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### /re-trigger edit disable (Slash Command)
Disable a trigger<br/>
 - Usage: `/re-trigger edit disable <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger list (Slash Command)
List information about a trigger<br/>
 - Usage: `/re-trigger list [trigger] [server_id]`
 - `trigger:` (Optional) …
 - `server_id:` (Optional) Only available to bot owner

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### server_id: str
> - Autocomplete: False
> - Default: None
> 
> Only available to bot owner
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger remove (Slash Command)
Remove a specified trigger<br/>
 - Usage: `/re-trigger remove <trigger>`
 - `trigger:` (Required) …

Extended Arg Info
> ### trigger: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger explain (Slash Command)
Explain how to use retrigger<br/>
 - Usage: `/re-trigger explain [page_num]`
 - `page_num:` (Optional) …

Extended Arg Info
> ### page_num: int
> - Autocomplete: False
> - Default: 1
> 
> …
> 
> ```
> A number without decimal places.
> ```
## /re-trigger text (Slash Command)
Add a text response trigger<br/>
 - Usage: `/re-trigger text <name> <regex> <text> [delete_after]`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `text:` (Required) …
 - `delete_after:` (Optional) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### delete_after: str
> - Autocomplete: False
> - Default: None
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger dm (Slash Command)
Add a dm response trigger<br/>
 - Usage: `/re-trigger dm <name> <regex> <text>`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `text:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger dmme (Slash Command)
Add a trigger to dm yourself<br/>
 - Usage: `/re-trigger dmme <name> <regex> <text>`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `text:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger rename (Slash Command)
Add a trigger to rename users<br/>
 - Usage: `/re-trigger rename <name> <regex> <text>`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `text:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger ban (Slash Command)
Add a trigger to ban users<br/>
 - Usage: `/re-trigger ban <name> <regex>`
 - `name:` (Required) …
 - `regex:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger kick (Slash Command)
Add a trigger to kick users<br/>
 - Usage: `/re-trigger kick <name> <regex>`
 - `name:` (Required) …
 - `regex:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger command (Slash Command)
Add a command trigger<br/>
 - Usage: `/re-trigger command <name> <regex> <command>`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `command:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### command: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /re-trigger filter (Slash Command)
Add a trigger to filter messages<br/>
 - Usage: `/re-trigger filter <name> <regex> [check_filenames]`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `check_filenames:` (Optional) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### check_filenames: bool
> - Autocomplete: False
> - Default: False
> 
> …
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /re-trigger addrole (Slash Command)
Add a trigger to add a role<br/>
 - Usage: `/re-trigger addrole <name> <regex> <role>`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `role:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### role: discord.role.Role
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## /re-trigger removerole (Slash Command)
Add a trigger to remove a role<br/>
 - Usage: `/re-trigger removerole <name> <regex> <role>`
 - `name:` (Required) …
 - `regex:` (Required) …
 - `role:` (Required) …

Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### regex: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### role: discord.role.Role
> - Autocomplete: False
> 
> …
> 
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# s.retrigger
Setup automatic triggers based on regular expressions<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger`
 - Checks: `server_only`
## s.retrigger edit
Edit various settings in a set trigger.<br/>

Note: Only the server owner, Bot owner, or original<br/>
author can edit a saved trigger. Multi triggers<br/>
cannot be edited.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit`
 - Restricted to: `MOD`
### s.retrigger edit ocr
Toggle whether to use Optical Character Recognition to search for text within images.<br/>
`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit ocr <trigger>`
 - Restricted to: `MOD`
 - Checks: `ReTrigger`
### s.retrigger edit reply
Set whether or not to reply to the triggered message<br/>

`<trigger>` is the name of the trigger.<br/>
`[set_to]` `True` will reply with a notificaiton, `False` will reply without a notification,<br/>
leaving this blank will clear replies entirely.<br/>

Note: This is only availabe for Red 3.4.6/discord.py 1.6.0 or greater.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit reply <trigger> [set_to=None]`
 - Restricted to: `MOD`
 - Aliases: `replies`
Extended Arg Info
> ### set_to: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.retrigger edit edited
Toggle whether the bot will listen to edited messages as well as on_message for<br/>
the specified trigger.<br/>

Note: This will disable suppress for this trigger since it edits the original users<br/>
message.<br/>
`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit edited <trigger>`
 - Restricted to: `MOD`
### s.retrigger edit readfilenames
Toggle whether to search message attachment filenames.<br/>

Note: This will append all attachments in a message to the message content. This **will not**<br/>
download and read file content using regex.<br/>

`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit readfilenames <trigger>`
 - Restricted to: `MOD`
 - Aliases: `filenames`
### s.retrigger edit disable
Disable a trigger<br/>

`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit disable <trigger>`
 - Restricted to: `MOD`
### s.retrigger edit react
Edit the emoji reactions of a saved trigger.<br/>

`<trigger>` is the name of the trigger.<br/>
`<emojis>` The new emojis to be used in the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit react <trigger> <emojis>`
 - Restricted to: `MOD`
 - Aliases: `emojis`
### s.retrigger edit tts
Set whether or not to send the message with text-to-speech<br/>

`<trigger>` is the name of the trigger.<br/>
`[set_to]` either `true` or `false` on whether to send the text<br/>
reply with text-to-speech enabled.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit tts <trigger> [set_to=False]`
 - Restricted to: `MOD`
 - Aliases: `texttospeech and text-to-speech`
Extended Arg Info
> ### set_to: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.retrigger edit thread
Set whether or not this trigger will attempt to create a private thread on the triggered<br/>
message. This will automatically add the user who triggered this to the thread.<br/>

`<trigger>` is the name of the trigger.<br/>
`<public_or_private>` `True` will create a public thread, `False` will create a private thread. `None`<br/>
or leaving this option blank will tell the trigger not to create a thread.<br/>
`<thread_name>` The name of the thread created. This uses replacements if you want dynamic<br/>
information such as the users name, etc.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit thread <trigger> [public_or_private=None] [thread_name]`
 - Restricted to: `MOD`
 - Aliases: `makethread and createthread`
Extended Arg Info
> ### public_or_private: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### thread_name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.retrigger edit role
Edit the added or removed roles of a saved trigger.<br/>

`<trigger>` is the name of the trigger.<br/>
`<roles>` space separated list of roles or ID's to edit on the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit role <trigger> <roles>`
 - Restricted to: `MOD`
 - Aliases: `roles`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.retrigger edit ignorecommands
Toggle the trigger ignoring command messages entirely.<br/>

`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit ignorecommands <trigger>`
 - Restricted to: `MOD`
### s.retrigger edit text
Edit the text of a saved trigger.<br/>

`<trigger>` is the name of the trigger.<br/>
`<text>` The new text to respond with.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit text <trigger> <text>`
 - Restricted to: `MOD`
 - Aliases: `msg`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.retrigger edit deleteafter
Edit the delete_after parameter of a saved text trigger.<br/>

`<trigger>` is the name of the trigger.<br/>
`<delete_after>` The time until the message is deleted must include units.<br/>
Example: `s.retrigger edit deleteafter trigger 2 minutes`<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit deleteafter <trigger> [delete_after]`
 - Restricted to: `MOD`
 - Aliases: `autodelete and delete`
### s.retrigger edit suppress
Toggle whether a trigger will suppress original message embeds.<br/>
This will cause the original message embeds to be disabled for everyone.<br/>

Useful if you're wanting to remove the embed of a url and replace with a new url.<br/>

Note: This will disable checking edits for this trigger since it edits the original users<br/>
message.<br/>
`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit suppress <trigger>`
 - Restricted to: `MOD`
### s.retrigger edit mention
Set whether or not to send this trigger will allow role mentions<br/>

`<style>` either `everyone`, `users`, or `roles`.<br/>
`<trigger>` is the name of the trigger.<br/>
`[set_to]` either `true` or `false` on whether to allow this trigger<br/>
to actually ping roles if the bot has correct permissions.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit mention <style> <trigger> [set_to=False]`
 - Restricted to: `MOD`
 - Aliases: `ping`
Extended Arg Info
> ### set_to: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.retrigger edit cooldown
Set cooldown options for retrigger<br/>

`<trigger>` is the name of the trigger.<br/>
`<time>` is a time in seconds until the trigger will run again<br/>
set a time of 0 or less to remove the cooldown<br/>
`[style=server]` must be either `server`, `server`, `channel`, `user`, or `member`<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit cooldown <trigger> [time=0] [style=server]`
 - Restricted to: `MOD`
Extended Arg Info
> ### time: int = 0
> ```
> A number without decimal places.
> ```
> ### style='server'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.retrigger edit includethreads
Toggle whether the allowlist/blocklist will include threads within the channel.<br/>
`<trigger>` is the name of the trigger.<br/>

This will allow a trigger to run only within a channel and not within threads if<br/>
the channel is added to the allowlist or only run within threads in a channel if<br/>
the channel is added to the blocklist. Forum channels can only have threads<br/>
so are exempt from this toggle.<br/>

# Note: this only affects allowed/blocked triggers for specific channels.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit includethreads <trigger>`
 - Restricted to: `MOD`
### s.retrigger edit readthreads
Toggle whether a filter trigger will check thread titles.<br/>
`<trigger>` is the name of the trigger.<br/>

This will toggle whether filter triggers are allowed to delete<br/>
threads that are matched based on the thread title. This is enabled by default<br/>
so if you only want filter triggers to work on messages disable this.<br/>

# Note: This also requires the bot to have `manage_threads` permission<br/>
in the channel that the threads are created to work.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit readthreads <trigger>`
 - Restricted to: `MOD`
 - Aliases: `readthread`
### s.retrigger edit chance
Edit the chance a trigger will execute.<br/>

`<trigger>` is the name of the trigger.<br/>
`<chance>` The chance the trigger will execute in form of 1 in chance.<br/>

Set the `chance` to 0 to remove the chance and always perform the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit chance <trigger> [chance=0]`
 - Restricted to: `MOD`
 - Aliases: `chances`
Extended Arg Info
> ### chance: int = 0
> ```
> A number without decimal places.
> ```
### s.retrigger edit nsfw
Toggle whether a trigger is considered NSFW.<br/>
This will prevent the trigger from activating in non-NSFW channels.<br/>
`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit nsfw <trigger>`
 - Restricted to: `MOD`
### s.retrigger edit command
Edit the text of a saved trigger.<br/>

`<trigger>` is the name of the trigger.<br/>
`<command>` The new command for the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit command <trigger> <command>`
 - Restricted to: `MOD`
 - Aliases: `cmd`
Extended Arg Info
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.retrigger edit regex
Edit the regex of a saved trigger.<br/>

`<trigger>` is the name of the trigger.<br/>
`<regex>` The new regex pattern to use.<br/>

Note: **"double quotes" is not required for regex with spaces in this command**<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit regex <trigger> <regex>`
 - Restricted to: `MOD`
### s.retrigger edit readembeds
Toggle whether a trigger will check embeds.<br/>
This will allow the additional searching of Embed content.<br/>
`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit readembeds <trigger>`
 - Restricted to: `MOD`
### s.retrigger edit enable
Enable a trigger<br/>

`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger edit enable <trigger>`
 - Restricted to: `MOD`
## s.retrigger dmme
Add trigger to DM yourself<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`<text>` response of the trigger<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger dmme <name> <regex> <text>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger removerole
Add a trigger to remove a role<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`[role...]` the roles applied when the regex pattern matches space separated<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger removerole <name> <regex> <roles>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger text
Add a text response trigger<br/>

`<name>` name of the trigger.<br/>
`<regex>` the regex that will determine when to respond.<br/>
`[delete_after]` Optionally have the text autodelete must include units e.g. 2m.<br/>
`<text>` response of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger text <name> <regex> [delete_after=None] <text>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger list
List information about triggers.<br/>

`[trigger]` if supplied provides information about named trigger.<br/>
⏯️ will toggle the displayed triggers active setting<br/>
❎ will toggle the displayed trigger to be not active<br/>
✅ will toggle the displayed trigger to be active<br/>
🚮 will delete the displayed trigger<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger list [server_id=None] [trigger=None]`
Extended Arg Info
> ### server_id: Optional[int] = None
> ```
> A number without decimal places.
> ```
## s.retrigger image
Add an image/file response trigger<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`image_url` optional image_url if none is provided the bot will ask to upload an image<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger image <name> <regex> [image_url=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### image_url: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger allowlist
Set allowlist options for retrigger<br/>

allowlisting supports channels, users, or roles<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger allowlist`
 - Restricted to: `MOD`
 - Aliases: `whitelist`
### s.retrigger allowlist add
Add a channel, user, or role to triggers allowlist<br/>

`<trigger>` is the name of the trigger.<br/>
`[channel_user_role...]` is the channel, user or role to allowlist<br/>
(You can supply more than one of any at a time)<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger allowlist add <triggers> <channel_user_role>`
 - Restricted to: `MOD`
### s.retrigger allowlist remove
Remove a channel, user, or role from triggers allowlist<br/>

`<trigger>` is the name of the trigger.<br/>
`[channel_user_role...]` is the channel, user or role to remove from the allowlist<br/>
(You can supply more than one of any at a time)<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger allowlist remove <triggers> <channel_user_role>`
 - Restricted to: `MOD`
 - Aliases: `rem and del`
## s.retrigger explain
Explain how to use retrigger<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger explain [page_num=1]`
Extended Arg Info
> ### page_num: Optional[int] = 1
> ```
> A number without decimal places.
> ```
## s.retrigger filter
Add a trigger to delete a message<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger filter <name> [check_filenames=False] <regex>`
 - Restricted to: `MOD`
 - Aliases: `deletemsg`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### check_filenames: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### regex: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger remove
Remove a specified trigger<br/>

`<trigger>` is the name of the trigger.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger remove <trigger>`
 - Restricted to: `MOD`
 - Aliases: `del, rem, and delete`
## s.retrigger blocklist
Set blocklist options for retrigger<br/>

blocklisting supports channels, users, or roles<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger blocklist`
 - Restricted to: `MOD`
 - Aliases: `blacklist`
### s.retrigger blocklist add
Add a channel, user, or role to triggers blocklist<br/>

`<trigger>` is the name of the trigger.<br/>
`[channel_user_role...]` is the channel, user or role to blocklist<br/>
(You can supply more than one of any at a time)<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger blocklist add <triggers> <channel_user_role>`
 - Restricted to: `MOD`
### s.retrigger blocklist remove
Remove a channel, user, or role from triggers blocklist<br/>

`<trigger>` is the name of the trigger.<br/>
`[channel_user_role...]` is the channel, user or role to remove from the blocklist<br/>
(You can supply more than one of any at a time)<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger blocklist remove <triggers> <channel_user_role>`
 - Restricted to: `MOD`
 - Aliases: `rem and del`
## s.retrigger dm
Add a dm response trigger<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`<text>` response of the trigger<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger dm <name> <regex> <text>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger resize
Add an image to resize in response to a trigger<br/>
this will attempt to resize the image based on length of matching regex<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`[image_url]` optional image_url if none is provided the bot will ask to upload an image<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger resize <name> <regex> [image_url=None]`
 - Restricted to: `MOD`
 - Checks: `ReTrigger`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### image_url: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger modlog
Set which events to record in the modlog.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog`
 - Restricted to: `MOD`
### s.retrigger modlog kicks
Toggle custom kick messages in the modlog<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog kicks`
 - Restricted to: `MOD`
 - Aliases: `kick`
### s.retrigger modlog removeroles
Toggle custom add role messages in the modlog<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog removeroles`
 - Restricted to: `MOD`
 - Aliases: `removerole, remrole, and rolerem`
### s.retrigger modlog addroles
Toggle custom add role messages in the modlog<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog addroles`
 - Restricted to: `MOD`
 - Aliases: `addrole`
### s.retrigger modlog channel
Set the modlog channel for filtered words<br/>

`<channel>` The channel you would like filtered word notifications to go<br/>
Use `none` or `clear` to not show any modlogs<br/>
User `default` to use the built in modlog channel<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog channel <channel>`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, str, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.retrigger modlog settings
Show the current modlog settings for this server.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog settings`
 - Aliases: `list`
### s.retrigger modlog filter
Toggle custom filter messages in the modlog<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog filter`
 - Restricted to: `MOD`
 - Aliases: `delete, filters, and deletes`
### s.retrigger modlog bans
Toggle custom ban messages in the modlog<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger modlog bans`
 - Restricted to: `MOD`
 - Aliases: `ban`
## s.retrigger random
Add a random text response trigger<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger random <name> <regex>`
 - Restricted to: `MOD`
 - Aliases: `randomtext and rtext`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger publish
Add a trigger to automatically publish content in news channels.<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger publish <name> <regex>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger imagetext
Add an image/file response with text trigger<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`<text>` the triggered text response<br/>
`[image_url]` optional image_url if none is provided the bot will ask to upload an image<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger imagetext <name> <regex> <text> [image_url=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### image_url: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger kick
Add a trigger to kick users for saying specific things found with regex<br/>
This respects hierarchy so ensure the bot role is lower in the list<br/>
than mods and admin so they don't get kicked by accident<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger kick <name> <regex>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger randomimage
Add a random image/file response trigger<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger randomimage <name> <regex>`
 - Restricted to: `MOD`
 - Aliases: `randimage, randimg, rimage, and rimg`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger command
Add a command trigger<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`<command>` the command that will be triggered, do not add s. prefix<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger command <name> <regex> <command>`
 - Restricted to: `MOD`
 - Aliases: `cmd`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger rename
Add trigger to rename users<br/>

`<name>` name of the trigger.<br/>
`<regex>` the regex that will determine when to respond.<br/>
`<text>` new users nickanme.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger rename <name> <regex> <text>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger ban
Add a trigger to ban users for saying specific things found with regex<br/>
This respects hierarchy so ensure the bot role is lower in the list<br/>
than mods and admin so they don't get banned by accident<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger ban <name> <regex>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger react
Add a reaction trigger<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`emojis` the emojis to react with when triggered separated by spaces<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger react <name> <regex> <emojis>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger addrole
Add a trigger to add a role<br/>

`<name>` name of the trigger<br/>
`<regex>` the regex that will determine when to respond<br/>
`[role...]` the roles applied when the regex pattern matches space separated<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger addrole <name> <regex> <roles>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.retrigger multi
Add a multiple response trigger<br/>

- `<name>` name of the trigger.<br/>
- `<regex>` the regex that will determine when to respond.<br/>
- `<multi>` The actions you want the trigger to perform.<br/>
 - `dm:` DM the message author something.<br/>
 - `dmme:` DM the trigger author something.<br/>
 - `add:` or `remove:` Roles which can be added/removed.<br/>
 - `ban:` True to ban the user who sent the message.<br/>
 - `kick:` True to kick the user who sent the message.<br/>
 - `text:` The text to send in the channel when triggers.<br/>
 - `react:` The emojis to react to the triggered messages with.<br/>
 - `rename:` What to change the message authors nickname to.<br/>
 - `command:` The bot command to run when triggered. Don't include a prefix.<br/>
 - `filter:` True to delete the triggered message.<br/>

See https://regex101.com/ for help building a regex pattern.<br/>
See `s.retrigger explain` or click the link below for more details.<br/>
[For more details click here.](https://github.com/TrustyJAID/Trusty-cogs/blob/master/retrigger/README.md)<br/>
 - Usage: `s.retrigger multi <name> <regex> <multi>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
