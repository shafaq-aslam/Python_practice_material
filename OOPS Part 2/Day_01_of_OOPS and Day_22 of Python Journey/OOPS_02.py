
# Question No 02
# Write a  Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        area = math.pi*self.radius*self.radius
        print(f'Area of the circle is: {area}')

    def perimeter_of_circle(self):
        peri = 2*math.pi*self.radius
        print(f'The Perimeter of Circle is: {peri}')

radius = float(input('Enter the value of radius: '))

circle = Circle(radius)
area = circle.area_of_circle()
perimeter = circle.perimeter_of_circle()