count = 0 
num = int(input("enter a number"))
if num == 0:
    count = 1 
while num != 0:
    #מכניס לקאונט כל פעם את המספר האחרון במספר שהוכנס עד שהוא ניהיה שווה ל 0 ואז התוכנית מפסיקה
    count+=num%10 #אפשר לעשות +=1 כדי להדפיס בסוף כמה מספרים יש במספר עצמו לדוגמא 123 יש בו 3 מספרים 
    #מחלק את המספר ב 10 כדי להוריד ממנו כל הזמן שלא יתקע על אותו מספר ואז יהיה לולאה שלא נגמרת 
    num = int(num / 10)  #  653 //10 = 65 
print(f"num of digits is {count}")

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
print(f"the sum of the digits is: {counter}")