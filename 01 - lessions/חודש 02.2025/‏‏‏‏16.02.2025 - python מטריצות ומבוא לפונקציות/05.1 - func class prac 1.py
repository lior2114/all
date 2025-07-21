import random

def randomi():
    ran = random.randint(1, 100)
    print(ran)

print("=====random 10 numbers======")
def randomi2():
    for i in range(10):
        randomi() # קוראים לפונקציה שמדפיסה מספר רנדומלי וכל פעם שהיא נקראת היא מדפיסה מספר אחר
randomi2()