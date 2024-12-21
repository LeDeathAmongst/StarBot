# s.setemotes (Hybrid Command)
Change the configurations for Emotes Cog<br/>

Setting global values to `False` will override server settings and disable it across the whole bot.<br/>
 - Usage: `s.setemotes`
 - Slash Usage: `/setemotes`
 - Aliases: `se, setemote, and setemotesheet`
## s.setemotes serverall (Hybrid Command)
The power switch for Cherry Emotes in this server<br/>
 - Usage: `s.setemotes serverall <true_or_false>`
 - Slash Usage: `/setemotes serverall <true_or_false>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setemotes serverrecentsmax (Hybrid Command)
Determines how many messages back to search for emotes in this server<br/>

Not recommended to set higher than 20, for performance reasons.<br/>
 - Usage: `s.setemotes serverrecentsmax <count>`
 - Slash Usage: `/setemotes serverrecentsmax <count>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### count: int
> ```
> A number without decimal places.
> ```
# s.emotesearch (Hybrid Command)
Search for image-ized emote url<br/>
 - Usage: `s.emotesearch <search> [page=1]`
 - Slash Usage: `/emotesearch <search> [page=1]`
 - Aliases: `esearch and ee`
Extended Arg Info
> ### search
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### page: int = 1
> ```
> A number without decimal places.
> ```
# s.emotesend (Hybrid Command)
Send an emote from Emote Sheet, with first search result<br/>
 - Usage: `s.emotesend <search>`
 - Slash Usage: `/emotesend <search>`
 - Aliases: `esend and eee`
Extended Arg Info
> ### search
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.emoteinfo (Hybrid Command)
Send info about an emote<br/>

If you don't have access to the emote (ie. no Nitro, or can't send the emote because it's from another server), you can reply to the message with the emote you want and the `s.emoteinfo` command will pick up the emote.<br/>
 - Usage: `s.emoteinfo [emote=None]`
 - Slash Usage: `/emoteinfo [emote=None]`
 - Aliases: `ei`
Extended Arg Info
> ### emote=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.emotelist (Hybrid Command)
List all emotes in message<br/>

Shows a list of names and urls for all emotes in a message, when you reply to a message with this command. Useful for Emote Spreadsheet.<br/>
 - Usage: `s.emotelist [hist=False]`
 - Slash Usage: `/emotelist [hist=False]`
Extended Arg Info
> ### hist=False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.showemote (Hybrid Command)
Show an emote you have an URL for<br/>
 - Usage: `s.showemote <emoteurl>`
 - Slash Usage: `/showemote <emoteurl>`
Extended Arg Info
> ### emoteurl: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
