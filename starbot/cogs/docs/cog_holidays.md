# s.holiday
Group command for interacting with holidays.<br/>
 - Usage: `s.holiday`
## s.holiday regions
Show a directory of all settable country codes and country names.<br/>
 - Usage: `s.holiday regions`
## s.holiday weekends
Fetch long weekends for a given year and country.<br/>
 - Usage: `s.holiday weekends [year=None] [country_code=None]`
Extended Arg Info
> ### year: int = None
> ```
> A number without decimal places.
> ```
> ### country_code: str = None
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.holiday upcoming
Fetch upcoming public holidays worldwide.<br/>
 - Usage: `s.holiday upcoming`
## s.holiday list
List all public holidays for the current year.<br/>
 - Usage: `s.holiday list`
## s.holiday next
Fetch the next public holiday for your saved region.<br/>
 - Usage: `s.holiday next`
# s.holidayset
Configure holiday-related settings<br/>
 - Usage: `s.holidayset`
## s.holidayset country
Set your country code for fetching public holidays.<br/>
 - Usage: `s.holidayset country <country_code>`
Extended Arg Info
> ### country_code: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
## s.holidayset dms
Toggle DM alerts for holidays.<br/>
 - Usage: `s.holidayset dms`
