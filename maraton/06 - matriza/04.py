print("========A=========")
grades = []
for i in range (3):
    lis = []
    for j in range(4):
        n = int(input(f"enter grade number:{j+1}, for student number:{i+1} "))
        lis.append(n)
    grades.append(lis)

print("========B=========")
for i in grades:
    print(i,end = " ")
    print()

print("========C=========")
# אופציה א
for gra in grades:
    summ = 0
    counter = 0
    avg = 0
    max = 0
    for i in gra:
        summ += i 
        counter += 1 
        avg = summ/counter
    if avg > max:
        max = avg 
print(max)

# #אופציה ב 
# max_avg = max(sum(gra) / len(gra) for gra in grades)
# print(max_avg)

#אפשר גם לעשות אותו הדבר ב C
print("========D=========")
min_avg = float("inf")
seria = []
for row_grades in grades:
    avg = (sum(row_grades)/ len(row_grades))
    if avg < min_avg:
        min_avg = avg 
        seria = row_grades
print(seria, min_avg)
