dictionary = { "jan":31,"feb":28,"mar":30,"apr":31}

month = input("enter a month( 3 chars ) : ")

print("The number of days in ",month," is ", dictionary[month])

delete = input("Enter a month to delet( 3 chars ) : ")

dictionary.pop(delete)

print(delete," removed!")

key = input("Enter a month to add to dictionary : ")

value = int(input("Enter the number of days of the month : "))

dictionary[key] = value


print("sorted items (asc) ",sorted(dictionary.items()))
print("sorted items (dec) ",sorted(dictionary.items(),reverse=True))
