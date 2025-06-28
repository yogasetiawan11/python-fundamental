## Loops (for/while)
 In programming, loops are fundamental control flow structures that allow you to repeatedly execute a block of code.
 This is incredibly useful for automating repetitive tasks, processing collections of data, or waiting for certain conditions to be met

## For Loop
using ``` for loop ``` to execute block of code a fixed number of times. you can iterate over a range, string, sequence, etc. 

**example**
```bash
student = ("yoga", "maryam","jhon")
for list in student:
     print(list) 
```
Output
```bash
yoga
maryam
jhon
```

**example 2**
```bash
for number in range(1, 15):
  if number == 10:  # number 10 is skipped
     continue     # this will skip number 10     
  else:  
     print(number)
```

**example 3**
```bash
for number in range(1, 15):
  if number == 10: 
     break     # output will stop in no 10     
  else:  
     print(number)
```
---

## While loop
execute some code WHILE some conditions is true
**example**
```bash
x = 1
y = 5

while x <= y:
   print(x)
   x = x + 1
```
Output
```bash
1
2
3
4
5
```
