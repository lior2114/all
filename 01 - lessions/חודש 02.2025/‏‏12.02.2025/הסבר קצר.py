print("============= סט - רשימה ללא כפילויות =====================")
numbers = {10, 20, 20, 10}
print(numbers)  # מדפיס סט ללא כפילויות
# פלט: {10, 20}

print("============= מילון - dictionary =====================")
products = {"apple": 3.5, "Banana": 4, "peach": 4}
print(products)
# פלט: {'apple': 3.5, 'Banana': 4, 'peach': 4}

print(products["apple"])  # מדפיס ערך לפי מפתח
# פלט: 3.5

products["Banana"] = 200
print(products)  # מדפיס מילון עם ערך מעודכן
# פלט: {'apple': 3.5, 'Banana': 200, 'peach': 4}

for key in products:
    print(key, end="|")  # מדפיס מפתחות
# פלט: apple|Banana|peach|

for key in products.keys():
    print(key, end="|")  # מדפיס מפתחות
# פלט: apple|Banana|peach|

for value in products.values():
    print(value, end="|")  # מדפיס ערכים
# פלט: 3.5|200|4|

for key, value in products.items():
    print(f"{key} ===> {value}")  # מדפיס מפתחות וערכים
# פלט:
# apple ===> 3.5
# Banana ===> 200
# peach ===> 4

# דוגמאות נוספות:
print("============= הוספת פריט למילון =====================")
products["orange"] = 6
print(products)  # מדפיס מילון עם הפריט החדש
# פלט: {'apple': 3.5, 'Banana': 200, 'peach': 4, 'orange': 6}

print("============= מחיקת פריט מהמילון =====================")
del products["apple"]
print(products)  # מדפיס מילון ללא הפריט שנמחק
# פלט: {'Banana': 200, 'peach': 4, 'orange': 6}

print("============= בדיקת קיום מפתח במילון =====================")
print("Banana" in products)  # מדפיס True אם המפתח קיים
# פלט: True

print("============= איחוד שני סטים =====================")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # מדפיס את האיחוד של שני הסטים
# פלט: {1, 2, 3, 4, 5}

print("============= חיתוך שני סטים =====================")
intersection_set = set1 & set2
print(intersection_set)  # מדפיס את החיתוך של שני הסטים
# פלט: {3}