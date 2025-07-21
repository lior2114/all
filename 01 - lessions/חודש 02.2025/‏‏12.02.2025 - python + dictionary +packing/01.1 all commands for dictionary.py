# שיטות של מילון בפייתון

# 1. clear()
# מסיר את כל הפריטים מהמילון.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # פלט: {}

# 2. copy()
# מחזיר עותק שטחי של המילון.
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = my_dict.copy()
print(new_dict)  # פלט: {'a': 1, 'b': 2, 'c': 3}

# 3. fromkeys()
# יוצר מילון חדש עם מפתחות מרשימה נתונה וערכים מוגדרים לערך מסוים.
keys = ('a', 'b', 'c')
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # פלט: {'a': 0, 'b': 0, 'c': 0}

# 4. get()
# מחזיר את הערך עבור המפתח הנתון אם המפתח נמצא במילון.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)  # פלט: 2

# 5. items()
# מחזיר אובייקט תצוגה שמציג רשימה של זוגות מפתח-ערך במילון.
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # פלט: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 6. keys()
# מחזיר אובייקט תצוגה שמציג רשימה של כל המפתחות במילון.
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)  # פלט: dict_keys(['a', 'b', 'c'])

# 7. pop()
# מסיר את המפתח הנתון ומחזיר את הערך המתאים.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.pop('b')
print(value)  # פלט: 2
print(my_dict)  # פלט: {'a': 1, 'c': 3}

# 8. popitem()
# מסיר ומחזיר את זוג המפתח-ערך האחרון כטופל.
my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem()
print(item)  # פלט: ('c', 3)
print(my_dict)  # פלט: {'a': 1, 'b': 2}

# 9. setdefault()
# מחזיר את הערך של המפתח הנתון. אם המפתח לא קיים, מוסיף את המפתח עם הערך הנתון.
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.setdefault('d', 4)
print(value)  # פלט: 4
print(my_dict)  # פלט: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 10. update()
# מעדכן את המילון עם זוגות מפתח-ערך נתונים.
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update({'d': 4, 'e': 5})
print(my_dict)  # פלט: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 11. values()
# מחזיר אובייקט תצוגה שמציג רשימה של כל הערכים במילון.
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)  # פלט: dict_values([1, 2, 3])