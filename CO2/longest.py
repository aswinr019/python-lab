#accept a list of words and return the longest word

n = int(input("How many words : "))

print("Enter ",n," words : ")
list = []
count = []

for i in range(n):
    string = input()
    list.append(string)

for i in list:
    count.append(len(i))

print("the length of longest word is : ",max(count))