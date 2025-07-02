## What is Command Line Arguments (argv)
In Python, sys.argv is a list of strings that represents the command-line arguments passed to a Python script when it's executed.

Command-Line Arguments: When you run a Python script from your terminal or command prompt, you can provide additional pieces of information (arguments) right after the script name. These are called command-line arguments.

### example:

i have a folder ``example.com`` inside this file i have 2 argument that is hello & 123

```bash
python example.py hello 123
```

to pull the argument i can just say ``sys.argv[position the argument]``

```bash
import sys

print(sys.argv)  # ['example.py', 'hello', '123']
print(sys.argv[1])  # hello
print(sys.argv[2])  # 123
```
``sys.argv`` is a list. ``sys.argv[0]`` is the script name.