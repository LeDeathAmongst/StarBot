# s.trigger
Group command for triggers.<br/>
 - Usage: `s.trigger`
 - Checks: `server_only`
## s.trigger delete
Delete a trigger.<br/>
 - Usage: `s.trigger delete <trigger_name>`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.trigger create
Create a trigger.<br/>

Variables can be used within the responses.<br/>
user: The user that triggered the trigger.<br/>
channel: The channel the trigger was triggered in.<br/>
message: The message that triggered the trigger.<br/>
server: The server the trigger was triggered in.<br/>
uses: The number of times the trigger has been used.<br/>
trigger: The name of the trigger that was triggered.<br/>

Example: `{user} has triggered the trigger {trigger} in {channel} {uses} times.`<br/>
 - Usage: `s.trigger create <trigger_name> <triggered_by>`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### triggered_by: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.trigger edit
Edit a trigger.<br/>
 - Usage: `s.trigger edit`
### s.trigger edit boundary
Toggle word boundaries for a trigger.<br/>
 - Usage: `s.trigger edit boundary <trigger_name> <toggle>`
 - Aliases: `wordboundary`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.trigger edit case
Toggle case sensitivity for a trigger.<br/>
 - Usage: `s.trigger edit case <trigger_name> <case_sensitive>`
 - Aliases: `casesensitive`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### case_sensitive: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.trigger edit responses
Edit the responses for a trigger.<br/>
 - Usage: `s.trigger edit responses <trigger_name>`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.trigger edit trigger
Edit the trigger.<br/>
 - Usage: `s.trigger edit trigger <trigger_name> <triggered_by>`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### triggered_by: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.trigger edit embeds
Toggle searching within embeds for the trigger.<br/>
 - Usage: `s.trigger edit embeds <trigger_name> <toggle>`
 - Aliases: `embedsearch`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.trigger edit cooldown
Set the cooldown for a trigger.<br/>
 - Usage: `s.trigger edit cooldown <trigger_name> <seconds>`
Extended Arg Info
> ### trigger_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### seconds: int
> ```
> A number without decimal places.
> ```
## s.trigger list
List all triggers.<br/>
 - Usage: `s.trigger list`
## s.trigger toggle
Toggle a trigger.<br/>
 - Usage: `s.trigger toggle <trigger_name>`
Extended Arg Info
> ### trigger_name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
