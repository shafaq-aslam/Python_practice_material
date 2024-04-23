
# 23. Write a function called calculate_area that takes base and height as an input and
# returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def calculate_area(base, height):
    area = (1/2)*base*height
    return area

base = float(input('Enter a value of base: '))
height = float(input('Enter a value of height: '))

# print(f'Area of Triangle is: {calculate_area(base, height)}')

# 24. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". 
# Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape


def calculate_area(val1, val2, shape="triangle"):

    # for triangle: val1 will be base and val2 will be height
    # for rectangle: val1 will be length and val2 will be width 

    if shape == 'triangle':
        print("Area of Triangle is: ",(1/2) * val1 * val2)
    elif shape == 'rectangle':
        print("Area of Rectangle is: ",val1 * val2)
    else:
        print(f'Sorry, {shape} shape is not my program. Defaulting to triangle.')
        print("Area of Triangle is: ",(1/2) * val1 * val2)

val1 = float(input('Enter the value of base or length: '))
val2 = float(input('Enter the value of height or width: '))
shape = input('Enter the shape (triangle/rectangle): ')

calculate_area(val1, val2, shape)
    