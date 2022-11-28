#prompt the user for a list of integers . For all values greater than 100 store 'over' instead
numbers = []
num = int(input("How many numbers : "))

for i in range(num):
    n = int(input("Enter number "))
    numbers.append(n)

for i in range(num) :
    if numbers[i] > 100:
        numbers[i] = "over"
        
print(numbers)