# s.adventurealert (Hybrid Command)
Set notifications for all adventures<br/>
 - Usage: `s.adventurealert`
 - Slash Usage: `/adventurealert`
## s.adventurealert settings (Hybrid Command)
Shows a list of servers you have alerts<br/>
 - Usage: `s.adventurealert settings`
 - Slash Usage: `/adventurealert settings`
 - Aliases: `setting`
## s.adventurealert global (Hybrid Command)
Toggle adventure notifications in all shared servers<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `s.adventurealert global [alert_style=None]`
 - Slash Usage: `/adventurealert global [alert_style=None]`
## s.adventurealert role (Hybrid Command)
Add or remove a role to be pinged when a dragon appears<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `s.adventurealert role [alert_style=None] <role>`
 - Slash Usage: `/adventurealert role [alert_style=None] <role>`
 - Restricted to: `MOD`
 - Aliases: `roles`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.adventurealert removeuser (Hybrid Command)
Remove a specific user ID from adventure alerts<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `s.adventurealert removeuser <user_id> [alert_style=None]`
 - Slash Usage: `/adventurealert removeuser <user_id> [alert_style=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
## s.adventurealert removeall (Hybrid Command)
Remove all adventurealert settings in all servers<br/>
 - Usage: `s.adventurealert removeall`
 - Slash Usage: `/adventurealert removeall`
## s.adventurealert toggle (Hybrid Command)
Toggle adventure notifications in this server<br/>

`alert_style` - Must be one of:<br/>
    - `adventure` (default)<br/>
    - `boss` or `dragon`<br/>
    - `cart`<br/>
    - `immortal`<br/>
    - `miniboss`<br/>
    - `possessed`<br/>
    - `ascended`<br/>
    - `transcended`<br/>
 - Usage: `s.adventurealert toggle [alert_style=None]`
 - Slash Usage: `/adventurealert toggle [alert_style=None]`
 - Aliases: `user, users, remove, rem, and add`
 - Checks: `server_only`
