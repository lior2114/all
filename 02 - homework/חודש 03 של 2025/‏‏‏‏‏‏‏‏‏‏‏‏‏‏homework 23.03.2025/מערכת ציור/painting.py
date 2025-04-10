import tkinter as tk
from tkinter import messagebox
class Shape:
    def __init__(self,color):
        self.color = color 

    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        print(f"Drawing a Circle with color {self.color} and radius {self.radius}")

class Square(Shape):
    def __init__(self, color,side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        print(f"Drawing a Square with color {self.color} with side length {self.side_length}")
    
class Triangle(Shape):
    def __init__(self, color, base, high):
        super().__init__(color)
        self.base = base 
        self.high = high 
        if not isinstance(self.base, int):
            self.base_root = tk.Tk()
            self.base_root.withdraw()
            self.base_root.attributes("-topmost",True)
            messagebox.showerror("invaild input", "enter only integers for base")
            self.base_root.destroy()
            raise ValueError ("int only")
        elif not isinstance(self.high, int):
            self.high_root = tk.Tk()
            self.high_root.withdraw()
            self.high_root.attributes("topmost",True)
            messagebox.showerror("invaild input", "enter integer for high")
            self.high_root.destroy()
            raise ValueError ("int only")
        else:
            pass

    def draw(self):
        print(f"Drawing a Triangle with color {self.color} with base {self.base} and high {self.high}")

    def triangle_area(self):
        return (self.base * self.high) /2