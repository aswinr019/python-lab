#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’


string = input("Enter a string : ")

l = len(string)

if string[l-3:] == "ing":
    print(string+"ly")
else : 
     print(string+"ing")