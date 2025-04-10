# פונקציה שמחזירה ערך
# הפונקציה מקבלת 3 מספרים ומחזירה את הממוצע שלהם
print("=====A=====")
def average_numbers(x, y, z):
    average = (x + y + z) / 3
    return average
# קריאה לפונקציה והדפסת התוצאה
result = average_numbers(1, 2, 3)
print(result)  # פלט: 2.0


# פונקציה שמדפיסה ערך
# הפונקציה מקבלת 3 מספרים ומדפיסה את הממוצע שלהם
print("=====B=====")
def print_average_numbers(x, y, z):
    average = (x + y + z) / 3
    print(average)
# קריאה לפונקציה
print_average_numbers(1, 2, 3)  # פלט: 2.0


# פונקציה ללא פרמטרים
# הפונקציה מדפיסה הודעה קבועה
print("=====C=====")
def greet():
    print("Hello, world!")
# קריאה לפונקציה
greet()  # פלט: Hello, world!


# פונקציה עם פרמטרים ברירת מחדל
# הפונקציה מקבלת שם ומדפיסה הודעת ברכה
print("=====D=====")
def greet_with_name(name="Guest"):
    print(f"Hello, {name}!")
# קריאה לפונקציה עם פרמטר
greet_with_name("Alice")  # פלט: Hello, Alice!
# קריאה לפונקציה ללא פרמטר
greet_with_name()  # פלט: Hello, Guest!


# פונקציה עם מספר משתנה של פרמטרים
# הפונקציה מקבלת מספר משתנה של פרמטרים ומדפיסה את כולם
print("=====E=====")
def print_all(*args):
    for arg in args:
        print(arg, end=" ")
    print()
# קריאה לפונקציה עם מספר משתנה של פרמטרים
print_all(1, 2, 3)  # פלט: 1 2 3 
print_all("a", "b", "c")  # פלט: a b c 


# פונקציה עם פרמטרים מילות מפתח
# הפונקציה מקבלת פרמטרים מילות מפתח ומדפיסה אותם
print("=====F=====")
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# קריאה לפונקציה עם פרמטרים מילות מפתח
print_kwargs(name="Alice", age=30)  # פלט: name: Alice age: 30
