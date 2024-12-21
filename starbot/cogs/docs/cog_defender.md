# s.dset
Defender system settings<br/>
 - Usage: `s.dset`
 - Restricted to: `ADMIN`
 - Aliases: `defset`
 - Checks: `server_only`
## s.dset rank3
Rank 3 configuration<br/>

See s.defender status for more information about this rank<br/>
 - Usage: `s.dset rank3`
 - Restricted to: `ADMIN`
### s.dset rank3 joineddays
Days since join required to be considered Rank 3<br/>
 - Usage: `s.dset rank3 joineddays <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
### s.dset rank3 minmessages
Minimum messages required to reach Rank 3<br/>
 - Usage: `s.dset rank3 minmessages <messages>`
Extended Arg Info
> ### messages: int
> ```
> A number without decimal places.
> ```
## s.dset silence
Silence manual module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset silence`
 - Restricted to: `ADMIN`
### s.dset silence enable
Toggle silence manual module<br/>
 - Usage: `s.dset silence enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.dset voteout
Voteout manual module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset voteout`
 - Restricted to: `ADMIN`
### s.dset voteout rank
Sets target rank<br/>
 - Usage: `s.dset voteout rank <rank>`
Extended Arg Info
> ### rank: int
> ```
> A number without decimal places.
> ```
### s.dset voteout wipe
Sets how many days worth of messages to delete if the action is ban<br/>

Setting 0 will not delete any message<br/>
 - Usage: `s.dset voteout wipe <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
### s.dset voteout enable
Toggles voteout<br/>
 - Usage: `s.dset voteout enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset voteout votes
Sets required votes number for it to pass<br/>
 - Usage: `s.dset voteout votes <votes>`
Extended Arg Info
> ### votes: int
> ```
> A number without decimal places.
> ```
### s.dset voteout action
Sets action (ban, kick, softban, punish)<br/>
 - Usage: `s.dset voteout action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.dset general
Defender general settings<br/>
 - Usage: `s.dset general`
 - Restricted to: `ADMIN`
### s.dset general reset
Resets Defender configuration for this server<br/>
 - Usage: `s.dset general reset [confirmation=False]`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset general countmessages
Toggles message count (and rank 4)<br/>
 - Usage: `s.dset general countmessages <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset general punishmessage
Sets the messages that I will send after assigning the punish role<br/>

Supports context variables. You can add the following to your message:<br/>
$user -> User's name + tag<br/>
$user_name -> User's name<br/>
$user_display -> User's nickname if set or user's name<br/>
$user_id -> User's id<br/>
$user_mention -> User's mention<br/>
$user_nickname -> User's nickname if set or 'None'<br/>
 - Usage: `s.dset general punishmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset general punishrole
Sets the role that will be assigned to misbehaving users<br/>

Note: this will only be assigned if the 'action' of a module<br/>
is set to 'punish'.<br/>
 - Usage: `s.dset general punishrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.dset general notifyrole
Sets the role that will be pinged in case of alerts<br/>
 - Usage: `s.dset general notifyrole <role>`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.dset general notifychannel
Sets the channel where notifications will be sent<br/>

This channel should preferably be staff readable only as it could<br/>
potentially contain sensitive info<br/>
 - Usage: `s.dset general notifychannel <channel>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.dset general enable
Toggle defender system<br/>
 - Usage: `s.dset general enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset general trustedroles
Sets the trusted roles<br/>

Users belonging to this role will be classified as Rank 1<br/>
 - Usage: `s.dset general trustedroles <roles>`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.dset general helperroles
Sets the helper roles<br/>

See s.defender status for more information about these roles<br/>
 - Usage: `s.dset general helperroles <roles>`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.dset importfrom
Import the configuration from another server<br/>

This is permitted only if the command issuer is admin in both servers<br/>
 - Usage: `s.dset importfrom <server>`
## s.dset vaporize
Vaporize manual module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset vaporize`
 - Restricted to: `ADMIN`
### s.dset vaporize enable
Toggle vaporize manual module<br/>
 - Usage: `s.dset vaporize enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset vaporize maxtargets
Sets the maximum amount of targets (1-999)<br/>

By default only a maximum of 15 users can be vaporized at once<br/>
 - Usage: `s.dset vaporize maxtargets <max_targets>`
Extended Arg Info
> ### max_targets: int
> ```
> A number without decimal places.
> ```
## s.dset raiderdetection
Raider detection auto module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset raiderdetection`
 - Restricted to: `ADMIN`
 - Aliases: `rd`
### s.dset raiderdetection messages
Sets messages (User posted X messages in Y minutes)<br/>
 - Usage: `s.dset raiderdetection messages <messages>`
Extended Arg Info
> ### messages: int
> ```
> A number without decimal places.
> ```
### s.dset raiderdetection wdchecks
Implement advanced Warden based checks<br/>

Issuing this command with no arguments will show the current checks<br/>
Passing 'remove' will remove existing checks<br/>
 - Usage: `s.dset raiderdetection wdchecks [conditions]`
Extended Arg Info
> ### conditions: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset raiderdetection wipe
Sets how many days worth of messages to delete if the action is ban<br/>

Setting 0 will not delete any message<br/>
 - Usage: `s.dset raiderdetection wipe <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
### s.dset raiderdetection action
Sets action (ban, kick, softban, punish or none (notify only))<br/>
 - Usage: `s.dset raiderdetection action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset raiderdetection rank
Sets target rank<br/>
 - Usage: `s.dset raiderdetection rank <rank>`
Extended Arg Info
> ### rank: int
> ```
> A number without decimal places.
> ```
### s.dset raiderdetection minutes
Sets minutes (User posted X messages in Y minutes)<br/>
 - Usage: `s.dset raiderdetection minutes <minutes>`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```
### s.dset raiderdetection enable
Toggles raider detection<br/>
 - Usage: `s.dset raiderdetection enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.dset alert
Alert manual module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset alert`
 - Restricted to: `ADMIN`
### s.dset alert enable
Toggle alert manual module<br/>
 - Usage: `s.dset alert enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.dset commentanalysis
Comment analysis configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset commentanalysis`
 - Restricted to: `ADMIN`
 - Aliases: `ca`
### s.dset commentanalysis reason
Sets a reason for the action (modlog use)<br/>
 - Usage: `s.dset commentanalysis reason <reason>`
Extended Arg Info
> ### reason: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset commentanalysis deletemessage
Toggles whether to delete the offending message<br/>
 - Usage: `s.dset commentanalysis deletemessage <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset commentanalysis action
Sets action (ban, kick, softban, punish or none (notification only))<br/>
 - Usage: `s.dset commentanalysis action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset commentanalysis threshold
Sets the threshold that will trigger CA's action (20-100)<br/>
 - Usage: `s.dset commentanalysis threshold <threshold>`
Extended Arg Info
> ### threshold: int
> ```
> A number without decimal places.
> ```
### s.dset commentanalysis rank
Sets target rank<br/>
 - Usage: `s.dset commentanalysis rank <rank>`
Extended Arg Info
> ### rank: int
> ```
> A number without decimal places.
> ```
### s.dset commentanalysis attributes
Setup the attributes that CA will check<br/>
 - Usage: `s.dset commentanalysis attributes`
### s.dset commentanalysis wipe
Sets how many days worth of messages to delete if the action is ban<br/>

Setting 0 will not delete any message<br/>
 - Usage: `s.dset commentanalysis wipe <days>`
Extended Arg Info
> ### days: int
> ```
> A number without decimal places.
> ```
### s.dset commentanalysis wdchecks
Implement advanced Warden based checks<br/>

Issuing this command with no arguments will show the current checks<br/>
Passing 'remove' will remove existing checks<br/>
 - Usage: `s.dset commentanalysis wdchecks [conditions]`
Extended Arg Info
> ### conditions: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset commentanalysis token
Sets Perspective API token<br/>

https://developers.perspectiveapi.com/s/docs<br/>
 - Usage: `s.dset commentanalysis token <token>`
Extended Arg Info
> ### token: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset commentanalysis enable
Toggles comment analysis<br/>
 - Usage: `s.dset commentanalysis enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.dset invitefilter
Invite filter auto module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset invitefilter`
 - Restricted to: `ADMIN`
 - Aliases: `if`
### s.dset invitefilter wdchecks
Implement advanced Warden based checks<br/>

Issuing this command with no arguments will show the current checks<br/>
Passing 'remove' will remove existing checks<br/>
 - Usage: `s.dset invitefilter wdchecks [conditions]`
Extended Arg Info
> ### conditions: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset invitefilter deletemessage
Toggles whether to delete the invite's message<br/>
 - Usage: `s.dset invitefilter deletemessage <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset invitefilter excludeowninvites
Excludes this server's invites from the filter<br/>
 - Usage: `s.dset invitefilter excludeowninvites <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset invitefilter action
Sets action (ban, kick, softban, punish or none (deletion only))<br/>
 - Usage: `s.dset invitefilter action <action>`
Extended Arg Info
> ### action: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.dset invitefilter enable
Toggle invite filter<br/>
 - Usage: `s.dset invitefilter enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset invitefilter rank
Sets target rank<br/>
 - Usage: `s.dset invitefilter rank <rank>`
Extended Arg Info
> ### rank: int
> ```
> A number without decimal places.
> ```
## s.dset warden
Warden auto module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset warden`
 - Restricted to: `ADMIN`
 - Aliases: `wd`
### s.dset warden enable
Toggles warden<br/>
 - Usage: `s.dset warden enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.dset joinmonitor
Join monitor auto module configuration<br/>

See s.defender status for more information about this module<br/>
 - Usage: `s.dset joinmonitor`
 - Restricted to: `ADMIN`
 - Aliases: `jm`
### s.dset joinmonitor verificationlevel
Raises the server's verification level on raids<br/>

You can find a full description of Discord's verification levels in<br/>
the server's settings "Moderation" tab.<br/>

Verification levels:<br/>
0 - No action<br/>
1 - Low: verified email<br/>
2 - Medium: must be registered for longer than 5 minutes<br/>
3 - High: must be a member of this server for longer than 10 minutes<br/>
4 - Highest: must have a verified phone on their Discord account<br/>
 - Usage: `s.dset joinmonitor verificationlevel`
### s.dset joinmonitor notifynew
Enables notifications for users younger than X hours<br/>

Use 0 hours to disable notifications<br/>
 - Usage: `s.dset joinmonitor notifynew <hours>`
Extended Arg Info
> ### hours: int
> ```
> A number without decimal places.
> ```
### s.dset joinmonitor users
Sets users (X users joined in Y minutes)<br/>
 - Usage: `s.dset joinmonitor users <users>`
Extended Arg Info
> ### users: int
> ```
> A number without decimal places.
> ```
### s.dset joinmonitor enable
Toggles join monitor<br/>
 - Usage: `s.dset joinmonitor enable <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.dset joinmonitor minutes
Sets minutes (X users joined in Y minutes)<br/>
 - Usage: `s.dset joinmonitor minutes <minutes>`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```
### s.dset joinmonitor wdchecks
Implement advanced Warden based checks<br/>

Issuing this command with no arguments will show the current checks<br/>
Passing 'remove' will remove existing checks<br/>
 - Usage: `s.dset joinmonitor wdchecks [conditions]`
Extended Arg Info
> ### conditions: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.dset emergency
Emergency mode configuration<br/>

See s.defender status for more information about emergency mode<br/>
 - Usage: `s.dset emergency`
 - Restricted to: `ADMIN`
### s.dset emergency modules
Sets emergency modules<br/>

Emergency modules will be rendered available to helper roles<br/>
during emergency mode. Selecting no modules to this command will<br/>
disable emergency mode.<br/>
Available emergency modules: voteout, vaporize, silence<br/>
 - Usage: `s.dset emergency modules`
### s.dset emergency minutes
Sets max inactivity minutes for staff<br/>

After X minutes of inactivity following an alert emergency<br/>
mode will be engaged and helper roles will be able to use<br/>
the emergency modules.<br/>
 - Usage: `s.dset emergency minutes <minutes>`
Extended Arg Info
> ### minutes: int
> ```
> A number without decimal places.
> ```
# s.defender
Defender commands reserved to staff<br/>
 - Usage: `s.defender`
 - Restricted to: `MOD`
 - Aliases: `def`
 - Checks: `server_only`
## s.defender messages
Access recorded messages of users / channels<br/>
 - Usage: `s.defender messages`
 - Aliases: `msg`
### s.defender messages user
Shows recent messages of a user<br/>
 - Usage: `s.defender messages user <user>`
### s.defender messages exportuser
Exports recent messages of a user to a file<br/>
 - Usage: `s.defender messages exportuser <user>`
### s.defender messages exportchannel
Exports recent messages of a channel to a file<br/>
 - Usage: `s.defender messages exportchannel <channel>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.defender messages channel
Shows recent messages of a channel<br/>
 - Usage: `s.defender messages channel <channel>`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.defender status
Shows overall status of the Defender system<br/>
 - Usage: `s.defender status`
## s.defender updates
Shows all the past announcements of Defender<br/>
 - Usage: `s.defender updates`
## s.defender emergency
Manually engage or turn off emergency mode<br/>

Upon activation, staff will be pinged and any module<br/>
that is set to be active in emergency mode will be rendered<br/>
available to helpers<br/>
 - Usage: `s.defender emergency <on_or_off>`
Extended Arg Info
> ### on_or_off: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.defender warden
Warden rules management<br/>

See s.defender status for more information about Warden<br/>
 - Usage: `s.defender warden`
 - Restricted to: `ADMIN`
 - Aliases: `wd`
### s.defender warden add
Adds a new rule<br/>
 - Usage: `s.defender warden add <rule>`
Extended Arg Info
> ### rule: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.defender warden show
Shows a rule<br/>
 - Usage: `s.defender warden show <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.defender warden list
Lists existing rules<br/>
 - Usage: `s.defender warden list`
### s.defender warden removeall
Removes all rules<br/>
 - Usage: `s.defender warden removeall`
### s.defender warden memory
Shows or resets the memory of Warden<br/>

Can be filtered. Supports wildcards (* and ?)<br/>
 - Usage: `s.defender warden memory [keywords]`
Extended Arg Info
> ### keywords: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.defender warden debug
Simulate and give a detailed summary of an event<br/>

A Warden event must be passed with the proper target ID (user or local message)<br/>

When this command is issued all the rules registered to the event will be<br/>
processed in a safe way against the target, if any.<br/>
If the target satisfies the conditions, *only* the heatpoint related actions<br/>
will be carried on.<br/>
The heatpoint actions will be "sandboxed", so the newly added heatpoints won't<br/>
have any effect outside this test.<br/>
Remember that Warden evaluates each condition in order and stops at the first failed<br/>
root condition: the last condition that is listed in a failed rule is where Warden<br/>
stopped evaluating them.<br/>
If a valid Rank is also passed it will be used in place of the target's real<br/>
rank during the test.<br/>
See the documentation for a full list of Warden events.<br/>

Example:<br/>
s.def warden debug <valid_user_id> on-user-join<br/>
s.def warden debug <valid_message_id> on-message<br/>
s.def warden debug <valid_message_id> on-message-edit 3<br/>
 - Usage: `s.defender warden debug <_id> <event> [rank=None]`
Extended Arg Info
> ### _id: int
> ```
> A number without decimal places.
> ```
> ### rank: int = None
> ```
> A number without decimal places.
> ```
### s.defender warden find
Search for text in existing rules<br/>
 - Usage: `s.defender warden find <text>`
 - Aliases: `search`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.defender warden run
Runs a rule against the whole userbase<br/>

Confirmation is asked before execution.<br/>
 - Usage: `s.defender warden run <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.defender warden exportall
Sends all the rules as a tar.gz archive<br/>
 - Usage: `s.defender warden exportall`
### s.defender warden export
Sends the rule as a YAML file<br/>
 - Usage: `s.defender warden export <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.defender warden remove
Removes a rule by name<br/>
 - Usage: `s.defender warden remove <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.defender warden upload
Starts a rule upload session<br/>
 - Usage: `s.defender warden upload`
 - Cooldown: `1 per 86400.0 seconds`
## s.defender monitor
Shows recent events that might require your attention<br/>

Can be filtered. Supports wildcards (* and ?)<br/>
 - Usage: `s.defender monitor [keywords]`
Extended Arg Info
> ### keywords: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.defender freshmeat
Returns a list of the new users of the day<br/>

Can be filtered. Supports wildcards (* and ?)<br/>
 - Usage: `s.defender freshmeat [hours=24] [keywords]`
Extended Arg Info
> ### hours: int = 24
> ```
> A number without decimal places.
> ```
> ### keywords: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.defender notifynew
Sends you a DM if a user younger than X hours joins<br/>

Use 0 hours to disable notifications<br/>
 - Usage: `s.defender notifynew <hours>`
Extended Arg Info
> ### hours: int
> ```
> A number without decimal places.
> ```
## s.defender identify
Shows a member's rank + info<br/>
 - Usage: `s.defender identify <user>`
Extended Arg Info
> ### user: discord.member.Member
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
## s.defender memberranks
Counts how many members are in each rank<br/>
 - Usage: `s.defender memberranks`
# s.alert
Alert the staff members<br/>
 - Usage: `s.alert`
 - Aliases: `staff`
 - Cooldown: `1 per 120.0 seconds`
 - Checks: `server_only`
# s.vaporize
Gets rid of bad actors in a quick and silent way<br/>

Works only on Rank 3 and under<br/>
 - Usage: `s.vaporize <members>`
 - Checks: `server_only`
Extended Arg Info
> ### *members: discord.member.Member
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
# s.voteout
Initiates a vote to expel a user from the server<br/>

Can be used by members with helper roles during emergency mode<br/>
 - Usage: `s.voteout <user>`
 - Cooldown: `1 per 22.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### user: discord.member.Member
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
# s.silence
Enables server wide message autodeletion for the specified rank (and below)<br/>

Passing 0 will disable this.<br/>
 - Usage: `s.silence <rank>`
 - Checks: `server_only`
Extended Arg Info
> ### rank: int
> ```
> A number without decimal places.
> ```
