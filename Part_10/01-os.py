import os

directory = input('enter file : ') .split()

for direc in directory:
    files = os.listdir(direc)
    print(f'========== these all of your files =========')
