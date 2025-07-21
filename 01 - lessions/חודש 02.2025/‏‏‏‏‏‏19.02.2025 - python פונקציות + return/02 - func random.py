import random
#הפונקציה קולטת = ריקה 
def r():
    print("hello")
#הפונקציה מקבלת יש לה ערכים משתנים
def gf(x,y):
    print(gf(2,3))

print("==========A=========")
#מה שהפונקציה הזאת עושה היא מדפיסה מספר רנדומלי בין 1 ל 100
def random_number():
    num=random.randint(1,100)
    print(num)
random_number()

print("==========B=========")
#מה שהפונקציה הזאת עושה היא קוראת לפונקציה שמדפיסה מספר רנדומלי בין 1 ל 100 ומדפיסה אותו כ-10 פעמים
def random_10_numbers():
    for i in range(10):
        random_number() 
random_10_numbers()

print("==========C=========")
#מה שהפונקציה הזאת עושה היא מדפיסה מספר רנדומלי בין 10 ל 20
def random_max_min(max,min):
    num=random.randint(min,max)
    print(num,end=" ") #הדפסת מספר רנדומלי ומחזיר אותו לפונקציה הראשית ככה ברגע שנקרא לה נוכל להשתמש במספר שהיא הדפיסה
random_max_min(50,100) #מדפיס מספר בין 50 ל 100
print()
random_max_min(10,20) #מדפיס מספר בין 10 ל 20
print()
startint_num = int(input("Enter the start number: "))
endint_num = int(input("Enter the end number: "))
random_max_min(startint_num , endint_num) #מדפיס מספר בין המספרים שהמשתמש הכניס