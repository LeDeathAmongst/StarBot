# s.fx
Apply or remove filters<br/>
 - Usage: `s.fx`
## /fx nightcore (Slash Command)
Apply a Nightcore preset to the player<br/>
 - Usage: `/fx nightcore`
 - Checks: `Server Only`
## /fx varporwave (Slash Command)
Apply a Vaporwave preset to the player<br/>
 - Usage: `/fx varporwave`
 - Checks: `Server Only`
## /fx vibrato (Slash Command)
Apply a vibrato filter to the player<br/>
 - Usage: `/fx vibrato [frequency] [depth] [reset]`
 - `frequency:` (Optional) The vibrato frequency
 - `depth:` (Optional) The vibrato depth value
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx tremolo (Slash Command)
Apply a tremolo filter to the player<br/>
 - Usage: `/fx tremolo [frequency] [depth] [reset]`
 - `frequency:` (Optional) The tremolo frequency
 - `depth:` (Optional) The tremolo depth value
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx timescale (Slash Command)
Apply a timescale filter to the player<br/>
 - Usage: `/fx timescale [speed] [pitch] [rate] [reset]`
 - `speed:` (Optional) The timescale speed value
 - `pitch:` (Optional) The timescale pitch value
 - `rate:` (Optional) The timescale rate value
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx rotation (Slash Command)
Apply a rotation filter to the player<br/>
 - Usage: `/fx rotation [hertz] [reset]`
 - `hertz:` (Optional) The rotation hertz frequency
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx lowpass (Slash Command)
Apply a low pass filter to the player<br/>
 - Usage: `/fx lowpass [smoothing] [reset]`
 - `smoothing:` (Optional) The low pass smoothing value
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx karaoke (Slash Command)
Apply a karaoke filter to the player<br/>
 - Usage: `/fx karaoke [level] [mono_level] [filter_band] [filter_width] [reset]`
 - `level:` (Optional) The level value
 - `mono_level:` (Optional) The mono level value
 - `filter_band:` (Optional) The filter band
 - `filter_width:` (Optional) The filter width value
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx channelmix (Slash Command)
Apply a channel mix filter to the player<br/>
 - Usage: `/fx channelmix [left_to_left] [left_to_right] [right_to_left] [right_to_right] [reset]`
 - `left_to_left:` (Optional) The channel mix left to left weight
 - `left_to_right:` (Optional) The channel mix left to right weight
 - `right_to_left:` (Optional) The channel mix right to left weight
 - `right_to_right:` (Optional) The channel mix right to right weight
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx distortion (Slash Command)
Apply a distortion filter to the player<br/>
 - Usage: `/fx distortion [sin_offset] [sin_scale] [cos_offset] [cos_scale] [tan_offset] [tan_scale] [offset] [scale] [reset]`
 - `sin_offset:` (Optional) The distortion Sine offset
 - `sin_scale:` (Optional) The distortion Sine scale
 - `cos_offset:` (Optional) The distortion Cosine offset
 - `cos_scale:` (Optional) The distortion Cosine scale
 - `tan_offset:` (Optional) The distortion Tangent offset
 - `tan_scale:` (Optional) The distortion Tangent scale
 - `offset:` (Optional) The distortion offset
 - `scale:` (Optional) The distortion scale
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx echo (Slash Command)
Apply a echo filter to the player<br/>
 - Usage: `/fx echo [delay] [decay] [reset]`
 - `delay:` (Optional) The delay of the echo
 - `decay:` (Optional) The decay of the echo
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx reverb (Slash Command)
Apply a reverb filter to the player<br/>
 - Usage: `/fx reverb [delays] [gains] [reset]`
 - `delays:` (Optional) The delays of the reverb
 - `gains:` (Optional) The gains of the reverb
 - `reset:` (Optional) Reset any existing effects currently applied to the player

 - Checks: `Server Only`
Extended Arg Info
> ### delays: str
> - Autocomplete: False
> - Default: None
> 
> The delays of the reverb
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### gains: str
> - Autocomplete: False
> - Default: None
> 
> The gains of the reverb
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### reset: bool
> - Autocomplete: False
> - Default: False
> 
> Reset any existing effects currently applied to the player
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx show (Slash Command)
Show the current filters applied to the player<br/>
 - Usage: `/fx show`
 - Checks: `Server Only`
## /fx reset (Slash Command)
Reset any existing filters currently applied to the player<br/>
 - Usage: `/fx reset`
 - Checks: `Server Only`
## /fx bassboost (Slash Command)
Apply a Bass boost equalizer preset to the player.<br/>
 - Usage: `/fx bassboost <level>`
 - `level:` (Required) The bass boost level to apply

 - Checks: `Server Only`
Extended Arg Info
> ### level: str
> - Autocomplete: True
> 
> The bass boost level to apply
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## /fx piano (Slash Command)
Apply a Piano equalizer preset to the player.<br/>
 - Usage: `/fx piano`
 - Checks: `Server Only`
## /fx rock (Slash Command)
Apply an experimental Metal/Rock equalizer preset.<br/>
 - Usage: `/fx rock`
 - Checks: `Server Only`
## /fx customeq (Slash Command)
Apply and/or save a custom equalizer setting<br/>
 - Usage: `/fx customeq <name> [description] [band_25] [band_40] [band_63] [band_100] [band_160] [band_250] [band_400] [band_630] [band_1000] [band_1600] [band_2500] [band_4000] [band_6300] [band_10000] [band_16000] [save]`
 - `name:` (Required) The name of the specified equalizer
 - `description:` (Optional) A brief description of the equalizer
 - `band_25:` (Optional) Control the 25Hz band of this equalizer
 - `band_40:` (Optional) Control the 40Hz band of this equalizer
 - `band_63:` (Optional) Control the 63Hz band of this equalizer
 - `band_100:` (Optional) Control the 100Hz band of this equalizer
 - `band_160:` (Optional) Control the 160Hz band of this equalizer
 - `band_250:` (Optional) Control the 250Hz band of this equalizer
 - `band_400:` (Optional) Control the 400Hz band of this equalizer
 - `band_630:` (Optional) Control the 630Hz band of this equalizer
 - `band_1000:` (Optional) Control the 1kHz band of this equalizer
 - `band_1600:` (Optional) Control the 1.6kHz band of this equalizer
 - `band_2500:` (Optional) Control the 2.5kHz band of this equalizer
 - `band_4000:` (Optional) Control the 4kHz band of this equalizer
 - `band_6300:` (Optional) Control the 6.3kHz band of this equalizer
 - `band_10000:` (Optional) Control the 10kHz band of this equalizer
 - `band_16000:` (Optional) Control the 16kHz band of this equalizer
 - `save:` (Optional) Should the equalizer you specified be saved?

 - Checks: `Server Only`
Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> The name of the specified equalizer
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description: str
> - Autocomplete: False
> - Default: None
> 
> A brief description of the equalizer
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### save: bool
> - Autocomplete: False
> - Default: False
> 
> Should the equalizer you specified be saved?
> 
> ```
> Can be 1, 0, true, false, t, f
> ```
## /fx saveeq (Slash Command)
Save the current applied EQ<br/>
 - Usage: `/fx saveeq <name> [description]`
 - `name:` (Required) The name of the equalizer
 - `description:` (Optional) A brief description of the equalizer

 - Checks: `Server Only`
Extended Arg Info
> ### name: str
> - Autocomplete: False
> 
> The name of the equalizer
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### description: str
> - Autocomplete: False
> - Default: None
> 
> A brief description of the equalizer
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.fxset
Configure the Player behaviour when an effect is set<br/>
 - Usage: `s.fxset`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.fxset version
Show the version of the Cog and PyLav<br/>
 - Usage: `s.fxset version`
# s.eq
Configure the Player behaviour when an equalizer preset is set<br/>
 - Usage: `s.eq`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
## s.eq persist
Persist the last used preset<br/>
 - Usage: `s.eq persist`
