for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k)

for i in range(6):
    for j in range(i, i + 5):
        print(j, end=', ')
    print()


x = int(input("Enter a number: "))

for i in range(1, x + 1):       
    for j in range(i):           
        print("*", end="")       
    print()    
