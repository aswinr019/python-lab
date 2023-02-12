#List comprehensions
# a)Generate positive list of numbers from a given list of integers
# b)square of N numbers 
# c)form a list of vowels selected from a given word
# d)list ordinal values of each word in a line of text


# list = []

# n = int(input("How many numbers : "))

# for i in range(n):
#     num = int(input("Enter number : "))
#     list.append(num)

# print("Positive numbers : ")
# for i in list:
#     if i > 0 :
#         print(i)
       
# print("Square of numbers : ")
# for i in list:
#         print(i*i)
       
# vowels = []

# string = input("Enter a string : ")

# for i in range(0,len(string)):
#     if ((string[i] == 'a') or  (string[i] == 'e') or  (string[i] == 'o') or (string[i] == 'i')   or (string[i] == 'u')):
#         vowels.append(string[i])

# print("Vowels in the string : ",vowels)

# print("list ordinal values of the string : ")
# for i in range(0,len(string)):
#     print(ord(string[i]))
    

list = []
positive = []
square = []
ordinal = []

n = int(input("How many nyumbers : "))

print("Enter ",n," numbers : ")

for i in range(n):
    num = int(input())
    list.append(num)

positive = [ num for num in list if num > 0]
print("Positive list : ",positive)

n = int(input("How many numbers : "))
square = [ num*num for num in range(1,n+1) ]
print("Square list : ",square)



word =  input("Enter a word : ")
vowels = [ elm for elm in word if (elm == 'a') or  (elm == 'e') or  (elm == 'o') or (elm == 'i')   or (elm == 'u')]
print("Vowel list : ",vowels)


string =  input("Enter a string : ")
ordinal = [ ord(elm) for elm in string]
print("Ordinal list : ",ordinal)





