# s.messagestats
Commands for tracking how many messages matched patterns.<br/>
 - Usage: `s.messagestats`
 - Restricted to: `ADMIN`
## s.messagestats notifychannel
Whenever a message containing this word appears in this server a message is sent to the set channel.<br/>
 - Usage: `s.messagestats notifychannel <channel> <word>`
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
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats delcounter
Deletes the counter for this word.<br/>
 - Usage: `s.messagestats delcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats resetcounter
Resets the counter of the word to 0 and the started-counting date to now.<br/>
 - Usage: `s.messagestats resetcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats list
Lists all words we are looking for in this server with their stored info.<br/>
 - Usage: `s.messagestats list`
## s.messagestats dontnotifychannel
Turn off the notifychannel trigger.<br/>
 - Usage: `s.messagestats dontnotifychannel <channel> <word>`
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
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats checkcounter
Checks how many messages containing this word have been sent since we started counting.<br/>
 - Usage: `s.messagestats checkcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats info
Checks the complete info of a tracked word.<br/>
 - Usage: `s.messagestats info <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats notifyme
Whenever the word appears in a message on this server you will receive a DM from this bot.<br/>
 - Usage: `s.messagestats notifyme <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats addcounter
Adds a counter for how many times a message with this word has been sent in this server.<br/>
 - Usage: `s.messagestats addcounter <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.messagestats dontnotifyme
Turn off the notifyme trigger.<br/>
 - Usage: `s.messagestats dontnotifyme <word>`
Extended Arg Info
> ### word: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
