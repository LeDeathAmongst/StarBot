# s.zipline
Commands to interact with Zipline's API.<br/>
 - Usage: `s.zipline`
## s.zipline shorten
Shorten URL endpoint.<br/>
 - Usage: `s.zipline shorten <url>`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline info
Get information about a specific file by ID.<br/>
 - Usage: `s.zipline info <file_id>`
Extended Arg Info
> ### file_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline auth
Auth endpoints.<br/>
 - Usage: `s.zipline auth <endpoint>`
Extended Arg Info
> ### endpoint: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline random
Get a random file.<br/>
 - Usage: `s.zipline random`
## s.zipline setbaseurl
Set the base URL for Zipline.<br/>
 - Usage: `s.zipline setbaseurl <base_url>`
Extended Arg Info
> ### base_url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline upload
Upload a file from a URL or upload a file directly.<br/>
 - Usage: `s.zipline upload [url]`
Extended Arg Info
> ### url: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline version
Version endpoint.<br/>
 - Usage: `s.zipline version`
## s.zipline delete
Delete a file by its ID.<br/>
 - Usage: `s.zipline delete <file_id>`
Extended Arg Info
> ### file_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline stats
Get stats. If the token is admin, show admin stats; otherwise, show user stats.<br/>
 - Usage: `s.zipline stats`
## s.zipline register
Register your account token with your Discord user.<br/>
 - Usage: `s.zipline register <api_token>`
Extended Arg Info
> ### api_token: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline user
User endpoints.<br/>
 - Usage: `s.zipline user <endpoint> [user_id=None]`
Extended Arg Info
> ### endpoint: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### user_id: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.zipline listfiles
List all files in your account.<br/>
 - Usage: `s.zipline listfiles`
