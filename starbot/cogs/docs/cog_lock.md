# s.lock
Lock a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Examples:**<br/>
- `s.lock #testing`<br/>
- `s.lock 133251234164375552 @members`<br/>
 - Usage: `s.lock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
## s.lock server
Lock the server.<br/>

Provide a role if you would like to lock if for that role.<br/>

**Example:**<br/>
- `s.lock server @members`<br/>
 - Usage: `s.lock server <roles>`
# s.unlock
Unlock a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Examples:**<br/>
- `s.unlock #testing`<br/>
- `s.unlock 133251234164375552 true`<br/>
 - Usage: `s.unlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
## s.unlock server
Unlock the server.<br/>

Provide a role if you would unlock it for that role.<br/>

**Examples:**<br/>
- `s.unlock server @members`<br/>
 - Usage: `s.unlock server <roles>`
# s.viewlock
Prevent users from viewing a channel.<br/>

Provide a role or member if you would like to lock it for them.<br/>
You can only lock a maximum of 10 things at once.<br/>

**Example:**<br/>
- `s.viewlock #testing`<br/>
- `s.viewlock 133251234164375552 @nubs`<br/>
 - Usage: `s.viewlock [channel=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
# s.unviewlock
Allow users to view a channel.<br/>

Provide a role or member if you would like to unlock it for them.<br/>
If you would like to override-unlock for something, you can do so by pass `true` as the state argument.<br/>
You can only unlock a maximum of 10 things at once.<br/>

**Example:**<br/>
- `s.unviewlock #testing true`<br/>
- `s.unviewlock 133251234164375552 @boosters`<br/>
 - Usage: `s.unviewlock [channel=None] [state=None] [roles_or_members=None]`
 - Restricted to: `ADMIN`
