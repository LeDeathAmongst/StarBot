# s.remindme (Hybrid Command)
Create a reminder with optional reminder text or message.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `s.reminder timetips` to display tips for time parsing.<br/>

**Examples:**<br/>
- `s.remindme in 8min45sec to do that thing`<br/>
- `s.remindme to water my plants in 2 hours`<br/>
- `s.remindme in 3 days`<br/>
- `s.remindme 8h`<br/>
- `s.remindme every 1 week to take out the trash`<br/>
- `s.remindme in 1 hour <message_link>`<br/>
- `s.remindme at 10h to add some feature to my codes`<br/>
 - Usage: `s.remindme <time> [message_or_text]`
 - Slash Usage: `/remindme <time> [message_or_text]`
Extended Arg Info
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message_or_text: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.remind (Hybrid Command)
Create a reminder with optional reminder text or message, in a channel with an user/role ping.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `s.reminder timetips` to display tips for time parsing.<br/>

Examples:<br/>
- `s.remind #destination @user1 @user2 @user2 in 2 hours to buy a gift`<br/>
 - Usage: `s.remind <destination> <targets> <time> [message_or_text]`
 - Slash Usage: `/remind <destination> <targets> <time> [message_or_text]`
 - Checks: `server_only`
Extended Arg Info
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### message_or_text: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.reminder (Hybrid Command)
List, edit and delete existing reminders, or create FIFO/commands or Say reminders.<br/>
 - Usage: `s.reminder`
 - Slash Usage: `/reminder`
 - Aliases: `reminders`
## s.reminder text (Hybrid Command)
Edit the text of an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>
 - Usage: `s.reminder text <reminder> <text>`
 - Slash Usage: `/reminder text <reminder> <text>`
Extended Arg Info
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.reminder expires (Hybrid Command)
Edit the expires time of an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>
It's the same converter as for creation, but without the option of repetition.<br/>
 - Usage: `s.reminder expires <reminder> <time>`
 - Slash Usage: `/reminder expires <reminder> <time>`
 - Aliases: `expiresat`
Extended Arg Info
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.reminder clear (Hybrid Command)
Clear all your existing reminders.<br/>
 - Usage: `s.reminder clear [confirmation=False]`
 - Slash Usage: `/reminder clear [confirmation=False]`
Extended Arg Info
> ### confirmation: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.reminder timestamps (Hybrid Command)
Get a list of Discord timestamps for a given time. You can provide a repeat.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule.<br/>
You don't have to put quotes around the `time` argument.<br/>
Use `s.reminder timetips` to display tips for time parsing.<br/>
 - Usage: `s.reminder timestamps [repeat_times=100] [time]`
 - Slash Usage: `/reminder timestamps [repeat_times=100] [time]`
 - Aliases: `timestamp`
Extended Arg Info
> ### repeat_times: Optional[int] = 100
> ```
> A number without decimal places.
> ```
> ### time: str = 'now'
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.reminder list (Hybrid Command)
List your existing reminders.<br/>

Sort options:<br/>
- `expire`: Display them in order of next triggering.<br/>
- `created`: Display them in order of creating.<br/>
- `id`: Display them in order of their ID.<br/>
 - Usage: `s.reminder list [card=False] [content_type=None] [sort=expire]`
 - Slash Usage: `/reminder list [card=False] [content_type=None] [sort=expire]`
Extended Arg Info
> ### card: Optional[bool] = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.reminder timetips (Hybrid Command)
Show time parsing tips.<br/>
 - Usage: `s.reminder timetips`
 - Slash Usage: `/reminder timetips`
 - Aliases: `parsingtips`
## s.reminder remove (Hybrid Command)
Remove existing Reminder(s) from their IDs.<br/>

- Use `last` to remove your last created reminder.<br/>
- Use `next` to remove your next triggered reminder.<br/>
 - Usage: `s.reminder remove <reminders>`
 - Slash Usage: `/reminder remove <reminders>`
 - Aliases: `delete and -`
## s.reminder edit (Hybrid Command)
Edit an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>
 - Usage: `s.reminder edit <reminder>`
 - Slash Usage: `/reminder edit <reminder>`
 - Aliases: `info and show`
## s.reminder repeat (Hybrid Command)
Edit the repeat of an existing Reminder from its ID.<br/>

- Use `last` to edit your last created reminder.<br/>
- Use `next` to edit your next triggered reminder.<br/>

Allowed **intervals** are:<br/>
• `years`/`year`/`y`<br/>
• `months`/`month`/`mo`<br/>
• `weeks`/`week`/`w`<br/>
• `days`/`day`/`d`<br/>
• `hours`/`hour`/`hrs`/`hr`/`h`<br/>
• `minutes`/`minute`/`mins`/`min`/`m`<br/>

You can combine **relative intervals** like this:<br/>
• `1y 1mo 2 days -5h`<br/>
 - Usage: `s.reminder repeat <reminder> <repeat>`
 - Slash Usage: `/reminder repeat <reminder> <repeat>`
Extended Arg Info
> ### repeat: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.reminder fifo (Hybrid Command)
Create a FIFO/command reminder. The chosen command will be executed with you as invoker. Don't provide the prefix.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `s.reminder timetips` to display tips for time parsing.<br/>

Examples:<br/>
- `s.reminder fifo #destination "at 10h every day" ping<br/>
 - Usage: `s.reminder fifo <destination> <time> <command>`
 - Slash Usage: `/reminder fifo <destination> <time> <command>`
 - Restricted to: `ADMIN`
 - Aliases: `command`
 - Checks: `server_only`
Extended Arg Info
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### command: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.reminder say (Hybrid Command)
Create a reminder who will say/send text.<br/>

The specified time can be fuzzy parsed or use the kwargs `in`, `on` and `every` to find a repeat rule and your text.<br/>
You don't have to put quotes around the `time` argument. For more precise parsing, you can place quotation marks around the text. Put quotation marks around the time too, if it contains spaces.<br/>
Use `s.reminder timetips` to display tips for time parsing.<br/>

Examples:<br/>
- `s.reminder say #destination "at 9h every day" Hello everyone!<br/>
 - Usage: `s.reminder say <destination> <time> <text>`
 - Slash Usage: `/reminder say <destination> <time> <text>`
 - Restricted to: `GUILD_OWNER`
 - Checks: `server_only`
Extended Arg Info
> ### destination: Union[discord.channel.TextChannel, discord.channel.VoiceChannel, discord.threads.Thread, NoneType]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### time: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### text: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.reminder timezone (Hybrid Command)
Set your timezone for the time converter.<br/>

Timezone should be specified in the format: `Continent/City`.<br/>
Example: `Europe/Paris`, `America/New_York`...<br/>
You can find a list of valid timezones at: https://timezonedb.com/time-zones.<br/>
 - Usage: `s.reminder timezone <timezone>`
 - Slash Usage: `/reminder timezone <timezone>`
