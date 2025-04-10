import numpy as e #אפשר במקום e לרשום מה שרוצים 
print("==========A=========")
def some_matriza(matriz):
    #אופציה א 
    summ = 0 
    counter = 0 
    for i in matriz:
        for j in i:
            summ += j 
            counter += 1
    # אופציה ב 
    avg = e.mean(matriz)
    return avg


print("==========B=========")
mat = [ 
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
x = some_matriza(mat)
print(x)