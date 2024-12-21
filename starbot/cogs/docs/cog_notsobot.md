# s.magik
Apply magik to an image.<br/>
 - Usage: `s.magik [urls=None] [scale=2] [scale_msg=]`
 - Aliases: `imagemagic, imagemagick, magic, magick, cas, and liquid`
Extended Arg Info
> ### scale: int = 2
> ```
> A number without decimal places.
> ```
> ### scale_msg: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.gmagik
Attempt to do magik on a gif<br/>
 - Usage: `s.gmagik [urls=None] [frame_delay=1]`
Extended Arg Info
> ### frame_delay: int = 1
> ```
> A number without decimal places.
> ```
# s.caption
Add caption to an image<br/>

`[urls]` are the image urls or users or previous images in chat to add a caption to.<br/>
`[text=Caption]` is the text to caption on the image.<br/>
`[color=white]` is the color of the text.<br/>
`[size=40]` is the size of the text<br/>
`[x=0]` is the height the text starts at between 0 and 100% where 0 is the top and 100 is the bottom of the image.<br/>
`[y=0]` is the width the text starts at between 0 and 100% where 0 is the left and 100 is the right of the image.<br/>
 - Usage: `s.caption [urls=None] [text=Caption] [color=white] [size=40] [x=0] [y=0]`
Extended Arg Info
> ### text: str = 'Caption'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### color: str = 'white'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### size: int = 40
> ```
> A number without decimal places.
> ```
> ### x: int = 0
> ```
> A number without decimal places.
> ```
> ### y: int = 0
> ```
> A number without decimal places.
> ```
# s.triggered
Generate a Triggered GIF for a user or image<br/>
 - Usage: `s.triggered [urls=None]`
# s.aesthetics
Returns inputed text in aesthetics<br/>
 - Usage: `s.aesthetics <text>`
 - Aliases: `aes`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.ascii
Convert text into ASCII<br/>
 - Usage: `s.ascii <text>`
 - Aliases: `expand`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.iascii
Generate an ascii art image of last image in chat or from URL<br/>
 - Usage: `s.iascii [urls=None]`
 - Checks: `NotSoBot`
# s.gascii
Gif to ASCII<br/>
 - Usage: `s.gascii [urls=None]`
 - Checks: `NotSoBot`
# s.rip
Generate tombstone image with name and optional text<br/>
 - Usage: `s.rip [name=None] [text]`
Extended Arg Info
> ### name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.merge
Merge/Combine Two Photos<br/>

`[vertical=True]` `true` or `false` to merge vertically.<br/>
`[urls]` The Image URL's you want to merge together. If not supplied<br/>
images are searched from message history.<br/>
 - Usage: `s.merge [vertical=True] <urls>`
Extended Arg Info
> ### vertical: Optional[bool] = True
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.emojify
Replace characters in text with emojis<br/>
 - Usage: `s.emojify <txt>`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.jpeg
Add more JPEG to an Image<br/>

Needs More JPEG!<br/>
`[urls]` is optional, if not provided will search chat for a valid image.<br/>
`[quality]` is the quality of the new jpeg image to make<br/>
 - Usage: `s.jpeg [urls=None] [quality=1]`
 - Aliases: `needsmorejpeg, jpegify, and magik2`
Extended Arg Info
> ### quality: int = 1
> ```
> A number without decimal places.
> ```
# s.vw
Add vaporwave flavours to an image<br/>
 - Usage: `s.vw [urls=None] [txt]`
 - Aliases: `vaporwave, vape, and vapewave`
Extended Arg Info
> ### txt: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.minecraftachievement
Generate a Minecraft Achievement<br/>
 - Usage: `s.minecraftachievement <txt>`
 - Aliases: `achievement`
Extended Arg Info
> ### txt: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.watermark
Add a watermark to an image<br/>

`[urls]` are the image urls or users or previous images in chat to add a watermark to.<br/>
`[mark]` is the image to use as the watermark. By default the brazzers icon is used.<br/>
`[x=0]` is the height the watermark will be at between 0 and 100% where 0 is the top and 100 is the bottom of the image.<br/>
`[y=0]` is the width the watermark will be at between 0 and 100% where 0 is the left and 100 is the right of the image.<br/>
`[transparency=0]` is a value from 0 to 100 which determines the percentage the watermark will be transparent.<br/>
 - Usage: `s.watermark [urls=None] [mark=None] [x=0] [y=0] [transparency=0]`
 - Aliases: `wm`
Extended Arg Info
> ### mark: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### x: int = 0
> ```
> A number without decimal places.
> ```
> ### y: int = 0
> ```
> A number without decimal places.
> ```
> ### transparency: Union[int, float] = 0
> ```
> A number without decimal places.
> ```
# s.glitch
Glitch a gif or png<br/>
 - Usage: `s.glitch [urls=None] [iterations=None] [amount=None] [seed=None]`
 - Aliases: `jpglitch`
Extended Arg Info
> ### iterations: int = None
> ```
> A number without decimal places.
> ```
> ### amount: int = None
> ```
> A number without decimal places.
> ```
> ### seed: int = None
> ```
> A number without decimal places.
> ```
# s.pixelate
Pixelate an image<br/>
 - Usage: `s.pixelate [urls=None] [pixels=9]`
 - Aliases: `pixel`
Extended Arg Info
> ### pixels: int = 9
> ```
> A number without decimal places.
> ```
# s.waaw
Mirror an image vertically right to left<br/>
 - Usage: `s.waaw [urls=None]`
 - Aliases: `magik3 and mirror`
# s.haah
Mirror an image vertically left to right<br/>
 - Usage: `s.haah [urls=None]`
 - Aliases: `magik4 and mirror2`
# s.woow
Mirror an image horizontally top to bottom<br/>
 - Usage: `s.woow [urls=None]`
 - Aliases: `magik5 and mirror3`
# s.hooh
Mirror an image horizontally bottom to top<br/>
 - Usage: `s.hooh [urls=None]`
 - Aliases: `magik6 and mirror4`
# s.flipimg
Rotate an image 180 degrees<br/>
 - Usage: `s.flipimg [urls=None]`
# s.flop
Flip an image horizontally<br/>
 - Usage: `s.flop [urls=None]`
# s.invert
Invert the colours of an image<br/>
 - Usage: `s.invert [urls=None]`
 - Aliases: `inverse and negate`
# s.rotate
Rotate image X degrees<br/>
 - Usage: `s.rotate [degrees=90] [urls=None]`
Extended Arg Info
> ### degrees: int = 90
> ```
> A number without decimal places.
> ```
