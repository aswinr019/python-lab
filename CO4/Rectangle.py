

class Rectangle :

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)

    def peri(self):
        return (2*(self.length + self.breadth))



a= int(input("Enter length of rectangle one : "))
b= int(input("Enter breadth of rectangle one : "))
c= int(input("Enter length of rectangle two : "))
d= int(input("Enter breadth of rectangle two : "))

rectangle1 = Rectangle(a,b)
rectangle2 = Rectangle(c,d)

area1 = Rectangle.area(rectangle1)
area2 = Rectangle.area(rectangle2)
peri1 = Rectangle.peri(rectangle1)
peri2 = Rectangle.peri(rectangle2)
print("area of rectangle one",area1)
print("area of rectangle two",area2)
print("perimeter of rectangle one",peri1)
print("perimeter of rectangle one",peri2)

if( area1 > area2):
    print("rectangle one is bigger")
else : 
    print("rectangle two is bigger")