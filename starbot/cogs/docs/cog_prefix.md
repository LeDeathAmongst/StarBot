# s.prefix
Manage server prefixes.<br/>

Running this command without subcommands will show this server's prefixes.<br/>

**Example:**<br/>
`s.prefix`<br/>
 - Usage: `s.prefix`
 - Checks: `server_only`
## s.prefix clear
Reset this server's prefixes to the default list.<br/>

This cannot be undone.<br/>

**Example:**<br/>
`s.prefix clear`<br/>
 - Usage: `s.prefix clear`
 - Restricted to: `ADMIN`
 - Aliases: `reset`
## s.prefix add
Add a prefix to this server's prefix list.<br/>

Use quotes to add a prefix with spaces.<br/>

**Examples:**<br/>
`s.prefix add ?`<br/>
`s.prefix + "Starfire, can you please "`<br/>
 - Usage: `s.prefix add <prefix>`
 - Restricted to: `ADMIN`
 - Aliases: `+`
## s.prefix set
Set the prefixes for this server.<br/>

Multiple prefixes can be set at once.<br/>
To add a prefix with spaces, use quotes.<br/>
This will overwrite any current prefixes.<br/>

**Examples:**<br/>
`s.prefix set ! n!`<br/>
`s.prefix set .. & "Hey siri, "`<br/>
 - Usage: `s.prefix set <prefixes>`
 - Restricted to: `ADMIN`
 - Aliases: `=`
## s.prefix remove
Remove a prefix from this server's prefix list.<br/>

Use quotes to remove a prefix with spaces.<br/>

**Examples:**<br/>
`s.prefix remove ~`<br/>
`s.prefix - "Alexa, "`<br/>
 - Usage: `s.prefix remove <prefix>`
 - Restricted to: `ADMIN`
 - Aliases: `-`
Extended Arg Info
> ### prefix: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
