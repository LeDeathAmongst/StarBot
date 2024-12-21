# s.roletools
Commands for creating custom role settings<br/>
 - Usage: `s.roletools`
 - Checks: `server_only`
## s.roletools exclude
Set role exclusions<br/>
 - Usage: `s.roletools exclude`
 - Aliases: `exclusive`
### s.roletools exclude mutual
Allow setting roles mutually exclusive to eachother<br/>

This is equivalent to individually setting each roles exclusive roles to another<br/>
set of roles.<br/>

`[role...]` The roles you want to set as mutually exclusive.<br/>
 - Usage: `s.roletools exclude mutual <roles>`
 - Restricted to: `ADMIN`
### s.roletools exclude remove
Remove role exclusion<br/>

`<role>` This is the role a user may acquire you want to set exclusions for.<br/>
`<exclude>` The role(s) currently excluded you no longer wish to have excluded<br/>
 - Usage: `s.roletools exclude remove <role> <exclude>`
 - Restricted to: `ADMIN`
### s.roletools exclude add
Add role exclusion (This will remove if the designated role is acquired<br/>
if the included roles are not selfremovable they will not be removed<br/>
and the designated role will not be given)<br/>

`<role>` This is the role a user may acquire you want to set exclusions for.<br/>
`<exclude>` The role(s) you wish to have removed when a user gains the `<role>`<br/>

Note: This will only work for roles assigned by this cog.<br/>
 - Usage: `s.roletools exclude add <role> <exclude>`
 - Restricted to: `ADMIN`
## s.roletools buttons
Setup role buttons<br/>
 - Usage: `s.roletools buttons`
 - Restricted to: `ADMIN`
 - Aliases: `button`
### s.roletools buttons delete
Delete a saved button.<br/>

`<name>` - the name of the button you want to delete.<br/>
 - Usage: `s.roletools buttons delete <name>`
 - Aliases: `del and remove`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools buttons view
View current buttons setup for role assign in this server.<br/>
 - Usage: `s.roletools buttons view`
 - Restricted to: `ADMIN`
### s.roletools buttons create
Create a role button<br/>

- `<name>` - The name of the button for use later in setup.<br/>
- `<role>` - The role this button will assign or remove.<br/>
- `[extras]`<br/>
 - `label:` - The optional label for the button.<br/>
 - `emoji:` - The optional emoji used in the button.<br/>
 - `style:` - The background button style. Must be one of the following:<br/>
   - `primary`<br/>
   - `secondary`<br/>
   - `success`<br/>
   - `danger`<br/>
   - `blurple`<br/>
   - `grey`<br/>
   - `green`<br/>
   - `red`<br/>

Note: If no label and no emoji are provided the roles name will be used instead.<br/>
This name will not update if the role name is changed.<br/>

Example:<br/>
    `s.roletools button create role1 @role label: Super fun role style: blurple emoji: 😀`<br/>
 - Usage: `s.roletools buttons create <name> <role> <extras>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools buttons cleanup
Check each button that has registered a message still exists and remove buttons with<br/>
missing messages.<br/>

# Note: This will also potentially cause problems if the button exists in a thread<br/>
it will not be found if the thread is archived and subsequently removed.<br/>
 - Usage: `s.roletools buttons cleanup`
 - Restricted to: `ADMIN`
## s.roletools sticky
Set whether or not a role will be re-applied when a user leaves and rejoins the server.<br/>

`[true_or_false]` optional boolean of what to set the setting to.<br/>
If not provided the current setting will be shown instead.<br/>
`<role>` The role you want to set.<br/>
 - Usage: `s.roletools sticky [true_or_false=None] <role>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### true_or_false: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.roletools atomic
Set the atomicity of role assignment.<br/>
What this means is that when this is `True` roles will be<br/>
applied inidvidually and not cause any errors. When this<br/>
is set to `False` roles will be grouped together into one call.<br/>

This can cause race conditions if you have other methods of applying<br/>
roles setup when set to `False`.<br/>

`[true_or_false]` optional boolean of what to set the setting to.<br/>
To reset back to the default global rules use `clear`.<br/>
If not provided the current setting will be shown instead.<br/>
 - Usage: `s.roletools atomic [true_or_false=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### true_or_false: Union[str, bool, NoneType] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.roletools required
Set role requirements<br/>
 - Usage: `s.roletools required`
 - Aliases: `requires, require, and req`
### s.roletools required add
Add role requirements<br/>

`<role>` This is the role a user may acquire you want to set requirements for.<br/>
`<requires>` The role(s) the user requires before being allowed to gain this role.<br/>

Note: This will only work for roles assigned by this cog.<br/>
 - Usage: `s.roletools required add <role> <required>`
 - Restricted to: `ADMIN`
### s.roletools required remove
Remove role requirements<br/>

`<role>` This is the role a user may acquire you want to set requirements for.<br/>
`<requires>` The role(s) you wish to have added when a user gains the `<role>`<br/>

Note: This will only work for roles assigned by this cog.<br/>
 - Usage: `s.roletools required remove <role> <required>`
 - Restricted to: `ADMIN`
### s.roletools required any
Set the required roles to require any of the roles instead of all of them<br/>

`<role>` This is the role a user may acquire you want to set requirements for.<br/>
`<require_any>` Either `True` or `False`. If `True` any of the required roles will allow<br/>
the user to acquire the `<role>`.<br/>

Note: This will only work for roles assigned by this cog.<br/>
 - Usage: `s.roletools required any <role> <require_any>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### require_any: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.roletools select
Setup role select menus<br/>
 - Usage: `s.roletools select`
 - Restricted to: `ADMIN`
 - Aliases: `selects`
### s.roletools select view
View current select menus setup for role assign in this server.<br/>
 - Usage: `s.roletools select view`
 - Restricted to: `ADMIN`
 - Aliases: `list`
### s.roletools select delete
Delete a saved select menu.<br/>

`<name>` - the name of the select menu you want to delete.<br/>
 - Usage: `s.roletools select delete <name>`
 - Aliases: `del and remove`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools select deleteoption
Delete a saved option.<br/>

`<name>` - the name of the select option you want to delete.<br/>
 - Usage: `s.roletools select deleteoption <name>`
 - Aliases: `deloption, removeoption, and remoption`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools select createoption
Create a select menu option<br/>

- `<name>` - The name of the select option for use later in setup.<br/>
- `<role>` - The role this select option will assign or remove.<br/>
- `[extras]`<br/>
 - `label:` - The optional label for the option, max of 25 characters.<br/>
 - `description:` - The description for the option, max of 50 characters.<br/>
 - `emoji:` - The optional emoji used in the select option.<br/>

Note: If no label and no emoji are provided the roles name will be used instead.<br/>
This name will not update if the role name is changed.<br/>

Example:<br/>
    `s.roletools select createoption role1 @role label: Super Fun Role emoji: 😀`<br/>
 - Usage: `s.roletools select createoption <name> <role> <extras>`
 - Aliases: `addoption`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools select create
Create a select menu<br/>

- `<name>` - The name for you to use when you send a message with this menu.<br/>
- `[options]...` - The select menu options you designated previously.<br/>
- `[extras]`<br/>
 - `min:` - The minimum number of items from this menu to be selected.<br/>
 - `max:` - The maximum number of items from this menu that can be selected.<br/>
 (If not provided this will default to the number of options provided.)<br/>
 - `placeholder:` - This is the default text on the menu when no option has been<br/>
chosen yet.<br/>
Example:<br/>
    `s.roletools select create myrolemenu role1 role2 role3 placeholder: Pick your role!`<br/>
 - Usage: `s.roletools select create <name> <options> <extras>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools select cleanup
Check each select menu that has registered a message still exists and remove buttons with<br/>
missing messages.<br/>

# Note: This will also potentially cause problems if the button exists in a thread<br/>
it will not be found if the thread is archived and subsequently removed.<br/>
 - Usage: `s.roletools select cleanup`
 - Restricted to: `ADMIN`
### s.roletools select viewoptions
View current select menus setup for role assign in this server.<br/>
 - Usage: `s.roletools select viewoptions`
 - Restricted to: `ADMIN`
 - Aliases: `listoptions, viewoption, and listoption`
## s.roletools cost
Set the cost to acquire a role.<br/>

`[cost]` The price you want to set the role at in bot credits.<br/>
Setting this to 0 or lower will remove the cost.<br/>
If not provided the current setting will be shown instead.<br/>
`<role>` The role you want to set.<br/>
 - Usage: `s.roletools cost [cost=None] <role>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### cost: Optional[int] = None
> ```
> A number without decimal places.
> ```
## s.roletools include
Set role inclusion<br/>
 - Usage: `s.roletools include`
 - Aliases: `inclusive`
### s.roletools include add
Add role inclusion (This will add roles if the designated role is acquired<br/>
if the designated role is removed the included roles will also be removed<br/>
if the included roles are set to selfremovable)<br/>

`<role>` This is the role a user may acquire you want to set exclusions for.<br/>
`<include>` The role(s) you wish to have added when a user gains the `<role>`<br/>

Note: This will only work for roles assigned by this cog.<br/>
 - Usage: `s.roletools include add <role> <include>`
 - Restricted to: `ADMIN`
### s.roletools include remove
Remove role inclusion<br/>

`<role>` This is the role a user may acquire you want to set exclusions for.<br/>
`<include>` The role(s) currently inclusive you no longer wish to have included<br/>
 - Usage: `s.roletools include remove <role> <include>`
 - Restricted to: `ADMIN`
### s.roletools include mutual
Allow setting roles mutually inclusive to eachother<br/>

This is equivalent to individually setting each roles inclusive roles to another<br/>
set of roles.<br/>

`[role...]` The roles you want to set as mutually inclusive.<br/>
 - Usage: `s.roletools include mutual <roles>`
 - Restricted to: `ADMIN`
## s.roletools removerole
Removes a role from the designated members.<br/>

`<role>` The role you want to give.<br/>
`[who...]` Who you want to give the role to. This can include any of the following:```diff<br/>
+ Member<br/>
    A specified member of the server.<br/>
+ Role<br/>
    People who already have a specified role.<br/>
+ TextChannel<br/>
    People who have access to see the channel provided.<br/>
Or one of the following:<br/>
+ everyone - everyone in the server.<br/>
+ here     - everyone who appears online in the server.<br/>
+ bots     - all the bots in the server.<br/>
+ humans   - all the humans in the server.<br/>
```
**Note:** This runs through exclusive and inclusive role checks
which may cause unintended roles to be removed/applied.

**This command is on a cooldown of 10 seconds per member who receives
a role up to a maximum of 1 hour.**
 - Usage: `s.roletools removerole <role> <who>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### *who: Union[discord.role.Role, discord.channel.TextChannel, discord.member.Member, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.roletools selfadd
Set whether or not a user can apply the role to themselves.<br/>

`[true_or_false]` optional boolean of what to set the setting to.<br/>
If not provided the current setting will be shown instead.<br/>
`<role>` The role you want to set.<br/>
 - Usage: `s.roletools selfadd [true_or_false=None] <role>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### true_or_false: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.roletools selfrole
Add or remove a defined selfrole<br/>

`<role>` The role you want to add or remove.<br/>
If you already have the role it will be removed.<br/>
 - Usage: `s.roletools selfrole <role>`
 - Checks: `server_only`
## s.roletools viewroles
View current roletools setup for each role in the server<br/>

`[role]` The role you want to see settings for.<br/>
 - Usage: `s.roletools viewroles [role]`
 - Aliases: `viewrole`
Extended Arg Info
> ### role: Optional[discord.role.Role] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.roletools selfrem
Set whether or not a user can remove the role from themselves.<br/>

`[true_or_false]` optional boolean of what to set the setting to.<br/>
If not provided the current setting will be shown instead.<br/>
`<role>` The role you want to set.<br/>
 - Usage: `s.roletools selfrem [true_or_false=None] <role>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### true_or_false: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.roletools reaction
Reaction role settings<br/>
 - Usage: `s.roletools reaction`
 - Aliases: `react and reactions`
### s.roletools reaction clearreact
Clear the reactions for reaction roles. This will remove<br/>
all reactions and then re-apply the bots reaction for you.<br/>

`<message>` The message you want to clear reactions on.<br/>
`[emojis...]` Optional emojis you want to specifically remove.<br/>
If no emojis are provided this will clear all the reaction role<br/>
emojis the bot has for the message provided.<br/>

Note: This will only clear reactions which have a corresponding<br/>
reaction role on it.<br/>
 - Usage: `s.roletools reaction clearreact <message> <emojis>`
 - Restricted to: `ADMIN`
 - Aliases: `clearreacts`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
> ### *emojis: Union[discord.emoji.Emoji, str, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
### s.roletools reaction create
Create a reaction role<br/>

`<message>` can be the channel_id-message_id pair<br/>
from copying message ID while holding SHIFT or a message link<br/>
`<emoji>` The emoji you want people to react with to get the role.<br/>
`<role>` The role you want people to receive for reacting.<br/>
 - Usage: `s.roletools reaction create <message> <emoji> <role>`
 - Restricted to: `ADMIN`
 - Aliases: `make and setup`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
> ### emoji: Union[discord.emoji.Emoji, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by extracting ID from the emoji.
>     3. Lookup by name
> 
>     
### s.roletools reaction reactroles
View current bound roles in the server<br/>
 - Usage: `s.roletools reaction reactroles`
 - Restricted to: `ADMIN`
 - Aliases: `reactionroles and reactrole`
### s.roletools reaction bulk
Create multiple roles reactions for a single message<br/>

`<message>` can be the channel_id-message_id pair<br/>
from copying message ID while holding SHIFT or a message link<br/>
`[role_emoji...]` Must be a role-emoji pair separated by either `;`, `,`, `|`, or `-`.<br/>

Note: Any spaces will be considered a new set of role-emoji pairs, if you<br/>
want to specify a role with a space in it without pinging it enclose<br/>
the full role-emoji pair in quotes.<br/>

e.g. `s.roletools bulkreact 461417772115558410-821105109097644052 @member-:smile:`<br/>
`s.roletools bulkreact 461417772115558410-821105109097644052 "Super Member-:frown:"`<br/>
 - Usage: `s.roletools reaction bulk <message> <role_emoji>`
 - Restricted to: `ADMIN`
 - Aliases: `bulkcreate and bulkmake`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
### s.roletools reaction cleanup
Cleanup old/missing reaction roles and settings.<br/>

Note: This will also clear out reaction roles if the bot is just<br/>
missing permissions to see the reactions.<br/>
 - Usage: `s.roletools reaction cleanup`
 - Restricted to: `ADMIN`
### s.roletools reaction remove
Remove a reaction role<br/>

`<message>` can be the channel_id-message_id pair<br/>
from copying message ID while holding SHIFT or a message link<br/>
`<emoji>` The emoji you want people to react with to get the role.<br/>
`<role>` The role you want people to receive for reacting.<br/>

Note: This will not remove the emoji reactions on the message.<br/>
 - Usage: `s.roletools reaction remove <message> <role_or_emoji>`
 - Restricted to: `ADMIN`
 - Aliases: `rem`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
## s.roletools giverole
Gives a role to designated members.<br/>

`<role>` The role you want to give.<br/>
`[who...]` Who you want to give the role to. This can include any of the following:```diff<br/>
+ Member<br/>
    A specified member of the server.<br/>
+ Role<br/>
    People who already have a specified role.<br/>
+ TextChannel<br/>
    People who have access to see the channel provided.<br/>
Or one of the following:<br/>
+ everyone - everyone in the server.<br/>
+ here     - everyone who appears online in the server.<br/>
+ bots     - all the bots in the server.<br/>
+ humans   - all the humans in the server.<br/>
```
**Note:** This runs through exclusive and inclusive role checks
which may cause unintended roles to be removed/applied.

**This command is on a cooldown of 10 seconds per member who receives
a role up to a maximum of 1 hour.**
 - Usage: `s.roletools giverole <role> <who>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### *who: Union[discord.role.Role, discord.channel.TextChannel, discord.threads.Thread, discord.member.Member, str]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.roletools message
Commands for sending/editing messages for roletools<br/>
 - Usage: `s.roletools message`
### s.roletools message sendbutton
Send buttons to a specified channel with optional message.<br/>

`<channel>` - the channel to send the button role buttons to.<br/>
`[buttons]...` - The names of the buttons you want included in the<br/>
message up to a maximum of 25.<br/>
`[text]` - The text to be included with the buttons.<br/>
 - Usage: `s.roletools message sendbutton <channel> <buttons> [text]`
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
> ### text: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools message edit
Edit a bots message to include Role Buttons<br/>

`<message>` - The existing message to add role buttons to. Must be a bots message.<br/>
`[buttons]...` - The names of the buttons you want to include up to a maximum of 25.<br/>
`[menus]...` - The names of the select menus you want to include up to a maximum of 5.<br/>

Note: There is a maximum of 25 slots available on one message. Each menu<br/>
uses up 5 slots while each button uses up 1 slot.<br/>
 - Usage: `s.roletools message edit <message> <buttons> <menus>`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
### s.roletools message send
Send a select menu to a specified channel for role assignment<br/>

`<channel>` - the channel to send the button role buttons to.<br/>
`[buttons]...` - The names of the buttons you want included in the<br/>
`[menus]...` - The names of the select menus you want included in the<br/>
message up to a maximum of 5.<br/>
`[text]` - The text to be included with the select menu.<br/>

Note: There is a maximum of 25 slots available on one message. Each menu<br/>
uses up 5 slots while each button uses up 1 slot.<br/>
 - Usage: `s.roletools message send <channel> <buttons> <menus> [text]`
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
> ### text: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools message sendselect
Send a select menu to a specified channel for role assignment<br/>

`<channel>` - the channel to send the button role buttons to.<br/>
`[menus]...` - The names of the select menus you want included in the<br/>
message up to a maximum of 5.<br/>
`[text]` - The text to be included with the select menu.<br/>
 - Usage: `s.roletools message sendselect <channel> <menus> [text]`
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
> ### text: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.roletools message editselect
Edit a bots message to include Role Buttons<br/>

`<message>` - The existing message to add role buttons to. Must be a bots message.<br/>
`[menus]...` - The names of the select menus you want to include up to a maximum of 5.<br/>
 - Usage: `s.roletools message editselect <message> <menus>`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
### s.roletools message editbutton
Edit a bots message to include Role Buttons<br/>

`<message>` - The existing message to add role buttons to. Must be a bots message.<br/>
`[buttons]...` - The names of the buttons you want to include up to a maximum of 25.<br/>
 - Usage: `s.roletools message editbutton <message> <buttons>`
Extended Arg Info
> ### message: discord.message.Message
> Converts to a :class:`discord.Message`.
> 
>     
## s.roletools forceroleremove
Force remove sticky role on one or more users.<br/>

`<users>` The users you want to have a forced stickyrole applied to.<br/>
`<roles>` The role you want to set.<br/>

Note: This is generally only useful for users who have left the server.<br/>
 - Usage: `s.roletools forceroleremove <users> <role>`
 - Restricted to: `ADMIN`
## s.roletools forcerole
Force a sticky role on one or more users.<br/>

`<users>` The users you want to have a forced stickyrole applied to.<br/>
`<roles>` The role you want to set.<br/>

Note: The only way to remove this would be to manually remove the role from<br/>
the user.<br/>
 - Usage: `s.roletools forcerole <users> <role>`
 - Restricted to: `ADMIN`
## s.roletools autorole
Set a role to be automatically applied when a user joins the server.<br/>

`[true_or_false]` optional boolean of what to set the setting to.<br/>
If not provided the current setting will be shown instead.<br/>
`<role>` The role you want to set.<br/>
 - Usage: `s.roletools autorole [true_or_false=None] <role>`
 - Restricted to: `ADMIN`
 - Aliases: `auto`
Extended Arg Info
> ### true_or_false: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
