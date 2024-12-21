# songshare

A simple Cog that makes the sharing of songs easier, by answering to any message detected with a music link with links to vary music services, thanks to Songlink/Odesli. It will show up as a reply to a message, with song title, artist, thumbnail; and various buttons linking to music services.

>[!WARNING]
>This cog does not respect ingored channels or guilds, neither blacklisted/whitelisted users
>
>Use the integrated channel/guild selection instead (via `[p]songshareset`)

## Installing guide


1. If you haven't already, add the repository

	`[p]repo add jak-cogs https://codeberg.org/jakjakob/jak-cogs`
	
2. Install the cog

	`[p]cog install jak-cogs songshare`
	
3. And finally, load the cog

	`[p]load songshare`
	
>[!NOTE]
>If you need higher Songshare API rate limits, and have access to an API key, you can set an API key with
>
>`[p]set api songlink <API-token>`


## Usage and Setup

### Setup

You can setup the cog with the `[p]songshareset` command


**`[p]songshareset allguild [toggle]`**

Enable in the guild. Argument toggle can be left empty to toggle between active and not, or a bool (True or False) to enable or disable.

**`[p]songshareset blacklist` and `[p]songshareset channel`**

The blacklist commands adds channels to the blacklist, aka where the bot will not sending the messages; while the channel commands adds single channels where the cog should be enabled.

Both of them have the following subcommands, that are pretty self-explanatory:
`[p]songshareset <blacklist or channel> add <channel>`, `[p]songshareset <blacklist or channel>  remove <channel>` and `[p]songshareset <blacklist or channel> reset`

### Usage

To use the Cog, just send a link to a music services in the specified channels/guilds you set up before