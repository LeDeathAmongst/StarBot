# s.kofiprofile (Hybrid Command)
Get the details of a KoFi profile.<br/>
 - Usage: `s.kofiprofile <kofi_page_url>`
 - Slash Usage: `/kofiprofile <kofi_page_url>`
Extended Arg Info
> ### kofi_page_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.setkofitracker (Hybrid Command)
Commands to configure KoFiTracker.<br/>
 - Usage: `s.setkofitracker`
 - Slash Usage: `/setkofitracker`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setkofitracker list (Hybrid Command)
List the KoFi pages being tracked.<br/>
 - Usage: `s.setkofitracker list <channel>`
 - Slash Usage: `/setkofitracker list <channel>`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.setkofitracker add (Hybrid Command)
Add a KoFi page to track.<br/>

⚠ **Note:** If you choose to show personal details, the user's email and shipping details will be shown to everyone in the channel.<br/>
 - Usage: `s.setkofitracker add <channel> <kofi_page_url> <verification_token> [types=['Donation', 'Subscription', 'Shop Order']] [show_private=False] [show_personal_details=False]`
 - Slash Usage: `/setkofitracker add <channel> <kofi_page_url> <verification_token> [types=['Donation', 'Subscription', 'Shop Order']] [show_private=False] [show_personal_details=False]`
 - Aliases: `+`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### kofi_page_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### verification_token: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### show_private: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### show_personal_details: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setkofitracker instructions (Hybrid Command)
Instructions on how to set up KoFiTracker.<br/>
 - Usage: `s.setkofitracker instructions`
 - Slash Usage: `/setkofitracker instructions`
 - Checks: `server_only`
## s.setkofitracker remove (Hybrid Command)
Remove a KoFi page from tracking.<br/>
 - Usage: `s.setkofitracker remove <channel> <kofi_page_url>`
 - Slash Usage: `/setkofitracker remove <channel> <kofi_page_url>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### kofi_page_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
