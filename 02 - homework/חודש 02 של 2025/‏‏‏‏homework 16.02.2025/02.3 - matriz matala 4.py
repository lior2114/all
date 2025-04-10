matriza = [[0]*4 for i in range(3)]
print(matriza)

for i in range(3):
    for j in range(4):
        matriza [i][j] = int(input(f"for student {i+1} enter grade {j+1} : "))
print(matriza)

for i in matriza:
    for j in i:
        print(j, end = " ")
    print()
    
print ("=========max avg========")
summ = 0
counter = 0
max = 0 
for i in matriza:
    for j in i:
        summ += j 
        counter += 1
    print(f"the sum of line 1 is: {summ}", end=" ")
    print()
    avg = summ/counter
    print(f" the avg of student {j} is: {avg}")
    if avg > max:
        max = avg
    summ = 0
    counter = 0
print("======max avg is:======")
print(max)

print ("=========lowest avg========")
summ = 0
counter = 0
minnn = float('inf') #מזהה את המשתנה בתור מספר אין סופי זה קוד מובנה בתוך פייתון 
min = []
for i in matriza:
    for j in i:
        summ += j
        counter += 1 
    avg = summ/counter
    if avg < minnn: 
        minnn = avg
        min = i # כאן אני מכניס את השורה של המטריצה שהממוצע שלה הוא הנמוך ביותר כי אנחנו עדין בתור הלולאה של השורה
    summ = 0
    counter = 0
print("========lowest avg is:========")
print(f"the lowest list is {min} and its avarage is: {minnn}")

#אופציה ב'
# summ = 0
# counter = 0
# min_avg = float('inf')
# min_line = []
# for i in matriza:
#     for j in i:
#         summ += j
#         counter += 1
#     avg = summ / counter
#     if avg < min_avg:
#         min_avg = avg
#         min_line = i
#     summ = 0
#     counter = 0

# print(f"The line with the lowest average is: {min_line} with an average of {min_avg}")