grades = [80, 90, 60, 70, 90,100,70,80,90] #how to list 
# index   0    1   2   3   4   
print("grades: ", grades )# [80, 90, 40, 50, 60]
print ("first grade: ", grades[0])# 80
print("total grades: ", len(grades))# 5
print("last grade ", grades[-1])#last grade plan a 
print("last grade ", grades[len(grades)-1])#last grade plan b 
print("some grades:", grades [2:5]) #index 2-5
print("some grades:", grades [2: ]) #index 2 and above
print("some grades:", grades [:5]) #index 5 and below
print("some grades:", grades [1:5:1]) # 1-5 1 steps 

grades.append(1000) #add new item
print("grades:", grades)

#    המספר ששמים במקום     והמיקום שמחליפים
grades.insert(2,3000) # index מזיז את כל המספרים ימינה ושם את המספר 3000 בתור האינדקס השני 
print("grades:", grades)

last = grades.pop() #מוציאה מהרשימה את האיבר האחרון ומבצעת השמה ושמה את המספר האחרון בתוך המשתנה שהשוונו אליו 
print("the last number is: ", last)
print("grades after pop:", grades)

if 70 in grades:
    grades.remove(70)
print(grades)

friends = ["moshe"] #יצירת רשימה
for i in range(4):
    name = input("enter friends names: ")
    friends.append(name) #הוספת שמות לרשימה
print("my friends is: ", friends)

name = input("search for friends if exist: ")
if name in friends:
    print(f"{name} exist")
else:
    print("friend not exist")