# s.listpermissions
Generates the permissions of a certain object and puts them in a nice table for you.<br/>
 - Usage: `s.listpermissions`
 - Aliases: `lp`
 - Checks: `server_only`
## s.listpermissions channel
Generates the permissions of a channel for either a member or a role.<br/>
 - Usage: `s.listpermissions channel`
### s.listpermissions channel member
Generates the permissions for a member in a channel.<br/>

Permissions Values:<br/>
    True: means that the person has that permission<br/>
    False: means that the person does not have that permission<br/>
 - Usage: `s.listpermissions channel member [member=None] [channel=None]`
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
> ### channel: Union[discord.channel.VoiceChannel, discord.channel.TextChannel, discord.channel.CategoryChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.listpermissions channel role
Generates the basic permissions for a role in a channel.  Note that these are only the basic permissions, True or False will only show when the permissions is different from the default permissions of a role.<br/>

Role name can be the name of the role (or at least close to it) or the ID of it.<br/>

Permissions Values:<br/>
    None: means that it depends on the role permissions<br/>
    True: means that a person can explicitly do that, despite role permissions<br/>
    False: means that a person can explicitly not do that, despite role permissions<br/>
 - Usage: `s.listpermissions channel role [channel=None] <rolename>`
Extended Arg Info
> ### channel: Union[discord.channel.VoiceChannel, discord.channel.TextChannel, discord.channel.CategoryChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### rolename
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.listpermissions server
Generates the permissions for a role or member server wide.  These will change between channels.<br/>
 - Usage: `s.listpermissions server`
### s.listpermissions server role
Generates the permissions of a role.<br/>

Role name can be the name of the role (or at least close to it) or the ID of it.<br/>

Permissions Values:<br/>
    True: means that the role has that permission<br/>
    False: means that the role does not have that permission<br/>
 - Usage: `s.listpermissions server role <rolename>`
Extended Arg Info
> ### rolename
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.listpermissions server member
Generates the server wide permissions for a member.  This only takes into account their server permissions, not any for specific channels.<br/>
 - Usage: `s.listpermissions server member [member=None]`
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
# s.availablepermissions
Generates the permissions of a certain object and puts them in a nice table for you.  Only shows the available permissions.<br/>
 - Usage: `s.availablepermissions`
 - Aliases: `ap`
 - Checks: `server_only`
## s.availablepermissions channel
Generates the permissions of a channel for either a member or a role.<br/>
 - Usage: `s.availablepermissions channel`
### s.availablepermissions channel member
Generates the permissions for a member in a channel.<br/>

Permissions Values:<br/>
    True: means that the person has that permission<br/>
    False: means that the person does not have that permission<br/>
 - Usage: `s.availablepermissions channel member [member=None] [channel=None]`
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
> ### channel: Union[discord.channel.VoiceChannel, discord.channel.TextChannel, discord.channel.CategoryChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.availablepermissions channel role
Generates the basic permissions for a role in a channel.  Note that these are only the basic permissions, True or False will only show when the permissions is different from the default permissions of a role.<br/>

Role name can be the name of the role (or at least close to it) or the ID of it.<br/>

Permissions Values:<br/>
    None: means that it depends on the role permissions<br/>
    True: means that a person can explicitly do that, despite role permissions<br/>
    False: means that a person can explicitly not do that, despite role permissions<br/>
 - Usage: `s.availablepermissions channel role [channel=None] <rolename>`
Extended Arg Info
> ### channel: Union[discord.channel.VoiceChannel, discord.channel.TextChannel, discord.channel.CategoryChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### rolename
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.availablepermissions server
Generates the permissions for a role or member server wide.  These will change between channels.<br/>
 - Usage: `s.availablepermissions server`
### s.availablepermissions server member
Generates the server wide permissions for a member.  This only takes into account their server permissions, not any for specific channels.<br/>
 - Usage: `s.availablepermissions server member [member=None]`
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
### s.availablepermissions server role
Generates the permissions of a role.<br/>

Role name can be the name of the role (or at least close to it) or the ID of it.<br/>

Permissions Values:<br/>
    True: means that the role has that permission<br/>
    False: means that the role does not have that permission<br/>
 - Usage: `s.availablepermissions server role <rolename>`
Extended Arg Info
> ### rolename
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.deniedpermissions
Generates the permissions of a certain object and puts them in a nice table for you.  Only shows the denied permissions.<br/>
 - Usage: `s.deniedpermissions`
 - Aliases: `dp`
 - Checks: `server_only`
## s.deniedpermissions channel
Generates the permissions of a channel for either a member or a role.<br/>
 - Usage: `s.deniedpermissions channel`
### s.deniedpermissions channel role
Generates the basic permissions for a role in a channel.  Note that these are only the basic permissions, True or False will only show when the permissions is different from the default permissions of a role.<br/>

Role name can be the name of the role (or at least close to it) or the ID of it.<br/>

Permissions Values:<br/>
    None: means that it depends on the role permissions<br/>
    True: means that a person can explicitly do that, despite role permissions<br/>
    False: means that a person can explicitly not do that, despite role permissions<br/>
 - Usage: `s.deniedpermissions channel role [channel=None] <rolename>`
Extended Arg Info
> ### channel: Union[discord.channel.VoiceChannel, discord.channel.TextChannel, discord.channel.CategoryChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### rolename
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.deniedpermissions channel member
Generates the permissions for a member in a channel.<br/>

Permissions Values:<br/>
    True: means that the person has that permission<br/>
    False: means that the person does not have that permission<br/>
 - Usage: `s.deniedpermissions channel member [member=None] [channel=None]`
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
> ### channel: Union[discord.channel.VoiceChannel, discord.channel.TextChannel, discord.channel.CategoryChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.deniedpermissions server
Generates the permissions for a role or member server wide.  These will change between channels.<br/>
 - Usage: `s.deniedpermissions server`
### s.deniedpermissions server member
Generates the server wide permissions for a member.  This only takes into account their server permissions, not any for specific channels.<br/>
 - Usage: `s.deniedpermissions server member [member=None]`
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
### s.deniedpermissions server role
Generates the permissions of a role.<br/>

Role name can be the name of the role (or at least close to it) or the ID of it.<br/>

Permissions Values:<br/>
    True: means that the role has that permission<br/>
    False: means that the role does not have that permission<br/>
 - Usage: `s.deniedpermissions server role <rolename>`
Extended Arg Info
> ### rolename
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
