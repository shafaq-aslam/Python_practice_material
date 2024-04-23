
# Question No 18

# 1) Define a class called Shape with methods to calculate the area and perimeter 
#    of different shapes (circle, rectangle, triangle).
# 2) Include methods to display information about each shape.
# 3) Test the methods with instances of different shapes.

import math

class Shape:

    def circle(self, radius):
        self.area_of_circle= math.pi*radius*radius
        self.perimeter_of_circle = 2*math.pi*radius
        print(f'\nArea of Circle is: {self.area_of_circle}\nCircumference of Circle is: {self.perimeter_of_circle}')


    def triangle(self, base, height, side):
        self.area_of_triangle = (1/2)*base*height
        self.perimeter_of_triangle = 3*side
        print(f'\nArea of Triangle is: {self.area_of_triangle}\nPerimeter of Triangle is: {self.perimeter_of_triangle}')
        

    def rectangle(self, length, width):
        self.area_of_rectangle = length*width
        self.perimeter_of_rectangle = 2*(length + width)
        print(f'\nArea of Rectangle is: {self.area_of_rectangle}\nPerimeter of Rectangle is: {self.perimeter_of_rectangle}')

shapes = Shape()
shapes.circle(9)
shapes.rectangle(6,8)
shapes.triangle(5,6,8)