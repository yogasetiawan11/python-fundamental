## Arithmetic Operators
### Introduction
Like a calculator in python there are option such as adding, subtracting, multiplying, dividing. 
using python we can code our calculator, after all programing is just writing a rules for a computer to follow specific input and condition.
**here an example**
| No | Name           | Symmbol |  Example           |
|----|----------------|---------|--------------------|
| 1  | Addition       |    +    |  1 + 2 = 3         |
| 2  | Subtraction    |    -    |  2 - 2 = 0         |
| 3  | Multification  |    *    |  5 * 5 = 25        |
| 4  | Division       |    /    |  3 / 3 = 1         |
| 5  | Modulus        |    %    |  10 % 2 = 0        |
| 6  | Exponent       |    **   |  5 ** 2 = 25 (5^)  |



## Relational Operator
### Introduction
Logical operators allow assignment and comparisons to be made and are used in conditional testing (such as if statements).

| No | Name                       |    Symmbol    |       Example      |
|----|----------------------------|---------------|--------------------|
| 1  | Equivalence                |       ==      |  if x == 5         |
| 2  | Less than                  |       <       |  if x <  2         |
| 3  | Less than or equal to      |       =<      |  if x <= 3         |
| 4  | Greater than               |       >       |  if x >  1         |
| 5  | Greater than or equal to   |       >=      |  if x => 4         |
| 6  | not equal to               |       !=      |  if x != 2         |


**Equivalence to** --> check if 2 value are equal
**Less than** --> chek if the left operand greater than righ
**greater than or equal to** --> chek if the left operand greater than or equal to than right


**Example**
## Greater than or equal to
```bash
a = 5
b = 2
result = a >= b
print (result)
# result will be True
```

**Not equal to**
```bash
a = 8
b = 5
result = a != b
print(result)
# result will be True
```

## Logical Operators
### Introduction
Logical operator in python used to combine with boolean values.
this operator allow you to perform Logical operator like AND, OR, NOT

**AND** :Returns True only if both conditions are True.
| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |


**Example**
```bash
x = 10
y = 5 
print ( x > y and y < x ) # True -> true and true 
print ( x < y and y < x ) # False  -> false and true
```
**OR** :Returns True if the least one condition is true
| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |


**example**
```bash
x = 10
y = 5 
print ( x > y or y < x ) # True -> true and true 
print ( x < y or y > x ) # False  -> false and true
```
**NOT** :Revels the result True become False and False become True
| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |


**Example**
```bash
y = 5
print (not (y == 5)) #False -> because result is true
print (not (y == 2)) #True -> because result is false
```