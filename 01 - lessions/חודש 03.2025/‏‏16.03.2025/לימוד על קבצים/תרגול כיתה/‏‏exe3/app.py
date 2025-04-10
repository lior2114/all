from class1 import Speaker

s1 = Speaker("avater", "kora","red",100)
s2 = Speaker ("lol1","my1","yellow", 120)

s1.details()
s1.write_file()
print(s1.brand) #מציגים עם פרינט
print(s1) #__str__ מציגים עם פרינט

s2.details()
s2.write_file()
print(s2.brand) #מציגים עם פרינט
#print(s2.brand()) אם היה בלי הפרופרטי זה היה פונקציה רגילה ואז היינו צריכים להציג אותה עם הסוגריים
print(s2) #__str__ מציגים עם פרינט