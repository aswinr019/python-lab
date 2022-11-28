#create a single string separated with space from two strings by swapping the characters at position 1
string1 = input("Enter string one : ")
string2 = input("Enter string two : ")
s1 = string1[0]
s2 = string2[0]
string3 = s2 + string1[1::]
string4 = s1 + string2[1::]

string = string3 +' '+ string4

print(string)