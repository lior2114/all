print("========A=========")
multiplication_board = []
for i in range (1,11):
    mut = [] #אין צורך בקליר כי הרשימה בכל סיבוב מתחילה מחדש כי היא בתוך הלולאה הראשונה 
    for j in range (1,11):
        multe = j*i
        mut.append(multe)
    multiplication_board.append(mut)

print("========B=========")
summ = 0     
for row in multiplication_board:
    print(row)
    for j in row:
        summ+= j 
print(summ)
