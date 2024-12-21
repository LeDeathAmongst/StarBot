# s.autopublisher
Manage AutoPublisher setting.<br/>
 - Usage: `s.autopublisher`
 - Restricted to: `ADMIN`
 - Aliases: `aph and autopub`
 - Checks: `server_only`
## s.autopublisher settings
Show AutoPublisher setting.<br/>
 - Usage: `s.autopublisher settings`
 - Aliases: `view`
## s.autopublisher reset
Reset AutoPublisher setting.<br/>
 - Usage: `s.autopublisher reset`
## s.autopublisher ignorechannel
Ignore/Unignore a news channel to prevent AutoPublisher from publishing messages in it.<br/>

You can provide multiple channels to ignore or unignore at once.<br/>
You decide if you wanna use the select menu or provide the channel(s) manually in the command.<br/>
 - Usage: `s.autopublisher ignorechannel <channels>`
## s.autopublisher version
Shows the version of the cog.<br/>
 - Usage: `s.autopublisher version`
## s.autopublisher toggle
Toggle AutoPublisher enable or disable.<br/>

- It's disabled by default.<br/>
    - Please ensure that the bot has access to `view_channel` in your news channels. it also need `manage_messages` to be able to publish.<br/>

**Note:**<br/>
- This cog requires News Channel. If you don't have it, you can't use this cog.<br/>
    - Learn more [here on how to enable](https://support.discord.com/hc/en-us/articles/360047132851-Enabling-Your-Community-Server) community server. (which is a part of news channel feature.)<br/>
 - Usage: `s.autopublisher toggle`
