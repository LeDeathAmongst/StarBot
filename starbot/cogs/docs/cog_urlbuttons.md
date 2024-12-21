# s.urlbuttons (Hybrid Command)
Group of commands to use UrlButtons.<br/>
 - Usage: `s.urlbuttons`
 - Slash Usage: `/urlbuttons`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.urlbuttons list (Hybrid Command)
List all url-buttons of this server or display the settings for a specific one.<br/>
 - Usage: `s.urlbuttons list [message=None]`
 - Slash Usage: `/urlbuttons list [message=None]`
 - Checks: `server_only`
## s.urlbuttons add (Hybrid Command)
Add a url-button for a message.<br/>
 - Usage: `s.urlbuttons add <message> <url> <emoji> [text_button]`
 - Slash Usage: `/urlbuttons add <message> <url> <emoji> [text_button]`
 - Aliases: `+`
 - Checks: `server_only`
## s.urlbuttons bulk (Hybrid Command)
Add a url-button for a message.<br/>

```s.urlbuttons bulk <message> :red_circle:|<https://github.com/Cog-Creators/Red-DiscordBot> :smiley:|<https://github.com/Cog-Creators/Red-SmileyBot> :green_circle:|<https://github.com/Cog-Creators/Green-DiscordBot>```
 - Usage: `s.urlbuttons bulk <message> <url_buttons>`
 - Slash Usage: `/urlbuttons bulk <message> <url_buttons>`
 - Checks: `server_only`
## s.urlbuttons remove (Hybrid Command)
Remove a url-button for a message.<br/>

Use `s.urlbuttons list <message>` to find the config identifier.<br/>
 - Usage: `s.urlbuttons remove <message> <config_identifier>`
 - Slash Usage: `/urlbuttons remove <message> <config_identifier>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### config_identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.urlbuttons clear (Hybrid Command)
Clear all url-buttons for a message.<br/>
 - Usage: `s.urlbuttons clear <message>`
 - Slash Usage: `/urlbuttons clear <message>`
 - Checks: `server_only`
