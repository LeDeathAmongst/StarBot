# s.pixlboard
View the Pixl leaderboard!<br/>

**Arguments**<br/>
`show_global`: show the global leaderboard<br/>

example: `s.pixlb true`<br/>
 - Usage: `s.pixlboard <show_global>`
 - Aliases: `pixlb, pixelb, pixlelb, and pixleaderboard`
 - Checks: `server_only`
Extended Arg Info
> ### show_global: Optional[bool]
> ```
> Can be 1, 0, true, false, t, f
> ```
# s.pixl
Start a Pixl game!<br/>
Guess the image as it is slowly revealed<br/>
 - Usage: `s.pixl`
 - Aliases: `pixle, pixlguess, pixelguess, and pixleguess`
 - Checks: `server_only`
# s.pixlset
Configure the Pixl game<br/>
 - Usage: `s.pixlset`
 - Aliases: `pixelset and pixleset`
 - Checks: `server_only`
## s.pixlset view
View the current settings<br/>
 - Usage: `s.pixlset view`
## s.pixlset showanswer
(Toggle) Showing the answer after a game over<br/>
 - Usage: `s.pixlset showanswer`
## s.pixlset useglobal
(Toggle) Whether to use global images in this server<br/>
 - Usage: `s.pixlset useglobal`
## s.pixlset usedefault
(Toggle) Whether to use the default hardcoded images in this server<br/>
 - Usage: `s.pixlset usedefault`
## s.pixlset image
Add/Remove images<br/>
 - Usage: `s.pixlset image`
### s.pixlset image view
View the server images<br/>
 - Usage: `s.pixlset image view`
### s.pixlset image viewglobal
View the global images<br/>
 - Usage: `s.pixlset image viewglobal`
### s.pixlset image add
Add an image for your server to use<br/>

**Arguments**<br/>
`url:     `the url of the image<br/>
`answers: `a list of possible answers separated by a comma<br/>

**Alternative**<br/>
If args are left blank, a text file can be uploaded with the following format for bulk image adding.<br/>
Each line starts with the url followed by all the possible correct answers separated by a comma<br/>

Example: `url, answer, answer, answer...`<br/>
```
https://some_url.com/example.png, answer1, answer two, another answer
https://yet_another_url.com/another_example.jpg, answer one, answer 2, another answer
```
 - Usage: `s.pixlset image add <url> <answers>`
Extended Arg Info
> ### url: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
> ### answers: Optional[str]
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
### s.pixlset image viewdefault
View the default images<br/>
 - Usage: `s.pixlset image viewdefault`
### s.pixlset image testserver
Test the server images to ensure they are valid urls<br/>
 - Usage: `s.pixlset image testserver`
## s.pixlset participants
Set the minimum amount of participants for the game to reward users credits<br/>
 - Usage: `s.pixlset participants <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## s.pixlset ratio
Set the point to credit conversion ratio (points x ratio = credit reward)<br/>
Points are calculated based on how many hidden blocks are left at the end of the game<br/>

Ratio can be a decimal<br/>
Set to 0 to disable credit rewards<br/>
 - Usage: `s.pixlset ratio <ratio>`
Extended Arg Info
> ### ratio: float
> ```
> A number with or without decimal places.
> ```
## s.pixlset blocks
Set the amount of blocks to reveal after each delay<br/>
 - Usage: `s.pixlset blocks <amount>`
Extended Arg Info
> ### amount: int
> ```
> A number without decimal places.
> ```
## s.pixlset timelimit
Set the time limit for Pixl games<br/>
 - Usage: `s.pixlset timelimit <seconds>`
Extended Arg Info
> ### seconds: int
> ```
> A number without decimal places.
> ```
