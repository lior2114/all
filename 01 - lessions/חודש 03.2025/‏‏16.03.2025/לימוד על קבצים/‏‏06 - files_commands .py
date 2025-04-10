# פתיחת קובץ
file = open("example.txt", "r")  # פותח את הקובץ במצב קריאה
# דוגמה: אין פלט, אבל הקובץ מוכן לפעולות.

# קריאת כל התוכן של הקובץ
content = file.read()
print(content)  # # פלט: כל התוכן של הקובץ כמחרוזת.

# קריאת שורה אחת מהקובץ
file.seek(0)  # מאפס את מצביע הקובץ להתחלה
line = file.readline()
print(line)  # # פלט: השורה הראשונה של הקובץ.

# קריאת כל השורות לרשימה
file.seek(0)  # מאפס את מצביע הקובץ להתחלה
lines = file.readlines()
print(lines)  # # פלט: רשימה שבה כל אלמנט הוא שורה מהקובץ.

# כתיבה לקובץ
file = open("example.txt", "w")  # פותח את הקובץ במצב כתיבה
file.write("Hello, World!")  # כותב את המחרוזת לקובץ
# דוגמה: אין פלט, אבל הקובץ עכשיו מכיל את "Hello, World!".

# הוספה לקובץ
file = open("example.txt", "a")  # פותח את הקובץ במצב הוספה
file.write("\nAppended text.")  # מוסיף את המחרוזת לקובץ
# דוגמה: אין פלט, אבל הקובץ עכשיו מכיל את הטקסט שהוסף.

# שימוש ב-'with' לטיפול בקבצים (סוגר את הקובץ אוטומטית)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # # פלט: התוכן של הקובץ.

# בדיקה אם הקובץ ניתן לקריאה
file = open("example.txt", "r")
print(file.readable())  # # פלט: True אם הקובץ ניתן לקריאה, אחרת False.

# בדיקה אם הקובץ ניתן לכתיבה
file = open("example.txt", "w")
print(file.writable())  # # פלט: True אם הקובץ ניתן לכתיבה, אחרת False.

# סגירת קובץ
file.close()  # סוגר את הקובץ
# דוגמה: אין פלט, אבל הקובץ עכשיו סגור.

# קיצור קובץ
file = open("example.txt", "w")
file.write("This is a test.")
file.truncate(4)  # מקצר את הקובץ ל-4 התווים הראשונים
# דוגמה: אין פלט, אבל הקובץ עכשיו מכיל "This".

# קבלת המיקום הנוכחי של מצביע הקובץ
file = open("example.txt", "r")
print(file.tell())  # # פלט: המיקום הנוכחי של מצביע הקובץ.

# הגדרת מצביע הקובץ למיקום מסוים
file.seek(0)  # מעביר את מצביע הקובץ להתחלה
# דוגמה: אין פלט, אבל מצביע הקובץ עכשיו בהתחלה.

# מעבר על הקובץ שורה אחר שורה
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # # פלט: כל שורה בקובץ, אחת אחרי השנייה.
