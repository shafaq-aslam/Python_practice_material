""" Q1: Write a program to create area calculator 
        a) To find the area of circle
        b) To find the area of triangle
        c) To find the area of rectangle
        d) To find the area of square"""


print('\nWelcome to Area Calculator\n')
userInput = input('For area of Circle (C/c)\nFor area of Triangle (T/t)\nFor area of Rectangle (R/r)\nFor area of Square (S/s)\n\nChoose any one from them: ')

if userInput == 'C'.lower():
    pi = 3.14159
    radius = float(input('Enter the radius: '))
    print('Area of Circle is: ',pi*radius)
elif userInput == 'T'.lower():
    base = float(input('Enter the base: '))
    height = float(input('Enter the height: '))
    print('Area of Trianle is: ',(base*height)/2)
elif userInput == 'R'.lower():
    length = float(input('Enter the length: '))
    width = float(input('Enter the width: '))
    print('Area of Rectangle is: ',(length*width))
elif userInput == 'S'.lower():
    sides = float(input('Enter the side: '))
    print('Area of Square is: ',sides**2)
else:
    print('Invalid enter.....')
