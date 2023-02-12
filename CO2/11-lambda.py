square = lambda x : x*x
triangle = lambda x,y : (x*y)/z
rectangle = lambda x, y : x*y


s = int(input("Enter the side of the square : "))
print("Area of square : ", square(s))

b = int(input("Enter the base of the triangle : "))
h = int(input("Enter  the height of the triangle : "))
print("Area of the triangle : " , triangle(b,h))


l = int(input("Enter the length of the rectangle : "))
b = int(input("Enter the breadth of the rectangle : "))
print("Area of the rectangle is : ", rectangle(l,b))
