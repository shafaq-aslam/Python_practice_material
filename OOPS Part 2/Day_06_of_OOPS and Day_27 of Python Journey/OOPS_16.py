
# Question No 16

# 1) Define a class called Point with attributes x and y.
# 2) Include a method distance(other_point) that calculates the distance between two points.
# 3) Create two instances of Point and calculate the distance between them.
import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2+(self.y - other_point.y)**2)
        print(f'\nThe distance between Two points are: {distance}\n')

dis1 = Point(5,8)
dis2 = Point(10,3)
dis1.distance(dis2)