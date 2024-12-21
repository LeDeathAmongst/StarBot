# s.reactrole
Base command for Reaction Role management.<br/>
 - Usage: `s.reactrole`
## s.reactrole delete
Delete an entire reaction role for a message.<br/>
 - Usage: `s.reactrole delete <message>`
 - Aliases: `remove`
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     
### s.reactrole delete bind
Delete an emoji-role bind for a reaction role.<br/>
 - Usage: `s.reactrole delete bind <message> <emoji>`
Extended Arg Info
> ### message: Union[discord.message.Message, roleutils.converters.ObjectConverter]
> Converts to a :class:`discord.Message`.
> 
>     
## s.reactrole create
Create a reaction role.<br/>

Emoji and role groups should be seperated by a ';' and have no space.<br/>

Example:<br/>
    - s.reactrole create 🎃;@SpookyRole 🅱️;MemeRole #role_channel Red<br/>
 - Usage: `s.reactrole create <emoji_role_groups> [channel=None] [color=None] [name]`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### color: Optional[discord.colour.Colour] = None
> Converts to a :class:`~discord.Colour`.
> 
>     
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.reactrole list
View the reaction roles on this server.<br/>
 - Usage: `s.reactrole list`
## s.reactrole bind
Bind a reaction role to an emoji on a message.<br/>
 - Usage: `s.reactrole bind <message> <emoji> <role>`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
# s.autorole
Manage autoroles and sticky roles.<br/>
 - Usage: `s.autorole`
 - Checks: `server_only`
## s.autorole sticky

 - Usage: `s.autorole sticky`
 - Aliases: `stickyrole`
### s.autorole sticky set

 - Usage: `s.autorole sticky set <add_or_remove> <role>`
 - Aliases: `role`
### s.autorole sticky add

 - Usage: `s.autorole sticky add <users> <role>`
### s.autorole sticky remove

 - Usage: `s.autorole sticky remove <users> <role>`
## s.autorole remove
Remove an autorole.<br/>
 - Usage: `s.autorole remove <role>`
## s.autorole toggle
Toggle the auto role system.<br/>
 - Usage: `s.autorole toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.autorole humans
Manage autoroles for humans.<br/>
 - Usage: `s.autorole humans`
### s.autorole humans remove
Remove an autorole for humans.<br/>
 - Usage: `s.autorole humans remove <role>`
### s.autorole humans add
Add a role to be added to all new humans on join.<br/>
 - Usage: `s.autorole humans add <role>`
### s.autorole humans toggle
Toggle the human only autorole system.<br/>
 - Usage: `s.autorole humans toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.autorole add
Add a role to be added to all new members on join.<br/>
 - Usage: `s.autorole add <role>`
## s.autorole bots
Manage autoroles for bots.<br/>
 - Usage: `s.autorole bots`
### s.autorole bots toggle
Toggle the bots only autorole system.<br/>
 - Usage: `s.autorole bots toggle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.autorole bots add
Add a role to be added to all new bots on join.<br/>
 - Usage: `s.autorole bots add <role>`
### s.autorole bots remove
Remove an autorole for bots.<br/>
 - Usage: `s.autorole bots remove <role>`
# s.role
Base command for modifying roles.<br/>

Invoking this command will add or remove the given role from the member, depending on whether they already had it.<br/>
 - Usage: `s.role <member> <role>`
 - Checks: `server_only`
## s.role info
Get information about a role.<br/>
 - Usage: `s.role info <role>`
## s.role humans
Add a role to all humans (non-bots) in the server.<br/>
 - Usage: `s.role humans <role>`
## s.role rin
Remove a role from all members of a another role.<br/>
 - Usage: `s.role rin <target_role> <remove_role>`
## s.role rhumans
Remove a role from all humans (non-bots) in the server.<br/>
 - Usage: `s.role rhumans <role>`
## s.role all
Add a role to all members of the server.<br/>
 - Usage: `s.role all <role>`
## s.role remove
Remove a role from a member.<br/>
 - Usage: `s.role remove <member> <role>`
## s.role name
Change a role's name.<br/>
 - Usage: `s.role name <role> <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.role color
Change a role's color.<br/>
 - Usage: `s.role color <role> <color>`
 - Aliases: `colour`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
## s.role target
Modify roles using 'targeting' args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `s.target`.<br/>
 - Usage: `s.role target`
 - Checks: `targeter_cog`
### s.role target add
Add a role to members using targeting args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `s.target`.<br/>
 - Usage: `s.role target add <role> <args>`
### s.role target remove
Remove a role from members using targeting args.<br/>

An explanation of Targeter and test commands to preview the members affected can be found with `s.target`.<br/>
 - Usage: `s.role target remove <role> <args>`
## s.role bots
Add a role to all bots in the server.<br/>
 - Usage: `s.role bots <role>`
## s.role addmulti
Add a role to multiple members.<br/>
 - Usage: `s.role addmulti <role> <members>`
## s.role uniquemembers
View the total unique members between multiple roles.<br/>
 - Usage: `s.role uniquemembers <roles>`
 - Aliases: `um`
## s.role create
Creates a role.<br/>

Color and whether it is hoisted can be specified.<br/>
 - Usage: `s.role create [color=#000000] [hoist=False] [name]`
Extended Arg Info
> ### color: Optional[discord.colour.Colour] = <Colour value=0>
> Converts to a :class:`~discord.Colour`.
> 
>     
> ### hoist: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### name: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.role hoist
Toggle whether a role should appear seperate from other roles.<br/>
 - Usage: `s.role hoist <role> [hoisted=None]`
Extended Arg Info
> ### hoisted: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.role members
Sends a list of members in a role.<br/>

You can supply a custom formatting tagscript for each member.<br/>
The [member](https://seina-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block) block is available to use, found on the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/index.html).<br/>

**Example:**<br/>
`s.role dump @admin <t:{member(timestamp)}> - {member(mention)}`<br/>
 - Usage: `s.role members <role> [formatting]`
 - Aliases: `dump`
Extended Arg Info
> ### formatting: str = '{member} - {member(id)}'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.role rbots
Remove a role from all bots in the server.<br/>
 - Usage: `s.role rbots <role>`
## s.role custom
Add/Remove roles to one or more users<br/>

You cannot add and remove the same Role<br/>

**Example:**<br/>
- `s.role custom inthedark.org --add role1 --remove role2`<br/>
- `s. role custom inthedark.org --add role1 "role to remove"`<br/>
 - Usage: `s.role custom <users> <flags>`
## s.role removemulti
Remove a role from multiple members.<br/>
 - Usage: `s.role removemulti <role> <members>`
## s.role colors
Sends the server's roles, ordered by color.<br/>
 - Usage: `s.role colors`
## s.role rall
Remove a role from all members of the server.<br/>
 - Usage: `s.role rall <role>`
 - Aliases: `removeall`
## s.role in
Add a role to all members of a another role.<br/>
 - Usage: `s.role in <target_role> <add_role>`
## s.role add
Add a role to a member.<br/>
 - Usage: `s.role add <member> <role>`
# s.multirole
Add multiple roles to a member.<br/>
 - Usage: `s.multirole <member> <roles>`
## s.multirole remove
Remove multiple roles from a member.<br/>
 - Usage: `s.multirole remove <member> <roles>`
