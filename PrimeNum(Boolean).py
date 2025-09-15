def isPrime(num):
    if num < 2:   
        return False
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            return False
    return True

limit = int(input("Enter a number: "))

print(f"Prime numbers between 1 and {limit}:")
for n in range(1, limit + 1):
    if isPrime(n):
        print(n, end=" ")