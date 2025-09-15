count = 0
total = 0

while True:
    grade = int(input("Enter a grade: "))
    
    if grade == -1:    
        break
    elif grade < 0 or grade > 100:
        print("Error: Enter a grade between 0 and 100")
        continue
    
    total += grade     
    count += 1         

print("=====================")
print("Number of students:", count)
if count > 0:
    average = total / count
    print("Average grade:", round(average, 2))
else:
    print("No grades entered.")