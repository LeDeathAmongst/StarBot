# s.hammertime
Use this command followed by a date/time phrase to convert it to hammertime! <br/>
(a discord time format that shows correctly for everyone that sees it)<br/>

Put a person's name or mention before the time phrase to see what the time would be relative to them.<br/>

Example usage:<br/>

`s.ht 1 hour ago`<br/>
`s.ht in 1 day and 12 hrs`<br/>
`s.ht irdumb Saturday at 6:30pm`<br/>
 - Usage: `s.hammertime [user_or_time=None] [time]`
 - Aliases: `ht`
Extended Arg Info
> ### time=''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.hammertimeset
Commands to set hammertime timezone and settings<br/>
 - Usage: `s.hammertimeset`
## s.hammertimeset role
Set the timezone of a role. Everyone with this role we'll assume is in this timezone<br/>
Except for those who manually set their timezone.<br/>
 - Usage: `s.hammertimeset role <role> <tz>`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.hammertimeset timezone
Set your timezone.<br/>

If you want to unset your timezone, enter a timezone, then choose the last option<br/>
 - Usage: `s.hammertimeset timezone <tz_or_location>`
 - Aliases: `tz`
## s.hammertimeset auto
Toggle automatically converting times in messages if they have the word at/in in them<br/>
 - Usage: `s.hammertimeset auto [toggle=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### toggle: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
