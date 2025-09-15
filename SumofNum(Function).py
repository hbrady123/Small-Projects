def total(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total
print(total(6, 16))       
print(total(1000, 2024))