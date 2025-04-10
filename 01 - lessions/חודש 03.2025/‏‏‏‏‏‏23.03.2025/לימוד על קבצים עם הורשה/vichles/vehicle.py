class Vehicle:
    def __init__(self, brand):
        self.brand = brand 
    
    def move (self):
        print(f"The vehicle {self.brand} is moving")
    
class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors

    def move(self):
        print("The car drives on the road.")

class Bicycle(Vehicle):
    def __init__(self, brand, has_basket):
        super().__init__(brand)
        self.has_basket = has_basket
    
    def move(self):
        print("The bicycle is pedaling on the path")
    
    def hasbasket(self):
        if self.has_basket == True:
            print("yes has basket")
        else:
            print("no")

class Airplane(Vehicle): 
    def __init__(self, brand, engine_count):
        super().__init__(brand)
        self.engine_count = engine_count
    
    def move(self):
        print("The airplane flies in the sky")