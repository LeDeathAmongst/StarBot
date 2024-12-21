# s.dps
Dont ping staff.<br/>
 - Usage: `s.dps`
 - Restricted to: `ADMIN`
## s.dps action
Choose none, kick, ban, mute, addroles, removeroles as the action.<br/>
 - Usage: `s.dps action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.dps toggle
Toggle the module.<br/>
 - Usage: `s.dps toggle`
## s.dps message
Set the message to be sent to the user.<br/>
 - Usage: `s.dps message <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.dps staffrole
Command for managing the staff role.<br/>
 - Usage: `s.dps staffrole`
### s.dps staffrole add
Add a role to the staff role.<br/>
 - Usage: `s.dps staffrole add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.dps staffrole list
List the staff roles.<br/>
 - Usage: `s.dps staffrole list`
### s.dps staffrole remove
Remove a role from the staff role.<br/>
 - Usage: `s.dps staffrole remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.dps scope
Set the scope of the module.<br/>

**Scope**<br/>
- `server` - Enable DPS __**server-wide**__ by passing **server**.<br/>
- `category` - Enable DPS for a specific category by passing its **category ID**.<br/>
- `channel` - Enable DPS for a specific channel by passing its **channel ID**.<br/>

**Note**: You can specify multiple categories and channels, separated **by a space**. Running the command again will **override** the previous configuration.<br/>

**Example**<br/>
- To enable DPS for **specific channels**, **categories**, or a **mix of both**: `dps scope 123456789 123456789 123456789`<br/>
 - Usage: `s.dps scope <scope>`
 - Restricted to: `ADMIN`
## s.dps removeroles
Manage roles to be removed from the user.<br/>
 - Usage: `s.dps removeroles`
### s.dps removeroles list
List the roles to be removed from the user.<br/>
 - Usage: `s.dps removeroles list`
### s.dps removeroles remove
Remove a role from being removed from the user.<br/>
 - Usage: `s.dps removeroles remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.dps removeroles add
Add a role to be removed from the user.<br/>
 - Usage: `s.dps removeroles add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.dps per
Set how long to wait between actions.<br/>
 - Usage: `s.dps per <time>`
## s.dps amount
Set how many pings are needed to trigger an action.<br/>
 - Usage: `s.dps amount <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## s.dps settings
Show the current settings.<br/>
 - Usage: `s.dps settings`
## s.dps muterole
Set a role to be used for muting.<br/>
 - Usage: `s.dps muterole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.dps whitelist
Manage whitelist.<br/>
 - Usage: `s.dps whitelist`
 - Aliases: `ignore`
### s.dps whitelist add
Add users/roles/channels to the whitelist.<br/>
 - Usage: `s.dps whitelist add`
#### s.dps whitelist add user
Add users to the whitelist.<br/>
 - Usage: `s.dps whitelist add user [users=None]`
#### s.dps whitelist add channel
Add channels to the whitelist.<br/>
 - Usage: `s.dps whitelist add channel [channels=None]`
#### s.dps whitelist add role
Add roles to the whitelist.<br/>
 - Usage: `s.dps whitelist add role [roles=None]`
### s.dps whitelist remove
Remove users/roles/channels from the whitelist.<br/>
 - Usage: `s.dps whitelist remove`
#### s.dps whitelist remove user
Remove users from the whitelist.<br/>
 - Usage: `s.dps whitelist remove user [users=None]`
#### s.dps whitelist remove role
Remove roles from the whitelist.<br/>
 - Usage: `s.dps whitelist remove role [roles=None]`
#### s.dps whitelist remove channel
Remove channels from the whitelist.<br/>
 - Usage: `s.dps whitelist remove channel [channels=None]`
## s.dps addroles
Manage roles to be added to the user.<br/>
 - Usage: `s.dps addroles`
### s.dps addroles add
Add a role to be added to the user.<br/>
 - Usage: `s.dps addroles add <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.dps addroles remove
Remove a role from being added to the user.<br/>
 - Usage: `s.dps addroles remove <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.dps addroles list
List the roles to be added to the user.<br/>
 - Usage: `s.dps addroles list`
