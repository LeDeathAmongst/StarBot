# s.quiz
Play a kahoot-like trivia game.<br/>
Questions from the Open Trivia Database.<br/>

In this game, you will compete with other players to correctly answer each<br/>
question as quickly as you can. You have 10 seconds to type the answer<br/>
choice before time runs out. The longer you take to say the right answer,<br/>
the fewer points you get. If you get it wrong, you get no points. Only the<br/>
first valid answer (A, B, C, or D) will be recorded - be sure of the<br/>
answer before replying!<br/>

To end the game, stop responding to the questions and the game will time out.<br/>
 - Usage: `s.quiz`
 - Checks: `server_only`
## s.quiz play
Create or join a quiz game.<br/>
Specify a category name or ID number, otherwise it will be random.<br/>
Use s.quiz categories to list category names or id numbers.<br/>
 - Usage: `s.quiz play [category_name_or_id]`
Extended Arg Info
> ### category_name_or_id=None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.quiz categories
List quiz categories.<br/>
 - Usage: `s.quiz categories`
# s.quizset
Quiz settings.<br/>
 - Usage: `s.quizset`
 - Restricted to: `MOD`
 - Checks: `server_only`
## s.quizset multiplier
Set the credit multiplier.<br/>
The accepted range is 0 - 10000.<br/>
0 will turn credit gain off.<br/>
Credit gain will be based on the number of questions set and user speed.<br/>
1x = A small amount of credits like 1-10.<br/>
100x = A handful of credits: 100-500.<br/>
10000x = Quite a lot of credits, around 10k to 50k.<br/>
        <br/>
 - Usage: `s.quizset multiplier <multiplier>`
 - Checks: `check_global_setting_admin`
Extended Arg Info
> ### multiplier: int
> ```
> A number without decimal places.
> ```
## s.quizset show
Toggle revealing the answers.<br/>
 - Usage: `s.quizset show`
## s.quizset afk
Set number of questions before the game ends due to non-answers.<br/>
 - Usage: `s.quizset afk <questions>`
Extended Arg Info
> ### questions: int
> ```
> A number without decimal places.
> ```
## s.quizset questions
Set number of questions per game.<br/>
 - Usage: `s.quizset questions <questions>`
Extended Arg Info
> ### questions: int
> ```
> A number without decimal places.
> ```
