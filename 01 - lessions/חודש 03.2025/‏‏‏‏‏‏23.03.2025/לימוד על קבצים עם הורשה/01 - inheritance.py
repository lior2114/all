class Product: 
    counter = 0
    def __init__ (self,name, description,price):
        self.name = name
        self.description = description
        self.price = price
        Product.counter +=1

    def display(self):
        print(f"name{self.name}, description:{self.description}, price:{self.price}")

    def __str__(self):
        return f"name{self.name}, description:{self.description}, price:{self.price}"
    
    @staticmethod
    def show_counter():
        print(Product.counter)

    #super() - יורש מהאבא שלו שזה מה שמעליו 
class Food (Product):
    def __init__(self, name, description, price, taste):
        super().__init__(name, description, price) #להעביר את הפרטמרים שהוא מכיל 
        self.taste = taste #מוסיפים משתנה חדש 

    def __str__(self):
        return super().__str__() +f", taste:{self.taste}" #super לוקח אותה מהפונקציה של האבא שלה 
                                                           # ולהגדיר בנפרד את מחלקת הבן שזה ה taste     

    def display(self):                                                     
        print("***")

    def f(self):#סתם שם רנדומלי שקראנו לפונקציה 
        super().display() #קורא לפונקצית האב
        self.display()# קורא לפונקצית הבן 
        print(self.name) #אין כאן בקלאסס אז עובר לקלאסס שמעליו 

f1 = Food("Pizza", "Cheesy and delicious", 12, "Savory")
print(f1)
f1.f()
f1.show_counter()