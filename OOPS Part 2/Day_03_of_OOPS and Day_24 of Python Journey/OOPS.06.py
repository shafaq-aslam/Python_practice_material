
# Question No 06
# 1) Define a class called 'Rectangle' with attributes 'length' and 'width'.
# 2) Create an object of the 'Rectangle' class and initialize it with 
#    values for 'length' and 'width'.
# 3) Add a method to the Rectangle class called 'calculate_area()' which 
#    returns the area of the rectangle.
# 4) Create an instance of the Rectangle class and call the 'calculate_area() '
#    method on it.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(8.5, 5.5)
area = rectangle.calculate_area()
print(f'\nLength is: {rectangle.length}\nWidth is: {rectangle.width}\n\nArea of the Rectangle is: {area}')