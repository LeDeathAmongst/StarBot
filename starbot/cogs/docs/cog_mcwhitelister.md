# s.whitelister
MCWhitelister commands<br/>
 - Usage: `s.whitelister`
## s.whitelister adminremove
Remove someone else from the whitelist manually.<br/>

This might not be reflected correctly in `s.whitelister list`.<br/>
 - Usage: `s.whitelister adminremove <name>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.whitelister add
Add yourself to the whitelist.<br/>
 - Usage: `s.whitelister add <name>`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.whitelister setup
Set up MCWhitelister.<br/>

`host`: The IP/URL of your minecraft server.<br/>
`port`: Your server's RCON port. (The default is 25575)<br/>
`password`: The RCON password.<br/>
RCON needs to be enabled and set up in your `server.properties` file.<br/>
More information is available [here](https://minecraft.wiki/w/Server.properties)<br/>
 - Usage: `s.whitelister setup <host> <port> <password>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### host: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### port: int
> ```
> A number without decimal places.
> ```
> ### password: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.whitelister remove
Remove yourself from the whitelist.<br/>
 - Usage: `s.whitelister remove`
## s.whitelister addmin
Add someone else to the whitelist manually.<br/>

They will not be removed automatically when leaving the server.<br/>
 - Usage: `s.whitelister addmin <name>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.whitelister list
See who is whitelisted on your server.<br/>
 - Usage: `s.whitelister list`
 - Restricted to: `ADMIN`
# s.mccommand
Run a command on the Minecraft server.<br/>

**NO VALIDATION is performed on your inputs.**<br/>
 - Usage: `s.mccommand <command>`
 - Restricted to: `GUILD_OWNER`
Extended Arg Info
> ### command
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
