# s.runcode (Hybrid Command)
Run a code in a langage, with Wandbox API.<br/>

Arguments:<br/>
- `verbose`: Without this mode, only the programme output will be sent, without any additional information. In case of an error, it will be used automatically.<br/>
- `language`: If not specified, the command will try to "guess" with the file extension or Discord Markdown syntax.<br/>
- `parameters`: Optional option to send with the request. `engine:1/cpython-3.10.2`, `input:<input>`, `compiler_options:option1|option2|option3` and `runtime_options:option1|option2|option3`.<br/>
- `code`: May be normal code, but also an attached file, or a link from [pastebin](https://pastebin.com), [Github gist](https://gist.github.com) or another "raw" website.<br/>
          If you use a link, your command must end with this syntax: `link=<link>` (no space around `=`). You may also not provide it and upload an attachment instead.<br/>
 - Usage: `s.runcode [verbose=False] [language=None] [parameters=None] [code]`
 - Slash Usage: `/runcode [verbose=False] [language=None] [parameters=None] [code]`
 - Aliases: `executecode`
Extended Arg Info
> ### verbose: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### code: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.runtio (Hybrid Command)
Run a code in a langage, with Tio API.<br/>

Arguments:<br/>
- `verbose`: Without this mode, only the programme output will be sent, without any additional information. In case of an error, it will be used automatically.<br/>
- `language`: If not specified, the command will try to "guess" with the file extension or Discord Markdown syntax.<br/>
- `parameters`: Optional option to send with the request. `inputs:input1|input2|input3`, `compiler_flags:flag1|flag2|flag3`, `command_line_options:option1|option2|option3` and `args:arg1|arg2|arg3`.<br/>
- `code`: May be normal code, but also an attached file, or a link from [pastebin](https://pastebin.com), [Github gist](https://gist.github.com) or another "raw" website.<br/>
          If you use a link, your command must end with this syntax: `link=<link>` (no space around `=`). You may also not provide it and upload an attachment instead.<br/>
 - Usage: `s.runtio <verbose> <language> [parameters=None] [code]`
 - Slash Usage: `/runtio <verbose> <language> [parameters=None] [code]`
 - Aliases: `tiorun`
Extended Arg Info
> ### verbose: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### code: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.setruncode (Hybrid Command)
View RunCode options.<br/>
 - Usage: `s.setruncode`
 - Slash Usage: `/setruncode`
## s.setruncode listengines (Hybrid Command)
Shows a list of all the available engines for a specified language, only for Wandbox API.<br/>

Arguments:<br/>
- `language`: The language name.<br/>
 - Usage: `s.setruncode listengines <language>`
 - Slash Usage: `/setruncode listengines <language>`
Extended Arg Info
> ### language: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setruncode listidentifiers (Hybrid Command)
Lists all the languages identifiers recognized by the bot, only for Wandbox API.<br/>
 - Usage: `s.setruncode listidentifiers`
 - Slash Usage: `/setruncode listidentifiers`
## s.setruncode listlanguages (Hybrid Command)
Shows a list of all the available languages, or Wandbox or Tio API.<br/>
 - Usage: `s.setruncode listlanguages <api>`
 - Slash Usage: `/setruncode listlanguages <api>`
## s.setruncode listextensions (Hybrid Command)
Lists all the languages extensions.<br/>
 - Usage: `s.setruncode listextensions`
 - Slash Usage: `/setruncode listextensions`
