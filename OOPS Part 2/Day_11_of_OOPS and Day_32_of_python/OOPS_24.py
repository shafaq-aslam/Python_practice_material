
# Question No 24

# Define a class Device with attributes like brand, model, and methods 
# like turn_on() and turn_off(). Then, create subclasses like Smartphone, 
# Laptop, and Tablet, each with their own specific attributes and methods.

class Device:

    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    def trun_on(self):
        print(f'{self.brand} {self.model} is trunig on...')

    def turn_off(self):
        print(f'{self.brand} {self.model} is trunig off...')

class Smartphone(Device):

    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.price = price

    def camera(self):
        print(f'{self.brand} {self.model} has high pixel camera')

    def info(self):
        print(f'\n{self.brand} {self.model} Price: Rs.{self.price}')

class Laptop(Device):

    def __init__(self, brand, model, generation):
        super().__init__(brand, model)
        self.generation = generation

    def info(self):
        print(f'\n{self.brand} {self.model} has {self.generation} generation')

class Tablet(Device):

    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def info(self):
        print(f'{self.brand} {self.model} has {self.color} color')


smartphone = Smartphone('Realme', '9i', 38000)
laptop = Laptop('Hp', 'Envy Series', 8)
tablet = Tablet('Apple', 'iPad Pro', 'silver')

smartphone.info()
smartphone.camera()
laptop.info()
laptop.trun_on()
tablet.info()
tablet.turn_off()

    