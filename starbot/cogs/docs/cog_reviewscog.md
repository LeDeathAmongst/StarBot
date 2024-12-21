# s.review
Review commands.<br/>
 - Usage: `s.review`
 - Checks: `server_only`
## s.review list
List all reviews.<br/>
 - Usage: `s.review list`
## s.review export
Export reviews to a CSV or PDF file.<br/>
 - Usage: `s.review export <file_format>`
Extended Arg Info
> ### file_format: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.review submit
Submit a review for approval.<br/>
 - Usage: `s.review submit`
## s.review setchannel
Set the channel where approved reviews will be posted.<br/>
 - Usage: `s.review setchannel <channel>`
Extended Arg Info
> ### channel: discord.channel.TextChannel
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.review approve
Approve a review.<br/>
 - Usage: `s.review approve <review_id>`
Extended Arg Info
> ### review_id: int
> ```
> A number without decimal places.
> ```
## s.review remove
Remove a review.<br/>
 - Usage: `s.review remove <review_id>`
Extended Arg Info
> ### review_id: int
> ```
> A number without decimal places.
> ```
