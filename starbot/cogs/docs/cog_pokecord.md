# s.poke
Pokecord commands<br/>
 - Usage: `s.poke`
## s.poke set
Manage pokecord settings<br/>
 - Usage: `s.poke set`
 - Restricted to: `ADMIN`
 - Checks: `server_only`
### s.poke set toggle
Toggle pokecord on or off.<br/>
 - Usage: `s.poke set toggle [_type=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### _type: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.poke set levelup
Toggle levelup messages on or off.<br/>

If active channels are set, level up messages will only be sent in said channels. Otherwise it is ignored.<br/>
If no active channels are set then level up messages will send as normal.<br/>
 - Usage: `s.poke set levelup [_type=None]`
 - Restricted to: `ADMIN`
Extended Arg Info
> ### _type: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.poke set settings
Overview of pokécord settings.<br/>
 - Usage: `s.poke set settings`
 - Restricted to: `ADMIN`
### s.poke set blacklist
Blacklist channels from contributing to pokémon spawning.<br/>
 - Usage: `s.poke set blacklist <channel>`
 - Restricted to: `ADMIN`
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
### s.poke set channel
Set the channel(s) that pokemon are to spawn in.<br/>
 - Usage: `s.poke set channel <channel>`
 - Restricted to: `ADMIN`
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
### s.poke set whitelist
Whitelist channels that will contribute to pokémon spawning.<br/>
 - Usage: `s.poke set whitelist <channel>`
 - Restricted to: `ADMIN`
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
## s.poke trade
Pokecord Trading<br/>

Currently a work in progress.<br/>
 - Usage: `s.poke trade <user> <id>`
Extended Arg Info
> ### user: discord.member.Member
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
> ### id: int
> ```
> A number without decimal places.
> ```
### s.poke dev ivs
Manually set a pokemons IVs<br/>
 - Usage: `s.poke dev ivs <user> <pokeid> <hp> <attack> <defence> <spatk> <spdef> <speed>`
Extended Arg Info
> ### user: Optional[discord.member.Member]
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
> ### pokeid: int
> ```
> A number without decimal places.
> ```
> ### hp: int
> ```
> A number without decimal places.
> ```
> ### attack: int
> ```
> A number without decimal places.
> ```
> ### defence: int
> ```
> A number without decimal places.
> ```
> ### spatk: int
> ```
> A number without decimal places.
> ```
> ### spdef: int
> ```
> A number without decimal places.
> ```
> ### speed: int
> ```
> A number without decimal places.
> ```
### s.poke dev strip
Forcably removes a pokemone from user<br/>
 - Usage: `s.poke dev strip <user> <id>`
Extended Arg Info
> ### user: discord.member.Member
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
> ### id: int
> ```
> A number without decimal places.
> ```
### s.poke dev stats
Manually set a pokemons stats<br/>
 - Usage: `s.poke dev stats <user> <pokeid> <hp> <attack> <defence> <spatk> <spdef> <speed>`
Extended Arg Info
> ### user: Optional[discord.member.Member]
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
> ### pokeid: int
> ```
> A number without decimal places.
> ```
> ### hp: int
> ```
> A number without decimal places.
> ```
> ### attack: int
> ```
> A number without decimal places.
> ```
> ### defence: int
> ```
> A number without decimal places.
> ```
> ### spatk: int
> ```
> A number without decimal places.
> ```
> ### spdef: int
> ```
> A number without decimal places.
> ```
> ### speed: int
> ```
> A number without decimal places.
> ```
### s.poke dev level
Manually set a pokemons level<br/>
 - Usage: `s.poke dev level <user> <pokeid> <lvl>`
Extended Arg Info
> ### user: Optional[discord.member.Member]
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
> ### pokeid: int
> ```
> A number without decimal places.
> ```
> ### lvl: int
> ```
> A number without decimal places.
> ```
### s.poke dev reveal
Shows raw info for an owned pokemon<br/>
 - Usage: `s.poke dev reveal <user> <pokeid>`
Extended Arg Info
> ### user: Optional[discord.member.Member]
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
> ### pokeid: int
> ```
> A number without decimal places.
> ```
### s.poke dev spawn
Spawn a pokemon by name or random<br/>
 - Usage: `s.poke dev spawn <pokemon>`
Extended Arg Info
> ### *pokemon
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.poke nick
Set a pokémons nickname.<br/>

ID refers to the position within your pokémon listing.<br/>
This is found at the bottom of the pokemon on `s.list`<br/>
 - Usage: `s.poke nick <id> <nickname>`
Extended Arg Info
> ### id: int
> ```
> A number without decimal places.
> ```
> ### nickname: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.poke locale
Set the Pokecord locale to use for yourself.<br/>
 - Usage: `s.poke locale <locale>`
 - Checks: `server_only`
Extended Arg Info
> ### locale: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.poke release
Release a pokémon.<br/>
 - Usage: `s.poke release <id>`
 - Aliases: `free`
Extended Arg Info
> ### id: int
> ```
> A number without decimal places.
> ```
## s.poke silence
Toggle pokecord levelling messages on or off.<br/>
 - Usage: `s.poke silence [_type=None]`
 - Checks: `server_only`
Extended Arg Info
> ### _type: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.list
List a trainers or your own pokémon!<br/>
 - Usage: `s.list [user=None]`
 - Aliases: `pokemon`
Extended Arg Info
> ### user: discord.member.Member = None
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
# s.select
Select your default pokémon.<br/>
 - Usage: `s.select <_id>`
 - Checks: `server_only`
Extended Arg Info
> ### _id: Union[int, str]
> ```
> A number without decimal places.
> ```
# s.pokedex
Check your caught pokémon!<br/>
 - Usage: `s.pokedex`
# s.psearch
Search your pokemon.<br/>

Arguements must have `--` before them.<br/>
    `--name` | `--n` - Search pokemon by name.<br/>
    `--level`| `--l` - Search pokemon by level.<br/>
    `--id`   | `--i` - Search pokemon by ID.<br/>
    `--variant`   | `--v` - Search pokemon by variant.<br/>
    `--type`   | `--t` - Search pokemon by type.<br/>
    `--gender` | `--g` - Search by gender.<br/>
    `--iv` | - Search by total IV.<br/>
 - Usage: `s.psearch <args>`
# s.current
Show your current selected pokemon<br/>
 - Usage: `s.current`
# s.starter
Choose your starter pokémon!<br/>
 - Usage: `s.starter [pokemon=None]`
Extended Arg Info
> ### pokemon: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.hint
Get a hint on the pokémon!<br/>
 - Usage: `s.hint`
 - Cooldown: `1 per 30.0 seconds`
# s.catch
Catch a pokemon!<br/>
 - Usage: `s.catch <pokemon>`
Extended Arg Info
> ### pokemon: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
