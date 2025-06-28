# difference beetween list & tupples
In Python, lists and tuples are both used to store collections of items, but they have key differences that affect performance, mutability, and use cases.

1. Muttablility
List is muttable (can be change)
Tupple is immutable (cannot be change)

2. syntax
List use ``[]``
Tupple use ``()``

### Exanple List

```bash
vm = ["vm_1", "vm_2", "vm_3"]
vm.append("vm_4")  #<- add vm_4 in program 
print (vm)
```

Output
```bash
['vm_1', 'vm_2', 'vm_3', 'vm_4']
```

### Example Tupple

```bash
vm = ("vm_1", "vm_2", "vm_3")
vm.append("vm_4")  #<- add vm_4 in program 
print (vm)
```

Output Tupple
``AttributeError: 'tuple' object has no attribute 'append'``  

Error because python program read the file as ``tupple`` and it can't be change

