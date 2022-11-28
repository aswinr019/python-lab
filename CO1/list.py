#enter two lists of integers , check
# a)Wheather lists are of the same length
# b) Wheather list sums to the same value
# c) Whether any value occure in both


list1 = []
num = int(input("How many numbers in list one : "))

for i in range(num):
    n = int(input("Enter numbers  :  "))
    list1.append(n)


list2 = []
num = int(input("How many numbers in list two : "))

for i in range(num):
    n = int(input("Enter numbers  :  "))
    list2.append(n)


if len(list1) == len(list2):
    print("both list are of the same length!")
else : 
    print("list are not of the same length ")

sum1 = 0
sum2 = 0


for i in list1:
    sum1 = sum1+i
    
for i in list2:
    sum2 = sum2+i

if sum1 == sum2 :
    print("sum of both lists are the same!")
else : 
     print("sum of both lists are not the same!")
    
set1 = set(list1)
set2 = set(list2)
common = set1.intersection(set2)

if common :
    print(common, " are common elements")
else :
    print("no common elements in list! ")
