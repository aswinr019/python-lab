
#find gcd of two numbers
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

common1 = []
common2 = []

for i in range(1,a+1):
    if a%i ==  0 :
        common1.append(i)

for i in range(1,b+1):
    if b%i ==  0 :
        common2.append(i)

set1 = set(common1)
set2 = set(common2)

factors = set1.intersection(set2)

print("Greatest common divisor of ",a," , ",b, " is ",max(factors))