# s.lockdown
Enables lockdown for this server<br/>

A profile ID must be specified. To list profiles,<br/>
do `s.lockdownset listprofiles`<br/>
 - Usage: `s.lockdown <profile>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### profile: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.unlockdown
Ends the lockdown for this server<br/>
 - Usage: `s.unlockdown`
 - Restricted to: `MOD`
 - Checks: `server_only`
# s.lockdownset
Settings for lockdown<br/>
 - Usage: `s.lockdownset`
 - Restricted to: `MOD`
 - Checks: `server_only`
## s.lockdownset reset
Removes all lockdown profiles for the current server.<br/>
 - Usage: `s.lockdownset reset`
 - Restricted to: `GUILD_OWNER`
## s.lockdownset addprofile
Adds a lockdown profile.<br/>

Role is the role to be applied when triggering a lockdown<br/>
with this profile.<br/>
 - Usage: `s.lockdownset addprofile <role>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.lockdownset listprofiles
List all lockdown profiles for the server.<br/>
 - Usage: `s.lockdownset listprofiles`
## s.lockdownset removeprofile
Removes the lockdown profile with the specified IDs<br/>

To see a list of profiles and their IDs,<br/>
do `s.lockdownset listprofiles`<br/>
 - Usage: `s.lockdownset removeprofile <profile_id>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### profile_id: int
> ```
> A number without decimal places.
> ```
