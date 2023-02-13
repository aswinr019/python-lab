

year1  = int(input("Enter the base year : "))

year2  = int(input("Enter the last year : "))

print("Leep years between ",year1," and ",year2, " are  ")
for i in range(year1,year2):
    if(i % 4 == 0 or i % 400 == 0):
        print(i)
