# s.addimage
Add an image for the bot to directly upload<br/>
 - Usage: `s.addimage`
 - Checks: `server_only`
## s.addimage clean_deleted_images
Cleanup deleted images that are not supposed to be saved anymore<br/>
 - Usage: `s.addimage clean_deleted_images`
 - Restricted to: `MOD`
## s.addimage clear_images
Clear all the images stored for the current server<br/>
 - Usage: `s.addimage clear_images`
 - Restricted to: `MOD`
## s.addimage delete
Remove a selected images<br/>

`name` the command name used to post the image<br/>
 - Usage: `s.addimage delete <name>`
 - Restricted to: `MOD`
 - Aliases: `remove, rem, and del`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.addimage list
List images added to bot<br/>
 - Usage: `s.addimage list [image_loc=server] [server_id=None]`
Extended Arg Info
> ### image_loc='server'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### server_id: discord.server.Guild = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by name. (There is no disambiguation for Guilds with multiple matching names).
> 
>     
## s.addimage add
Add an image to direct upload on this server<br/>

`name` the command name used to post the image<br/>
 - Usage: `s.addimage add <name>`
 - Restricted to: `MOD`
Extended Arg Info
> ### name: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.addimage ignoreglobal
Toggle usage of bot owner set global images on this server<br/>
 - Usage: `s.addimage ignoreglobal`
 - Restricted to: `MOD`
