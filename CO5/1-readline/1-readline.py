import os 

list = []

path = os.getcwd()


if ( os.path.exists(path+"/demo_file.txt")):
    file = open(path+"/demo_file.txt","r")
    for line in file:
        list.append(line)
else :
    print("File doesn't exist")

file.close()

print(list)
