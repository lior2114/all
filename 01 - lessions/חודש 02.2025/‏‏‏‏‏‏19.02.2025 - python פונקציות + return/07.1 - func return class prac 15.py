import random 

def numbers_2 (x,y):
    if x>y:
        y,x = x,y #אם המשתמש הכניס את המספר הקטן ראשון אז מחליף בניהם כי אחרת האפליקציה קורסת
    num = random.randint(x,y)#מספר רנדומלי בין x ל y
    return (num)
x = numbers_2(10,15) #משווה את x ו y למספרים 
print(x)

x1 = int(input("enter number 1: "))
x2 = int(input("enter number 2: "))
x = numbers_2(x1,x2)
print(x)

def max_numbers(): #הפונקציה ריקה כי כבר מחזירים אליה משתנה אם היא הייתה מלאה לא היה אפשר להכניס אליה משתנים אחרים 
    x1 = int(input("enter number1: "))
    x2 = int(input("enter number2: "))
    x3 = int(input("enter number3: "))
    return max(x1,x2,x3)

x = max_numbers()
print(x)
