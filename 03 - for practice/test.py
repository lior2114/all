n = int(input("enter a number: "))
counter = 0
if n ==0:
    counter = 1
while n != 0:
    counter+=n%10
    # לחלק בלי שארית ככה שהלולאה לא תטעה ותחשב גם אותה 
    n = n//10
    #מכניס את כל הגורם לאינט כי אינט הוא מספר בלי נקודה אחריו ככה שהלולאה לא תטעה ותחשב גם אותה
    n = int(n/10)
print(counter)