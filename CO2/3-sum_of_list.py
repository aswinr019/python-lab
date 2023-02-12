#Find the sum of all items in a list 
num = int(input("how many elements : "))

list = []
sum = 0

print("enter ",num," numbers : ")
for i in range(num):
    n  = int(input())
    list.append(n)

for i in range(num):
    sum = sum+list[i]

print("Sum of list elements is ",sum)