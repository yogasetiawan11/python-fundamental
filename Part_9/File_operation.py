def update_server (file_path, key, value):
    with open (file_path, "r") as file:
        lines = file.readlines()
    
    with open (file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)
update_server("server.conf", "MAX_CONNECTION", "580")



'''
 In this python program we will perform file operations 
 where we will edit "server.conf" using python
'''

