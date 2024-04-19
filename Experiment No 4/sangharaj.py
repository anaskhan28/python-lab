import math
class Rectangle:
    def __init__(self):
        self.length = 5
        self.width = 4
    def area(self):
        return self.length * self.width
class Circle:
    def __init__(self):
        self.radius = 3
    def area(self):
        return math.pi * (self.radius ** 2)
class Triangle:
    def __init__(self):
        self.base = 6
        self.height = 7
    def area(self):
        return 0.5 * self.base * self.height
class Square(Rectangle):
    def __init__(self):
        super().__init__()
class Shape(Square, Circle, Triangle):
    def __init__(self, side, radius, base, height):
        Square.__init__(self, side)
        Circle.__init__(self, radius)
        Triangle.__init__(self, base, height)
shape = input("Enter the shape (rectangle, circle, triangle, square): ")
if shape == "rectangle":
    rectangle = Rectangle()
    print("Area of Rectangle: ", rectangle.area())
elif shape == "circle":
    circle = Circle()
    print("Area of Circle: ", circle.area())
elif shape == "triangle":
    triangle = Triangle()
    print("Area of Triangle: ", triangle.area())
elif shape == "square":
    square = Square()
    print("Area of Square: ", square.area())
else:
    print("Invalid shape")