import os
class Flashlight():
    counter = 0
    def __init__(self, name ,color , length, light_power, batterys):
        self.name = name
        self.color = color
        self.length = length
        self.light_power = light_power
        self.batterys = batterys
        Flashlight.counter+=1

    def display(self): #פונקציית הצגה
        print(f"name:{self.name} ,color:{self.color}, length:{self.__length}, light power: {self.__light_power}, batterys:{self.batterys}")

    def __str__(self): #פונקצית הקסם 
        return f"name:{self.name}, color:{self.color}, length:{self.__length}, light power: {self.__light_power}, batterys:{self.batterys}"

    def light_up(self):
        print(f"flashlight: {self.name} is up!")

    def light_off(self):
        print(f"flashlight: {self.name} is off!")

    def switch_battery(self):
       if self.batterys > 0:
            self.batterys -=1
            print(f"Battery of {self.name} is switched. Remaining batteries: {self.batterys}")
       else:
            print(f"No batteries left for {self.name} Flashlight. Please buy more.")

    @property
    def light_power(self):
        return self.__light_power
    @light_power.setter
    def light_power(self,value):
        if value <= 0:
            raise ValueError ("must be bigger then Zero")
        else:
            self.__light_power = value

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self,value):
        if value <= 0:
            raise ValueError ("must be biggher then Zero")
        else:
            self.__length = value

    @staticmethod
    def show_counter():
        print(f"there is {Flashlight.counter} Flashlights")

    def create_file(self):
        path_name = self.name
        if not os.path.exists(path_name):
            os.makedirs(path_name)
        with open (f"./{path_name}/{self.color}.txt" , "w") as txt_file:
            txt_file.write(self.__str__())
    