# /draw (Slash Command)
Generate an image with Dalle-3<br/>
 - Usage: `/draw <prompt> [size] [quality] [style]`
 - `prompt:` (Required) What would you like to draw?
 - `size:` (Optional) The size of the image to generate
 - `quality:` (Optional) The quality of the image to generate
 - `style:` (Optional) The style of the image to generate

 - Checks: `Server Only`
Extended Arg Info
> ### prompt: str
> - Autocomplete: False
> 
> What would you like to draw?
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### size: str
> - Autocomplete: False
> - Default: 1024x1024
> - Choices: ['1024x1024', '1792x1024', '1024x1792']
> 
> The size of the image to generate
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### quality: str
> - Autocomplete: False
> - Default: standard
> - Choices: ['standard', 'hd']
> 
> The quality of the image to generate
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### style: str
> - Autocomplete: False
> - Default: vivid
> - Choices: ['natural', 'vivid']
> 
> The style of the image to generate
> 
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.chathelp
Get help using assistant<br/>
 - Usage: `s.chathelp`
# s.chat
Chat with Starfire!<br/>

Conversations are *Per* user *Per* channel, meaning a conversation you have in one channel will be kept in memory separately from another conversation in a separate channel<br/>

**Optional Arguments**<br/>
`--outputfile <filename>` - uploads a file with the reply instead (no spaces)<br/>
`--extract` - extracts code blocks from the reply<br/>
`--last` - resends the last message of the conversation<br/>

**Example**<br/>
`s.chat write a python script that prints "Hello World!"`<br/>
- Including `--outputfile hello.py` will output a file containing the whole response.<br/>
- Including `--outputfile hello.py --extract` will output a file containing just the code blocks and send the rest as text.<br/>
- Including `--extract` will send the code separately from the reply<br/>
 - Usage: `s.chat <question>`
 - Aliases: `ask, escribir, razgovor, discuter, plaudern, 채팅, charlar, baterpapo, and sohbet`
 - Cooldown: `1 per 6.0 seconds`
 - Checks: `server_only`
Extended Arg Info
> ### question: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.convostats
Check the token and message count of yourself or another user's conversation for this channel<br/>

Conversations are *Per* user *Per* channel, meaning a conversation you have in one channel will be kept in memory separately from another conversation in a separate channel<br/>

Conversations are only stored in memory until the bot restarts or the cog reloads<br/>
 - Usage: `s.convostats [user]`
 - Checks: `server_only`
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
# s.convoclear
Reset your conversation with the bot<br/>

This will clear all message history between you and the bot for this channel<br/>
 - Usage: `s.convoclear`
 - Aliases: `clearconvo`
 - Checks: `server_only`
# s.convopop
Pop the last message from your conversation<br/>
 - Usage: `s.convopop`
 - Checks: `bot_has_server_permissions and server_only`
# s.convocopy
Copy the conversation to another channel, thread, or forum<br/>
 - Usage: `s.convocopy <channel>`
 - Checks: `bot_has_server_permissions and server_only`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.ForumChannel]
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.convoprompt
Set a system prompt for this conversation!<br/>

This allows customization of assistant behavior on a per channel basis!<br/>

Check out [This Guide](https://platform.openai.com/docs/guides/prompt-engineering) for prompting help.<br/>
 - Usage: `s.convoprompt [prompt]`
 - Checks: `server_only`
Extended Arg Info
> ### prompt: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.convoshow
View the current transcript of a conversation<br/>

This is mainly here for moderation purposes<br/>
 - Usage: `s.convoshow [user=None] [channel=operator.attrgetter('channel')]`
 - Restricted to: `GUILD_OWNER`
 - Aliases: `showconvo`
 - Checks: `server_only`
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
> ### channel: discord.channel.TextChannel = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
# s.query
Fetch related embeddings according to the current topn setting along with their scores<br/>

You can use this to fine-tune the minimum relatedness for your assistant<br/>
 - Usage: `s.query <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.assistant
Setup the assistant<br/>

You will need an **[api key](https://platform.openai.com/account/api-keys)** from OpenAI to use ChatGPT and their other models.<br/>
 - Usage: `s.assistant`
 - Restricted to: `ADMIN`
 - Aliases: `assist`
 - Checks: `server_only`
## s.assistant refreshembeds
Refresh embedding weights<br/>

*This command can be used when changing the embedding model*<br/>

Embeddings that were created using OpenAI cannot be use with the self-hosted model and vice versa<br/>
 - Usage: `s.assistant refreshembeds`
 - Aliases: `refreshembeddings, syncembeds, and syncembeddings`
## s.assistant override
Override settings for specific roles<br/>

**NOTE**<br/>
If a user has two roles with override settings, override associated with the higher role will be used.<br/>
 - Usage: `s.assistant override`
### s.assistant override maxtokens
Assign a max token override to a role<br/>

*Specify same role and token count to remove the override*<br/>
 - Usage: `s.assistant override maxtokens <max_tokens> <role>`
Extended Arg Info
> ### max_tokens: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.assistant override model
Assign a role to use a model<br/>

*Specify same role and model to remove the override*<br/>
 - Usage: `s.assistant override model <model> <role>`
Extended Arg Info
> ### model: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.assistant override maxresponsetokens
Assign a max response token override to a role<br/>

Set to 0 for response tokens to be dynamic<br/>

*Specify same role and token count to remove the override*<br/>
 - Usage: `s.assistant override maxresponsetokens <max_tokens> <role>`
Extended Arg Info
> ### max_tokens: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.assistant override maxtime
Assign a max retention time override to a role<br/>

*Specify same role and time to remove the override*<br/>
 - Usage: `s.assistant override maxtime <retention_seconds> <role>`
Extended Arg Info
> ### retention_seconds: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
### s.assistant override maxretention
Assign a max message retention override to a role<br/>

*Specify same role and retention amount to remove the override*<br/>
 - Usage: `s.assistant override maxretention <max_retention> <role>`
Extended Arg Info
> ### max_retention: int
> ```
> A number without decimal places.
> ```
> ### role: discord.role.Role
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by name
> 
>     
## s.assistant model
Set the OpenAI model to use<br/>
 - Usage: `s.assistant model [model=None]`
Extended Arg Info
> ### model: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.assistant importexcel
Import embeddings from an .xlsx file<br/>

Args:<br/>
    overwrite (bool): overwrite embeddings with existing entry names<br/>
 - Usage: `s.assistant importexcel <overwrite>`
Extended Arg Info
> ### overwrite: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.assistant embedmethod
Cycle between embedding methods<br/>

**Dynamic** embeddings mean that the embeddings pulled are dynamically appended to the initial prompt for each individual question.<br/>
When each time the user asks a question, the previous embedding is replaced with embeddings pulled from the current question, this reduces token usage significantly<br/>

**Static** embeddings are applied in front of each user message and get stored with the conversation instead of being replaced with each question.<br/>

**Hybrid** embeddings are a combination, with the first embedding being stored in the conversation and the rest being dynamic, this saves a bit on token usage.<br/>

**User** embeddings are injected into the beginning of the prompt as the first user message.<br/>

Dynamic embeddings are helpful for Q&A, but not so much for chat when you need to retain the context pulled from the embeddings. The hybrid method is a good middle ground<br/>
 - Usage: `s.assistant embedmethod`
## s.assistant resetconversations
Wipe saved conversations for the assistant in this server<br/>

This will delete any and all saved conversations for the assistant.<br/>
 - Usage: `s.assistant resetconversations <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.assistant relatedness
Set the minimum relatedness an embedding must be to include with the prompt<br/>

Relatedness threshold between 0 and 1 to include in embeddings during chat<br/>

Questions are converted to embeddings and compared against stored embeddings to pull the most relevant, this is the score that is derived from that comparison<br/>

**Hint**: The closer to 1 you get, the more deterministic and accurate the results may be, just don't be *too* strict or there wont be any results.<br/>
 - Usage: `s.assistant relatedness <mimimum_relatedness>`
Extended Arg Info
> ### mimimum_relatedness: float
> ```
> A number with or without decimal places.
> ```
## s.assistant tutor
Add/Remove items from the tutor list.<br/>

If using OpenAI's function calling and talking to a tutor, the AI is able to create its own embeddings to remember later<br/>

`role_or_member` can be a member or role<br/>
 - Usage: `s.assistant tutor <role_or_member>`
 - Aliases: `tutors`
Extended Arg Info
> ### role_or_member: Union[discord.member.Member, discord.role.Role]
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
## s.assistant importcsv
Import embeddings to use with the assistant<br/>

Args:<br/>
    overwrite (bool): overwrite embeddings with existing entry names<br/>

This will read excel files too<br/>
 - Usage: `s.assistant importcsv <overwrite>`
Extended Arg Info
> ### overwrite: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.assistant timezone
Set the timezone used for prompt placeholders<br/>
 - Usage: `s.assistant timezone <timezone>`
Extended Arg Info
> ### timezone: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.assistant resetembeddings
Wipe saved embeddings for the assistant<br/>

This will delete any and all saved embedding training data for the assistant.<br/>
 - Usage: `s.assistant resetembeddings <yes_or_no>`
Extended Arg Info
> ### yes_or_no: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.assistant questionmark
Toggle whether questions need to end with **__?__**<br/>
 - Usage: `s.assistant questionmark`
## s.assistant maxtime
Set the conversation expiration time<br/>

Regardless of this number, the initial prompt and internal system message are always included,<br/>
this only applies to any conversation between the user and bot after that.<br/>

Set to 0 to store conversations indefinitely or until the bot restarts or cog is reloaded<br/>
 - Usage: `s.assistant maxtime <retention_seconds>`
Extended Arg Info
> ### retention_seconds: int
> ```
> A number without decimal places.
> ```
## s.assistant toggledraw
Toggle the draw command on or off<br/>
 - Usage: `s.assistant toggledraw`
 - Aliases: `drawtoggle`
## s.assistant seed
Make the model more deterministic by setting a seed for the model.<br/>
- Default is None<br/>

If specified, the system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.<br/>
 - Usage: `s.assistant seed [seed=None]`
Extended Arg Info
> ### seed: int = None
> ```
> A number without decimal places.
> ```
## s.assistant topn
Set the embedding inclusion amout<br/>

Top N is the amount of embeddings to include with the initial prompt<br/>
 - Usage: `s.assistant topn <top_n>`
Extended Arg Info
> ### top_n: int
> ```
> A number without decimal places.
> ```
## s.assistant minlength
set min character length for questions<br/>

Set to 0 to respond to anything<br/>
 - Usage: `s.assistant minlength <min_question_length>`
Extended Arg Info
> ### min_question_length: int
> ```
> A number without decimal places.
> ```
## s.assistant regexfailblock
Toggle whether failed regex blocks the assistant's reply<br/>

Some regexes can cause [catastrophically backtracking](https://www.rexegg.com/regex-explosive-quantifiers.html)<br/>
The bot can safely handle if this happens and will either continue on, or block the response.<br/>
 - Usage: `s.assistant regexfailblock`
## s.assistant exportcsv
Export embeddings to a .csv file<br/>

**Note:** csv exports do not include the embedding values<br/>
 - Usage: `s.assistant exportcsv`
## s.assistant resetusage
Reset the token usage stats for this server<br/>
 - Usage: `s.assistant resetusage`
## s.assistant exportexcel
Export embeddings to an .xlsx file<br/>

**Note:** csv exports do not include the embedding values<br/>
 - Usage: `s.assistant exportexcel`
## s.assistant view
View current settings<br/>

To send in current channel, use `s.assistant view false`<br/>
 - Usage: `s.assistant view [private=False]`
 - Aliases: `v`
Extended Arg Info
> ### private: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.assistant collab
Toggle collaborative conversations<br/>

Multiple people speaking in a channel will be treated as a single conversation.<br/>
 - Usage: `s.assistant collab`
## s.assistant toggle
Toggle the assistant on or off<br/>
 - Usage: `s.assistant toggle`
## s.assistant temperature
Set the temperature for the model (0.0 - 2.0)<br/>
- Defaults is 1<br/>

Closer to 0 is more concise and accurate while closer to 2 is more imaginative<br/>
 - Usage: `s.assistant temperature <temperature>`
Extended Arg Info
> ### temperature: float
> ```
> A number with or without decimal places.
> ```
## s.assistant maxresponsetokens
Set the max response tokens the model can respond with<br/>

Set to 0 for response tokens to be dynamic<br/>
 - Usage: `s.assistant maxresponsetokens <max_tokens>`
Extended Arg Info
> ### max_tokens: int
> ```
> A number without decimal places.
> ```
## s.assistant importjson
Import embeddings to use with the assistant<br/>

Args:<br/>
    overwrite (bool): overwrite embeddings with existing entry names<br/>
 - Usage: `s.assistant importjson <overwrite>`
Extended Arg Info
> ### overwrite: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.assistant frequency
Set the frequency penalty for the model (-2.0 to 2.0)<br/>
- Defaults is 0<br/>

Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.<br/>
 - Usage: `s.assistant frequency <frequency_penalty>`
Extended Arg Info
> ### frequency_penalty: float
> ```
> A number with or without decimal places.
> ```
## s.assistant exportjson
Export embeddings to a json file<br/>
 - Usage: `s.assistant exportjson`
## s.assistant system
Set the system prompt for GPT to use<br/>

Check out [This Guide](https://platform.openai.com/docs/guides/prompt-engineering) for prompting help.<br/>

**Placeholders**<br/>
- **botname**: Starfire<br/>
- **timestamp**: discord timestamp<br/>
- **day**: Mon-Sun<br/>
- **date**: MM-DD-YYYY<br/>
- **time**: HH:MM AM/PM<br/>
- **timetz**: HH:MM AM/PM Timezone<br/>
- **members**: server member count<br/>
- **username**: user's name<br/>
- **displayname**: user's display name<br/>
- **roles**: the names of the user's roles<br/>
- **rolementions**: the mentions of the user's roles<br/>
- **avatar**: the user's avatar url<br/>
- **owner**: the owner of the server<br/>
- **servercreated**: the create date/time of the server<br/>
- **server**: the name of the server<br/>
- **py**: python version<br/>
- **dpy**: discord.py version<br/>
- **red**: red version<br/>
- **cogs**: list of currently loaded cogs<br/>
- **channelname**: name of the channel the conversation is taking place in<br/>
- **channelmention**: current channel mention<br/>
- **topic**: topic of current channel (if not forum or thread)<br/>
- **banktype**: whether the bank is global or not<br/>
- **currency**: currency name<br/>
- **bank**: bank name<br/>
- **balance**: the user's current balance<br/>
 - Usage: `s.assistant system [system_prompt]`
 - Aliases: `sys`
Extended Arg Info
> ### system_prompt: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.assistant channel
Set the channel for the assistant<br/>
 - Usage: `s.assistant channel [channel=None]`
Extended Arg Info
> ### channel: Union[discord.channel.TextChannel, discord.threads.Thread, discord.channel.ForumChannel, NoneType] = None
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.assistant blacklist
Add/Remove items from the blacklist<br/>

`channel_role_member` can be a member, role, channel, or category channel<br/>
 - Usage: `s.assistant blacklist <channel_role_member>`
Extended Arg Info
> ### channel_role_member: Union[discord.member.Member, discord.role.Role, discord.channel.TextChannel, discord.channel.CategoryChannel, discord.threads.Thread, discord.channel.ForumChannel]
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
## s.assistant embedmodel
Set the OpenAI Embedding model to use<br/>
 - Usage: `s.assistant embedmodel [model=None]`
Extended Arg Info
> ### model: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.assistant openaikey
Set your OpenAI key<br/>
 - Usage: `s.assistant openaikey`
 - Aliases: `key`
## s.assistant mention
Toggle whether to ping the user on replies<br/>
 - Usage: `s.assistant mention`
## s.assistant channelpromptshow
Show the channel specific system prompt<br/>
 - Usage: `s.assistant channelpromptshow [channel=operator.attrgetter('channel')]`
Extended Arg Info
> ### channel: discord.channel.TextChannel = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
## s.assistant usage
View the token usage stats for this server<br/>
 - Usage: `s.assistant usage`
## s.assistant sysoverride
Toggle allowing per-conversation system prompt overriding<br/>
 - Usage: `s.assistant sysoverride`
## s.assistant maxtokens
Set maximum tokens a convo can consume<br/>

Set to 0 for dynamic token usage<br/>

**Tips**<br/>
- Max tokens are a soft cap, sometimes messages can be a little over<br/>
- If you set max tokens too high the cog will auto-adjust to 100 less than the models natural cap<br/>
- Ideally set max to 500 less than that models maximum, to allow adequate responses<br/>

Using more than the model can handle will raise exceptions.<br/>
 - Usage: `s.assistant maxtokens <max_tokens>`
Extended Arg Info
> ### max_tokens: int
> ```
> A number without decimal places.
> ```
## s.assistant mentionrespond
Toggle whether the bot responds to mentions in any channel<br/>
 - Usage: `s.assistant mentionrespond`
## s.assistant regexblacklist
Remove certain words/phrases in the bot's responses<br/>
 - Usage: `s.assistant regexblacklist <regex>`
Extended Arg Info
> ### regex: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.assistant prompt
Set the initial prompt for GPT to use<br/>

Check out [This Guide](https://platform.openai.com/docs/guides/prompt-engineering) for prompting help.<br/>

**Placeholders**<br/>
- **botname**: Starfire<br/>
- **timestamp**: discord timestamp<br/>
- **day**: Mon-Sun<br/>
- **date**: MM-DD-YYYY<br/>
- **time**: HH:MM AM/PM<br/>
- **timetz**: HH:MM AM/PM Timezone<br/>
- **members**: server member count<br/>
- **username**: user's name<br/>
- **displayname**: user's display name<br/>
- **roles**: the names of the user's roles<br/>
- **rolementions**: the mentions of the user's roles<br/>
- **avatar**: the user's avatar url<br/>
- **owner**: the owner of the server<br/>
- **servercreated**: the create date/time of the server<br/>
- **server**: the name of the server<br/>
- **py**: python version<br/>
- **dpy**: discord.py version<br/>
- **red**: red version<br/>
- **cogs**: list of currently loaded cogs<br/>
- **channelname**: name of the channel the conversation is taking place in<br/>
- **channelmention**: current channel mention<br/>
- **topic**: topic of current channel (if not forum or thread)<br/>
- **banktype**: whether the bank is global or not<br/>
- **currency**: currency name<br/>
- **bank**: bank name<br/>
- **balance**: the user's current balance<br/>
 - Usage: `s.assistant prompt [prompt]`
 - Aliases: `pre`
Extended Arg Info
> ### prompt: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.assistant maxretention
Set the max messages for a conversation<br/>

Conversation retention is cached and gets reset when the bot restarts or the cog reloads.<br/>

Regardless of this number, the initial prompt and internal system message are always included,<br/>
this only applies to any conversation between the user and bot after that.<br/>

Set to 0 to disable conversation retention<br/>

**Note:** *actual message count may exceed the max retention during an API call*<br/>
 - Usage: `s.assistant maxretention <max_retention>`
Extended Arg Info
> ### max_retention: int
> ```
> A number without decimal places.
> ```
## s.assistant presence
Set the presence penalty for the model (-2.0 to 2.0)<br/>
- Defaults is 0<br/>

Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.<br/>
 - Usage: `s.assistant presence <presence_penalty>`
Extended Arg Info
> ### presence_penalty: float
> ```
> A number with or without decimal places.
> ```
## s.assistant resolution
Switch vision resolution between high and low for relevant GPT-4-Turbo models<br/>
 - Usage: `s.assistant resolution`
## s.assistant functioncalls
Toggle whether GPT can call functions<br/>
 - Usage: `s.assistant functioncalls`
 - Aliases: `usefunctions`
## s.assistant maxrecursion
Set the maximum function calls allowed in a row<br/>

This sets how many times the model can call functions in a row<br/>

Only the following models can call functions at the moment<br/>
- gpt-4o-mini<br/>
- gpt-4o<br/>
- ect..<br/>
 - Usage: `s.assistant maxrecursion <recursion>`
Extended Arg Info
> ### recursion: int
> ```
> A number without decimal places.
> ```
## s.assistant questionmode
Toggle question mode<br/>

If question mode is on, embeddings will only be sourced during the first message of a conversation and messages that end in **?**<br/>
 - Usage: `s.assistant questionmode`
## s.assistant channelprompt
Set a channel specific system prompt<br/>
 - Usage: `s.assistant channelprompt [channel=operator.attrgetter('channel')] [system_prompt]`
Extended Arg Info
> ### channel: discord.channel.TextChannel = operator.attrgetter('channel')
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by channel URL.
>     4. Lookup by name
> 
>     
> ### system_prompt: Optional[str] = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.embeddings (Hybrid Command)
Manage embeddings for training<br/>

Embeddings are used to optimize training of the assistant and minimize token usage.<br/>

By using this the bot can store vast amounts of contextual information without going over the token limit.<br/>

**Note**<br/>
You can enter a search query with this command to bring up the menu and go directly to that embedding selection.<br/>
 - Usage: `s.embeddings [query]`
 - Slash Usage: `/embeddings [query]`
 - Restricted to: `ADMIN`
 - Aliases: `emenu`
 - Checks: `server_only`
Extended Arg Info
> ### query: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
# s.customfunctions (Hybrid Command)
Add custom function calls for Assistant to use<br/>

**READ**<br/>
- [Function Call Docs](https://platform.openai.com/docs/guides/gpt/function-calling)<br/>
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb)<br/>
- [JSON Schema Reference](https://json-schema.org/understanding-json-schema/)<br/>

The following objects are passed by default as keyword arguments.<br/>
- **user**: the user currently chatting with the bot (discord.Member)<br/>
- **channel**: channel the user is chatting in (TextChannel|Thread|ForumChannel)<br/>
- **server**: current server (discord.Guild)<br/>
- **bot**: the bot object (Red)<br/>
- **conf**: the config model for Assistant (GuildSettings)<br/>
- All functions **MUST** include `*args, **kwargs` in the params and return a string<br/>
```python
# Can be either sync or async
async def func(*args, **kwargs) -> str:
```
Only bot owner can manage this, server owners can see descriptions but not code<br/>
 - Usage: `s.customfunctions [function_name=None]`
 - Slash Usage: `/customfunctions [function_name=None]`
 - Aliases: `customfunction and customfunc`
 - Checks: `server_only`
Extended Arg Info
> ### function_name: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
