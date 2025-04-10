
# אופציה ב עם שורת קוד אחת יותר 
counter = 0

while True: 
    num = int (input("enter a number: "))
    counter +=1
    if num < 0:
        counter -= 1  #כדי שלא יוסיף גם את המספר השלילי 
        break 
    
print (f"the total of the numbers is: {counter}")
   