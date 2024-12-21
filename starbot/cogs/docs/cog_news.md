# s.news
Group Command for News.<br/>
 - Usage: `s.news`
## s.news global
News from around the World.<br/>

Not considered top-headlines. May be unreliable, unknown etc.<br/>
 - Usage: `s.news global [query]`
Extended Arg Info
> ### query: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.news topglobal
Top Headlines from around the world.<br/>
 - Usage: `s.news topglobal <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.news top
Top News from a Country - County must be 2-letter ISO 3166-1 code. Supports querys to search news.<br/>

Check s.news countrycodes for a list of all possible country codes supported.<br/>
 - Usage: `s.news top <countrycode> [query]`
Extended Arg Info
> ### countrycode: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### query: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.newssetup
Instructions on how to setup news related APIs.<br/>
 - Usage: `s.newssetup`
