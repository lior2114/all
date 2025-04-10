#numbers = []
#for i in range (10):
   # num = int(input("enter a number for the list: "))
    #numbers.append(num)

n = [10, 20, 40 ,50 , 60, 80, 90, 60, 100, 110]
print("the list is: ", n)
print("the 3rd is: ", n[2])
print("the list no first and last: ", n [1:-1])

#מחיקת מספר מהליסט
n2 = int(input( "enter number to delte from the list: "))
if n2 in n:
    n.remove(n2)
print (n)

print ("the number in jump of 2 is: " , n[0:len(n):2]) #קפיצות של 2 א
print ("the number in jump of 2 is: " , n[1:10:2])#קפיצות של 2 ב
print ("the number in jump of 2 is: " , n[::2])# deafult 0, deafult end , jump 2
print ("the number in jump of 2 is: " , n[1::2])# 1, deafult end , jump 2

print ("the number in jump of 3 is: " , n[0:len(n):3])#אפשרי אותו הדבר כמו למעלה רק עם קפיצות של 3

#סריקת איברים
#[10, 20, 40 ,50 , 60, 80, 90, 60, 100, 110]
for x in n:
    if x%2 == 0:
        print(x, "is even")

#סריקת האינדקסים הם(המיקומים שלהם)
for i in range (len(n)):
    #i מסמן את המיקום שברשימה של ה אן 
    if n[i] %2 ==0:
        print (n[i] , "is even ")

