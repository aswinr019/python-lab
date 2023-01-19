import os
import csv

path = os.getcwd()


if(os.path.exists(path+"/auto.csv")):

    file1 = open(path+"/auto.csv", "r")
    file2 = open(path+"/new.csv", "x")
    

    
    fileds = ['INDEX','COMPANY','BODY-STYLE','WHEEL-BASE','ENGINE-TYPE','NUM_OF_CYLINDERS','HORSEPOWER','AVERAGE_MILAGE','PRICE','']

    csvreader = csv.DictReader(file1)
    csvwriter = csv.DictWriter(file2,fieldnames=fileds)


    csvwriter.writeheader()


    list = []
    for row in csvreader:
        if(int(row['PRICE']) > 1000000):
           
            list.append(row)
          
    
    csvwriter.writerows(list)
    file1.close()
    file2.close()
else:
    print("File not present in " + path)


file = open(path+"/new.csv","r")

for line in file:
    print(line)

file.close()