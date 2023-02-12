# names = input("Enter names : ")

# count = names.count("a")

# print("The number of a's is ",count)



#store a list of names and count the occurences of 'a' within the list
n = int(input("Enter the number of names : "))
names = []
count = 0

print("Enter names : ")

for i in range(0,n):
    name = input()
    names.append(name)


for name in names:
    cnt = name.count("a")
    count = count+cnt

print("The number of a's is ",count)
