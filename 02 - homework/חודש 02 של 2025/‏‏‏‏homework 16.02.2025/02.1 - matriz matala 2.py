
print("==========A=============")
#אופציה א'
matrix= []
for i in range(1,11): #מכניס את המספרים מ1 עד 10
    line= [] #מייצר רשימה ריקה
    for j in range (1,11): #מכפיל את המספרים מ1 עד 10
        line.append(i*j) #מכניס את המספרים לתוך הרשימה בהכפלה
    matrix.append(line) #מכניס את הרשימה לתוך המטריצה
for i in matrix:
    print(i) #מדפיס את המטריצה בצורה יפה

mutliboard = [[0]*10 for _ in range (10)] #מייצר רשימה ריקה עם 10 תאים ומכפיל אותה ב10
print("==========B=============")
#אופציה ב'
for i in range (1,11):
    for j in range (1,11):
        mutliboard[i-1][j-1] = j*i #מה שהמינוס מצייג זה את המקום ברשימה

summ = 0 
for numbers in mutliboard:
    for num in numbers:
        print(num, end = " ")
        summ += num
    print()
print(summ)

