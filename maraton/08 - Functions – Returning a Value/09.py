'''
אם לא היית מחסיר 1 מהאינדקסים,
 היית מנסה לגשת לאינדקסים שמתחילים מ-1, מה שהיה גורם לשגיאה של 
 "IndexError" מכיוון שהאינדקסים במטריצה מתחילים מ-0.
'''
print("==========A=========")
def some_matriza(matriz):
    if matriz[i-1][j-1] != i*j:#ההסבר בכתום לכאן וזה אומר שאם הם לא כפולות אחד של השני זה יחזיר פולס
        return False
    else:
        return True 

print("==========B=========")
#מטריצה שנחזירה נכון 
mat = []
for i in range(1,11):
    rows = []
    for j in range(1,11):
        rows.append(i*j)
    mat.append(rows)
x = some_matriza(mat)
print(x)

print("==========C=========")
#מטריצה שנחזירה לא נכון 
mat = []
for i in range(1,11):
    rows = []
    for j in range(1,11):
        rows.append(i*j+1)#מחזירה לא נכון כי הוספנו לה אחד ואז זה לא כפולות רק אחד של השני אלא כפולות בתוספת אחד 
    mat.append(rows)
x = some_matriza(mat)
print(x)
