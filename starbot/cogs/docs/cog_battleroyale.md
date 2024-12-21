# s.setbattleroyale
Configuration commands for BattleRoyale.<br/>
 - Usage: `s.setbattleroyale`
 - Aliases: `battleset`
## s.setbattleroyale prize
Changes the prize amount.<br/>
 - Usage: `s.setbattleroyale prize <amount>`
 - Checks: `is_owner_if_bank_global`
# s.battleroyale
Battle Royale with other members!<br/>

**Parameters:**<br/>
- `delay`: min 10, max 20.<br/>
- `skip`: will skip to results.<br/>
 - Usage: `s.battleroyale [delay=10] [skip=False]`
 - Aliases: `br`
 - Checks: `server_only`
Extended Arg Info
> ### skip: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.battleroyale role
Battle Royale with members from a specific role in your server.<br/>

Command author is automatically added to the player queue even if they don't have the role.<br/>

**Parameters**<br/>
- `role`: which role to add to the player queue.<br/>
- `delay`: min 10, max 20.<br/>
- `skip`: will skip to results.<br/>
 - Usage: `s.battleroyale role <role> [delay=10] [skip=False]`
Extended Arg Info
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
> ### skip: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.battleroyale auto
Battle Royale with random players from your server.<br/>

Command author is automatically added to the player queue.<br/>

**Parameters**<br/>
- `players`: how many players you want to join.<br/>
- `delay`: min 10, max 20.<br/>
- `skip`: will skip to results.<br/>
 - Usage: `s.battleroyale auto [players=30] [delay=10] [skip=False]`
Extended Arg Info
> ### skip: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.battleroyale leaderboard
Show the leaderboard.<br/>

**Parameters:**<br/>
- `sort_by`: `wins`, `games` or `kills`.<br/>
 - Usage: `s.battleroyale leaderboard [sort_by=wins]`
 - Aliases: `lb`
## s.battleroyale profile
Show your battle royale profile.<br/>

- Use the `s.br profile bio <message>` command to change the bio.<br/>
 - Usage: `s.battleroyale profile [user]`
 - Aliases: `stats`
Extended Arg Info
> ### user: Optional[discord.member.Member] = None
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
### s.battleroyale profile bio
Change your default bio.<br/>
 - Usage: `s.battleroyale profile bio <message>`
 - Aliases: `setbio and bioset`
