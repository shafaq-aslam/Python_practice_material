
# Question No 26

# Design a hierarchy of geometric shapes. Start with a base class Shape with methods for calculating area and perimeter. 
# Then, create subclasses like Rectangle, Circle, and Triangle. Implement these subclasses with appropriate methods and attributes.
# Finally, create more specific shapes like Square, Ellipse, EquilateralTriangle, etc., inheriting from the appropriate classes.

import math

class Shape:

    def calculating_area(self):
        pass

    def calculating_parimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self,height, width, length):
         self.height = height
         self.width = width
         self.length = length
     
    def calculating_area(self):
         return self.height * self.width 
     
    def calculating_parimeter(self):
         return 2*(self.length+self.width)
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def calculating_area(self):
        return math.pi*self.radius*self.radius
        
    def calculating_circumference(self):
         return 2*math.pi*self.radius
    
class Triangle(Shape):

    def __init__(self, height, base, side1, side2, side3):
        self.height = height
        self.base = base
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculating_area(self):
        return (1/2)*(self.base*self.height)
        
    
    def calculating_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
class Square(Rectangle):

    def __init__(self, side):
        self.side = side

    def calculating_area(self):
        return self.side**2
    
    def calculating_parimeter(self):
        return 4*self.side

class Ellipse(Circle):

    def __init__(self, a, b):
        self.x_axis = a
        self.y_axis = b

    def calculating_area(self):
        return math.pi * self.x_axis*self.y_axis
    
    def calculating_circumference(self):
        return 2 * math.pi * (math.sqrt(((self.x_axis**2)+(self.y_axis**2))/2))
    
class EquilateralTriangle(Triangle):

    def __init__(self, side):
         self.side = side

    def calculating_area(self):
        return (math.sqrt(3)/4) * self.side**2
    
    def calculating_parimeter(self):
        return 3 * self.side

rectangle = Rectangle(5,6,5)
triangle = Triangle(6,8,6,6,3)
circle = Circle(6)
equTriangle = EquilateralTriangle(6)
ellipse = Ellipse(6,6)
square = Square(5)

print(f"\nRectange\nArea: {rectangle.calculating_area()}\nPerimeter: {rectangle.calculating_parimeter()}")
print(f"\nTriangle\nArea: {triangle.calculating_area()}\nPerimeter: {triangle.calculating_parimeter()}")
print(f"\nCircle\nArea: {circle.calculating_area()}\nCircumference: {circle.calculating_circumference()}")
print(f"\nEquilateral Triangle\nArea: {equTriangle.calculating_area()}\nPerimeter: {equTriangle.calculating_parimeter()}")
print(f"\nEllipse\nArea: {ellipse.calculating_area()}\nCircumference: {ellipse.calculating_circumference()}")
print(f"\nSquare\nArea: {square.calculating_area()}\nCircumference: {square.calculating_parimeter()}")

