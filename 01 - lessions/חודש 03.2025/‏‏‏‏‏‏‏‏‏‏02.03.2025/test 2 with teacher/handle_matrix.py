print("=======D=======")
def max_number_and_index (matriz):
    if len(matriz) <= 0:
        raise ValueError ("empty matriza!") 
    for i in matriz:
        for j in i:
            if not isinstance(j,int):
                raise TypeError ("enter only number!")
    max_value = matriz[0][0]
    row = 0
    col = 0 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > max_value:
                max_value = matriz[i][j]
                row,col = i,j
    return max_value,row,col

#יותר היה מובן
# # print("=======D2=======")
#     maxx = 0 
#     max_row = -1
#     max_rowinrow = -1 # כי המטריצה מתחילה מ 0 והלולאה מ 1 ככה שלא יהיה בלבול אז מתחילים מ -1 ואז זה ישר יקפוץ ל 0 
#     for indexi,i in enumerate(matriz):
#         for indexj,j in enumerate(i): # בקוד שלך, enumerate משמש כדי לעבור על השורות של המטריצה ולקבל גם את האינדקס של כל שורה:
#             if j > maxx:
#                 maxx = j
#                 max_row = indexi
#                 max_rowinrow = indexj
#     return (maxx, max_row,max_rowinrow)






# print("=======D3=======")
    # if not matriz or not any(matriz):
    #     raise ValueError("The matrix is empty")

    # max_value = float('-inf')# ערך אין סופי שלילי ככה שהכל יהיה גדול ממנו 
    # max_row = -1
    # max_col = -1

    # for row_index, row in enumerate(matriz):
    #     for col_index, value in enumerate(row):
    #         if value > max_value:
    #             max_value = value
    #             max_row = row_index
    #             max_col = col_index

    # return (max_value, max_row, max_col)
