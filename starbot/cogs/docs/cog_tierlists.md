# s.tierlistset
Tierlist settings<br/>
 - Usage: `s.tierlistset`
 - Aliases: `tlset`
 - Checks: `server_only`
## s.tierlistset setpercentiles
Set the percentile value for a tier<br/>
 - Usage: `s.tierlistset setpercentiles <tier> <value>`
 - Restricted to: `ADMIN`
 - Aliases: `setp`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.tierlistset setmaxvotes
Set the maximum number of votes a user can cast<br/>
 - Usage: `s.tierlistset setmaxvotes <vote_type> <value>`
 - Restricted to: `ADMIN`
 - Aliases: `setmv`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.tierlistset showsettings
Show the current tierlist settings<br/>
 - Usage: `s.tierlistset showsettings`
 - Aliases: `ss, show, and settings`
## s.tierlistset category
Category settings<br/>
 - Usage: `s.tierlistset category`
 - Restricted to: `ADMIN`
 - Aliases: `cat`
### s.tierlistset category edit
Edit a category<br/>
 - Usage: `s.tierlistset category edit`
 - Restricted to: `ADMIN`
#### s.tierlistset category edit channel
Edit a category's channel<br/>
 - Usage: `s.tierlistset category edit channel <name> <channel>`
 - Restricted to: `ADMIN`
 - Aliases: `chan`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.threads.Thread]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.tierlistset category edit name
Edit a category's name<br/>
 - Usage: `s.tierlistset category edit name <name> <new_name>`
 - Restricted to: `ADMIN`
 - Aliases: `rename`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### new_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### s.tierlistset category edit description
Edit a category's description<br/>
 - Usage: `s.tierlistset category edit description <name> <description>`
 - Restricted to: `ADMIN`
 - Aliases: `desc`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.tierlistset category updatemessage
Update a category's voting message<br/>
 - Usage: `s.tierlistset category updatemessage <name>`
 - Restricted to: `ADMIN`
 - Aliases: `update and refresh`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.tierlistset category create
Create a new tierlist category<br/>

A category is a list that can have options added to it that users can vote for<br/>
 - Usage: `s.tierlistset category create <name> [channel=operator.attrgetter('channel')] [description]`
 - Restricted to: `ADMIN`
 - Aliases: `add, +, and  new`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.channel.StageChannel, discord.threads.Thread] = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### description: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.tierlistset category list
See a list of all cateogries with their choices.<br/>
 - Usage: `s.tierlistset category list`
### s.tierlistset category option
Option settings<br/>
 - Usage: `s.tierlistset category option`
 - Aliases: `opt, options, choices, and choice`
#### s.tierlistset category option add
Add an option to a category<br/>
 - Usage: `s.tierlistset category option add <category> <option>`
 - Aliases: `+ and new`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### option: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### s.tierlistset category option clear
Clear all options from a category<br/>
 - Usage: `s.tierlistset category option clear <category>`
 - Restricted to: `ADMIN`
 - Aliases: `reset`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
#### s.tierlistset category option remove
Remove an option from a category<br/>

Use the index number of the option, as shown in `s.tlset show`<br/>
 - Usage: `s.tierlistset category option remove <category> <option>`
 - Restricted to: `ADMIN`
 - Aliases: `del and -`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### option: int
> ```
> A number without decimal places.
> ```
#### s.tierlistset category option forceadd
Force add an option to a category<br/>
 - Usage: `s.tierlistset category option forceadd <category> <option>`
 - Restricted to: `ADMIN`
 - Aliases: `force and addforce`
Extended Arg Info
> ### category: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### option: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.tierlistset category delete
Delete a tierlist category<br/>
 - Usage: `s.tierlistset category delete <name>`
 - Restricted to: `ADMIN`
 - Aliases: `remove, -, and del`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
