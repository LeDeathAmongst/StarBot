# s.paginator
Commands to manage paginators.<br/>

JSON example:<br/>
    https://pastebin.com/DiuFREBW<br/>

YAML example:<br/>
    https://pastebin.com/e9ZvhYUn<br/>
 - Usage: `s.paginator`
 - Restricted to: `MOD`
 - Aliases: `paginate and page`
## s.paginator start
Starts a paginator of the given group name<br/>
 - Usage: `s.paginator start <group_name> [page_number=1] [timeout=None]`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### timeout: Optional[int] = None
> ```
> A number without decimal places.
> ```
## s.paginator list
List all paginator groups in the server.<br/>
 - Usage: `s.paginator list`
 - Aliases: `l`
## s.paginator addpage
Add a page to a paginator group.<br/>
 - Usage: `s.paginator addpage`
 - Aliases: `ap`
### s.paginator addpage fromjson
Add a page to a paginator group.<br/>

The `page` argument should be a pastebin link containing valid json.<br/>
If `index` is not provided, the page will be added to the end of the paginator group.<br/>
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.<br/>

Example JSON: https://pastebin.com/DiuFREBW<br/>
 - Usage: `s.paginator addpage fromjson <group_name> <page> [index=None]`
 - Aliases: `fj and json`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int = None
> ```
> A number without decimal places.
> ```
### s.paginator addpage fromyaml
Add a page to a paginator group.<br/>

The `page` argument should be a pastebin link containing valid yaml.<br/>
If `index` is not provided, the page will be added to the end of the paginator group.<br/>
Otherwise, the page will be added at the specified index and the page on that index and all the pages after it will be shifted one index ahead.<br/>


Example YAML: https://pastebin.com/e9ZvhYUn<br/>
 - Usage: `s.paginator addpage fromyaml <group_name> <page> [index=None]`
 - Aliases: `fy and yaml`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int = None
> ```
> A number without decimal places.
> ```
## s.paginator info
Get information about a paginator group.<br/>
 - Usage: `s.paginator info <group_name>`
 - Aliases: `i`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.paginator editpage
Edit a page in a paginator group.<br/>
 - Usage: `s.paginator editpage <group_name> <page_number> <page>`
 - Aliases: `ep`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### page_number: int
> ```
> A number without decimal places.
> ```
## s.paginator raw
Get the raw JSON of a paginator group's page.<br/>
 - Usage: `s.paginator raw <group_name> <index>`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### index: int
> ```
> A number without decimal places.
> ```
## s.paginator create
Initiate a new paginator group.<br/>
 - Usage: `s.paginator create <group_name> [use_reactions=False] [timeout=60] [delete_on_timeout=False]`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### use_reactions: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### timeout: int = 60
> ```
> A number without decimal places.
> ```
> ### delete_on_timeout: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.paginator delete
Delete a paginator group.<br/>
 - Usage: `s.paginator delete <group_name>`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.paginator removepage
Remove a page from a paginator group.<br/>
 - Usage: `s.paginator removepage <group_name> <page_number>`
 - Aliases: `rp`
Extended Arg Info
> ### group_name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### page_number: int
> ```
> A number without decimal places.
> ```
