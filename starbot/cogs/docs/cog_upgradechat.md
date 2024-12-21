# s.upgradechat
Base command for cog settings<br/>
 - Usage: `s.upgradechat`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `upchat`
 - Checks: `server_only`
## s.upgradechat delproduct
Delete an Upgrade.Chat product by UUID<br/>
 - Usage: `s.upgradechat delproduct <uuid>`
Extended Arg Info
> ### uuid: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.upgradechat view
View your current products<br/>
 - Usage: `s.upgradechat view`
## s.upgradechat purchases
View user purchase history<br/>
 - Usage: `s.upgradechat purchases [member]`
Extended Arg Info
> ### member: Union[discord.member.Member, int] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
>     7. Lookup by server nickname.
> 
>     
## s.upgradechat ratio
Set the worth of 1 unit of real currency to economy credits<br/>

for example, if `credit_worth` is 100, then $1 = 100 Credits<br/>
 - Usage: `s.upgradechat ratio <credit_worth>`
Extended Arg Info
> ### credit_worth: int
> ```
> A number without decimal places.
> ```
## s.upgradechat tokens
Set your Upgrade.Chat api tokens<br/>
By using this feature it is assumed that you are already familiar with Upgrade.Chat<br/>

1. Create your api keys here: https://upgrade.chat/developers<br/>

2. Copy your client ID and Client Secret<br/>

3. Run this command with your credentials<br/>

**Enjoy!**<br/>
 - Usage: `s.upgradechat tokens <client_id> <client_secret>`
Extended Arg Info
> ### client_id: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### client_secret: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.upgradechat addproduct
Add an Upgrade.Chat product by UUID<br/>

This can be any type of product, either subscription or one-time purchase.<br/>
Users will be accredited based on `amount spend * conversion ratio`.<br/>
Transactions can only be claimed once.<br/>
 - Usage: `s.upgradechat addproduct <uuid>`
Extended Arg Info
> ### uuid: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.upgradechat logchannel
Set log channel for claims<br/>
 - Usage: `s.upgradechat logchannel <channel>`
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
## s.upgradechat message
Set the message the bot sends when a user claims a purchase<br/>

Valid placeholders:<br/>
{mention} - mention the user<br/>
{username} - the users discord name<br/>
{displayname} - the users nickname(if they have one)<br/>
{uid} - the users Discord ID<br/>
{server} - server name<br/>
{creditsname} - name of the currency in your server<br/>
{amount} - the amount of credits the user has claimed<br/>

set to `default` to use the default message<br/>
 - Usage: `s.upgradechat message <claim_message>`
Extended Arg Info
> ### claim_message: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.claim
Claim your Upgrade.Chat purchases!<br/>
 - Usage: `s.claim`
 - Cooldown: `1 per 60.0 seconds`
 - Checks: `server_only`
