#Count the number of characters (character frequency) in a string. 

string = list(input("Enter a string : "))


unique = set(string)

count = {}

for elm in unique:
    count[elm] = string.count(elm)


print("Character count : ",count)