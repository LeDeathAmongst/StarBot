# s.serverlocale
Check the current server's locale<br/>
 - Usage: `s.serverlocale`
# s.translate (Hybrid Command)
Translate a message<br/>
 - Usage: `s.translate <to_language> [message]`
 - Slash Usage: `/translate <to_language> [message]`
Extended Arg Info
> ### to_language: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.fluent
Base command<br/>
 - Usage: `s.fluent`
 - Restricted to: `MOD`
## s.fluent remove
Remove a channel from Fluent<br/>
 - Usage: `s.fluent remove [channel=None]`
 - Aliases: `delete, del, and rem`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.ForumChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.fluent add
Add a channel and languages to translate between<br/>

Tip: Language 1 is the first to be converted. For example, if you expect most of the conversation to be<br/>
in english, then make english language 2 to use less api calls.<br/>
 - Usage: `s.fluent add <language1> <language2> [channel=None]`
Extended Arg Info
> ### language1: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### language2: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.ForumChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.fluent view
View all fluent channels<br/>
 - Usage: `s.fluent view`
