# s.dropdownstexts (Hybrid Command)
Group of commands to use DropdownsTexts.<br/>
 - Usage: `s.dropdownstexts`
 - Slash Usage: `/dropdownstexts`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.dropdownstexts clear (Hybrid Command)
Clear a dropdown-texts for a message.<br/>
 - Usage: `s.dropdownstexts clear <message>`
 - Slash Usage: `/dropdownstexts clear <message>`
 - Checks: `server_only`
## s.dropdownstexts remove (Hybrid Command)
Remove a dropdown-text for a message.<br/>

Use `s.dropdownstexts list <message>` to find the config identifier.<br/>
 - Usage: `s.dropdownstexts remove <message> <config_identifier>`
 - Slash Usage: `/dropdownstexts remove <message> <config_identifier>`
 - Aliases: `-`
 - Checks: `server_only`
Extended Arg Info
> ### config_identifier: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.dropdownstexts list (Hybrid Command)
List all dropdowns-texts of this server or display the settings for a specific one.<br/>
 - Usage: `s.dropdownstexts list [message=None]`
 - Slash Usage: `/dropdownstexts list [message=None]`
 - Checks: `server_only`
## s.dropdownstexts bulk (Hybrid Command)
Add dropdown-texts for a message.<br/>
 - Usage: `s.dropdownstexts bulk <message> <dropdown_texts>`
 - Slash Usage: `/dropdownstexts bulk <message> <dropdown_texts>`
 - Checks: `server_only`
## s.dropdownstexts add (Hybrid Command)
Add a dropdown-text for a message.<br/>
 - Usage: `s.dropdownstexts add <message> <emoji> <label> <text_or_message>`
 - Slash Usage: `/dropdownstexts add <message> <emoji> <label> <text_or_message>`
 - Aliases: `+`
 - Checks: `server_only`
