# Write a python program using nested loops to print a right angled triangle using stars


rows = 5
for i in range(1, rows + 1):
    
    for j in range(i):
        print("*", end="")

    print()
