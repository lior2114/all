print("============A=============")
salary1 = int(input("enter your 1 salary: "))
salary2 = int(input("enter your 2 salary: "))
salary3 = int(input("enter your 3 salary: "))
salary4 = int(input("enter your 4 salary: "))
salary5 = int(input("enter your 5 salary: "))
salary6 = int(input("enter your 6 salary: "))
packing = {"first":salary1, "second":salary2, "third":salary3, "fourth":salary4, "five":salary5, "six":salary6}

print("============B=============")
summ = 0
counter = 0
for values in packing.values():
    summ+= values
    counter += 1    
print(summ/counter)

print("============C=============")
max = 0
for val in packing.values():
    if val > max:
        max = val
print(f"the most high salary you got is: {max}")

print("============D=============")
# min = float("inf") #קוד בתוך פייתון למספר אינסופי חיובי שכל מה שנשווה אליו יהיה קטן ממנט 
min = packing["first"] #השוואה לערך הראשון ומשם מתחילה הבדיקה 
for val in packing.values():
    if val < min: # הרי המספרים יותר קטנים מאינסוף שהשוונו אותם אליו 
        min = val # אז כאן משווים את המספר הקטן ומחליפים את האיןסוף 
print(f"the lowest salary you got is: {min}")
