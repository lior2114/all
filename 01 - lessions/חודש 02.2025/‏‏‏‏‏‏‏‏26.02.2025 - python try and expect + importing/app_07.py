'''
app - בנוסף מכניסים את כל המקרים שיכולים לקרות לי של שגיאות 
'''
import calc_06

try:
    grade = int(input("enter grade: "))
    new_grade = calc_06.factor_grade(grade)
    print(new_grade)
except ValueError as err:
    print(f"value error {err}") #מתנקז הכל ל err
except Exception as err: #תמיד להשים באחרון כי אני לא יודע מה הארירורים  שיכולים להיות לי 
    print(f"some error: {err}")