def matriza (matrix):
    sum = 0 
    counter = 0
    for i in matrix:
        for j in i:
            sum += j
            counter += 1        
    avrage = sum/counter
    print(avrage)

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
matriza(mat)
