# /email (Slash Command)
Send an email<br/>
 - Usage: `/email <sender> <recipient> <subject> <message> [attachment1] [attachment2] [attachment3]`
 - `sender:` (Required) …
 - `recipient:` (Required) …
 - `subject:` (Required) …
 - `message:` (Required) …
 - `attachment1:` (Optional) …
 - `attachment2:` (Optional) …
 - `attachment3:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### sender: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### recipient: str
> - Autocomplete: True
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### subject: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str
> - Autocomplete: False
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### attachment1: discord.message.Attachment
> - Autocomplete: False
> - Default: None
> 
> …
> 
> Represents an attachment from Discord.
> 
>     
> ### attachment2: discord.message.Attachment
> - Autocomplete: False
> - Default: None
> 
> …
> 
> Represents an attachment from Discord.
> 
>     
> ### attachment3: discord.message.Attachment
> - Autocomplete: False
> - Default: None
> 
> …
> 
> Represents an attachment from Discord.
> 
>     
# s.email
Send an email<br/>

Attach files to the command to send them as attachments<br/>
 - Usage: `s.email <sender> <recipient> <subject> <message>`
 - Checks: `server_only`
Extended Arg Info
> ### sender: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### recipient: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### subject: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.addemail
Add an email account<br/>
 - Usage: `s.addemail`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `addgmail`
 - Checks: `server_only`
# s.editemail
Edit an email account<br/>
 - Usage: `s.editemail <email>`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `editgmail`
 - Checks: `server_only`
Extended Arg Info
> ### email: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.deleteemail
Delete an email account<br/>
 - Usage: `s.deleteemail <email>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### email: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.gmailroles
Set the roles allowed to send emails<br/>
 - Usage: `s.gmailroles <roles>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### *roles: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
# s.gmailsettings
View the email settings for the server<br/>
 - Usage: `s.gmailsettings`
 - Checks: `server_only`
# s.gmailhelp
Get instructions for setting up Gmail<br/>
 - Usage: `s.gmailhelp`
 - Aliases: `gmailsetup`
 - Checks: `server_only`
