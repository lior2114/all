print("========A=========")
const_matrix = [[12, 23, 34, 45], [56, 67, 78, 89], [10, 20, 30, 40]]
for i in const_matrix:
    print(i)

print("========B=========")
summ = 0 
counter = 0 
for i in const_matrix:
    for j in i:
        summ+=j
        counter+=1
print(summ)
print(summ/counter)

print("========C=========")
maxx = 0
for i in const_matrix:
    for j in i:
        if j >= maxx:
            maxx = j 
print(maxx)

print("========D=========")
min = float("inf")
for i in const_matrix:
    for j in i:
        if j < min:
            min = j 
print(min)

print("========E=========")
for i in const_matrix:
    for j in i: 
        if j%2 != 0:
            print("x",  end =" ")
        else:
            print(j, end =" ")
    print() #בסוף כל סיבוב שירד שורה 

print("========F=========")
for i in const_matrix:
    for j in i:
        if j % 7 == 0 or j%10 == 7:
            print("*", end = " ")
        else: 
            print(j , end = " ")
    print()