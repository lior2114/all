print("==========A=========")
def some_matriza(matriz):
    maxx = 0
    for i in matriz: # ה איי מסמל את כמות הליסטים בתוך המטריצה
        for j in i: # הג'י מסמל את המספרים בכל שורה של המטריצה
            if j > maxx:
                maxx = j
    return maxx

print("==========B=========")
mat = [ 
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
x = some_matriza(mat)
print(x)