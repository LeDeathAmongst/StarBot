# s.calculate (Hybrid Command)
Calculate a simple expression.<br/>
 - Usage: `s.calculate [calculation]`
 - Slash Usage: `/calculate [calculation]`
 - Aliases: `calc`
Extended Arg Info
> ### calculation: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.setcalculator (Hybrid Command)
Commands to configure Calculator.<br/>
 - Usage: `s.setcalculator`
 - Slash Usage: `/setcalculator`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.setcalculator resetsetting (Hybrid Command)
Reset a setting.<br/>
 - Usage: `s.setcalculator resetsetting <setting>`
 - Slash Usage: `/setcalculator resetsetting <setting>`
 - Checks: `server_only`
Extended Arg Info
> ### setting: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setcalculator simpleembed (Hybrid Command)
Toggle the simple embed mode.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setcalculator simpleembed <value>`
 - Slash Usage: `/setcalculator simpleembed <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setcalculator resultcodeblock (Hybrid Command)
Toggle the codeblock mode.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setcalculator resultcodeblock <value>`
 - Slash Usage: `/setcalculator resultcodeblock <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setcalculator autocalculationsignoredchannels (Hybrid Command)
The channels to ignore for the auto calculations.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Union]`<br/>
 - Usage: `s.setcalculator autocalculationsignoredchannels <value>`
 - Slash Usage: `/setcalculator autocalculationsignoredchannels <value>`
 - Checks: `server_only`
## s.setcalculator modalconfig (Hybrid Command)
Set all settings for the cog with a Discord Modal.<br/>
 - Usage: `s.setcalculator modalconfig [confirmation=False]`
 - Slash Usage: `/setcalculator modalconfig [confirmation=False]`
 - Aliases: `configmodal`
 - Checks: `server_only`
Extended Arg Info
> ### confirmation: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setcalculator reactcalculations (Hybrid Command)
Toggle the reaction calculations.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setcalculator reactcalculations <value>`
 - Slash Usage: `/setcalculator reactcalculations <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setcalculator autocalculations (Hybrid Command)
Toggle the auto calculations.<br/>

Default value: `None`<br/>
Dev: `<class 'bool'>`<br/>
 - Usage: `s.setcalculator autocalculations <value>`
 - Slash Usage: `/setcalculator autocalculations <value>`
 - Checks: `server_only`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setcalculator reactcalculationsignoredchannels (Hybrid Command)
The channels to ignore for the reaction calculations.<br/>

Default value: `[]`<br/>
Dev: `Greedy[Union]`<br/>
 - Usage: `s.setcalculator reactcalculationsignoredchannels <value>`
 - Slash Usage: `/setcalculator reactcalculationsignoredchannels <value>`
 - Checks: `server_only`
## s.setcalculator showsettings (Hybrid Command)
Show all settings for the cog with defaults and values.<br/>
 - Usage: `s.setcalculator showsettings [with_dev=False]`
 - Slash Usage: `/setcalculator showsettings [with_dev=False]`
 - Checks: `server_only`
Extended Arg Info
> ### with_dev: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
