a = int(input("Enter  number : "))


factors = []


for i in range(1,a):
    if a%i ==  0 :
        factors.append(i)

print("the factors of the number " ,a, " are: ",factors)