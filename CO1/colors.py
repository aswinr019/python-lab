#create a list of colors from comma separated color names entered by user. Display first and last colors

c = input("Enter colors ( coma separated ) ")

colors = c.split(',')

print("The first and last colors are ",colors[0],colors[-1])