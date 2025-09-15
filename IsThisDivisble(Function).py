def isthisdivisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if isthisdivisible(num1, num2):
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")
    




