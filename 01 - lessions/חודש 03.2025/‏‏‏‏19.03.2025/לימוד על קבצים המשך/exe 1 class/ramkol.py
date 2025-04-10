import os
class Speaker:
    #constructor - בנאי
    counter = 0 
    def __init__(self, manufactor, model , color , volume):
        self.manufactor = manufactor
        self.model = model
        self.color =color
        self.volume = volume
        Speaker.counter +=1
    #phase - function    
    def display(self):
        print(f"{self.manufactor} {self.model} {self.color} {self.__volume}")


    def __str__(self):
        return f" manufactor:{self.manufactor}, model:{self.model}, color:{self.color}, volume:{self.__volume}"


    def volume_up(self):
        print(f"The speaker {self.manufactor} {self.model} is on")

    def volume_down(self):
        print(f"The speaker {self.manufactor} {self.model} is off")

    def sound(self):
        print(f"The sound is coming from {self.manufactor} {self.model}")
    

    @property
    def brand(self):
        return f"manufactor:{self.manufactor}, model:{self.model}"
    

    #phase 3 - getter
    @property
    def volume(self):
        return self.__volume
    
    #phase 4 -setter 
    @volume.setter
    def volume (self,value):
        if value <=0:
            raise ValueError ("enter right value")
        else:
            self.__volume = value

    @staticmethod #מחוץ לפונקציות וכל פעם שמפעילים את הקלאסס הוא מעלה את עצמו ב 1 
    def show_counter():
        print(Speaker.counter)
        
    #יצירת קובץ
    def create_file(self):
        path_name = self.manufactor
        if not os.path.exists(path_name):
            os.makedirs(path_name)
        with open(f"./{path_name}/{self.model}.txt", 'w') as file:
            file.write(f"{self.__str__()}")
