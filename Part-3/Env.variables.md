## What is environtment variables (env vars)
**Env Vars** are key value pairs to stored outside the program.
they're part of operating system environment and used to configure settings Like (Password, DB, API etc) without Hardcoding them into the code.

### Examples

```bash
# In linux or MacOS terminal
export DB_USERr=yoga
export DB_PASSWORD=yoga_aja

# In Windows Command Prompt
set DB_USER=yoga
set DB_PASSWORD=yoga_aja

``` 

You can access them in python like this
```bash
import os

user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

print("User:", user)
print("Password:", password)
```