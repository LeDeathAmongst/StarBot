# s.invoketag
Manually invoke a tag with its name and arguments.<br/>

Restricting this command with permissions in servers will restrict all members from invoking tags.<br/>

**Examples:**<br/>
`s.invoketag searchitem trophy`<br/>
`s.invoketag donate`<br/>
 - Usage: `s.invoketag <response> <tag_name> [args]`
Extended Arg Info
> ### response: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### tag_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### args: Optional[str] = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.tags
View all tags and aliases.<br/>

This command will show global tags if run in DMs.<br/>

**Example:**<br/>
`s.tags`<br/>
 - Usage: `s.tags`
# s.tag
Tag management with TagScript.<br/>

These commands use TagScriptEngine.<br/>
Read the [TagScript documentation](https://seina-cogs.readthedocs.io/en/latest/) to learn how to use TagScript blocks.<br/>
 - Usage: `s.tag`
 - Aliases: `customcom, cc, and alias`
 - Checks: `server_only`
## s.tag append
Add text to a tag's TagScript.<br/>

**Example:**<br/>
`s.tag append rickroll Never gonna let you down!`<br/>
 - Usage: `s.tag append <tag> <tagscript>`
 - Restricted to: `MOD`
## s.tag raw
Get a tag's raw content.<br/>

The sent TagScript will be escaped from Discord style formatting characters.<br/>

**Example:**<br/>
`s.tag raw noping`<br/>
 - Usage: `s.tag raw <tag>`
## s.tag pastebin
Add a tag with a Pastebin link.<br/>

**Example:**<br/>
`s.tag pastebin starwarsopeningcrawl https://pastebin.com/CKjn6uYv`<br/>
 - Usage: `s.tag pastebin <tag_name> <link>`
 - Restricted to: `MOD`
 - Aliases: `++`
## s.tag docs
Search the TagScript documentation for a block.<br/>

https://seina-cogs.readthedocs.io/en/latest/<br/>

**Example:**<br/>
`s.tag docs embed`<br/>
 - Usage: `s.tag docs [keyword=None]`
Extended Arg Info
> ### keyword: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tag backup
Backup all the tag data for your server.<br/>
 - Usage: `s.tag backup`
 - Restricted to: `ADMIN`
## s.tag edit
Edit a tag's TagScript.<br/>

The passed tagscript will replace the tag's current tagscript.<br/>
View the [TagScript docs](https://seina-cogs.readthedocs.io/en/latest/blocks.html) to find information on how to write valid tagscript.<br/>

**Example:**<br/>
`s.tag edit rickroll Never gonna give you up!`<br/>
 - Usage: `s.tag edit <tag> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `e`
## s.tag restore
Restore all tag data for your server.<br/>

This command will restore all data from the backup file.<br/>
This command will also delete all the previously made tags if<br/>
not present in the backup file.<br/>

You can pass a message ID, a ChannelID-MessageID pair, or a message link<br/>
to the `message` argument.<br/>
Alternatively, if you want to reply to a message, pass anything to the<br/>
message argument while replying to a message.<br/>
 - Usage: `s.tag restore <message>`
 - Restricted to: `ADMIN`
## s.tag alias
Add an alias for a tag.<br/>

        Adding an alias to the tag will make the tag invokable using the alias or the tag name.<br/>
        In the example below, running `s.donation` will invoke the `donate` tag.<br/>
​<br/>
        **Example:**<br/>
        `s.tag alias donate donation`<br/>
 - Usage: `s.tag alias <tag> <alias>`
 - Restricted to: `MOD`
## s.tag usage
See tag usage stats.<br/>

**Example:**<br/>
`s.tag usage`<br/>
 - Usage: `s.tag usage`
 - Aliases: `stats`
## s.tag unalias
Remove an alias for a tag.<br/>

​The tag will still be able to be used under its original name.<br/>
You can delete the original tag with the `s.tag remove` command.<br/>

**Example:**<br/>
`tag unalias donate donation`<br/>
 - Usage: `s.tag unalias <tag> <alias>`
 - Restricted to: `MOD`
## s.tag remove
Permanently delete a tag.<br/>

If you want to remove a tag's alias, use `s.tag unalias`.<br/>

**Example:**<br/>
`s.tag remove RickRoll`<br/>
 - Usage: `s.tag remove <tag>`
 - Restricted to: `MOD`
 - Aliases: `delete and -`
## s.tag search
Search for tags by name.<br/>

**Example:**<br/>
`s.tag search notsupport`<br/>
 - Usage: `s.tag search <keyword>`
Extended Arg Info
> ### keyword: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.tag list
View all stored tags on this server.<br/>

To view info on a specific tag, use `s.tag info`.<br/>

**Example:**<br/>
`s.tag list`<br/>
 - Usage: `s.tag list`
## s.tag add
Add a tag with TagScript.<br/>

[Tag usage guide](https://seina-cogs.readthedocs.io/en/latest/tags/blocks.html#usage)<br/>

**Example:**<br/>
`s.tag add lawsofmotion {embed(title):Newton's Laws of motion}<br/>
{embed(description): According to all known laws of aviation, there is no way a bee should be able to fly.}`<br/>
 - Usage: `s.tag add <tag_name> <tagscript>`
 - Restricted to: `MOD`
 - Aliases: `create and +`
## s.tag info
Show information about a tag.<br/>

You can view meta information for a tag on this server or a global tag.<br/>
If a tag on this server has the same name as a global tag, it will show the server tag.<br/>

**Example:**<br/>
`s.tag info notsupport`<br/>
 - Usage: `s.tag info <tag>`
