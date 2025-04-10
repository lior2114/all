
# אופציה ב עם שורת קוד אחת יותר 
counter = 0

while True: 
    num = int (input("enter a number: "))
    
    if num < 0:
        counter += num
        break 
    
print (f"the stop number is: {counter}")
   