user1 = int(input("Enter a start number: "))
user2 = int(input("Enter an end number: "))
total = 0
for i in range(user1, user2 + 1):
    total += i
print("The total is:", total)
