import os
import pandas

path = os.getcwd()
cols = []

if os.path.exists(path+"/username.csv"):
    file = pandas.read_csv("username.csv")
    columns = file.columns

    for col in columns:
        cols.append(col)
    print(cols)
    
    select = input("Enter the columns you want to display : ")

    specific_cols = pandas.read_csv("username.csv",usecols = ["Username"] )

    print(specific_cols)
else:
    print("File doesn't exist!")
