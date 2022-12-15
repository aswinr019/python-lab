import os

path = os.getcwd()

if (os.path.exists(path+'NewFolder') == False):
    os.mkdir(path+"/NewFolder")
    print("Folder "+path+"NewFolder created.")
else:
    print(path+"NewFolder exists.")

if (os.path.exists(path+'/NewFolder/newfile.txt')):
    print("NewFile.txt already exists") 
    f = open(path+"/NewFolder/newfile.txt", "w")
else:
    f = open(path+"/NewFolder/newfile.txt", "x")

f.write("hai")
f.close()

#read from file
# if (os.path.exists('C:/NewFolder/newfile.txt')):
#     print("NewFile.txt already exists") 
#     f = open("C:/NewFolder/newfile.txt", "w")
# else:
#     f = open("C:/NewFolder/newfile.txt", "x")
