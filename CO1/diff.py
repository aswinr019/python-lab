
#print out all colors from color-list1 not contained in color-list2. 
colors1 = input("Enter colors ( comma separated ) :").split(",")
colors2 = input("Enter colors ( comma separated ) :").split(",")

diff = set(colors1) - set(colors2)

print(diff)