
# Question No 21

# Define a class called Vehicle with attributes like make, model, and methods like start() 
# and stop(). Then, create subclasses like Car, Motorcycle, and Truck, each with specific 
# attributes and methods. Ensure that each subclass inherits from the Vehicle class.

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f'{self.brand} {self.model} is starting....')

    def stop(self):
        print(f'{self.brand} {self.model} is stopped.')


class Car(Vehicle):

    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def info(self):
        print(f'The car of {self.brand}, model {self.model}, has color {self.color}')

class Motorcycle(Vehicle):

    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.price = price

    def info(self):
        print(f'The Motocycle of {self.brand}, model {self.model}, has price {self.price}')

class Truck(Vehicle):

    def __init__(self, brand, model, payload):
        super().__init__(brand, model)
        self.payload = payload

    def info(self):
        print(f'The Truck of {self.brand}, model {self.model}, has {self.payload} Ton Payload capacity')


car = Car('Toyota', 'Camry', 'Gray')
motorcycle = Motorcycle('Honda', 'CBR500R', 252000)
truck = Truck('Ford', 'F-150', 2.5)

car.info()
motorcycle.info()
truck.info()

car.start()
motorcycle.stop()