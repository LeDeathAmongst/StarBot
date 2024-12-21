# s.linkquote (Hybrid Command)
Quote a message from a link.<br/>
 - Usage: `s.linkquote [message]`
 - Slash Usage: `/linkquote [message]`
 - Aliases: `linquoter and lq`
 - Cooldown: `3 per 10.0 seconds`
 - Checks: `server_only`
# s.setlinkquoter (Hybrid Command)
Commands to configure LinkQuoter.<br/>
 - Usage: `s.setlinkquoter`
 - Slash Usage: `/setlinkquoter`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setlinkquoter resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.setlinkquoter resetsetting <setting>`
 - Slash Usage: `/setlinkquoter resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setlinkquoter deletemessage (Hybrid Command)
Toggle deleting of messages for automatic quoting.<br/>

If automatic quoting is enabled, then Starfire will also delete messages that contain links in them.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setlinkquoter deletemessage <value>`
 - Slash Usage: `/setlinkquoter deletemessage <value>`
 - Aliases: `delete`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setlinkquoter crossserver (Hybrid Command)
Toggle cross-server quoting.<br/>

Turning this setting on will allow this server to quote other servers, and other servers to quote this one.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setlinkquoter crossserver <value>`
 - Slash Usage: `/setlinkquoter crossserver <value>`
 - Aliases: `global`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setlinkquoter webhooks (Hybrid Command)
Toggle sending message with the name and avatar of the Author of the quote (with webhooks)<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setlinkquoter webhooks <value>`
 - Slash Usage: `/setlinkquoter webhooks <value>`
 - Aliases: `webhook`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setlinkquoter whitelistchannels (Hybrid Command)
Set the channels in which auto-quoting will be enabled.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
 - Usage: `s.setlinkquoter whitelistchannels <value>`
 - Slash Usage: `/setlinkquoter whitelistchannels <value>`
 - Aliases: `whitelist`
 - Checks: `server_only`
## s.setlinkquoter modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.setlinkquoter modalconfig [confirmation=False]`
 - Slash Usage: `/setlinkquoter modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setlinkquoter deleteafter (Hybrid Command)
Set the time in seconds to delete the message after.<br/>

Default value: `0`<br/>
Dev: `<class 'int'>`<br/>
 - Usage: `s.setlinkquoter deleteafter <value>`
 - Slash Usage: `/setlinkquoter deleteafter <value>`
 - Aliases: `delete_time`
 - Checks: `server_only`
Extended Arg Info
> ### value: int
> ```
> A number without decimal places.
> ```
## s.setlinkquoter deletemessagebutton (Hybrid Command)
Toggle the delete message button on the quote messages.<br/>

Default value: `True`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setlinkquoter deletemessagebutton <value>`
 - Slash Usage: `/setlinkquoter deletemessagebutton <value>`
 - Aliases: `delete_button`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setlinkquoter blacklistchannels (Hybrid Command)
Set the channels in which auto-quoting will be disabled.<br/>

Default value: `[]`<br/>
Dev: `Greedy[GuildChannel]`<br/>
 - Usage: `s.setlinkquoter blacklistchannels <value>`
 - Slash Usage: `/setlinkquoter blacklistchannels <value>`
 - Aliases: `blacklist`
 - Checks: `server_only`
## s.setlinkquoter enabled (Hybrid Command)
Toggle automatic link-quoting.<br/>

Enabling this will make Starfire attempt to quote any message link that is sent in this server.<br/>
Starfire will ignore any message that has `no quote` in it.<br/>
If the user doesn't have permission to view the channel that they link, it will not quote.<br/>

To enable quoting from other servers, run `s.linkquoteset global`.<br/>

To prevent spam, links can be automatically quoted 3 times every 10 seconds.<br/>

Default value: `False`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setlinkquoter enabled <value>`
 - Slash Usage: `/setlinkquoter enabled <value>`
 - Aliases: `auto`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setlinkquoter showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setlinkquoter showsettings [with_dev=False]`
 - Slash Usage: `/setlinkquoter showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
