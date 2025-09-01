import os
test = input("enter") .split()
for file in test: 
    try:
        files = os.listdir(file)
    except FileNotFoundError:
        print('Your file does not exist')
        continue