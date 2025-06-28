## What is Command Line Arguments (argv)
These are inputs passed when you run a Python script. 
### example:

```bash
python example.py hello 123
```

in ``example.py`` contains 2 content hello and 123

```bash
import sys

print(sys.argv)  # ['example.py', 'hello', '123']
print(sys.argv[1])  # hello
print(sys.argv[2])  # 123
```
``sys.argv`` is a list. ``sys.argv[0]`` is the script name.