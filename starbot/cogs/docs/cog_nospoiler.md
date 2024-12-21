# s.nospoiler
Manage the spoiler filter settings.<br/>
 - Usage: `s.nospoiler`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.nospoiler logchannel
Set the channel where the bot will log the deleted spoiler messages.<br/>

If the channel is not set, the bot will not log the deleted spoiler messages.<br/>
 - Usage: `s.nospoiler logchannel [channel=None]`
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
## s.nospoiler deleteafter
Set when the warn message should delete.<br/>

Default timeout is 10 seconds.<br/>
Timeout must be between 10 and 120 seconds.<br/>
 - Usage: `s.nospoiler deleteafter <seconds>`
## s.nospoiler message
Set the spoiler warning message.<br/>

If the message is not set, the bot will use the default message.<br/>
 - Usage: `s.nospoiler message [message]`
Extended Arg Info
> ### message: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.nospoiler useembed
Toggle the spoiler warning message to use embed or not.<br/>
 - Usage: `s.nospoiler useembed [toggle=None]`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.nospoiler settings
Show the settings.<br/>
 - Usage: `s.nospoiler settings`
 - Aliases: `view and views`
## s.nospoiler version
Shows the version of the cog.<br/>
 - Usage: `s.nospoiler version`
## s.nospoiler toggle
Toggle NoSpoiler filter on/off.<br/>
 - Usage: `s.nospoiler toggle`
## s.nospoiler togglewarnmsg
Toggle the spoiler warning message on or off.<br/>
 - Usage: `s.nospoiler togglewarnmsg [toggle=None]`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
