# s.infochannel
Toggle info channel for this server<br/>
 - Usage: `s.infochannel`
 - Restricted to: `ADMIN`
# s.infochannelset
Toggle different types of infochannels<br/>
 - Usage: `s.infochannelset`
 - Restricted to: `ADMIN`
 - Aliases: `icset`
## s.infochannelset name
Change the name of the infochannel for the specified channel type.<br/>

{count} must be used to display number of total members in the server.<br/>
Leave blank to set back to default.<br/>

Examples:<br/>
- `s.infochannelset name members Cool Cats: {count}`<br/>
- `s.infochannelset name bots {count} Robot Overlords`<br/>

Valid Types are:<br/>
- `members`: Total members on the server<br/>
- `humans`: Total members that aren't bots<br/>
- `boosters`: Total amount of boosters<br/>
- `bots`: Total bots<br/>
- `roles`: Total number of roles<br/>
- `channels`: Total number of channels excluding infochannels<br/>
- `online`: Total online members<br/>
- `offline`: Total offline members<br/>

Warning: This command counts against the channel update rate limit and may be queued.<br/>
 - Usage: `s.infochannelset name <channel_type> [text]`
Extended Arg Info
> ### channel_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.infochannelset togglerole
Toggle an infochannel that shows the count of users with the specified role<br/>
 - Usage: `s.infochannelset togglerole <role> [enabled=None]`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### enabled: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.infochannelset togglechannel
Toggles the infochannel for the specified channel type.<br/>

Valid Types are:<br/>
- `members`: Total members on the server<br/>
- `humans`: Total members that aren't bots<br/>
- `boosters`: Total amount of boosters<br/>
- `bots`: Total bots<br/>
- `roles`: Total number of roles<br/>
- `channels`: Total number of channels excluding infochannels,<br/>
- `online`: Total online members,<br/>
- `offline`: Total offline members,<br/>
 - Usage: `s.infochannelset togglechannel <channel_type> [enabled=None]`
Extended Arg Info
> ### channel_type: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### enabled: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.infochannelset rolename
Change the name of the infochannel for specific roles.<br/>

{count} must be used to display number members with the given role.<br/>
{role} can be used for the roles name.<br/>
Leave blank to set back to default.<br/>

Default is set to: `{role}: {count}`<br/>

Examples:<br/>
- `s.infochannelset rolename @Patrons {role}: {count}`<br/>
- `s.infochannelset rolename Elite {count} members with {role} role`<br/>
- `s.infochannelset rolename "Space Role" Total boosters: {count}`<br/>

Warning: This command counts against the channel update rate limit and may be queued.<br/>
 - Usage: `s.infochannelset rolename <role> [text]`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### text=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
