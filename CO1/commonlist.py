list1 = input("Enter list 1 elements ( comma separated ) ").split(",")
list2 = input("Enter list 2 elements ( comma separated ) ").split(",")

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

print("Commonn elements are : ",common)
