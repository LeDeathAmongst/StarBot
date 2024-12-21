# s.react
Smart Reacts, modified.<br/>
 - Usage: `s.react`
 - Checks: `server_only`
## s.react add
Add an auto reaction to a word.<br/>

Parameters:<br/>
-----------<br/>
word: str<br/>
    The word you wish to react to.<br/>
emoji: Union[str, discord.Emoji]<br/>
    The emoji you wish to react with, interpreted as the string representation<br/>
    with <:name:id> if it is a custom emoji.<br/>
 - Usage: `s.react add <word> <emoji>`
 - Restricted to: `MOD`
 - Checks: `server_only`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### emoji: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.react reload
Reloads auto reactions with new emojis by name<br/>
 - Usage: `s.react reload`
 - Restricted to: `MOD`
 - Checks: `server_only`
## s.react del
Delete an auto reaction to a word.<br/>

Parameters:<br/>
-----------<br/>
word: str<br/>
    The word you wish to react to.<br/>
emoji: Union[str, discord.Emoji]<br/>
    The emoji you wish to react with, interpreted as the string representation<br/>
    with <:name:id> if it is a custom emoji.<br/>
 - Usage: `s.react del <word> <emoji>`
 - Restricted to: `MOD`
 - Aliases: `delete, remove, and rm`
 - Checks: `server_only`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### emoji: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.react list
List the auto reaction emojis and triggers.<br/>
 - Usage: `s.react list`
