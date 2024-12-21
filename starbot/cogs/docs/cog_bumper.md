# s.bumpset
Group command to set bump configuration.<br/>
 - Usage: `s.bumpset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.bumpset thumbnail
Set the thumbnail URL for the bump embed.<br/>
 - Usage: `s.bumpset thumbnail <thumbnail_url>`
Extended Arg Info
> ### thumbnail_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.bumpset image
Set the image URL for the bump embed.<br/>
 - Usage: `s.bumpset image <image_url>`
Extended Arg Info
> ### image_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.bumpset embed_color
Set the embed color.<br/>
 - Usage: `s.bumpset embed_color <color>`
Extended Arg Info
> ### color: discord.colour.Colour
> Converts to a :class:`~discord.Colour`.
> 
>     
## s.bumpset description
Set the server description (max 1024 characters).<br/>
 - Usage: `s.bumpset description <description>`
Extended Arg Info
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.bumpset invite
Set the invite link.<br/>
 - Usage: `s.bumpset invite <invite>`
Extended Arg Info
> ### invite: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.bumpset channel
Set the bump channel.<br/>
 - Usage: `s.bumpset channel <channel>`
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
# s.mycodes
List all premium codes assigned to the user.<br/>
 - Usage: `s.mycodes`
# s.codegen
Generate premium codes. Use -1 for permanent, or specify time and unit (e.g., 1d for 1 day, 1m for 1 month).<br/>
 - Usage: `s.codegen <user_id> <duration> [quantity=1]`
Extended Arg Info
> ### user_id: int
> ```
> A number without decimal places.
> ```
> ### duration: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### quantity: int = 1
> ```
> A number without decimal places.
> ```
# s.redeem
Redeem a premium code.<br/>
 - Usage: `s.redeem <code>`
 - Checks: `server_only`
Extended Arg Info
> ### code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.bumper
Send the bump message to all servers with a configured bump channel.<br/>
 - Usage: `s.bumper`
 - Checks: `server_only`
