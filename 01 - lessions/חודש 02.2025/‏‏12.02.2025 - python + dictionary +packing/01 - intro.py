# list [] #ליסט רגיל
# set = set() # אין כפילויות או סדר ברשימה
# tuple = () # לא ניתן לשנות את המשתנים בתוך הרשימה 





print ("=============unpacking 1=====================")
#לשים לב לסוגריים
friends1 = ('John', 'Michael', 'Terry', 'Eric', 'Graham') #זה נקרא טאפל רשימה שלא ניתן לשנות אותה
friends2 = ['John', 'Michael', 'Terry', 'Eric', 'Graham'] #זה רשימה שניתן לשנות אותה

first,second,third,fourth,fifth = friends1 #כאן אני מפרק את הטאפל רשימה למשתנים נפרדים
print(first) #מדפיס את המשתנה הראשון

print ("=============unpacking 2=====================")
#אופציה א'
#             לא משנה מה השם שבא אחרי הכוכבית זה יהיה השאר
first,second,*other = ['John', 'Michael', 'Terry', 'Eric', 'Graham'] #כאן אני מפרק את הרשימה למשתנים נפרדים ומשתנה שמכיל את השאר
print(*other) #מדפיס את השאר
print(other)#בלי כוכבית זה יוצר ליסט חדש של השאר
# אופציה ב'
first,*other,second = ['John', 'Michael', 'Terry', 'Eric', 'Graham'] 
print(*other) #מדפיס את מה שבניהם 
print(second)# second יהיה האחרון אפשרי בכללי לרשום מה שרוצים

print ("=============conver tuple to list=====================") #טאפל

children = ('Sue', 'John', 'Alice', 'John')
print(children)
children = list(children) #ממיר טאפל לרשימה
print(children)

print ("=============conver list to tuple=====================") 

children = ['Sue', 'John', 'Alice', 'John']
print(children)
children = tuple(children) #ממיר רשימה לטאפל
print(children)

print ("=============no dupllicate=====================") #נקרא סט set

numbers= {10,20,20,10} #סוגרים מסולסלים מדפיסים בלי כפילויות אם היו כפילויות הוא מוחק אותם 
print(numbers)
#print(numbers[0])  #יהיה שגיאה כי בסט אין מיקומים לכלום
#אופציה ב'
products = set() # כדי ליצור רשימה ריקה של סט לתוך משתנה


print ("=============dictionary=====================")

products = {"apple":3.5, "Banana":4, "peach":5,"peach":4} #אם יש לנו שתי פריטים שהם אותו הדבר אז האחרון מבינהם דורס את הקודם 
print(products)
print(products["apple"])
products["Banana"] = 200 #שינויי ערך בדיקשינרי  
print(products)

#סורק רק את המילים בדיקשינרי
for key in products:
    print(key, end = "|")

#אופציה ב' מחזיר את כל המילים ל products.keys
for key in products.keys():
    print(key, end ="|")

#מדפיס את המספרים 
for values in products.values():
    print(values, end ="|")

#מדפיס את שניהם 
for key in products.keys():
    #               המיקום והמספר שרשום לידו 
    print(f"{key} ===> {products[key]}")
print()

# מוציא כל מילה עם הערך שלה 
#products.items() אם מציגים אותה לבד מוציאה לבד את כל המילים עם הערכים שלהם
for item in products.items():
    key, values = item # פקודת הוצאה שמוציאה את שתי המשתנים ומכניסה אותם לאייטמס
    print(f"{key}===> {values}")

#אופציה ב'
for key,value in products.items():
    print(f"{key}===> {values}")