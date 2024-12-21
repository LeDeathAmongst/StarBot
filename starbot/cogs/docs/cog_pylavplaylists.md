# s.playlist
Control PyLav playlists<br/>
 - Usage: `s.playlist`
## /playlist version (Slash Command)
Show the version of the Cog and PyLav<br/>
 - Usage: `/playlist version`
 - Checks: `Server Only`
## /playlist create (Slash Command)
Create a playlist<br/>
 - Usage: `/playlist create [url] [name]`
 - `url:` (Optional) The URL of the playlist to create. YouTube, Spotify, SoundCloud, Apple Music playlists or albums
 - `name:` (Optional) The name of the playlist

 - Checks: `Server Only`
Extended Arg Info
> ### url: str
> - Autocomplete: True
> - Default: None
> 
> The URL of the playlist to create. YouTube, Spotify, SoundCloud, Apple Music playlists or albums
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### name: str
> - Autocomplete: False
> - Default: None
> 
> The name of the playlist
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /playlist list (Slash Command)
List all playlists you have access to on the invoked context<br/>
 - Usage: `/playlist list`
 - Checks: `Server Only`
## /playlist manage (Slash Command)
Manage a playlist<br/>
 - Usage: `/playlist manage <playlist> [operation]`
 - `playlist:` (Required) The playlist to perform the operation on
 - `operation:` (Optional) The operation to perform on the playlist, if not specified a menu will be shown for full control

 - Checks: `Server Only`
Extended Arg Info
> ### playlist: str
> - Autocomplete: True
> 
> The playlist to perform the operation on
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### operation: str
> - Autocomplete: False
> - Default: None
> - Choices: ['Info', 'Save', 'Play', 'Delete']
> 
> The operation to perform on the playlist, if not specified a menu will be shown for full control
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /playlist play (Slash Command)
Enqueue a playlist<br/>
 - Usage: `/playlist play <playlist>`
 - `playlist:` (Required) The playlist to enqueue

 - Checks: `Server Only`
Extended Arg Info
> ### playlist: str
> - Autocomplete: True
> 
> The playlist to enqueue
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /playlist delete (Slash Command)
Delete a playlist<br/>
 - Usage: `/playlist delete <playlist>`
 - `playlist:` (Required) The playlist to delete

 - Checks: `Server Only`
Extended Arg Info
> ### playlist: str
> - Autocomplete: True
> 
> The playlist to delete
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /playlist info (Slash Command)
Display info about a playlist<br/>
 - Usage: `/playlist info <playlist>`
 - `playlist:` (Required) The playlist show info about

 - Checks: `Server Only`
Extended Arg Info
> ### playlist: str
> - Autocomplete: True
> 
> The playlist show info about
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /playlist save (Slash Command)
Add the currently player queue to a playlist<br/>
 - Usage: `/playlist save <playlist>`
 - `playlist:` (Required) The playlist to append the queue to

 - Checks: `Server Only`
Extended Arg Info
> ### playlist: str
> - Autocomplete: True
> 
> The playlist to append the queue to
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /playlist upload (Slash Command)
Upload a playlist to the bot<br/>
 - Usage: `/playlist upload [url]`
 - `url:` (Optional) The URL of the playlist to upload

 - Checks: `Server Only`
Extended Arg Info
> ### url: str
> - Autocomplete: False
> - Default: None
> 
> The URL of the playlist to upload
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /playlist mix (Slash Command)
Play a YouTube mix playlist from a input<br/>
 - Usage: `/playlist mix [video] [playlist] [user] [channel]`
 - `video:` (Optional) The YouTube video ID to play a mix from
 - `playlist:` (Optional) The YouTube playlist ID to play a mix from
 - `user:` (Optional) The YouTube user ID to play a mix from
 - `channel:` (Optional) The YouTube channel ID to play a mix from

 - Checks: `Server Only`
Extended Arg Info
> ### video: str
> - Autocomplete: False
> - Default: None
> 
> The YouTube video ID to play a mix from
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### playlist: str
> - Autocomplete: False
> - Default: None
> 
> The YouTube playlist ID to play a mix from
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### user: str
> - Autocomplete: False
> - Default: None
> 
> The YouTube user ID to play a mix from
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### channel: str
> - Autocomplete: False
> - Default: None
> 
> The YouTube channel ID to play a mix from
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
