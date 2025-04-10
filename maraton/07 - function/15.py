import random
print("=======A========")
def draw(width, height):
    print("*" * width)
    for i in range(height-2):#המינוס שתיים זה כי יש לנו שורה בהתחלה ושורה בסוף שהם לא קשורות ללולאה ורק מדפיסות את האורך עצמו עם כל הכוכביות 
        #      לא לשכוח שכפל קודם לפלוס אז זה יעשה כוכבית בהתחלה ואז רווחים באורך של אותו אורך ואז בסוף כוכבית
        print("*" + " " * (width-2) + "*") # כדי שלא יזוז ממש לפינה כי הורדנו שתי טורים אז צריך להוריד גם שתי שורות שיהיה סימטרי
    print("*" * width)

print("=======B========")
draw(10,4)

print("=======C========")
n1 = random.randint(2,10)
n2 = random.randint(2,10)
draw(n1,n2)

print("=======D========")
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))
draw(width, height)