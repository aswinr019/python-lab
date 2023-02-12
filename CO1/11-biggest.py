#find the biggest of three numbers entered 

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter thrid number : "))

if(a >b and a > c):
    print(a," is the biggest")
elif ( b > a and b > c):    
    print(b, " is the biggest")
else : 
    print(c,"is the biggest")