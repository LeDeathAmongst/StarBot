# s.boosterrole
Manage booster roles<br/>
 - Usage: `s.boosterrole`
 - Aliases: `boosterroles`
 - Checks: `server_only`
## s.boosterrole setconfig
Set the configuration for the booster role<br/>

This command uses flags to set the configuration for the booster role.<br/>
The syntax of a flag is:<br/>
`flagname: value`<br/>

The available flags are:<br/>
- `above`: The role above which the booster role should be placed<br/>
- `name`: The name of the booster role<br/>
- `color`: The color of the booster role<br/>
- `hoist`: Whether the booster role should be hoisted<br/>
- `mentionable`: Whether the booster role should be mentionable<br/>
 - Usage: `s.boosterrole setconfig <flags>`
 - Restricted to: `ADMIN`
## s.boosterrole assign
Assign the booster role to yourself<br/>
 - Usage: `s.boosterrole assign`
 - Cooldown: `1 per 180.0 seconds`
 - Checks: `bot_has_server_permissions`
## s.boosterrole setthreshold
Set the number of boosts required to receive the booster role<br/>
 - Usage: `s.boosterrole setthreshold <threshold>`
 - Restricted to: `ADMIN`
 - Aliases: `setboostreq and threshold`
## s.boosterrole unassign
Unassign the booster role from yourself<br/>
 - Usage: `s.boosterrole unassign [member=operator.attrgetter('author')]`
 - Cooldown: `1 per 180.0 seconds`
 - Checks: `bot_has_server_permissions`
Extended Arg Info
> ### member: discord.member.Member = operator.attrgetter('author')
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
## s.boosterrole setboosts
Set the number of boosts for a member incase they are wrongly shown in `s.showboosts`<br/>
 - Usage: `s.boosterrole setboosts <member> <count>`
 - Restricted to: `ADMIN`
 - Aliases: `setboostcount`
Extended Arg Info
> ### member: discord.member.Member
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
> ### count: int
> ```
> A number without decimal places.
> ```
## s.boosterrole purgeroles
Purge all booster roles in the server<br/>
 - Usage: `s.boosterrole purgeroles`
 - Restricted to: `ADMIN`
## s.boosterrole disallowproperties
Disallow certain properties from being edited by users<br/>
 - Usage: `s.boosterrole disallowproperties <properties>`
 - Aliases: `disallow`
## s.boosterrole listboosters
List all boosters in the server<br/>
 - Usage: `s.boosterrole listboosters`
 - Aliases: `boosters`
## s.boosterrole showsettings
Show the current booster role settings<br/>
 - Usage: `s.boosterrole showsettings`
 - Aliases: `settings and ss`
## s.boosterrole getconfig
Get the configuration for the booster role<br/>
 - Usage: `s.boosterrole getconfig`
 - Restricted to: `ADMIN`
## s.boosterrole showboosts
Show the number of boosts a member has<br/>
 - Usage: `s.boosterrole showboosts <member>`
 - Aliases: `boosts`
Extended Arg Info
> ### member: discord.member.Member
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
## s.boosterrole list
List all booster roles in the server<br/>
 - Usage: `s.boosterrole list`
## s.boosterrole rolelimit
Set the maximum number of booster roles allowed in the server<br/>
 - Usage: `s.boosterrole rolelimit <limit>`
 - Restricted to: `ADMIN`
## s.boosterrole myrole
View your booster role settings<br/>
 - Usage: `s.boosterrole myrole`
 - Aliases: `mine`
### s.boosterrole myrole edit
Edit your booster role<br/>

This command uses flags to configure or view your booster role.<br/>
The syntax of a flag is:<br/>
`flagname: value`<br/>

The available flags are:<br/>

- `name`: The name of the booster role<br/>
- `color`: The color of the booster role<br/>
- `hoist`: Whether the booster role should be hoisted<br/>
- `mentionable`: Whether the booster role should be mentionable<br/>
- `icon`: The icon of the booster role. valid values for this are: `attachment` or  an emoji<br/>

    (If `attachment` is used the bot will read the image from the first attachment)<br/>

For example:<br/>
`s.boosterrole myrole edit color: red icon: 🎉`<br/>
`s.boosterrole myrole edit icon: attachment`<br/>
`s.boosterrole myrole edit hoist: true`<br/>

If no flags are provided, the current configuration will be displayed.<br/>
 - Usage: `s.boosterrole myrole edit <flags>`
 - Cooldown: `1 per 180.0 seconds`
