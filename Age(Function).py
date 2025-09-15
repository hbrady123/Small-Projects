def age_class(age):
    if age <= 1:
        return "infant"
    elif age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    else:
        return "adult"
    
print(age_class(0))   
print(age_class(12))  
print(age_class(15))  
print(age_class(20))