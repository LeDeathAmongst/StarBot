# s.timezones
See the time in all the configured timezones for this server.<br/>
 - Usage: `s.timezones`
 - Checks: `server_only`
# s.timechannelset
Manage channels which will show the time for a timezone.<br/>
 - Usage: `s.timechannelset`
 - Restricted to: `ADMIN`
 - Aliases: `tcset`
## s.timechannelset short
Get the short identifier for the main `create` command.<br/>

The list of acceptable timezones is here (the "TZ database name" column):<br/>
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List<br/>

There is a fuzzy search, so you shouldn't need to enter the region.<br/>

Please look at `s.help tcset create` for more information.<br/>

**Examples:**<br/>
- `s.tcset short New York`<br/>
- `s.tcset short UTC`<br/>
- `s.tcset short London`<br/>
- `s.tcset short Europe/London`<br/>
 - Usage: `s.timechannelset short <timezone>`
Extended Arg Info
> ### timezone: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.timechannelset remove
Delete and stop updating a channel.<br/>

For the <channel> argument, you can use its ID or mention (type #!channelname)<br/>

**Example:**<br/>
- `s.tcset remove #!channelname` (the ! is how to mention voice channels)<br/>
- `s.tcset remove 834146070094282843`<br/>
 - Usage: `s.timechannelset remove <channel>`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.timechannelset create
Set up a time channel in this server.<br/>

If you move the channel into a category, **click 'Keep Current Permissions' in the sync<br/>
permissions dialogue.**<br/>

**How to use this command:**<br/>

First, use the `s.tcset short <long_tz>` to get the short identifier for the<br/>
timezone of your choice.<br/>

Once you've got a short identifier from `tcset short`, you can use it in this command.<br/>
Simply put curly brackets, `{` and `}` around it, and it will be replaced with the time.<br/>

**For example**, running `s.tcset short new york` gives a short identifier of `fv`.<br/>
This can then be used like so:<br/>
`s.tcset create 🕑️ New York: {fv}`.<br/>

You could also use two in one, for example<br/>
`s.tcset create UK: {ni} FR: {nr}`<br/>

The default is 12 hour time, but you can use `{shortid-24h}` for 24 hour time,<br/>
eg `{ni-24h}`<br/>

**More Examples:**<br/>
- `s.tcset create 🕑️ New York: {fv}`<br/>
- `s.tcset create 🌐 UTC: {qw}`<br/>
- `s.tcset create {ni-24h} in London`<br/>
- `s.tcset create US Pacific: {qv-24h}`<br/>
 - Usage: `s.timechannelset create <string>`
Extended Arg Info
> ### string: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
