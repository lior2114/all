class Person: #קלאסים מתחילים מאות גדולה 

#חלק ראשון הבניה 
 # __init__ אומר שזה פונקצית הכנסה חובה להשים אותו 
    def __init__ (self,age1,firstname1,lastname1): #self = האובייקט, המופע
        self.age = age1
        self.firstname = firstname1
        self.lastname = lastname1

# חלק שני פונקציות
    def display(self):
        print("hello")
        print(f"my name is {self.firstname} {self.lastname} and i am {self.age} years old")
    
    def up_age(self):
        self.age+=1
    
    def __str__ (self):
        return f"{{'firstname': '{self.firstname}', 'lastname': '{self.lastname}', 'age': {self.age}}}"
    '''
    בגלל שיש ריטרן אז הוא לא ידפיס לי את המיקום בזיכרון של אותו קלאסס 
    אבל כשנציג אותו כמו בשורה 27 הוא ידפיס את הפונקציה הזאת
    '''

    def write_file(self):
        try:
            with open(f"./{self.firstname}.txt", 'w') as file:
                file.write(f"{{'firstname': '{self.firstname}', 'lastname': '{self.lastname}', 'age': {self.age}}}")

        except Exception as err:
            print(err)

    @property
    def is_old(self):
        return self.age >= 18




'''
רשום הכל במיין 
'''
# p1 = Person(14, "lebron","james") #p1 הוא האובייקט
# p1.up_age() # פונקציה שמעלה את הגיל ב 1 
# p1.display() #מדפיס את המשפט שרשמנו בשורה 12
# print(p1) # ציג את מה שמחזירה הפונקציה אם אין פקודת ריטרן מחזיר את המיקום בזיכרון 
# p1.write_file() # יוצר קובץ עם השם הראשון של אותו בחור ועם כל הפרטים שלו בפנים 
# # print(p1.age) #מחזיר רק את הגיל
# # print(p1.firstname) #מחזיר שם ראשון
# # print(p1.lastname) # מחזיר שם משפחה
# print(p1.is_old)

#לדוגמא אפשר להוסיף גם עוד 
# p2 = Person(12, "arik","edome") #p2 הוא האובייקט
# print(p2)
# print(p2.age)
# print(p2.firstname)
# print(p2.lastname)