'''
 טיפול בתקלות של אם הכניסו מספר לא נכון או אות בטעות או ההפניה לקובץ היא לא נכונה 
as err 
זה אומר הגדרת משתנה שיציג את הנתיב של הבעיה שנדע מאיפה היא נבעה 
'''
while True: #לא חובה רק שם בתוך לולאה
    try:
        grades = [100,90,80,60,40,100]
        index = int(input("enter number of your student search for grade: "))
        print(f"Grade of your student is: {grades[index]}")
    except ValueError as err:
        print(f"please enter right value {err}") # ערך שגוי
    except IndexError as err:
            print(f"please enter right index {err}") #אינדקס (מספר שגוי)
    except Exception as err: #(לדוגמא אם פנינו לקובץ שגוי או משהוא )
         print(f"input error {err}") #שגיאה כללית