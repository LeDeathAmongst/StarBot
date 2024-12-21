# s.aiemote
Totally not glorified sentiment analysis™<br/>

Picks a reaction for a message using gpt-3.5-turbo<br/>

To get started, please add a channel to the whitelist with:<br/>
`s.aiemote allow <#channel>`<br/>
 - Usage: `s.aiemote`
 - Restricted to: `ADMIN`
## s.aiemote optin
Opt in of sending your message to OpenAI (bot-wide)<br/>

This will allow the bot to react to your messages<br/>
 - Usage: `s.aiemote optin`
## s.aiemote allow
Add a channel to the whitelist<br/>

*Arguments*<br/>
- `<channel>` The mention of channel<br/>
 - Usage: `s.aiemote allow <channel>`
 - Restricted to: `ADMIN`
 - Aliases: `add`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.aiemote remove
Remove a channel from the whitelist<br/>

*Arguments*<br/>
- `<channel>` The mention of channel<br/>
 - Usage: `s.aiemote remove <channel>`
 - Restricted to: `ADMIN`
 - Aliases: `rm`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.aiemote whitelist
List all channels in the whitelist <br/>
 - Usage: `s.aiemote whitelist`
 - Restricted to: `ADMIN`
## s.aiemote optout
Opt out of sending your message to OpenAI (bot-wide)<br/>

The bot will no longer react to your messages<br/>
 - Usage: `s.aiemote optout`
## s.aiemote optinbydefault
Toggles whether users are opted in by default in this server<br/>

This command is disabled for servers with more than 150 members.<br/>
 - Usage: `s.aiemote optinbydefault`
 - Restricted to: `ADMIN`
