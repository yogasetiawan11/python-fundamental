## Object-Oriented Programing 

Object-Oriented Programming (OOP) is a powerful programming paradigm that focuses on organizing code around "objects" rather than just functions or logic. In Python, everything is an object, making it inherently object-oriented.

### Class
A class is a blueprint or template for creating objects (instances). It defines the properties (attributes) and behaviors (methods) that the objects created from it will have.

**Example**
```bash

class identity:
    def __init__(self, name, country):
       self.name = name
       self.country = country
person = identity ("Yoga", "Indonesia")
print(person.name)
print(person.country)

```

