print("==========A=========")
def is_evenv1(num):
    if num %2==0:
        return True 
    return False # אם התנאי לא קיים אז הוא יחזיר שגיאה

num = int(input("enter number to know if its even: "))
if is_evenv1(num):
    print(f"{num}, is even")


print("==========B=========")
def is_evenv2(num):
    return num%2==0 #מחזיר נכון אם הוא מתחלק או לא נכון עם לא מתחלק 

num = int(input("enter number to know if its even: "))
if is_evenv2(num):
    print(f"{num}, is even")