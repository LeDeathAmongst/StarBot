# s.rolesbuttons (Hybrid Command)
Group of commands to use RolesButtons.<br/>
 - Usage: `s.rolesbuttons`
 - Slash Usage: `/rolesbuttons`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.rolesbuttons bulk (Hybrid Command)
Add roles-buttons for a message.<br/>

```s.rolesbuttons bulk <message> :reaction1:|@role1 :reaction2:|@role2 :reaction3:|@role3```
 - Usage: `s.rolesbuttons bulk <message> <roles_buttons>`
 - Slash Usage: `/rolesbuttons bulk <message> <roles_buttons>`
 - Checks: `server_only`
## s.rolesbuttons remove (Hybrid Command)
Remove a role-button for a message.<br/>

Use `s.rolesbuttons list <message>` to find the config identifier.<br/>
 - Usage: `s.rolesbuttons remove <message> <config_identifier>`
 - Slash Usage: `/rolesbuttons remove <message> <config_identifier>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### config_identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.rolesbuttons add (Hybrid Command)
Add a role-button for a message.<br/>

(Use the number for the color.)<br/>
• `primary`: 1<br/>
• `secondary`: 2<br/>
• `success`: 3<br/>
• `danger`: 4<br/>
# Aliases<br/>
• `blurple`: 1<br/>
• `grey`: 2<br/>
• `gray`: 2<br/>
• `green`: 3<br/>
• `red`: 4<br/>
 - Usage: `s.rolesbuttons add <message> <role> <emoji> [style_button=2] [text_button]`
 - Slash Usage: `/rolesbuttons add <message> <role> <emoji> [style_button=2] [text_button]`
 - Aliases: `+`
 - Checks: `server_only`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.rolesbuttons list (Hybrid Command)
List all roles-buttons of this server or display the settings for a specific one.<br/>
 - Usage: `s.rolesbuttons list [message=None]`
 - Slash Usage: `/rolesbuttons list [message=None]`
 - Checks: `server_only`
## s.rolesbuttons mode (Hybrid Command)
Choose a mode for the roles-buttons of a message.<br/>

Mode `add_or_remove`:<br/>
- Users get the role if they do not already have it, or lose it.<br/>
Mode `add_only`:<br/>
- Users can only get the role, but only manual action will remove it.<br/>
Mode `remove_only`:<br/>
- Users can only lose a role, and will not be able to get it again without a manual action.<br/>
Mode `replace`:<br/>
- Same as `add_or_remove`, but the roles from this message will be mutually exclusive, and getting one will remove the previous.<br/>
 - Usage: `s.rolesbuttons mode <message> <mode>`
 - Slash Usage: `/rolesbuttons mode <message> <mode>`
 - Checks: `server_only`
## s.rolesbuttons clear (Hybrid Command)
Clear all roles-buttons for a message.<br/>
 - Usage: `s.rolesbuttons clear <message>`
 - Slash Usage: `/rolesbuttons clear <message>`
 - Checks: `server_only`
## s.rolesbuttons create (Hybrid Command)

 - Usage: `s.rolesbuttons create <channel> <roles_buttons>`
 - Slash Usage: `/rolesbuttons create <channel> <roles_buttons>`
 - Aliases: `direct`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
