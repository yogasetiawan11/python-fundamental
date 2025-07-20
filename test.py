import os

folders = input("Enter the path to the Python file: ")
print(folders)

for folder in folders:
    tested = os.listdir(folder)
    print(" ==== listing of the folder - " + folder)

    for test in tested:
        print(test)