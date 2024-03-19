import math
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
class Shape(Square, Circle, Triangle):
    def __init__(self, side, radius, base, height):
        Square.__init__(self, side)
        Circle.__init__(self, radius)
        Triangle.__init__(self, base, height)
shape = Shape(4, 5, 6, 7)
print("Area of Square: ", shape.Square.area())
print("Area of Circle: ", shape.Circle.area())
print("Area of Triangle: ", shape.Triangle.area())