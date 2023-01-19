class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img


    def __add__(self,other):
        r = self.real + other.real
        i = self.img + other.img
        return Complex(r,i)
    
    def display(self):
        print("Compelx number : ",self.real,"+",self.img,"i")



r1 = int(input("Enter the real part of first compex number : "))
r2 = int(input("Enter the real part of second compex number : "))
i1 = int(input("Enter the imaginary part of first compex number : "))
i2 = int(input("Enter the imaginary part of second compex number : "))


c1 = Complex(r1,i1)
c2 = Complex(r2,i2)


print("first")
print("______")
c1.display()

print("second")
print("______")
c2.display()

c3 = c1 + c2

print("result")
print("______")
c3.display()