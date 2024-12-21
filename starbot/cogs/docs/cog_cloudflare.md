# s.intel
Cloudforce One packages the vital aspects of modern threat intelligence and operations to make organizations smarter, more responsive, and more secure. Learn more at https://www.cloudflare.com/application-services/products/cloudforceone/<br/>
 - Usage: `s.intel`
## s.intel subnets
Fetch and display ASN subnets intelligence from Cloudflare.<br/>
 - Usage: `s.intel subnets <asn>`
Extended Arg Info
> ### asn: int
> ```
> A number without decimal places.
> ```
## s.intel asn
Fetch and display ASN intelligence from Cloudflare.<br/>
 - Usage: `s.intel asn <asn>`
Extended Arg Info
> ### asn: int
> ```
> A number without decimal places.
> ```
## s.intel domainhistory
Fetch and display category and domain history.<br/>
 - Usage: `s.intel domainhistory <domain>`
Extended Arg Info
> ### domain: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intel whois
Query WHOIS information for a given domain.<br/>
 - Usage: `s.intel whois <domain>`
Extended Arg Info
> ### domain: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intel ip
Query intelligence on a public IP address.<br/>
 - Usage: `s.intel ip <ip>`
Extended Arg Info
> ### ip: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.intel domain
Query Cloudflare API for domain intelligence and check blocklist status.<br/>
 - Usage: `s.intel domain <domain>`
Extended Arg Info
> ### domain: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.urlscanner
With Cloudflare’s URL Scanner, you have the ability to investigate the details of a domain, IP, URL, or ASN. Cloudflare’s URL Scanner is available in the Security Center of the Cloudflare dashboard, Cloudflare Radar and the Cloudflare API.<br/>

Learn more at https://developers.cloudflare.com/radar/investigate/url-scanner/<br/>
 - Usage: `s.urlscanner`
## s.urlscanner search
Search for URL scans by date and webpage requests.<br/>
 - Usage: `s.urlscanner search <query>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.urlscanner har
Fetch the HAR of a scan by the scan ID<br/>
 - Usage: `s.urlscanner har <scan_id>`
Extended Arg Info
> ### scan_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.urlscanner results
Get the result of a URL scan by its ID.<br/>
 - Usage: `s.urlscanner results <scan_id>`
Extended Arg Info
> ### scan_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.urlscanner create
Start a new scan for the provided URL.<br/>
 - Usage: `s.urlscanner create <url>`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.urlscanner scan
Scan a URL using Cloudflare URL Scanner and return the verdict.<br/>
 - Usage: `s.urlscanner scan <url>`
Extended Arg Info
> ### url: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.urlscanner autoscan
Enable or disable automatic URL scans.<br/>
 - Usage: `s.urlscanner autoscan <enabled>`
Extended Arg Info
> ### enabled: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.urlscanner screenshot
Get the screenshot of a scan by its scan ID<br/>
 - Usage: `s.urlscanner screenshot <scan_id>`
Extended Arg Info
> ### scan_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
