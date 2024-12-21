# s.roleplay
Role play configuration.<br/>

This is a group command, so you can use it to configure the roleplay for a channel.<br/>

Get started with `s.roleplay channel`.<br/>
 - Usage: `s.roleplay`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
## s.roleplay delete
Automatically delete messages in the role play channel after time has passed.<br/>

The time is in minutes.<br/>

The default is disabled.<br/>

**Examples:**<br/>
- `s.roleplay delete 5` - delete after 5 mins<br/>
- `s.roleplay delete 30` - delete after 30 mins<br/>
- `s.roleplay delete` - disable deletion<br/>
 - Usage: `s.roleplay delete <delete_after>`
Extended Arg Info
> ### delete_after: Optional[int]
> ```
> A number without decimal places.
> ```
## s.roleplay settings
View the current settings for the roleplay.<br/>
 - Usage: `s.roleplay settings`
## s.roleplay channel
Set the channel for the roleplay.<br/>

Leave blank to disable.<br/>

**Examples:**<br/>
- `s.roleplay channel` - disable roleplay<br/>
- `s.roleplay channel #roleplay` - set the channel to #roleplay<br/>
 - Usage: `s.roleplay channel <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.roleplay radiotitle
Set a title for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `s.roleplay radiotitle New radio transmission detected` - the default<br/>
 - Usage: `s.roleplay radiotitle <title>`
Extended Arg Info
> ### title: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.roleplay radio
Enable or disable radio.<br/>

The default is disabled.<br/>

**Examples:**<br/>
- `s.roleplay radio true` - enable radio mode<br/>
- `s.roleplay radio false` - disable radio mode<br/>
 - Usage: `s.roleplay radio <radio>`
Extended Arg Info
> ### radio: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.roleplay radioimage
Set an image for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `s.roleplay radioimage https://i.imgur.com/example.png`<br/>
- `s.roleplay radioimage` - reset to none<br/>
 - Usage: `s.roleplay radioimage <image_url>`
Extended Arg Info
> ### image_url: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.roleplay embed
Enable or disable embeds.<br/>

The default is disabled.<br/>

**Examples:**<br/>
- `s.roleplay embed true` - enable<br/>
- `s.roleplay embed false` - disable<br/>
 - Usage: `s.roleplay embed <embed>`
Extended Arg Info
> ### embed: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.roleplay radiofooter
Set a footer for radio mode (embed only)<br/>

This only applies to embeds.<br/>

**Example:**<br/>
- `s.roleplay radiofooter Transmission over`<br/>
- `s.roleplay radiofooter` - reset to none<br/>
 - Usage: `s.roleplay radiofooter <footer>`
Extended Arg Info
> ### footer: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.roleplay log
Set a channel to log role play messages to.<br/>

If you do not specify a channel logging will be disabled.<br/>

**Examples:**<br/>
- `s.roleplay log #logs` - set to a channel called logs<br/>
- `s.roleplay log` - disable logging<br/>
 - Usage: `s.roleplay log <channel>`
Extended Arg Info
> ### channel: Optional[discord.channel.TextChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
