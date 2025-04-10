class Speaker:
    def __init__ (self,manufacturer,model,color,Volume):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.Volume = Volume

    def turn_on(self):
        print("light")
    
    def turn_off(self):
        print("off")
    
    def voice(self):
        print("voice")
    
    def details (self):
        print(f"The speaker: {self.manufacturer}, and his modle is: {self.model} and his color is: {self.color}, and his volume is: {self.Volume}.")
    
    def __str__(self):
        return f"manufacturer = {self.manufacturer}, model = {self.model}, color = {self.color}, volume = {self.Volume}."
    
    def write_file(self):
        try:
            with open(f"./{self.manufacturer}.txt", "w") as file:
                file.write(f"manufacturer: {self.manufacturer}""\n")
                file.write(f"model: {self.model}""\n")
                file.write(f"color: {self.color}""\n")
                file.write(f"volume: {self.Volume}""\n")
        except Exception as err:
            print(err)

    @property
    def brand(self):
        return f"{self.manufacturer} {self.model}"
                