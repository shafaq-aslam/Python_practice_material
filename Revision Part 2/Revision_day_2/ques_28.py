
# 28. Write circle_calc() function that takes radius of a circle as an input from user
# and then it calculates and returns area, circumference and diameter. You should get
# these values in your main program by calling circle_calc function and then print them.

import math

def circle_calc(radius):

    area = math.pi*radius**2
    circumference = 2*math.pi*radius
    diameter = 2*radius

    return area, circumference, diameter


if __name__=="__main__":

    rad = float(input('Enter a radius: '))
    area, circumference, diameter = circle_calc(rad)
    print(f'Area of circle is: {round(area,2)}\nCircumference of circle is: {round(circumference, 2)}\nDiameter of circle is: {round(diameter, 2)}')
    
