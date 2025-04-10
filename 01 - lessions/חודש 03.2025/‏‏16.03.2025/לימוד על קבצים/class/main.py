from class1 import Person
p1 = Person(14, "lebron","james") #p1 הוא האובייקט
p1.up_age() # פונקציה שמעלה את הגיל ב 1 
p1.display() #מדפיס את המשפט שרשמנו בשורה 12
print(p1) # מציג את מה שמחזירה הפונקציה אם אין פקודת ריטרן מחזיר את המיקום בזיכרון 
p1.write_file() # יוצר קובץ עם השם הראשון של אותו בחור ועם כל הפרטים שלו בפנים 
# print(p1.age) #מחזיר רק את הגיל
# print(p1.firstname) #מחזיר שם ראשון
# print(p1.lastname) # מחזיר שם משפחה
print(p1.is_old)
