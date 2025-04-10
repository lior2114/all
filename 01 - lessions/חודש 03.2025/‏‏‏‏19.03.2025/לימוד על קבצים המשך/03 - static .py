class Car:
    #constructor - בנאי
    def __init__(self, model, color, price):
        self.model = model  # Calls the @model.setter
        self.color = color
        self.price = price  # Calls the @price.setter 
        
    @property 
    def model(self):
        return self.__model
    
    @model.setter
    def model(self,value):
        models = ['subaru', 'BMW', 'kia']
        if value not in models:
            raise ValueError ("wrong car model")
        self.__model = value


    #phase - function    
    def display(self):
        print(f"{self.color} {self.model} {self.__price}")

    #magic = פונקצית הקסם
    def __str__(self):
        return f"color:{self.color}, model:{self.model}, price:{self.__price}"

    #phase 3 - getter
    @property
    def price(self):
        return self.__price #  מחזיר את הערך של המחיר לתוך ערך מוגן

    
    #phase 4 - setter 
    # קורא לפונקציה של פרייס מהפרופירטי
    @price.setter 
    def price(self, value):  # מקבלת ערך חדש עבור המאפיין 'price'
        if value <= 0:  # בודקת אם הערך החדש קטן או שווה ל-0
            raise ValueError("price has to be positive")  # אם כן, מעלה חריגה מסוג ValueError עם הודעה מתאימה
        else:  # אחרת
            self.__price = value  # מעדכנת את הערך של המשתנה הפרטי __price

while True:          
    try:           
        price = int(input("enter car price bigger then 0: ")) 
        car1 = Car('subaru', 'brown', price)
        break

    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
print(car1)