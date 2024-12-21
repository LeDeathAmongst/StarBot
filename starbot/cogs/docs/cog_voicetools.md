# s.voicetools
Settings for voice tools.<br/>
 - Usage: `s.voicetools`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.voicetools vip
Settings for VIP module.<br/>

Set members and roles to not count to user limit in voice channel<br/>
(limit will be raised accordingly after they join to make it possible)<br/>
 - Usage: `s.voicetools vip`
### s.voicetools vip list
Shows vip list of VIP module.<br/>

Members and roles specified here will not count to user limit in voice channel.<br/>
 - Usage: `s.voicetools vip list`
### s.voicetools vip add
Adds members and roles to vip list of VIP module.<br/>

VIP members and roles will not count to user limit in voice channel.<br/>
 - Usage: `s.voicetools vip add <vips>`
### s.voicetools vip remove
Removes members and roles to vip list of VIP module.<br/>

VIP members and roles will not count to user limit in voice channel.<br/>
 - Usage: `s.voicetools vip remove <vips>`
### s.voicetools vip enable
Enables VIP module.<br/>
 - Usage: `s.voicetools vip enable`
### s.voicetools vip disable
Disables VIP module.<br/>
 - Usage: `s.voicetools vip disable`
## s.voicetools forcelimit
Settings for ForceLimit module.<br/>

Force user limit to all members of the server including admins<br/>
(Kicking is done the same way as in `s.voicekick`)<br/>

When combined with VIP module, this won't kick VIPs going over limit<br/>
You can also add user or role to this module's ignore list,<br/>
if you want to ignore going over limit while not raising user limit for channel<br/>
or you can ignore chosen channels to stop bot from kicking users from it.<br/>
 - Usage: `s.voicetools forcelimit`
### s.voicetools forcelimit enable
Enables ForceLimit module.<br/>
 - Usage: `s.voicetools forcelimit enable`
### s.voicetools forcelimit disable
Disables ForceLimit module.<br/>
 - Usage: `s.voicetools forcelimit disable`
### s.voicetools forcelimit unignore
Adds members, roles or voice channels to ignorelist of ForceLimit module<br/>

Members and roles on ignorelist will bypass forcelimit<br/>
(meaning - not getting kicked)<br/>

Voice channels on ignorelist won't be checked<br/>
(as if ForceLimit module was disabled for them)<br/>
 - Usage: `s.voicetools forcelimit unignore <ignores>`
### s.voicetools forcelimit ignorelist
Shows ignorelist of ForceLimit module.<br/>

This can include members and roles which bypass forcelimit<br/>
and voice channels which won't be checked.<br/>
 - Usage: `s.voicetools forcelimit ignorelist`
### s.voicetools forcelimit ignore
Adds members, roles or voice channels to ignorelist of ForceLimit module.<br/>

Members and roles on ignorelist will bypass forcelimit<br/>
(meaning - not getting kicked)<br/>

Voice channels on ignorelist won't be checked<br/>
(as if ForceLimit module was disabled for them)<br/>
 - Usage: `s.voicetools forcelimit ignore <ignores>`
