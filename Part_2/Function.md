## Function 
A function is a block of code that used specific task and can be reused.
You define once, and can use many time.
### Example
```bash
def student(highschool):
    print("Hello",highschool)
student("yoga setiawan")

#output
#Hello yoga setiawan
```

## Module
A module is a file that contains Python code — functions, variables, classes — which you can import and use in other files. It helps you organize code.

A module is like a toolbox: you open it to use the tools (functions) inside.

**Example:**
You have a file called simple.py:
```bash
a = 1 
print(a)
```

In another file you can 
```bash
import simple.py
print(simple.py)
```

## Package
A package is a folder that contains multiple modules and a special file named __init__.py which indicates the directory should be treated as a package

**Example**
```bash
my_package/
 __init__.py
    math_tools.py
    string.py
```

you can use from this Package as follows:
```bash
from my_package import string
result = string.function_from_string_module1()
```
in this example ``my package`` containing math and string.