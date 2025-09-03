import math
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y
    def describe(self):
        print(f"Rectange {self.x} by {self.y} has area {self.area}")
class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * (self.y / 2)
    def describe(self):
        print(f"Triangle {self.x} wide by {self.y} tall has area {self.area}")
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = (self.radius**2) * math.pi
    def describe(self):
        print(f"Circle {self.radius} has area {self.area}")
