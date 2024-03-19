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
shape = input("Enter the shape (rectangle, circle, triangle, square): ")
if shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    print("Area of Rectangle:", rectangle.area())
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print("Area of Circle:", circle.area())
elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    triangle = Triangle(base, height)
    print("Area of Triangle:", triangle.area())
elif shape == "square":
    side = float(input("Enter the side length of the square: "))
    square = Square(side)
    print("Area of Square:", square.area())
else:
    print("Invalid shape")
