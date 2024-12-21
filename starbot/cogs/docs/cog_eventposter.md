# s.event (Hybrid Command)
All event related commands.<br/>
 - Usage: `s.event`
 - Slash Usage: `/event`
 - Checks: `server_only`
## s.event ping (Hybrid Command)
Ping all the registered users for your event including optional message<br/>

`[include_maybe=True]` either `true` or `false` to include people who registered as maybe.<br/>
`[message]` Optional message to include with the ping.<br/>
 - Usage: `s.event ping [include_maybe=True] [message]`
 - Slash Usage: `/event ping [include_maybe=True] [message]`
 - Aliases: `mention`
 - Checks: `server_only`
Extended Arg Info
> ### include_maybe: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### message: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.event edit (Hybrid Command)
Edit various things in events<br/>
 - Usage: `s.event edit`
 - Slash Usage: `/event edit`
 - Checks: `server_only`
### s.event edit maybeadd (Hybrid Command)
Add members to your events maybe list<br/>

`[new_members...]` The members you want to add to your event<br/>
 - Usage: `s.event edit maybeadd <new_members>`
 - Slash Usage: `/event edit maybeadd <new_members>`
 - Checks: `server_only`
### s.event edit memberremove (Hybrid Command)
Remove members from your event (hopefully not against their will)<br/>

`[members...]` The members you want to add to your event<br/>
 - Usage: `s.event edit memberremove <members>`
 - Slash Usage: `/event edit memberremove <members>`
 - Aliases: `memberrem`
 - Checks: `server_only`
### s.event edit slots (Hybrid Command)
Edit the number of slots available for your event<br/>

`<new_slots>` The number of available slots for your events activity<br/>
 - Usage: `s.event edit slots [new_slots=None]`
 - Slash Usage: `/event edit slots [new_slots=None]`
 - Checks: `server_only`
Extended Arg Info
> ### new_slots: Optional[int] = None
> ```
> A number without decimal places.
> ```
### s.event edit mayberemove (Hybrid Command)
Remove members from your events maybe list<br/>

`[members...]` The members you want to remove from your event<br/>
 - Usage: `s.event edit mayberemove <members>`
 - Slash Usage: `/event edit mayberemove <members>`
 - Aliases: `mayberem`
 - Checks: `server_only`
### s.event edit memberadd (Hybrid Command)
Add members to your event (hopefully not against their will)<br/>

`[new_members...]` The members you want to add to your event<br/>
 - Usage: `s.event edit memberadd <new_members>`
 - Slash Usage: `/event edit memberadd <new_members>`
 - Checks: `server_only`
### s.event edit remaining (Hybrid Command)
Show how long until your event will be automatically ended if available.<br/>
 - Usage: `s.event edit remaining`
 - Slash Usage: `/event edit remaining`
 - Checks: `server_only`
### s.event edit title (Hybrid Command)
Edit the title of your event<br/>

`<new_description>` The new description for your event<br/>
 - Usage: `s.event edit title <new_description>`
 - Slash Usage: `/event edit title <new_description>`
 - Checks: `server_only`
Extended Arg Info
> ### new_description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.event make (Hybrid Command)
Create an event<br/>

`[members...]` Add members already in the event you want to host.<br/>
`[max_slots=None]` Specify maximum number of Slots the event can have, default is no limit.<br/>
`<description>` provide a description for the event you're hosting.<br/>
With custom keyword links setup this will add an image to the events thumbnail<br/>
after being approved by an admin.<br/>

If a date or time is provided the timestamp in the event will try to display<br/>
the correct time for everyone. For example `s.event Deep Stone Crypt Sunday at 9PM MDT`<br/>
will convert the "sunday at 9PM MDT" into a converted timestamp for everyone removing<br/>
the need to know what MDT is in their own time.<br/>
This also works for times relative to now, e.g. `s.event Last Wish in 3 hours`<br/>
will add the timestamp display in 3 hours from the time this message is posted.<br/>

Note: If a timezone is provided it must be the correct timezone according to<br/>
daylight savings time. For example PST time may sometimes be UTC+8 in which case<br/>
PDT must be used instead.<br/>
 - Usage: `s.event make [members=None] [max_slots=None] <description>`
 - Slash Usage: `/event make [members=None] [max_slots=None] <description>`
 - Checks: `server_only`
Extended Arg Info
> ### max_slots: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.event show (Hybrid Command)
Show current event being run by a member<br/>
 - Usage: `s.event show [member=None]`
 - Slash Usage: `/event show [member=None]`
 - Checks: `server_only`
Extended Arg Info
> ### member: discord.member.Member = None
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
## s.event clear (Hybrid Command)
Delete a stored event so you can create more<br/>

`[clear]` yes/no to clear your current running event.<br/>
 - Usage: `s.event clear [clear=False]`
 - Slash Usage: `/event clear [clear=False]`
 - Aliases: `end`
 - Checks: `server_only`
Extended Arg Info
> ### clear: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.event leave (Hybrid Command)
Leave an event being hosted<br/>
 - Usage: `s.event leave <hoster>`
 - Slash Usage: `/event leave <hoster>`
 - Checks: `server_only`
Extended Arg Info
> ### hoster: discord.member.Member
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
## s.event set (Hybrid Command)
Manage server specific settings for events<br/>
 - Usage: `s.event set`
 - Slash Usage: `/event set`
 - Checks: `server_only`
### s.event set links (Hybrid Command)
Set the custom thumbnail for events<br/>

`<keyword>` is the word that will be searched for in event titles.<br/>
`<link>` needs to be an image link to be used for the thumbnail when the keyword<br/>
is found in the event title.<br/>
 - Usage: `s.event set links <keyword> <link>`
 - Slash Usage: `/event set links <keyword> <link>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### keyword: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.event set defaultmax (Hybrid Command)
Set's the servers default maximum slots<br/>

`[max_slots]` The maximum number of slots allowed by default for events.<br/>
 - Usage: `s.event set defaultmax [max_slots=None]`
 - Slash Usage: `/event set defaultmax [max_slots=None]`
 - Restricted to: `MOD`
 - Aliases: `max`
 - Checks: `server_only`
Extended Arg Info
> ### max_slots: Optional[int] = None
> ```
> A number without decimal places.
> ```
### s.event set cleanup (Hybrid Command)
Set the events cleanup interval.<br/>

`[time]` How long events should be allowed to live before being<br/>
automatically ended.<br/>

Note: If there is a timestamp for the event, the cleanup interval<br/>
will check since the timestamp. If not it will check time after the event<br/>
has been posted. Timestamp can be seen from the events embed.<br/>
 - Usage: `s.event set cleanup [time]`
 - Slash Usage: `/event set cleanup [time]`
 - Restricted to: `MOD`
 - Checks: `server_only`
### s.event set class (Hybrid Command)
Set's the users default player class. If nothing is provided this will be rest.<br/>

`[player_class]` Your desired playerclass for events. This is listed<br/>
next to your name when you register for an event. If this is changed<br/>
during an event you have signed up for if the event updates with new<br/>
members or changes in any way the event will reflect this change.<br/>
 - Usage: `s.event set class [player_class]`
 - Slash Usage: `/event set class [player_class]`
 - Checks: `server_only`
Extended Arg Info
> ### player_class: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.event set approvalchannel (Hybrid Command)
Set the admin approval channel<br/>

`[channel]` The channel you have restricted to people you trust to approve events.<br/>
If no channel is provided this will be reset.<br/>

Note: This is required unless bypass has been enabled.<br/>
 - Usage: `s.event set approvalchannel [channel=None]`
 - Slash Usage: `/event set approvalchannel [channel=None]`
 - Restricted to: `MOD`
 - Aliases: `adminchannel`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.event set largelinks (Hybrid Command)
Set the custom embed image for events<br/>

`<keyword>` is the word that will be searched for in event titles.<br/>
`<link>` needs to be an image link to be used for the thumbnail when the keyword<br/>
is found in the event title.<br/>
 - Usage: `s.event set largelinks <keyword> <link>`
 - Slash Usage: `/event set largelinks <keyword> <link>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### keyword: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.event set viewlinks (Hybrid Command)
Show custom thumbnails available for events in this server<br/>
 - Usage: `s.event set viewlinks`
 - Slash Usage: `/event set viewlinks`
 - Restricted to: `MOD`
 - Aliases: `showlinks`
 - Checks: `server_only`
### s.event set thread (Hybrid Command)
Set whether or not to turn the announcement message into a thread<br/>
for people to join and discuss in.<br/>

`<true_or_false>` `True` or `False` whether or not to allow events<br/>
to bypass admin approval.<br/>
 - Usage: `s.event set thread <true_or_false>`
 - Slash Usage: `/event set thread <true_or_false>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.event set viewlargelinks (Hybrid Command)
Show custom images available for events in this server<br/>
 - Usage: `s.event set viewlargelinks`
 - Slash Usage: `/event set viewlargelinks`
 - Restricted to: `MOD`
 - Aliases: `showlargelinks`
 - Checks: `server_only`
### s.event set ping (Hybrid Command)
Set the ping to use when an event is announced<br/>

`[everyone=False]` True or False, whether to include everyone ping.<br/>
`[here=False]` True or False, whether to include here ping.<br/>
`[role...]` Is the role(s) you want to add to the list of pinged roles when<br/>
an event is created.<br/>

If you want to ping here but not everyone you would do something like:<br/>
 - `s.event set ping false true`<br/>

If you just want to set a few roles you can do:<br/>
 - `s.event set ping @role1 @role2`<br/>
 - Usage: `s.event set ping [everyone=False] [here=False] [roles=()]`
 - Slash Usage: `/event set ping [everyone=False] [here=False] [roles=()]`
 - Restricted to: `MOD`
 - Aliases: `mention`
 - Checks: `server_only`
Extended Arg Info
> ### everyone: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### here: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.event set removeplayerclass (Hybrid Command)
Remove a playerclass choice for users to pick from on this server.<br/>

`<player_class>` The name of the playerclass you want to remove.<br/>
 - Usage: `s.event set removeplayerclass <player_class>`
 - Slash Usage: `/event set removeplayerclass <player_class>`
Extended Arg Info
> ### player_class: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.event set settings (Hybrid Command)
Show the current event settings.<br/>
 - Usage: `s.event set settings`
 - Slash Usage: `/event set settings`
 - Checks: `server_only`
### s.event set remove (Hybrid Command)
Remove and end a current event.<br/>

`<hoster>` The member who is hosting the event.<br/>
 - Usage: `s.event set remove <hoster>`
 - Slash Usage: `/event set remove <hoster>`
 - Restricted to: `MOD`
 - Aliases: `rem`
 - Checks: `server_only`
Extended Arg Info
> ### hoster: discord.member.Member
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
### s.event set channel (Hybrid Command)
Set the Announcement channel for events<br/>

`[channel]` The channel events will be sent to. Providing no input will<br/>
clear the channel.<br/>

If no channel is set events cannot be created.<br/>
 - Usage: `s.event set channel [channel=None]`
 - Slash Usage: `/event set channel [channel=None]`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.event set bypass (Hybrid Command)
Set whether or not admin approval is required for events to be posted.<br/>

`<true_or_false>` `True` or `False` whether or not to allow events<br/>
to bypass admin approval.<br/>
 - Usage: `s.event set bypass <true_or_false>`
 - Slash Usage: `/event set bypass <true_or_false>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.event set roles (Hybrid Command)
Set the roles that are allowed to create events<br/>

`[roles...]` the role(s) that are allowed to create events. If not provided,<br/>
there will be no restriction on who can create an event.<br/>
 - Usage: `s.event set roles <role>`
 - Slash Usage: `/event set roles <role>`
 - Restricted to: `MOD`
 - Aliases: `role`
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
### s.event set listplayerclass (Hybrid Command)
List the playerclass choices in this server.<br/>
 - Usage: `s.event set listplayerclass`
 - Slash Usage: `/event set listplayerclass`
### s.event set addplayerclass (Hybrid Command)
Add a playerclass choice for users to pick from on this server.<br/>

`[emoji]` Can be any emoji and is used on the drop down selector to<br/>
help distinguish the classes.<br/>
`<player_class>` The name of the player class you want to have<br/>
as a server option.<br/>

Note: There is a maximum of 25 classes you can add. The class name<br/>
can also only be a maximum of 100 characters.<br/>
 - Usage: `s.event set addplayerclass [emoji=None] <player_class>`
 - Slash Usage: `/event set addplayerclass [emoji=None] <player_class>`
Extended Arg Info
> ### emoji: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### player_class: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.event join (Hybrid Command)
Join an event being hosted<br/>
 - Usage: `s.event join <hoster>`
 - Slash Usage: `/event join <hoster>`
 - Checks: `server_only`
Extended Arg Info
> ### hoster: discord.member.Member
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
