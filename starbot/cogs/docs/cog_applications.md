# s.appset
Configure the application system.<br/>
 - Usage: `s.appset`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.appset setchannel
Set the channel where applications will be sent.<br/>
 - Usage: `s.appset setchannel <channel>`
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
## s.appset setlogchannel
Set the channel for application logs.<br/>
 - Usage: `s.appset setlogchannel <channel>`
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
## s.appset setmessage
Set the message for the application embed.<br/>
 - Usage: `s.appset setmessage <message>`
Extended Arg Info
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.createapplyembed
Create an embed with a dropdown for users to start applications.<br/>
 - Usage: `s.createapplyembed`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
# s.apps
Manage application types and questions.<br/>
 - Usage: `s.apps`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
# s.apply
Start a new application.<br/>
 - Usage: `s.apply`
 - Checks: `server_only`
# s.appstats
View application statistics.<br/>
 - Usage: `s.appstats`
 - Checks: `server_only`
# s.appsearch
Search for applications by user or type.<br/>
 - Usage: `s.appsearch <search_term>`
 - Checks: `server_only`
Extended Arg Info
> ### search_term: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
