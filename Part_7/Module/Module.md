# Understanding Modules in Python

## What is a Module?

A **module** in Python is simply a file containing Python code. This code can define functions, classes, and variables, and can also include runnable code. Modules help you organize your code into separate files, making it easier to manage and reuse.

Think of a module as a toolbox: you can put your tools (functions, classes, variables) inside, and use them whenever you need by importing the toolbox.

## Why Use Modules?

- **Organization:** Break large programs into smaller, manageable files.
- **Reusability:** Use the same code in different programs without rewriting it.
- **Namespace:** Avoid name conflicts by keeping code in separate modules.

## Creating a Module

To create a module, just write your Python code in a file with a `.py` extension. For example, create a file named `math_tools.py`:

```python
# math_tools.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

## Using a Module

You can use the functions from your module in another Python file by importing it:

```python
# main.py
import math_tools

result = math_tools.add(5, 3)
print(result)  # Output: 8
```

You can also import specific functions:

```python
from math_tools import subtract

print(subtract(10, 4))  # Output: 6
```

## Built-in Modules

Python comes with many built-in modules, such as `math`, `random`, and `datetime`. You can use them without creating your own files:

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

# Difference beteween Function, Module, Packages.
## Function
Function is a piece of logic that you can use. example:
```bash
def yoga():
```
## Module
Module is a collection of code 
## Package
Package is a collection of Modules which means if your code are written in multiple files, you can bundle all the files in package. some people called as package, or library

when you want to create module for API request or boto3, Jira, http request, Github. there are people who have already written for this In Pypi (Python Package Image) you can search specific module [here](https://pypi.org)

Using ``pip`` command you can download anything that available in Pypi all of these thing called as Pypi modules and Packages. PIP is simmilar with docker CLI that used to download anything from docker HUB. 

Install pip on Linux machine:
```bash
python get-pip.py
```

use pip to install Boto3
```bash
pip install boto3
```
```bash
pip list
```
it will list the module that available on the machine

