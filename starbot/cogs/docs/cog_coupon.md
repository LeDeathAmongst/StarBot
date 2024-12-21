# s.coupon
Coupon commands.<br/>
 - Usage: `s.coupon`
 - Checks: `server_only and pred`
## s.coupon create
Generates a unique coupon code.<br/>
 - Usage: `s.coupon create <credits>`
 - Restricted to: `ADMIN`
 - Checks: `pred`
Extended Arg Info
> ### credits: int
> ```
> A number without decimal places.
> ```
## s.coupon list
Shows active coupon codes.<br/>
 - Usage: `s.coupon list`
 - Restricted to: `ADMIN`
 - Checks: `pred`
## s.coupon clearall
Clears all unclaimed coupons.<br/>
 - Usage: `s.coupon clearall`
 - Restricted to: `MOD`
 - Checks: `pred`
## s.coupon redeem
Redeems a coupon code.<br/>
 - Usage: `s.coupon redeem <coupon>`
 - Checks: `pred`
Extended Arg Info
> ### coupon: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
