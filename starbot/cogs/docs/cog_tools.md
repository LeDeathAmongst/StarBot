# s.access
Check channel access<br/>
 - Usage: `s.access`
 - Restricted to: `MOD`
 - Checks: `server_only`
## s.access text
Check text channel access.<br/>
 - Usage: `s.access text [user=None] [server=None]`
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
> ### server: int = None
> ```
> A number without decimal places.
> ```
## s.access compare
Compare channel access with another user.<br/>
 - Usage: `s.access compare <user> [server=None]`
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
> ### server: int = None
> ```
> A number without decimal places.
> ```
## s.access voice
Check voice channel access.<br/>
 - Usage: `s.access voice [user=None] [server=None]`
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
> ### server: int = None
> ```
> A number without decimal places.
> ```
# s.banlist
Displays the server's banlist.<br/>
 - Usage: `s.banlist`
 - Restricted to: `MOD`
 - Checks: `server_only`
# s.cid
Shows the channel id for the current channel.<br/>
 - Usage: `s.cid`
 - Checks: `server_only`
# s.chinfo
Shows channel information. Defaults to current text channel.<br/>
 - Usage: `s.chinfo [channel=None]`
 - Checks: `server_only`
Extended Arg Info
> ### channel: int = None
> ```
> A number without decimal places.
> ```
# s.eid
Get an id for an emoji.<br/>
 - Usage: `s.eid <emoji>`
 - Checks: `server_only`
Extended Arg Info
> ### emoji: discord.emoji.Emoji
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
# s.einfo
Emoji information.<br/>
 - Usage: `s.einfo <emoji>`
 - Checks: `server_only`
Extended Arg Info
> ### emoji: discord.emoji.Emoji
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
# s.inrole
Check members in the role specified.<br/>
 - Usage: `s.inrole <rolename>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### rolename: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.joined
Show when a user joined the server.<br/>
 - Usage: `s.joined [user=None]`
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
# s.listservers
List the servers|servers the bot is in.<br/>
 - Usage: `s.listservers`
 - Restricted to: `MOD`
 - Aliases: `listservers, serverlist, and serverlist`
# s.listchannel
List the channels of the current server<br/>
 - Usage: `s.listchannel`
 - Restricted to: `MOD`
 - Aliases: `channellist`
 - Checks: `server_only`
# s.newusers
Lists the newest 5 members.<br/>

`text_format` is the markdown language to use. Defaults to `py`.<br/>
 - Usage: `s.newusers [count=5] [text_format=py]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### count: int = 5
> ```
> A number without decimal places.
> ```
> ### text_format: str = 'py'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.perms
Fetch a specific user's permissions.<br/>
 - Usage: `s.perms [user=None]`
 - Restricted to: `MOD`
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
# s.rid
Shows the id of a role.<br/>
 - Usage: `s.rid <rolename>`
 - Checks: `server_only`
Extended Arg Info
> ### rolename
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.rinfo
Shows role info.<br/>
 - Usage: `s.rinfo <rolename>`
 - Checks: `server_only`
Extended Arg Info
> ### rolename: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# s.rolelist
Displays the server's roles.<br/>
 - Usage: `s.rolelist`
 - Restricted to: `MOD`
 - Aliases: `listroles`
 - Checks: `server_only`
# s.sid
Show the server id.<br/>
 - Usage: `s.sid`
 - Checks: `server_only`
# s.sinfo
Shows server information.<br/>
 - Usage: `s.sinfo [server=None]`
 - Aliases: `ginfo`
 - Checks: `server_only`
Extended Arg Info
> ### server=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.stinfo
Sticker information.<br/>

Attach a sticker to the command message or provide a link to a message with a sticker.<br/>
 - Usage: `s.stinfo [message_link=None]`
 - Aliases: `stickerinfo`
 - Checks: `server_only`
Extended Arg Info
> ### message_link: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.uid
Get a member's id from a fuzzy name search.<br/>
 - Usage: `s.uid <partial_name_or_nick>`
 - Checks: `server_only`
# s.uimages
Shows user image urls. Defaults to author.<br/>

`embed` is a True/False value for whether to display the info in an embed.<br/>
 - Usage: `s.uimages [user=None] [embed=False]`
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
> ### embed=False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.uinfo
Shows user information. Defaults to author.<br/>
 - Usage: `s.uinfo [user=None]`
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
# s.whatis
What is it?<br/>
 - Usage: `s.whatis <what_is_this_id>`
 - Checks: `server_only`
Extended Arg Info
> ### what_is_this_id: int
> ```
> A number without decimal places.
> ```
