
# Question No 22

# Create a class Shape with a method area() and perimeter(). Then, create subclasses like Rectangle, 
# Circle, and Triangle, each implementing their own version of the area() and perimeter() methods.

import math

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
     
     def __init__(self,height, width, length):
         self.height = height
         self.width = width
         self.length = length
     
     def area(self):
         return self.height * self.width 
     
     def perimeter(self):
         return 2*(self.length+self.width)
         


class Triangle(Shape):

    def __init__(self, height, base, side1, side2, side3):
        self.height = height
        self.base = base
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return (1/2)*(self.base*self.height)
        
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
         

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius*self.radius
        
    def perimeter(self):
         return 2*math.pi*self.radius
        
    

circle = Circle(5)
triangle = Triangle(5,6,5,4,4)
rectangle = Rectangle(5,9,3)

print(f'\nArea of Circle: {circle.area()}\nPerimeter of Circle is: {circle.perimeter()}')
print(f'\nArea of Triangle: {triangle.area()}\nPerimeter of Triangle is: {triangle.perimeter()}')
print(f'\nArea of Rectangle: {rectangle.area()}\nPerimeter of Rectangle is: {rectangle.perimeter()}\n')