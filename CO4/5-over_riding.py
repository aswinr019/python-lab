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

    def __init__(self,author,title,price,no_of_pages):
        self.author = author 
        self.title = title
        self.price = price
        self.no_of_pages = no_of_pages

    def display(self):
        print("Author : ",self.author)
        print("Title : ",self.title)
        print("Price : ",self.price)
        print("No of pages : ",self.no_of_pages)


author = input("Enter the name of the author: ")
title = input("Enter the title of the book: ")
pages = int(input("Enter the number of pages: "))
price = int(input("Enter the price of the book: "))

p = Python(author,title,price,pages)

Python.display(p)



