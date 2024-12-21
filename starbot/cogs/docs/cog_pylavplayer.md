# /search (Slash Command)
Search for a track, then play the selected response.<br/>
 - Usage: `/search <query> [source]`
 - `query:` (Required) The query to search for search query
 - `source:` (Optional) Where to search in

 - Checks: `Server Only`
Extended Arg Info
> ### query: str
> - Autocomplete: True
> 
> The query to search for search query
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### source: str
> - Autocomplete: False
> - Default: None
> - Choices: ['Deezer', 'YouTube Music', 'Spotify', 'Apple Music', 'SoundCloud', 'YouTube', 'Yandex Music']
> 
> Where to search in
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# /play (Slash Command)
Enqueue the specified query to be played.<br/>
 - Usage: `/play [query] [enqueue_type]`
 - `query:` (Optional) This argument is the query to play, a link or a search query.
 - `enqueue_type:` (Optional) …

 - Checks: `Server Only`
Extended Arg Info
> ### query: str
> - Autocomplete: False
> - Default: None
> 
> This argument is the query to play, a link or a search query.
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### enqueue_type: str
> - Autocomplete: False
> - Default: add_to_queue
> - Choices: ['Play Now', 'Play Next', 'Add to Queue']
> 
> …
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.playerset
Player settings commands<br/>
 - Usage: `s.playerset`
## s.playerset version
Show the version of the Cog and PyLav<br/>
 - Usage: `s.playerset version`
## s.playerset down
Notifies PyLav that a Player is having issues.<br/>

If enough (50% or more of currently playing players) report issues, PyLav will automatically<br/>
switch to a different node or restart the current node where possible.<br/>
 - Usage: `s.playerset down`
 - Cooldown: `1 per 600.0 seconds`
 - Checks: `requires_player and invoker_is_dj`
## s.playerset server
Server-specific settings.<br/>
 - Usage: `s.playerset server`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `server`
 - Checks: `server_only`
### s.playerset server dj
Add, remove or show the disc jockey roles and users for this server.<br/>
 - Usage: `s.playerset server dj`
#### s.playerset server dj add
Add disc jockey roles or users to this server.<br/>
 - Usage: `s.playerset server dj add <roles_or_users>`
#### s.playerset server dj clear
Clear the disc jockey roles and users for this server.<br/>
 - Usage: `s.playerset server dj clear`
#### s.playerset server dj remove
Remove disc jockey roles or users in this server.<br/>
 - Usage: `s.playerset server dj remove <roles_or_users>`
#### s.playerset server dj list
List the disc jockey roles and users for this server.<br/>
 - Usage: `s.playerset server dj list`
### s.playerset server autoshuffle
Set whether I should shuffle the queue after adding every new song.<br/>
 - Usage: `s.playerset server autoshuffle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.playerset server deafen
Set whether I should deafen myself when playing.<br/>
 - Usage: `s.playerset server deafen <toggle>`
 - Aliases: `deaf`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.playerset server vol
Set the maximum volume a user can set.<br/>
 - Usage: `s.playerset server vol <volume>`
 - Aliases: `volume`
Extended Arg Info
> ### volume: int
> ```
> A number without decimal places.
> ```
### s.playerset server dc
Set whether the bot should disconnect from the voice channel<br/>
 - Usage: `s.playerset server dc`
#### s.playerset server dc empty
Set whether I should disconnect from the voice channel when the queue is empty.<br/>

Arguments:<br/>
    - `<toggle>`: I should disconnect from the voice channel when the queue is empty.<br/>
    - `<duration>`: How long after the queue is empty should I disconnect?<br/>
    The Default is 60 seconds.<br/>
    Accept seconds, minutes, hours, days, and weeks.<br/>
    If no unit is specified, the duration is assumed to be seconds.<br/>
 - Usage: `s.playerset server dc empty <toggle> [after]`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
#### s.playerset server dc alone
Set whether I should disconnect from the voice channel when alone.<br/>

Arguments:<br/>
    - `<toggle>`: I should disconnect from the voice channel when it detects that it is<br/>
    alone.<br/>
    - `<duration>`: How longer after detecting should I disconnect?<br/>
    The Default is 60 seconds.<br/>
    Accept seconds, minutes, hours, days, and weeks.<br/>
    If no unit is specified, the duration is assumed to be seconds.<br/>
 - Usage: `s.playerset server dc alone <toggle> [after]`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.playerset server lock
Restrict which channels where I can be used.<br/>
 - Usage: `s.playerset server lock`
#### s.playerset server lock commands
Restrict me only to accept PyLav commands executed from the specified channel.<br/>
 - Usage: `s.playerset server lock commands [channel]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
#### s.playerset server lock voice
Restrict me only to join the specified voice channel.<br/>
 - Usage: `s.playerset server lock voice [channel]`
 - Aliases: `vc`
Extended Arg Info
> ### channel: discord.channel.VoiceChannel = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
### s.playerset server playlist
Specify a playlist to be used for autoplay.<br/>
 - Usage: `s.playerset server playlist <playlist>`
### s.playerset server auto
Set whether the bot should automatically play songs when the queue is empty.<br/>
 - Usage: `s.playerset server auto <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.playerset server shuffle
Set whether I should allow users to shuffle the queue<br/>
 - Usage: `s.playerset server shuffle <toggle>`
Extended Arg Info
> ### toggle: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.playerset up
Removes a vote for a Player being down.<br/>

If enough (50% or more of currently active players) report issues, PyLav will automatically<br/>
switch to a different node or restart the current node where possible.<br/>

This command is only valid if your server previously voted for a node to be down and is now back up.<br/>
 - Usage: `s.playerset up`
 - Checks: `requires_player and invoker_is_dj`
# s.play
Attempt to play the queries which you provide.<br/>

Separate multiple queries with a new line (`shift + enter`).<br/>

If you want to play a local track, you can specify the full path relative to the local tracks' folder.<br/>
For example, if my local tracks folder is: `/home/draper/music`.<br/>

I can play a single track with `track.mp3` or `/home/draper/music/track.mp3`.<br/>
I can play everything inside a folder with a `sub-folder/folder`.<br/>
I can play everything inside a folder and its sub-folders with the `all:` prefix, i.e. `all:sub-folder/folder`.<br/>

You can search specific services by using the following prefixes*:<br/>
`dzsearch:`  - Deezer<br/>
`spsearch:`  - Spotify<br/>
`amsearch:`  - Apple Music<br/>
`ytmsearch:` - YouTube Music<br/>
`ytsearch:`  - YouTube<br/>
`scsearch:`  - SoundCloud<br/>
`ymsearch:`  - Yandex Music<br/>

You can trigger text-to-speech by using the following prefixes*:<br/>
`speak:` - I will speak the query (limited to 200 characters)<br/>
`tts://` - I will speak the query<br/>
 - Usage: `s.play [query]`
 - Aliases: `p`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### query: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.bump
Plays the specified track from the queue.<br/>

If you specify the `after_current` argument, the track will be played after the current track; otherwise, it will replace the current track.<br/>
 - Usage: `s.bump <queue_number> [after_current=False]`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### queue_number: int
> ```
> A number without decimal places.
> ```
> ### after_current: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.playnext
Enqueue a track at the top of the queue.<br/>
 - Usage: `s.playnext <query>`
 - Aliases: `pn`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.remove
Remove the specified track from the queue.<br/>

If you specify the `remove_duplicates` argument, all tracks that are the same as your URL or the index track will be removed.<br/>
 - Usage: `s.remove <track_url_or_index> [remove_duplicates=False]`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### track_url_or_index: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### remove_duplicates: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.connect (Hybrid Command)
Request that I connect to the specified channel or your current channel.<br/>
 - Usage: `s.connect [channel]`
 - Slash Usage: `/connect [channel]`
 - Checks: `invoker_is_dj and server_only`
Extended Arg Info
> ### channel: Optional[discord.channel.VoiceChannel] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.np (Hybrid Command)
Shows which track is currently being played on this server.<br/>
 - Usage: `s.np [to_dm=False]`
 - Slash Usage: `/np [to_dm=False]`
 - Aliases: `now`
 - Checks: `requires_player and server_only`
Extended Arg Info
> ### to_dm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.skip (Hybrid Command)
Skips the current track.<br/>
 - Usage: `s.skip`
 - Slash Usage: `/skip`
 - Checks: `invoker_is_dj, requires_player, and server_only`
# s.stop (Hybrid Command)
Stops the player and clears the queue.<br/>
 - Usage: `s.stop`
 - Slash Usage: `/stop`
 - Checks: `invoker_is_dj, requires_player, and server_only`
# s.dc (Hybrid Command)
Request that I disconnect from the current voice channel.<br/>
 - Usage: `s.dc`
 - Slash Usage: `/dc`
 - Aliases: `disconnect`
 - Checks: `invoker_is_dj and requires_player`
# s.queue (Hybrid Command)
Shows the current queue for this server.<br/>
 - Usage: `s.queue`
 - Slash Usage: `/queue`
 - Aliases: `q`
 - Checks: `requires_player and server_only`
# s.shuffle (Hybrid Command)
Shuffles the current queue.<br/>
 - Usage: `s.shuffle`
 - Slash Usage: `/shuffle`
 - Checks: `invoker_is_dj, requires_player, and server_only`
# s.repeat (Hybrid Command)
Set whether to repeat the current song or queue.<br/>

If no argument is given, the current repeat mode will be toggled between the current track and off.<br/>
 - Usage: `s.repeat [queue=None]`
 - Slash Usage: `/repeat [queue=None]`
 - Checks: `invoker_is_dj, requires_player, and server_only`
Extended Arg Info
> ### queue: Optional[bool] = None
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.pause (Hybrid Command)
Pause the player<br/>
 - Usage: `s.pause`
 - Slash Usage: `/pause`
 - Checks: `invoker_is_dj, requires_player, and server_only`
# s.resume (Hybrid Command)
Resume the player<br/>
 - Usage: `s.resume`
 - Slash Usage: `/resume`
 - Checks: `invoker_is_dj, requires_player, and server_only`
# s.volume (Hybrid Command)
Set the current volume for the player.<br/>

The volume is a percentage value between 0% and 1,000%, where 100% is the default volume.<br/>
 - Usage: `s.volume <volume>`
 - Slash Usage: `/volume <volume>`
 - Checks: `invoker_is_dj, requires_player, and server_only`
Extended Arg Info
> ### volume: int
> ```
> A number without decimal places.
> ```
# s.seek (Hybrid Command)
Seek the current track.<br/>

Seek can either be a number of seconds, a timestamp, or a specific percentage of the track.<br/>

Examples:<br/>
`s.seek 10` Seeks 10 seconds forward<br/>
`s.seek -20` Seeks 20 seconds backwards<br/>
`s.seek 0:30` Seeks to 0:30<br/>
`s.seek 50%` Seeks to 50% of the track<br/>
 - Usage: `s.seek <seek>`
 - Slash Usage: `/seek <seek>`
 - Checks: `invoker_is_dj, requires_player, and server_only`
Extended Arg Info
> ### seek: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.prev (Hybrid Command)
Play previously played tracks.<br/>

A history of the last 100 tracks played is kept.<br/>
 - Usage: `s.prev`
 - Slash Usage: `/prev`
 - Aliases: `previous`
 - Checks: `invoker_is_dj, requires_player, and server_only`
