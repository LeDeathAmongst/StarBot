# s.automod (Hybrid Command)
Commnads for interacting with automod<br/>
 - Usage: `s.automod`
 - Slash Usage: `/automod`
 - Checks: `server_only`
## s.automod rules (Hybrid Command)
View the servers current automod rules<br/>
 - Usage: `s.automod rules`
 - Slash Usage: `/automod rules`
 - Restricted to: `MOD`
 - Aliases: `list, rule, and view`
 - Checks: `server_only`
## s.automod triggers (Hybrid Command)
View the servers saved automod triggers<br/>
 - Usage: `s.automod triggers`
 - Slash Usage: `/automod triggers`
 - Restricted to: `MOD`
 - Aliases: `trigger`
 - Checks: `server_only`
## s.automod create (Hybrid Command)
Create automod rules, triggers, and actions<br/>
 - Usage: `s.automod create`
 - Slash Usage: `/automod create`
 - Restricted to: `ADMIN`
 - Aliases: `c`
 - Checks: `server_only`
### s.automod create action (Hybrid Command)
Create a saved action for use in automod Rules.<br/>

- `<name>` The name of this action for reference later.<br/>
Usage: `<action>`<br/>
- `message:` The message to send to a user when triggered.<br/>
- `channel:` The channel to send a notification to.<br/>
- `duration:` How long to timeout the user for. Max 28 days.<br/>
Only one of these options can be applied at a time.<br/>
Examples:<br/>
    `s.automod create action grumpyuser message: You're being too grumpy`<br/>
    `s.automod create action notifymods channel: #modlog`<br/>
    `s.automod create action 2hrtimeout duration: 2 hours`<br/>
 - Usage: `s.automod create action <name> <action>`
 - Slash Usage: `/automod create action <name> <action>`
 - Restricted to: `ADMIN`
 - Aliases: `a`
 - Checks: `server_only`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.automod create rule (Hybrid Command)
Create an automod rule in the server<br/>

Usage:<br/>
- `trigger:` The name of a saved trigger.<br/>
- `actions:` The name(s) of saved actions.<br/>
- `enabled:` yes/true/t to enable this rule right away.<br/>
- `roles:` The roles that are exempt from this rule.<br/>
- `channels:` The channels that are exempt from this rule.<br/>
- `reason:` An optional reason for creating this rule.<br/>

Example:<br/>
    `s.automod create rule trigger: mytrigger actions: timeoutuser notifymods enabled: true roles: @mods`<br/>
    Will create an automod rule with the saved trigger `mytrigger` and<br/>
    the saved actions `timeoutuser` and `notifymods`.<br/>
 - Usage: `s.automod create rule <name> <rule>`
 - Slash Usage: `/automod create rule <name> <rule>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.automod create trigger (Hybrid Command)
Create a saved trigger for use in automod Rules.<br/>

- `<name>` The name of this trigger for reference later.<br/>
Usage: `<trigger>`<br/>
- `allows:` A space separated list of words to allow.<br/>
- `keywords:` A space separated list of words to filter.<br/>
- `mentions:` The number of user/role mentions that would trigger this rule (0-50).<br/>
- `presets:` Any combination of discord presets. e.g. `profanity`, `sexual_content`, or `slurs`.<br/>
- `regex:` A space separated list of regex patterns to include.<br/>
Note: If you want to use `mentions` you cannot also use `presets`, `keywords` or<br/>
`regex` in the same trigger. Likewise if you use any `presets` you cannot<br/>
use `keywords`, `regex`, or `mentions`.<br/>
Examples:<br/>
    `s.automod create trigger mytrigger regex: ^b(a|@)dw(o|0)rd(s|5)$`<br/>
 - Usage: `s.automod create trigger <name> <trigger>`
 - Slash Usage: `/automod create trigger <name> <trigger>`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.automod actions (Hybrid Command)
View the servers saved automod actions<br/>
 - Usage: `s.automod actions`
 - Slash Usage: `/automod actions`
 - Restricted to: `MOD`
 - Aliases: `action`
 - Checks: `server_only`
