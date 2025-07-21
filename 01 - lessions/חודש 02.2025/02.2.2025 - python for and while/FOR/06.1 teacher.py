sum =0  
for i in range(10): 
    number = int(input("enter a number: "))
    if number > 0:#הוסף כדי לא לתת תוצאה למספר שלילי 
        print(f"the number briboh is {number**2}") #אפשר גם לעשות ^2 בשביל חזקת 2 
    if number < 0:
        break
