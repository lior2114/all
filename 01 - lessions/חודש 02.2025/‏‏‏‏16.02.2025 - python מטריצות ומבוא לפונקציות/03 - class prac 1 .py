import numpy as np
matrix = [
    [12,23,34,45],
    [56,67,78,89],
    [10,20,30,40]
]

print(matrix)
sum = 0 
counter = 0
for num in matrix:
    for n in num:
        sum +=n 
        counter += 1 #לספור כמה מספרים יש במטריצה בסך הכל בשורה 1 2 3 וכן הלאה
print(sum)
 #אופציה א
avg = sum/counter
print(avg)
#אופציה ב 
print(np.mean(matrix))

max = matrix[0][0]
for num in matrix:
    for m in num:
        if m > max:
            max = m 
print(f"max number is: {max}")

min = matrix[0][0]
for minn in matrix:
    for mm in minn:
        if mm < min:
            min = mm
print(f"the lowest number is: {min}")

#הדפסת המטריצה בצורה כמו שהיא נראת במקור
for numbers in matrix:
    for num in numbers:
        print(num, end = " ")
    print()


# אופציה א
for i in range (len(matrix)):#לולאה שעושה פעולה על כל השורות
    for j in range (len(matrix[i])):#לולאה שעושה פעולה על כל העמודות
        if matrix[i][j] %2 == 0:#בדיקה אם המספר זוגי
             matrix[i][j] = "x"#החלפת המספר באות
print(matrix)

# אופציה ב
for numbers in matrix:
    for num in numbers:
        if num % 2 == 0:
            print("x", end = " ")
        else:
            print(num, end = " ")
    print()




# אופציה א
for i in range (len(matrix)):
    for j in range (len(matrix[i])):
        if matrix[i][j] % 7 == 0 or matrix[i][j] % 10 == 7:
            matrix[i][j] = "*"
print(matrix)

# אופציה ב
for numbers in matrix:
    for num in numbers:
        if num % 7 == 0 or num % 10 == 7:
            print("*", end = " ")
        else:
            print(num, end = " ")
    print()