grades = []
for i in range (5):
    g = int(input(f"enter your {i} grade: "))
    grades.append(g)

# אופציה א לפי ערכים של כמה שווה 
for g in grades:
    if g < 0 or g > 100:
        print (f"you must enter a number between 0-100 the incorrect number is: {g}")
    else:
        print (f"the good numbers are: {g}")


# אופציה ב לפי מיקומים 
for j in range (len(grades)):
    if grades [j] <0 or grades [j] > 100:
        print (f"you must enter a number between 0-100 the incorrect number is: { grades [j]}")
    else:
        print (f"the good numbers are: {grades [j]}")


#אופציה ג

grades = []
for i in range (5):
    g = int(input(f"enter grade {i}: "))
    grades.append(g)
for i in grades:
    if i <= 100 and i > 0:
        print (f"the good grades are: {i}")
    if i > 100 or i < 0:
        print(f"enter a numbers that are between 0-100 the incorrect numbers are: {i}")
