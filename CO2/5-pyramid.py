# Display the given pyramid with step number accepted from user. 
# Eg: N=4 
# 1
# 2 4 
# 3 6 9 
# 4 8 12 16 


n = int(input("How many layers : "))


for i in range(1,n+1):
    for j in range(i,(i*i)+1,i):
        print(j,end=" ")
    print(" ")
