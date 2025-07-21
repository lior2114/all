import random 

# def randomi():
#      numi=random.randint(1,100)
#     print(numi)
#randomi()


def random_number():
    num=random.randint(1,100)
    return num #מכניס את המספר שהפונקציה יצרה ומאחסן אותה בתוך הפונקציה

#מכניס את הפונקציה לתוך משתנה 
x=random_number()
print(x)
#עכשיו גם אפשר לעשות 
#לדוגמא
if x == 50:
    print("yes")   


def passi():
    pass #לדוגמא המתכנת סיים לעבוד ומחר הוא יחזור לעבוד על הפונקציה אז התוכנית מדלגת עליה 