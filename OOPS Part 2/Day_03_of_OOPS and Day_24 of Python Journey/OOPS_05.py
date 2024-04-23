
# Question No 05

# 1) Define a class called 'Car' with attributes such as 'manufacturer', 
#    'model', and 'year'.
# 2) Create an object of the 'Car' class and initialize it with values for 
#    'manufacturer', 'model', and 'year'.
# 3) Add a method to the 'Car' class called start() which prints "The car 
#    is starting".
# 4) Create an instance of the Car class and call the start() method on it.

class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f'\nCar brand: {self.brand}\nCar Model: {self.model}\nCar Introduction Year: {self.year}')
        print("\nThe car is starting....")

my_car1 = Car('Tokyo', 'Camry', 1982)
my_car1.start()

my_car2 = Car('Tesla', 'Roadster', 2008)
my_car2.start()