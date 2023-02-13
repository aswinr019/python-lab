#From a list of integers , create a list removing even numbers
n = int(input("How many numbers : "))
list = []
list2 = []
print("Enter " , n ," numbers : ")
for i in range(n):
    a = int(input())
    list.append(a)

print("List before removing even numbers : ",list)
for elm in list:
   if( elm % 2 == 0):
        list2.append(elm)

print("List after removing even numbers : ",list2)
