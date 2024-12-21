# s.madtranslate
Translate something into lots of languages, then back to English!<br/>

**Examples:**<br/>
- `s.mtrans This is a sentence.`<br/>
- `s.mtrans 25 Here's another one.`<br/>

At the bottom of the output embed is a count-seed pair. You can use this with<br/>
the `mtransseed` command to use the same language set.<br/>
 - Usage: `s.madtranslate [count=15] <text_to_translate>`
 - Aliases: `mtranslate and mtrans`
Extended Arg Info
> ### count: Optional[int] = 15
> ```
> A number without decimal places.
> ```
> ### text_to_translate: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.mtransseed
Use a count-seed pair to (hopefully) get reproducible results.<br/>

They may be unreproducible if Google Translate changes its translations.<br/>

The count-seed pair is obtained from the main command, `mtrans`, in the embed footer.<br/>

**Examples:**<br/>
- `s.mtrans 15-111111 This is a sentence.`<br/>
- `s.mtrans 25-000000 Here's another one.`<br/>
 - Usage: `s.mtransseed <count_seed> <text_to_translate>`
Extended Arg Info
> ### count_seed: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text_to_translate: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
