# s.slashtag
Slash Tag management with TagScript.<br/>

These commands use TagScriptEngine.<br/>
[This site](https://phen-cogs.readthedocs.io/en/latest/index.html) has documentation on how to use TagScript blocks.<br/>
 - Usage: `s.slashtag`
 - Aliases: `st`
 - Checks: `server_only`
## s.slashtag user
Add a user command tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `s.slashtag user <tag_name> <tagscript>`
 - Restricted to: `MOD`
## s.slashtag raw
Get a slash tag's raw content.<br/>
 - Usage: `s.slashtag raw <tag>`
## s.slashtag pastebin
Add a slash tag with a Pastebin link.<br/>
 - Usage: `s.slashtag pastebin <tag_name> <link>`
 - Restricted to: `MOD`
 - Aliases: `++`
## s.slashtag info
Get info about a slash tag that is stored on this server.<br/>
 - Usage: `s.slashtag info <tag>`
## s.slashtag remove
Delete a slash tag.<br/>
 - Usage: `s.slashtag remove <tag>`
 - Restricted to: `MOD`
 - Aliases: `delete and -`
## s.slashtag list
View stored slash tags.<br/>
 - Usage: `s.slashtag list`
## s.slashtag add
Add a slash tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `s.slashtag add <tag_name> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `create and +`
## s.slashtag message
Add a message command tag with TagScript.<br/>

[Slash tag usage guide](https://phen-cogs.readthedocs.io/en/latest/slashtags/slashtags.html)<br/>
 - Usage: `s.slashtag message <tag_name> <tagscript>`
 - Restricted to: `MOD`
## s.slashtag usage
See slash tag usage stats.<br/>

**Example:**<br/>
`s.slashtag usage`<br/>
 - Usage: `s.slashtag usage`
 - Aliases: `stats`
## s.slashtag edit
Edit a slash tag.<br/>
 - Usage: `s.slashtag edit <tag> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `e`
### s.slashtag edit description
Edit a slash tag's description.<br/>
 - Usage: `s.slashtag edit description <tag> <description>`
Extended Arg Info
> ### description: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.slashtag edit name
Edit a slash tag's name.<br/>
 - Usage: `s.slashtag edit name <tag> <name>`
### s.slashtag edit arguments
Edit a slash tag's arguments.<br/>

See [this documentation page](https://phen-cogs.readthedocs.io/en/latest/slashtags/slash_arguments.html) for more information on slash tag arguments.<br/>
 - Usage: `s.slashtag edit arguments <tag>`
 - Aliases: `options`
### s.slashtag edit argument
Edit a single slash tag's argument by name.<br/>
 - Usage: `s.slashtag edit argument <tag> <argument>`
 - Aliases: `option`
Extended Arg Info
> ### argument: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.slashtag edit tagscript
Edit a slash tag's TagScript.<br/>
 - Usage: `s.slashtag edit tagscript <tag> <tagscript>`
