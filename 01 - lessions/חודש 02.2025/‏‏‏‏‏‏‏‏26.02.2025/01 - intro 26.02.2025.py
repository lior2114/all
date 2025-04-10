import random
print("==========A=========")
def ran():
    num = random.randint(1,100)
    return num # החזרה לפונקציה ערך 

x = ran() #השוואת הערך שבפונקציה לתוך ערך חיצוני כדי שאוכל להציג אותו  
print(x)