# s.autoroomset
Configure the AutoRoom cog.<br/>

For a quick rundown on how to get started with this cog,<br/>
check out [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/autoroom/README.md)<br/>
 - Usage: `s.autoroomset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.autoroomset permissions
Check that the bot has all needed permissions.<br/>
 - Usage: `s.autoroomset permissions`
 - Aliases: `perms`
## s.autoroomset settings
Display current settings.<br/>
 - Usage: `s.autoroomset settings`
## s.autoroomset access
Control access to all AutoRooms.<br/>

Roles that are considered "admin" or "moderator" are<br/>
set up with the commands `s.set addadminrole`<br/>
and `s.set addmodrole` (plus the remove commands too)<br/>
 - Usage: `s.autoroomset access`
### s.autoroomset access admin
Allow Admins to join locked/private AutoRooms.<br/>
 - Usage: `s.autoroomset access admin`
### s.autoroomset access bot
Automatically allow bots into AutoRooms.<br/>

The AutoRoom Owner is able to freely allow or deny these roles as they see fit.<br/>
 - Usage: `s.autoroomset access bot`
#### s.autoroomset access bot remove
Disallow a bot role from joining every AutoRoom.<br/>
 - Usage: `s.autoroomset access bot remove <role>`
 - Aliases: `delete and del`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
#### s.autoroomset access bot add
Allow a bot role into every AutoRoom.<br/>
 - Usage: `s.autoroomset access bot add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.autoroomset access mod
Allow Moderators to join locked/private AutoRooms.<br/>
 - Usage: `s.autoroomset access mod`
## s.autoroomset modify
Modify an existing AutoRoom Source.<br/>
 - Usage: `s.autoroomset modify`
 - Aliases: `edit`
### s.autoroomset modify text
Configure sending an introductory message to the AutoRoom text channel.<br/>
 - Usage: `s.autoroomset modify text`
#### s.autoroomset modify text set
Send a message to the newly generated AutoRoom text channel.<br/>

This can have template variables and statements, which you can learn more<br/>
about by looking at `s.autoroomset modify name custom`, or by looking at<br/>
[the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/autoroom/README.md).<br/>

The only additional variable that may be useful here is the `mention` variable,<br/>
which will insert the users mention (pinging them).<br/>

- Example:<br/>
`Hello {{mention}}! Welcome to your new AutoRoom!`<br/>
 - Usage: `s.autoroomset modify text set <autoroom_source> <hint_text>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### hint_text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### s.autoroomset modify text disable
Disable sending a message to the newly generated AutoRoom text channel.<br/>
 - Usage: `s.autoroomset modify text disable <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.autoroomset modify name
Set the default name format of an AutoRoom.<br/>
 - Usage: `s.autoroomset modify name`
#### s.autoroomset modify name game
The users current playing game, otherwise the username format.<br/>

Custom format example:<br/>
`{{game}}{% if not game %}{{username}}'s Room{% endif %}{% if dupenum > 1 %} ({{dupenum}}){% endif %}`<br/>
 - Usage: `s.autoroomset modify name game <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.autoroomset modify name custom
A custom channel name.<br/>

Use `{{ expressions }}` to print variables and `{% statements %}` to do basic evaluations on variables.<br/>

Variables supported:<br/>
- `username` - AutoRoom Owner's username<br/>
- `game    ` - AutoRoom Owner's game<br/>
- `dupenum ` - An incrementing number that starts at 1, useful for un-duplicating channel names<br/>

Statements supported:<br/>
- `if/elif/else/endif`<br/>
- Example: `{% if dupenum > 1 %}DupeNum is {{dupenum}}, which is greater than 1{% endif %}`<br/>
- Another example: `{% if not game %}User isn't playing a game!{% endif %}`<br/>

It's kinda like Jinja2, but way simpler. Check out [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/autoroom/README.md) for more info.<br/>
 - Usage: `s.autoroomset modify name custom <autoroom_source> <template>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### template: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### s.autoroomset modify name username
Default format: PhasecoreX's Room.<br/>

Custom format example:<br/>
`{{username}}'s Room{% if dupenum > 1 %} ({{dupenum}}){% endif %}`<br/>
 - Usage: `s.autoroomset modify name username <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.autoroomset modify legacytextchannel
Manage if a legacy text channel should be created as well.<br/>
 - Usage: `s.autoroomset modify legacytextchannel`
#### s.autoroomset modify legacytextchannel enable
Enable creating a legacy text channel with the AutoRoom.<br/>
 - Usage: `s.autoroomset modify legacytextchannel enable <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.autoroomset modify legacytextchannel disable
Disable creating a legacy text channel with the AutoRoom.<br/>
 - Usage: `s.autoroomset modify legacytextchannel disable <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.autoroomset modify legacytextchannel topic
Manage the legacy text channel topic.<br/>
 - Usage: `s.autoroomset modify legacytextchannel topic`
##### s.autoroomset modify legacytextchannel topic disable
Disable setting a legacy text channel topic.<br/>
 - Usage: `s.autoroomset modify legacytextchannel topic disable <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
##### s.autoroomset modify legacytextchannel topic set
Set the legacy text channel topic.<br/>

- Example:<br/>
`This channel is only visible to members of your voice channel, and admins of this server. It will be deleted when everyone leaves. `<br/>
 - Usage: `s.autoroomset modify legacytextchannel topic set <autoroom_source> <topic_text>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### topic_text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.autoroomset modify type
Choose what type of AutoRoom is created.<br/>
 - Usage: `s.autoroomset modify type`
#### s.autoroomset modify type public
Rooms will be open to all. AutoRoom Owner has control over room.<br/>
 - Usage: `s.autoroomset modify type public <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.autoroomset modify type server
Rooms will be open to all, but the server owns the AutoRoom (so they can't be modified).<br/>
 - Usage: `s.autoroomset modify type server <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.autoroomset modify type locked
Rooms will be visible to all, but not joinable. AutoRoom Owner can allow users in.<br/>
 - Usage: `s.autoroomset modify type locked <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.autoroomset modify type private
Rooms will be hidden. AutoRoom Owner can allow users in.<br/>
 - Usage: `s.autoroomset modify type private <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.autoroomset modify specialperms
Modify special AutoRoom permissions.<br/>

Remember, most permissions are automatically copied<br/>
from the AuthRoom Source over to the AutoRoom.<br/>
These are for configuring special cases.<br/>
 - Usage: `s.autoroomset modify specialperms`
#### s.autoroomset modify specialperms sendmessage
Allow users to send messages in the AutoRoom built in text channel.<br/>
 - Usage: `s.autoroomset modify specialperms sendmessage <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.autoroomset modify specialperms ownermodify
Allow AutoRoom Owners to have the Manage Channels permission on their AutoRoom.<br/>
 - Usage: `s.autoroomset modify specialperms ownermodify <autoroom_source>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.autoroomset modify defaults
Learn how AutoRoom defaults are set.<br/>
 - Usage: `s.autoroomset modify defaults`
 - Aliases: `bitrate, memberrole, other, perms, and users`
### s.autoroomset modify category
Set the category that AutoRooms will be created in.<br/>
 - Usage: `s.autoroomset modify category <autoroom_source> <dest_category>`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### dest_category: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.autoroomset remove
Remove an AutoRoom Source.<br/>
 - Usage: `s.autoroomset remove <autoroom_source>`
 - Aliases: `disable, delete, and del`
Extended Arg Info
> ### autoroom_source: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.autoroomset create
Create an AutoRoom Source.<br/>

Anyone joining an AutoRoom Source will automatically have a new<br/>
voice channel (AutoRoom) created in the destination category,<br/>
and then be moved into it.<br/>
 - Usage: `s.autoroomset create <source_voice_channel> <dest_category>`
 - Aliases: `enable and add`
Extended Arg Info
> ### source_voice_channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### dest_category: discord.channel.CategoryChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.autoroom
Manage your AutoRoom.<br/>

For a quick rundown on how to manage your AutoRoom,<br/>
check out [the readme](https://github.com/PhasecoreX/PCXCogs/tree/master/autoroom/README.md)<br/>
 - Usage: `s.autoroom`
 - Checks: `server_only`
## s.autoroom public
Make your AutoRoom public.<br/>
 - Usage: `s.autoroom public`
## s.autoroom private
Make your AutoRoom private.<br/>
 - Usage: `s.autoroom private`
## s.autoroom name
Change the name of your AutoRoom.<br/>
 - Usage: `s.autoroom name <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.autoroom locked
Lock your AutoRoom (visible, but no one can join).<br/>
 - Usage: `s.autoroom locked`
## s.autoroom allow
Allow a user (or role) into your AutoRoom.<br/>
 - Usage: `s.autoroom allow <member_or_role>`
 - Aliases: `add`
Extended Arg Info
> ### member_or_role: Union[discord.role.Role, discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.autoroom settings
Display current settings.<br/>
 - Usage: `s.autoroom settings`
 - Aliases: `about and info`
## s.autoroom users
Change the user limit of your AutoRoom.<br/>
 - Usage: `s.autoroom users <user_limit>`
 - Aliases: `userlimit`
Extended Arg Info
> ### user_limit: int
> ```
> A number without decimal places.
> ```
## s.autoroom bitrate
Change the bitrate of your AutoRoom.<br/>
 - Usage: `s.autoroom bitrate <kbps>`
 - Aliases: `kbps`
Extended Arg Info
> ### kbps: int
> ```
> A number without decimal places.
> ```
## s.autoroom deny
Deny a user (or role) from accessing your AutoRoom.<br/>

If the user is already in your AutoRoom, they will be disconnected.<br/>

If a user is no longer able to access the room due to denying a role,<br/>
they too will be disconnected. Keep in mind that if the server is using<br/>
member roles, denying roles will probably not work as expected.<br/>
 - Usage: `s.autoroom deny <member_or_role>`
 - Aliases: `ban and block`
Extended Arg Info
> ### member_or_role: Union[discord.role.Role, discord.member.Member]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.autoroom claim
Claim ownership of this AutoRoom.<br/>
 - Usage: `s.autoroom claim`
