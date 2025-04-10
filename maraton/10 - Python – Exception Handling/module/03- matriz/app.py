import matriz as m

try: 
    matriza = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
  
    ]
    matriz_to_list = m.some_matriz(matriza)
    print(matriz_to_list)

except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except Exception as err:
    print("some eror")

