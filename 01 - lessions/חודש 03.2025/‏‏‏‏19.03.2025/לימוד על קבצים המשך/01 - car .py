class Car:
    #constructor - בנאי
    def __init__(self, color,model , price):
        self.color =color
        self.model = model
        self.price = price # go to setter call @price.setter 
        
    #phase - function    
    def display(self):
        print(f"{self.color} {self.model} {self.__price}")

    #magic = פונקצית הקסם
    def __str__(self):
        return f"color:{self.color}, model:{self.model}, price:{self.__price}"

    #phase 3 - getter
    @property
    def price(self):
        return self.__price
    """
    Getter for the price attribute.
    מחזיר את הערך של המחיר
    """
    
    #phase 4 - setter
     # קורא לפונקציה של פרייס מהפרופירטי
    @price.setter  # זהו דקורטור שמגדיר את המתודה כ-setter עבור המאפיין 'price'
    def price(self, value):  # מקבלת ערך חדש עבור המאפיין 'price'
        if value <= 0:  # בודקת אם הערך החדש קטן או שווה ל-0
            raise ValueError("price has to be positive")  # אם כן, מעלה חריגה מסוג ValueError עם הודעה מתאימה
        else:  # אחרת
            self.__price = value  # מעדכנת את הערך של המשתנה הפרטי __price

while True:          
    try:           
        price = int(input("enter car price bigger then 0: ")) 
        car1 = Car('subaru','brown',price)
        break

    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
print(car1)