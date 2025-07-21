first_name = "John"
last_name = "Doe"
email = "jhon@gmail.com"
phone = "1234567890"

customers = [
    {"first_name": first_name, "last_name": last_name, "email": email, "phone": phone},
    {"first_name": "Jane", "last_name": "Doe", "email": "jhon2222@gmail.com", "phone": "1234567890"},
 ]
print(customers[1]["email"]) #jhon2222@gmail.com זה אומר שהוא מדפיס את האימייל של הלקוח השני כי המספר הוא 1 והרשימה מתחילה מאינדקס 0

for customer in customers:
    print(customer["first_name"]) #John and Jane הוא מדפיס את כולם כי הוא רץ על כל הרשימה וכל מה שיש ברשימה ויש לו את הקי (שם) של הפירסט ניימ הוא ידפיס אותו 