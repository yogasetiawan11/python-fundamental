## What is conditional handling
conditioanal handling it says that handling a particular condition
conditional handling involves evaluating an expression that results in a Boolean value (true or false). Based on this evaluation, the program then follows a specific path of execution. The most common constructs for conditional handling are

**Example**
```bash
import sys

type = sys.argv[1]

if type == "t2.large":
    print("your instance type is t2.large")  
    #if user provide t2.large this word will exist 

else:
    print("instance is not t2")
    #else will exist if the if condition unmatched
```

there is another conditional that is ``elif`` we can use elif to provide any number of condition

**Example**
```bash
import sys

type = sys.argv[1]

if type == "t2.large":
    print("your instance type is t2.large")

elif type == "t2.medium":
    print("your instance type is t2.medium")
#if i provide input t2.medium it will provide this output

elif type == "t2.micro":
    print("your instance type is t2.micro")
#if i provide input t2.micro it will provide this output


else:
    print("instance is not t2")
#else will appear if the program doesn't match with if/elif
```
