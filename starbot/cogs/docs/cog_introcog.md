# s.intro
Manage your introduction.<br/>
 - Usage: `s.intro`
 - Checks: `server_only`
## s.intro viewfields
View the fields available for your introduction in this server.<br/>
 - Usage: `s.intro viewfields`
## s.intro setchannel
Set the channel where introductions will be sent.<br/>
 - Usage: `s.intro setchannel <channel>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
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
## s.intro addfield
Add a field to the introduction form.<br/>
 - Usage: `s.intro addfield <field_name>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro viewfooter
View the current footer for the introduction embed.<br/>
 - Usage: `s.intro viewfooter`
## s.intro preview
Preview your introduction.<br/>
 - Usage: `s.intro preview`
## s.intro send
Send your introduction to the configured channel.<br/>
 - Usage: `s.intro send`
## s.intro viewtitle
View the current title for the introduction embed.<br/>
 - Usage: `s.intro viewtitle`
## s.intro setbreakfield
Set the title for the break field.<br/>
 - Usage: `s.intro setbreakfield <break_field_title>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### break_field_title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro editvalue
Edit a field value in your introduction.<br/>

Example: s.intro editvalue name Jane Doe<br/>
 - Usage: `s.intro editvalue <field_name> <field_value>`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### field_value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro viewbreakfield
View the current break field title.<br/>
 - Usage: `s.intro viewbreakfield`
## s.intro setcolor
Set the color for your introduction embed.<br/>
 - Usage: `s.intro setcolor <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
## s.intro removevalue
Remove a field value from your introduction.<br/>
 - Usage: `s.intro removevalue <field_name>`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro removefield
Remove a field from the introduction form.<br/>
 - Usage: `s.intro removefield <field_name>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro settitle
Set the title for the introduction embed.<br/>
 - Usage: `s.intro settitle <title>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro setfooter
Set the footer for the introduction embed.<br/>
 - Usage: `s.intro setfooter <footer>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### footer: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro addvalue
Add a field value to your introduction.<br/>

Example: s.intro addvalue name John Doe<br/>
 - Usage: `s.intro addvalue <field_name> <field_value>`
Extended Arg Info
> ### field_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### field_value: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intro example
Set an example introduction with predefined fields and values.<br/>
 - Usage: `s.intro example`
