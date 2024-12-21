# s.selfassign

 - Usage: `s.selfassign`
## s.selfassign give
Allows a user to have a role assigned to them by request. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `s.selfassign give <role>`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.selfassign list
Lists roles that can be self-assigned, sorted alphabetically<br/>
 - Usage: `s.selfassign list`
 - Restricted to: `MOD`
## s.selfassign take
Allows a user to have a role removed from them by request. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `s.selfassign take <role>`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.selfassign unset
Removes a role from the allowed self-assign list. Role must be a string, NOT a snowflake (e.g. @Role)<br/>
 - Usage: `s.selfassign unset <role>`
 - Restricted to: `MOD`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.selfassign set
Flags a given role as self-assignable<br/>
 - Usage: `s.selfassign set <role>`
 - Restricted to: `MOD`
Extended Arg Info
> ### role: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
