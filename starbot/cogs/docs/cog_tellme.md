# s.tellme
Run a command.<br/>
 - Usage: `s.tellme <command_name>`
 - Checks: `server_only`
Extended Arg Info
> ### command_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tellme dm
Set the message to be sent in dms.<br/>

If nothing is passed, it will remove the dm message.<br/>
 - Usage: `s.tellme dm <command_name> [text]`
Extended Arg Info
> ### command_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tellme server
Set the message to be sent in the server.<br/>

If nothing is passed, it will remove the server message.<br/>
 - Usage: `s.tellme server <command_name> [text]`
Extended Arg Info
> ### command_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tellme list
List commands created with tellme.<br/>
 - Usage: `s.tellme list`
## s.tellme create
Create a new command.<br/>
 - Usage: `s.tellme create <command_name>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tellme delete
Delete a command.<br/>
 - Usage: `s.tellme delete <command_name>`
Extended Arg Info
> ### command_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
