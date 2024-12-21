# s.docs (Hybrid Command)
View rich documentation for a specific node/query.<br/>

The name must be exact, or else rtfm is invoked instead.<br/>

Arguments:<br/>
- `source`: The name of the documentation to use. Defaults to the one configured with `s.setgetdocs defaultsource`.<br/>
- `query`: The documentation node/query. (`random` to get a random documentation)<br/>
 - Usage: `s.docs [source=None] [query]`
 - Slash Usage: `/docs [source=None] [query]`
 - Aliases: `getdocs, getdoc, and doc`
Extended Arg Info
> ### query: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.rtfm (Hybrid Command)
Show all items matching your search.<br/>

Arguments:<br/>
- `source`: The name of the documentation to use. Defaults to the one configured with `s.setgetdocs defaultsource`.<br/>
- `limit`: The limit of objects to be sent.<br/>
- `with_std`: Also display links to non-API documentation.<br/>
- `query`: Your search. (`events` to get all dpy events, for `discord.py`, `starbot` and `pylav` source only)<br/>
 - Usage: `s.rtfm [source=None] [limit=10] [with_std=False] [query]`
 - Slash Usage: `/rtfm [source=None] [limit=10] [with_std=False] [query]`
 - Aliases: `rtfd`
Extended Arg Info
> ### limit: Optional[int] = 10
> ```
> A number without decimal places.
> ```
> ### with_std: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### query: Optional[str] = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.listsources (Hybrid Command)
Shows a list of all sources, those that are available or those that are disabled.<br/>
 - Usage: `s.listsources [_sorted=False] [status=available]`
 - Slash Usage: `/listsources [_sorted=False] [status=available]`
 - Aliases: `listdocsources, listrtfmsources, and listsource`
Extended Arg Info
> ### _sorted: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
