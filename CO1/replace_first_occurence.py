s = input("Enter a string : ")
 
first = s[0]
 
new = s.replace(first,'$')

newstr = new.replace('$',first,1)

print(newstr)