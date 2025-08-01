import os
folders = input('enter folder names:') .split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print('Your file does not exist')
        continue  # you can also use 'pass' here to skip to the next iteration

    print(f' =======  your files in =======')

    for file in files:
        print(file)