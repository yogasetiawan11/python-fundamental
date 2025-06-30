## Regex stands for Regular Expression, a sequence of characters that defines a search pattern. 
You use it to:
- Find text
- Match text
- Replace text
- Extract text

It works like a smart filter that understands patterns, not just exact words.

## WHY Use Regex?
You use regex when:
You want to find or manipulate strings that follow patterns.

You need more power than basic string functions like .split(), .find(), or .replace().

## How to use regex
firts import module regex in python file
``import re``

Example: 

```bash
import re 

text = "Contact me at yogasn@example.com"
pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

match = re.search(pattern, text)
if match:
    print("Valid email address")
else: 
    print("Invalid")
```