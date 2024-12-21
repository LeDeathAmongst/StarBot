# s.yandex
Yandex related search commands<br/>
 - Usage: `s.yandex`
## s.yandex reverse
Attach or paste the url of an image to reverse search, or reply to a message which has the image/embed with the image<br/>
 - Usage: `s.yandex reverse [url]`
 - Aliases: `rev`
Extended Arg Info
> ### url: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.google
Google search your query from Discord channel.<br/>
 - Usage: `s.google [query]`
Extended Arg Info
> ### query: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.google image
Search google images from discord<br/>
 - Usage: `s.google image [query]`
 - Aliases: `img`
Extended Arg Info
> ### query: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.google reverse
Attach or paste the url of an image to reverse search, or reply to a message which has the image/embed with the image<br/>
 - Usage: `s.google reverse [url]`
 - Aliases: `rev`
Extended Arg Info
> ### url: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.google book
Search for a book or magazine on Google Books.<br/>

This command requires an API key. If you are the bot owner,<br/>
you can follow instructions on below link for how to get one:<br/>
https://gist.github.com/ow0x/53d2dbf0f753a01b7579cd8c68edbf90<br/>

There are special keywords you can specify in the query to search in particular fields.<br/>
You can read more on that in detail over at:<br/>
https://developers.google.com/books/docs/v1/using#PerformingSearch<br/>
 - Usage: `s.google book <query>`
 - Aliases: `books`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.google autofill
Responds with a list of the Google Autofill results for a particular query.<br/>
 - Usage: `s.google autofill <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.google doodle
Responds with Google doodles of the current month.<br/>

Or doodles of specific month/year if `month` and `year` values are provided.<br/>
 - Usage: `s.google doodle [month=None] [year=None]`
Extended Arg Info
> ### month: Optional[int] = None
> ```
> A number without decimal places.
> ```
> ### year: Optional[int] = None
> ```
> A number without decimal places.
> ```
