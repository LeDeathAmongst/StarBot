# s.setjsonrequest
Change the configurations for s.jsonrequest<br/>

All configurations are server-based.<br/>

By default, all domains are allowed. When you add a domain below, the settings switch to a whitelist model where only added domains will work.<br/>
 - Usage: `s.setjsonrequest`
 - Restricted to: `MOD`
 - Aliases: `setjsonreq and setjreq`
 - Checks: `server_only`
## s.setjsonrequest add
Add an allowed domain to the list<br/>

Format: api.sampleapis.com<br/>

The bot will check the domain against [Python's urlparse of json requests](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse).<br/>
 - Usage: `s.setjsonrequest add <domain>`
Extended Arg Info
> ### domain
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setjsonrequest list
List current settings<br/>
 - Usage: `s.setjsonrequest list`
## s.setjsonrequest remove
Remove an allowed domain to the list<br/>
 - Usage: `s.setjsonrequest remove <domain>`
Extended Arg Info
> ### domain
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.jsonrequest
Makes a json request<br/>
 - Usage: `s.jsonrequest <url>`
 - Aliases: `jsonreq and jreq`
Extended Arg Info
> ### url
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
