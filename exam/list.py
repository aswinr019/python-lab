n1 = int(input("Enter the number of elements in list one "))
n2 = int(input("Enter the number of elements in list two "))
list1= []
list2 = []
list3 = []


print("Enter list one :")

for i in range(n1):
    a =int(input())
    list1.append(a)

print("Enter list two :")

for i in range(n2):
    b =int(input())
    list2.append(b)

list1.sort()
list2.sort()

# list1.append(list2)
list3 = list1 + list2
list3.sort()
# print(type(list3))
print("Sorted list is : ",list3)