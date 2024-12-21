# s.setspotifyembed
Set Spotify Embed settings<br/>

Automatically send a reply to Spotify links with a link to the embed preview. Convenient for mobile users who can finally listen to music samples from Discord, without needing an account.<br/>
 - Usage: `s.setspotifyembed`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `setspembed and setspe`
## s.setspotifyembed enable
Enable auto-responding to Spotify links<br/>
 - Usage: `s.setspotifyembed enable`
## s.setspotifyembed customurl
Set a custom URL. The parsed original Spotify link will be added on at the end.<br/>

Example:<br/>
> Custom URL: **`https://playsoju.netlify.app/?s=`**<br/>
> Final URL: **`https://playsoju.netlify.app/?s=https://open.spotify.com/...`**<br/>

Type "0" to reset to default.<br/>
Type "1" to disable this feature. (show no text)<br/>
 - Usage: `s.setspotifyembed customurl <text>`
Extended Arg Info
> ### text
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.setspotifyembed deleteoriginal
Delete the original message after it's processed<br/>

Only for messages processed via auto-responding feature<br/>
 - Usage: `s.setspotifyembed deleteoriginal <true_or_false>`
Extended Arg Info
> ### true_or_false: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.setspotifyembed disable
Disable auto-responding to Spotify links<br/>
 - Usage: `s.setspotifyembed disable`
## s.setspotifyembed note
Change the text that appears before auto-responses<br/>

Type "0" to reset to default.<br/>
Type "1" to disable this feature. (show no text)<br/>
 - Usage: `s.setspotifyembed note <text>`
Extended Arg Info
> ### text
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.spotifyembed
Return a Spotify embed link<br/>

Can set asMyself to true/false, for sending as webhook<br/>

*Admins: To edit auto-reply and other settings, use  `s.setspotifyembed`*<br/>
 - Usage: `s.spotifyembed <spotifyLink> [asMyself=False]`
 - Aliases: `spembed and spe`
Extended Arg Info
> ### spotifyLink
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### asMyself: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
