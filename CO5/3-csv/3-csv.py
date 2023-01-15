import os
import csv

path = os.getcwd()

header = []
rows = []

if os.path.exists(path+"/username.csv"):
    file = open(path+"/username.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    
    for row in csvreader:
        rows.append(row)

    print(header)
    print(rows)

    file.close()
else:
    print("File doesn't exist!")

