# s.shop
Shop commands.<br/>
 - Usage: `s.shop`
 - Checks: `server_only`
## s.shop offer
Offer an item for sale in the shop.<br/>
`item`: The item to sell.<br/>
`price`: The price of the item.<br/>
`amount`: The amount of the item you want to offer.<br/>

Once you offer an item up for sell, it will show up in the `s.shop selling` command for people to buy it.<br/>
 - Usage: `s.shop offer <item> <price> <amount>`
Extended Arg Info
> ### item: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### price: int
> ```
> A number without decimal places.
> ```
> ### amount: int
> ```
> A number without decimal places.
> ```
## s.shop selling

 - Usage: `s.shop selling <user>`
Extended Arg Info
> ### user: Optional[discord.user.User]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## s.shop listitems
List items for sale in the shop.<br/>
 - Usage: `s.shop listitems`
 - Aliases: `li`
