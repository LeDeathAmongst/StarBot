# s.todoset
Commands for configuring your todo list<br/>
 - Usage: `s.todoset`
 - Aliases: `todosettings`
## s.todoset pretty
Have your todo list look pretty<br/>

This will set it to use emojis such as ✅ and 🟩<br/>

**Arguments**<br/>
    - `value` Whether pretty should be enabled<br/>
 - Usage: `s.todoset pretty <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset showsettings
Show your todo settings<br/>

This will list the following:<br/>
    - `indexed todos`<br/>
    - `colour`<br/>
    - `emojis`<br/>
    - `embedded`<br/>
    - `markdown`<br/>
    - `autosort`<br/>
    - `combined lists`<br/>
    - `pretty todos`<br/>
    - `timestamps`<br/>
    - `extra details`<br/>
 - Usage: `s.todoset showsettings`
## s.todoset categoryemojis
Set your category emojis<br/>
 - Usage: `s.todoset categoryemojis`
 - Aliases: `catemojis`
### s.todoset categoryemojis todoemoji
Set the emoji for the todo category.<br/>

If you have markdown enabled only default emojis will work.<br/>

By default the emoji will be '🔘'.<br/>

**Arguments**<br/>
    - `reset` If specified this will reset the emoji back to default.<br/>
    - `emoji` The emoji that will be used for the category. This will skip the check. This argument can't be used if you have markdown enabled.<br/>
 - Usage: `s.todoset categoryemojis todoemoji <reset> [emoji=None]`
 - Aliases: `temoji`
Extended Arg Info
> ### reset: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
### s.todoset categoryemojis completedemoji
Set the emoji for the completed category.<br/>

If you have markdown enabled only default emojis will work.<br/>

By default the emoji will be '☑'.<br/>

**Arguments**<br/>
    - `reset` If specified this will reset the emoji back to default.<br/>
    - `emoji` The emoji that will be used for the category. This will skip the check, and this argument can't be used if you have markdown enabled.<br/>
 - Usage: `s.todoset categoryemojis completedemoji <reset> [emoji=None]`
 - Aliases: `cemoji`
Extended Arg Info
> ### reset: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset embeds
Set your todo list to use embeds<br/>

**NOTE** embeds will *only* be used if possible in the current channel<br/>

**Arguments**<br/>
    - `value` Whether to use embeds or not<br/>
 - Usage: `s.todoset embeds <value>`
 - Aliases: `embed`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset details
Have your todo list send you extra details.<br/>

This may be removed at a later date<br/>

**Arguments**<br/>
    - `value` Whether you should recieve extra details<br/>
 - Usage: `s.todoset details <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset private
Set your todo list to display privately<br/>

This will make the menu be ephemeral when you use it<br/>

**Arguments**<br/>
    - `value` Whether your todo list should be private.<br/>
 - Usage: `s.todoset private <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset completeemoji
Set the completed emoji used for completed todos.<br/>

This will prompt you to react with an emoji.<br/>
Note that only emojis that Starfire can use will work<br/>

**Arguments**<br/>
    - `reset` Whether to reset the emoji back to default.<br/>
    - `emoji` The emoji to use for the complete mark. This has to be custom and can only be an emoji that Starfire can use.<br/>
 - Usage: `s.todoset completeemoji <reset> [emoji=None]`
 - Aliases: `cemoji`
 - Checks: `pretty`
Extended Arg Info
> ### reset: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset autosort
Set your todo list to auto sort<br/>

**NOTE** This command won't autosort your todos. Use `s.todo sort` to sort your todos<br/>

**Arguments**<br/>
    - `value` Whether your todo list should auto sort<br/>
 - Usage: `s.todoset autosort <value>`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset colour
Set the colour of your todo list's embeds<br/>

**NOTE** this will only work if you have embeds enabled and the bot can embed links in the channel<br/>

**Arguments**<br/>
    - `colour` The colour you would like the embed to be. Type `None` to set it to the bot's default embed colour<br/>
 - Usage: `s.todoset colour <colour>`
Extended Arg Info
> ### colour: Optional[discord.colour.Colour]
> Converts to a :class:`~discord.Colour`.
> 
>     
## s.todoset preset
Set you settings to a preset<br/>

Current presets are `minimal` and `pretty`<br/>

**Arguments**<br/>
    - `preset` The preset for your settings. Must be either `minimal` or `pretty` as of right now.<br/>
 - Usage: `s.todoset preset <preset>`
## s.todoset todoemoji
Set the emoji used for todos<br/>

This will prompt you to react with an emoji. Note that the emoji must be one the bot can use.<br/>

If you have markdown enabled only default emojis will work.<br/>

**Arguments**<br/>
    - `reset` Whether to reset the emoji back to default.<br/>
    - `emoji` The emoji that will be used for this<br/>
 - Usage: `s.todoset todoemoji <reset> [emoji=None]`
 - Aliases: `temoji`
 - Checks: `pretty`
Extended Arg Info
> ### reset: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset timestamps
Set whether todo should use timestamps<br/>

**NOTE** this will only be in effect if the message is not embedded. This might also be removed at a later date<br/>

**Arguments**<br/>
    - `value` Whether to enable timestamps<br/>
 - Usage: `s.todoset timestamps <value>`
 - Aliases: `timestamp and ts`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset combine
Combine your todo list with your completed list<br/>

**NOTE** this will only be in effect if you have completed todos<br/>

**Arguments**<br/>
    - `value` Whether to combine your lists or not<br/>
 - Usage: `s.todoset combine <value>`
 - Aliases: `combined`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset number
Set your todo list to index todos whilst listing them<br/>

**Arguments**<br/>
    - `value` Whether to index todos or not<br/>
 - Usage: `s.todoset number <value>`
 - Aliases: `index`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todoset markdown
Set your todo list to use markdown blocks<br/>

This will look something like this<br/>
**Jojo's todos**<br/>
```md
1. Blah blah
2. Blah blah blah
3. aaaaaaaaaaaaaaaaaaa
```
**Arguments**<br/>
    - `value` Whether markdown should be used or not<br/>
 - Usage: `s.todoset markdown <value>`
 - Aliases: `md and codeblock`
Extended Arg Info
> ### value: bool
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.todo
Your todo list inside Discord<br/>

**Arguments**<br/>
    - `index` The todo you want to view.<br/>
    This is optional and if left out, it will show the help command instead<br/>
 - Usage: `s.todo <index>`
## s.todo delete
Delete a todo task<br/>

This will remove it from your list entirely<br/>

**Arguments**<br/>
    - `indexes` The indexes of the todos you want to delete<br/>
 - Usage: `s.todo delete <indexes>`
 - Aliases: `del, remove, clear, and r`
## s.todo multiadd
Add multiple todos in one command. These are split by a newline.<br/>

You can upload a file instead of inputting the todos, or reply to a message that contains a file<br/>
**Examples**<br/>
`s.todo multiadd Todo number 1<br/>
todo number 2<br/>
todo number 3`<br/>

**Arguments**<br/>
    - `todos` The todos you want to add.<br/>
    This is an optional argument and you can upload, or reply to a message with, a file instead<br/>
 - Usage: `s.todo multiadd [todos]`
Extended Arg Info
> ### todos: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.todo deleteall
Remove all of your todos<br/>

**Arguments**<br/>
    - `confirm` Skips the confirmation check. Defaults to False<br/>
 - Usage: `s.todo deleteall [confirm=False]`
 - Aliases: `delall, removeall, and clearall`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todo gettodos
Grab your todos in a clean file format.<br/>

This is handy for moving todos over from bot to bot<br/>
 - Usage: `s.todo gettodos`
 - Aliases: `todotofile`
 - Checks: `attach_or_in_dm`
## s.todo complete
Commands having to do with your completed tasks<br/>

**Arguments**<br/>
    - `indexes` Optional indexes to complete. If left at none the help command will be shown<br/>
 - Usage: `s.todo complete <indexes>`
 - Aliases: `c`
### s.todo complete view
View a completed todo. This has a similar effect to using `s.todo <index>`<br/>

This will have a menu that will allow you to delete the todo<br/>

**Arguments**<br/>
    - `index` The index of the todo you want to view.<br/>
 - Usage: `s.todo complete view <index>`
### s.todo complete delete
Delete completed todos<br/>

This will remove them from your completed list<br/>

**Arguments**<br/>
    - `indexes` A list of integers for the indexes of your completed todos<br/>
 - Usage: `s.todo complete delete <indexes>`
 - Aliases: `del, remove, and clear`
### s.todo complete list
List your completed todos<br/>

This will only list if you have completed todos<br/>
 - Usage: `s.todo complete list`
### s.todo complete reorder
Move a completed todo from one index to another<br/>

This will error if the index is larger than your completed todo list<br/>

**Arguments**<br/>
    - `from` The index of the completed todo<br/>
    - `to` The new index of the completed todo<br/>
 - Usage: `s.todo complete reorder <original> <new>`
 - Aliases: `move`
### s.todo complete deleteall
Remove all of your completed todos<br/>

**Arguments**<br/>
    - `confirm` Skips the confirmation check. Defaults to False<br/>
 - Usage: `s.todo complete deleteall [confirm=False]`
 - Aliases: `delall, removeall, and clearall`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todo manager
Manage who can manage your todo lists. These people can add and remove from your todo list, so be careful who you grant this to<br/>
 - Usage: `s.todo manager`
 - Aliases: `managers`
### s.todo manager add
Add a user to your todo list managers<br/>

This user cannot be a bot. Please be aware that they can add and remove from your todo list and they can view it at any time<br/>

**Arguments**<br/>
    - `user` The user you would like to add to your list's managers.<br/>
 - Usage: `s.todo manager add <user>`
### s.todo manager list
List your todo list's managers<br/>
 - Usage: `s.todo manager list`
### s.todo manager remove
Remove a user from your list's managers<br/>

This user cannot be a bot<br/>

**Arguments**<br/>
    - `user` The user to remove from your managers<br/>
 - Usage: `s.todo manager remove <user>`
 - Aliases: `del and delete`
Extended Arg Info
> ### user: discord.user.User
> 
> 
>     1. Lookup by ID.
>     2. Lookup by mention.
>     3. Lookup by username#discriminator (deprecated).
>     4. Lookup by username#0 (deprecated, only gets users that migrated from their discriminator).
>     5. Lookup by user name.
>     6. Lookup by global name.
> 
>     
## s.todo import
Import your todos from epic guy's todo cog.<br/>

This will only import todos from this bot's config.<br/>
To import todos from another bot, check out `s.todo multiadd`<br/>

**Arguments**<br/>
    - `confirm` Skips the confirmation check.<br/>
 - Usage: `s.todo import [confirm=False]`
Extended Arg Info
> ### confirm: bool = False
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todo search
Query your todo list for todos containing certain words<br/>

**Arguments**<br/>
    - `query` The words to search for.<br/>
 - Usage: `s.todo search <regex> <query>`
Extended Arg Info
> ### regex: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.todo suggestions
Get information about how you can suggest features for this cog<br/>
 - Usage: `s.todo suggestions`
 - Aliases: `suggest`
## s.todo pin
Pin or unpin a todo<br/>

This will stick it at the top of the list whenever you view it<br/>

**Arguments**<br/>
    - `index` The index of the todo you want to pin/unpin<br/>
 - Usage: `s.todo pin <index>`
 - Aliases: `unpin`
## s.todo suggestors
A thank you command for everyone who has either contributed, requested a feature, or reported a bug<br/>
 - Usage: `s.todo suggestors`
## s.todo shared
Shared todo lists.<br/>

These are lists that other users have given you access to, for adding/removing/completing<br/>
 - Usage: `s.todo shared`
 - Checks: `server_only`
### s.todo shared complete
Complete todos on a user's list<br/>

This only works if you are a moderator of that user's list<br/>

**Arguments**<br/>
    - `user` The user for completing todos. This **cannot** be a bot.<br/>
    - `indexes` The indexes of the todos you want to complete<br/>
 - Usage: `s.todo shared complete <user> <indexes>`
 - Aliases: `c`
#### s.todo shared complete list
List a user's completed todos<br/>

This only works if you are a manager of that user's todo list<br/>

**Arguments**<br/>
    - `user` The user to view the list of. This **cannot** be a bot.<br/>
 - Usage: `s.todo shared complete list <user>`
### s.todo shared remove
Remove a todo from a user's list<br/>

This will only work if you are a manager of that user's list<br/>

**Arguments**<br/>
    - `user` The user you want to edit the list of. This **cannot** be a bot.<br/>
    - `index` The index of the todo you want to remove.<br/>
 - Usage: `s.todo shared remove <user> <indexes>`
 - Aliases: `del and delete`
### s.todo shared view
View a todo of a user who's list you manage<br/>

This only works if you manage that user's list<br/>

**Arguments**<br/>
    - `user` The user of which you're viewing the todo.<br/>
    - `index` The index of the todo you want to view.<br/>
 - Usage: `s.todo shared view <user> <index>`
### s.todo shared add
Add a todo to a user's list<br/>

This will require you to have manager on their list<br/>

**Arguments**.<br/>
    - `user` The user to add to their list. This **cannot** be a bot.<br/>
    - `pinned` Whether the todo should be pinned or not. Defaults to False.<br/>
    - `todo` The task to add to the user's list.<br/>
 - Usage: `s.todo shared add <user> <pinned> <todo>`
Extended Arg Info
> ### pinned: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### todo: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.todo shared pin
Pin a user's todo<br/>

This will only work if you manage that user's list<br/>

**Arguments**<br/>
    - `user` The user to pin a todo for. This **cannot** be a bot.<br/>
    - `index` The index of the todo to pin.<br/>
 - Usage: `s.todo shared pin <user> <index>`
 - Aliases: `unpin`
### s.todo shared list
Lists a user's list that you manage<br/>

This will *only* work if you manage that user's list<br/>

**Arguments**<br/>
    - `user` A user who you manage a list for. This **cannot** be a bot.<br/>
 - Usage: `s.todo shared list <user>`
## s.todo reorder
Move a todo from one index to another<br/>

This will error if the index is larger than your todo list<br/>

**Arguments**<br/>
    - `from` The index of the todo<br/>
    - `to` The new index of the todo<br/>
 - Usage: `s.todo reorder <original> <new>`
 - Aliases: `move`
## s.todo edit
Edit a todo!<br/>
 - Usage: `s.todo edit <index> <new_todo>`
Extended Arg Info
> ### new_todo: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.todo list
List your todos<br/>

This will list them with pinned todos first and then whatever sorting you have<br/>
 - Usage: `s.todo list`
## s.todo sort
Sort your todos by alphabetical order<br/>

You can optionally set it to sort in reverse<br/>

**Arguments**<br/>
    - `reverse` Whether to set it to be reversed. Defaults to False<br/>
 - Usage: `s.todo sort [reverse=None]`
Extended Arg Info
> ### reverse: bool = None
> ```
> Can be 1, 0, true, false, t, f
> ```
## s.todo add
Add a todo task to your list<br/>

Don't store sensitive information here for Pete's sake<br/>

**Arguments**<br/>
    - `pinned` A boolean value that sets it to be pinned or not. Defaults to False<br/>
    - `todo` The todo task<br/>
 - Usage: `s.todo add <pinned> <todo>`
Extended Arg Info
> ### pinned: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
> ### todo: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
