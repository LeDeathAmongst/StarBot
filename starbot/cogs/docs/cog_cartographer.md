# s.cartographer
Open the Backup/Restore menu<br/>

This cog can backup & restore the following:<br/>
- Bans (including reason)<br/>
- Categories (permissions/order)<br/>
- Text channels (permissions/order)<br/>
- Voice channels (permissions/order)<br/>
- Forum channels  (permissions/order)[Not forum posts]<br/>
- Roles (permissions/color/name/icon and what members they're assigned to)<br/>
- Emojis (name/roles, Very slow and rate limit heavy)<br/>
- Stickers (name/description, Very slow and rate limit heavy)<br/>
- Members (roles and nicknames)<br/>
- Messages (Optional, can be disabled)<br/>
- Server icon/banner/splash/discovery splash/description/name<br/>
- All server verification/security settings<br/>
 - Usage: `s.cartographer`
 - Aliases: `carto`
 - Checks: `server_only`
# s.cartographerset
Backup & Restore Tools<br/>
 - Usage: `s.cartographerset`
 - Aliases: `cartoset`
 - Checks: `server_only`
## s.cartographerset restorelatest
Restore the latest backup for this server<br/>
 - Usage: `s.cartographerset restorelatest`
## s.cartographerset backup
Create a backup of this server<br/>

limit: How many messages to backup per channel (0 for None)<br/>
 - Usage: `s.cartographerset backup [limit=0]`
Extended Arg Info
> ### limit: int = 0
> ```
> A number without decimal places.
> ```
