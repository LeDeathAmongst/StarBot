# s.aliashook
Configure aliases for webhooks in your server<br/>
 - Usage: `s.aliashook`
 - Restricted to: `MOD`
 - Checks: `server_only`
## s.aliashook add
Add an alias for a webhook<br/>
 - Usage: `s.aliashook add <alias> <webhookUrl>`
Extended Arg Info
> ### alias
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.aliashook show
Show the saved webhook url for an alias<br/>
 - Usage: `s.aliashook show <alias>`
Extended Arg Info
> ### alias
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.aliashook remove
Remove an alias for a webhook<br/>
 - Usage: `s.aliashook remove <alias>`
Extended Arg Info
> ### alias
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.aliashook list
List all aliases for webhooks<br/>
 - Usage: `s.aliashook list`
# s.sendhook
Send a webhook<br/>

webhookUrl can be an alias<br/>
 - Usage: `s.sendhook <webhookUrl> [webhookText]`
 - Restricted to: `MOD`
Extended Arg Info
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### webhookText=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.sendhookself
Send a webhook as yourself<br/>

webhookUrl can be an alias<br/>
 - Usage: `s.sendhookself <webhookUrl> [webhookText]`
 - Restricted to: `MOD`
Extended Arg Info
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### webhookText=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.edithook
Edit a message sent by a webhook<br/>

webhookUrl can be an alias<br/>
 - Usage: `s.edithook <webhookUrl> <messageId> <webhookText>`
 - Restricted to: `MOD`
Extended Arg Info
> ### webhookUrl
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### messageId
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### webhookText
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.newhook
Create a webhook<br/>
 - Usage: `s.newhook <webhookName> <webhookImage> [channel=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### webhookName
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### webhookImage
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.listhooks
List the webhooks in a channel<br/>
 - Usage: `s.listhooks [channel=None]`
 - Restricted to: `MOD`
Extended Arg Info
> ### channel: discord.channel.TextChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
