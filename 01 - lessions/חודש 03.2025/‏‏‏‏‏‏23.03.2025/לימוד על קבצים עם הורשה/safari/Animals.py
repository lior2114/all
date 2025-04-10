class Animal: 
    def __init__(self, name):
        self.name = name 

    def display (self):
        print(f"animal name: {self.name}")

    def __str__(self):
        return f"name:{self.name}"
        
    def make_sound(self):
        print(f"animal {self.name} has make sound")
    
class Lion(Animal):
    def __init__(self, name, eating):
        super().__init__(name)
        self.eating = eating

    def make_sound(self):
        print("Roar! i am a Lion")
    
    def __str__(self):
        return super().__str__() + f", eating: {self.eating}"
        

class Elephant(Animal):
    def __init__(self, name,eating, tusk):
        super().__init__(name)
        self.eating = eating
        self.tusk = tusk 

    def make_sound(self):
        print("Trumpet! I am an Elephant")
    
    def __str__(self):
        return super().__str__() + f", eating: {self.eating}, tusk: {self.tusk}"
        

class Monkey(Animal):
    def __init__(self, name, eating , num_banana):
        super().__init__(name)
        self.eating = eating
        self.num_banana = num_banana
    
    def make_sound(self):
        print("Ooh ooh aah aah! I am a Monkey")

    def __str__(self):
        return super().__str__() + f", eating: {self.eating}, number: {self.num_banana}"

    def power(self):
        return self.num_banana*6

        