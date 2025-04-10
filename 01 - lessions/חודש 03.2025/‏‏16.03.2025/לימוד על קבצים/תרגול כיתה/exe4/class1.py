class Lighter:
    def __init__ (self, color , length, light_power, battery_counter):
        self.color = color
        self.length = length
        self.light_power = light_power
        self.battery_counter = battery_counter

    def power_up(self):
        print("power up")

    def power_down(self):
        print("power off")

    def switch_battery(self):
        print(f"switch battery")
    
    def details(self):
        print(f"color is:{self.color}, length is:{self.length}, power of light is:{self.light_power}, battery counter is:{self.battery_counter}")
    
    def __str__(self):
        return f"color = {self.color}, length = {self.length}, light power = {self.light_power}, battery counter = {self.battery_counter}"
    
    def write_file(self):
        try:
            with open (f"./{self.color}.txt", 'w') as file: 
                file.write (f"color: {self.color}" "\n")
                file.write (f"length: {self.length}" "\n")
                file.write (f"light_power: {self.light_power}" "\n")
                file.write (f"battery_counter: {self.battery_counter}" "\n")
        except Exception as err:
            print(err)