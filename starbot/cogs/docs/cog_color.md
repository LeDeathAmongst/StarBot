# s.color
Group command for color commands<br/>
 - Usage: `s.color`
 - Aliases: `colour`
## s.color hex
Provides the RGB value and HSL value of a passed hexadecimal value.  Hexadecimal value must in the format of something like `#ffffff` or `0xffffff` to be used.<br/>
 - Usage: `s.color hex <hexa>`
Extended Arg Info
> ### hexa: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.color name
Provides the hexadecimal value, RGB value and HSL value of a passed color.  For example, pass `red` or `blue` as the name argument.<br/>
 - Usage: `s.color name <name>`
Extended Arg Info
> ### name
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.color msgshort
Enable or disable the in-message shortcut.<br/>

In-message shortcuts can be used by using the hex, rgb or name after a `#` in the middle of a message, as follows:<br/>

`#000000` (hex)<br/>
`#1,1,1` (rgb)<br/>
`#black` (named)<br/>
 - Usage: `s.color msgshort <enable>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### enable: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.color decimal
Provides the RGB value of the decimal value given.<br/>
 - Usage: `s.color decimal <decimal>`
Extended Arg Info
> ### decimal: int
> ```
> A number without decimal places.
> ```
## s.color hsl
Provides the hexadecimal value and the RGB value of the hsl value given.  Each value must have a space between them.<br/>
 - Usage: `s.color hsl <h> <s> <l>`
Extended Arg Info
> ### h: float
> ```
> A number with or without decimal places.
> ```
> ### s: float
> ```
> A number with or without decimal places.
> ```
> ### l: float
> ```
> A number with or without decimal places.
> ```
## s.color rgb
Provides the hexadecimal value and HSL value of the rgb value given.  Each value must have a space between them.  Highest argument must be 1 or 255, indicating the highest value of a single value (r, g, or b).<br/>
 - Usage: `s.color rgb <highest> <r> <g> <b>`
Extended Arg Info
> ### highest: int
> ```
> A number without decimal places.
> ```
> ### r: float
> ```
> A number with or without decimal places.
> ```
> ### g: float
> ```
> A number with or without decimal places.
> ```
> ### b: float
> ```
> A number with or without decimal places.
> ```
