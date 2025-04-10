import os
try:
    x = int(input("enter number 1: "))
    y = int(input("enter number 2: "))
    soulution = x+y
    dir_name = "solutions" # שם של התקייה שאנחנו רוצים ליצור
    if not os.path.exists(dir_name): #תנאי אם היא קיימת או לא
        os.makedirs(dir_name) # אם לא היא פותחת תיקיה חדשה בשם הזה 
#                ותוכה אנחנו מכניסים קובץ טקסט בשם שבחרנו 
    with open(f"./exe1/{dir_name}/plus2.txt", 'w') as file:
        file.write(f"{x} + {y} = {soulution}")
        
except Exception as err:
    print(err)
