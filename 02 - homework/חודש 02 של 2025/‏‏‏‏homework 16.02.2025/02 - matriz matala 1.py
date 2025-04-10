matrix = [[12, 23, 34, 45], [56, 67, 78, 89], [10, 20, 30, 40]]
for i in matrix:
    for j in i:
        print(j, end = " ")
    print()

print ("=========sum and avg========")
summ = 0
counter = 0 
for i in matrix:
    for j in i:
        summ += j
        counter += 1
print(summ)
print(f"avg is: {summ/counter}")

print ("=========max========")
max = 0
for i in matrix: 
    for j in i:
        if j > max:
            max = j 
print(max) 

print ("=========min========")
min = matrix[0][0]
for i in matrix:
    for j in i:
        if j < min:
            min = j 
print(min)

print ("=========zogi========")
for i in matrix:
    for j in i:
        if j % 2 == 0:
            print(j , end = " ")
        else:
            print("*", end = " ")
    print()

print ("=========7========")
for i in matrix:
    for j in i: 
        if j % 7 == 0 or j % 10 == 7:
            print("*" , end = " ")
        else: 
            print(j, end = " ")
    print()