class Publisher : 

    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

class Book(Publisher) : 

    def __int__(self,author,title):
        self.author = author 
        self.title = title



class Python(Book) :

    def __init__(self,price,no_of_pages):
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        print("Price : ",self.price)
        print("No of pages : ",self.no_of_pages)


pages = int(input("Enter the number of pages: "))
price = int(input("Enter the price of the book: "))

p = Python(price,pages)

Python.display(p)



