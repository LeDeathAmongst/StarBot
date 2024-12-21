# s.github
Group command for github stuff<br/>
 - Usage: `s.github`
 - Aliases: `gh`
## s.github wiki
Displays PRs that have not yet been added to the wiki.<br/>
 - Usage: `s.github wiki`
## s.github checks
Shows status of GitHub checks of the default branch or of a PR.<br/>
 - Usage: `s.github checks <pr>`
Extended Arg Info
> ### pr: Optional[int]
> ```
> A number without decimal places.
> ```
## s.github commits
Searches commits.<br/>
 - Usage: `s.github commits <query>`
 - Aliases: `commit`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.github changelog

 - Usage: `s.github changelog`
## s.github file
Gets a link to files matching the `file` argument. You can also put a line or a line range after a semicolon like `pali.dm:69-420`.<br/>
 - Usage: `s.github file <file>`
Extended Arg Info
> ### file: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.github issues
Searches issues.<br/>
 - Usage: `s.github issues <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.github adminchangelog

 - Usage: `s.github adminchangelog`
## s.github randomissue
Picks a random open issue.<br/>
 - Usage: `s.github randomissue [query]`
Extended Arg Info
> ### query: str = ''
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.github prs
Searches PRs.<br/>
 - Usage: `s.github prs <query>`
Extended Arg Info
> ### query: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.github labelled
Displays open PRs with a given label.<br/>
 - Usage: `s.github labelled <label>`
Extended Arg Info
> ### label: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.github lastcommit
Gets the link to the latest commit from the repo or a link to commit some steps back (up to 10).<br/>
 - Usage: `s.github lastcommit [how_far_back=0]`
Extended Arg Info
> ### how_far_back: int = 0
> ```
> A number without decimal places.
> ```
