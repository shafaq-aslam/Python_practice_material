
# 37. Create a base class Animal with methods speak() and move(). Then, create subclasses Dog, 
# and Cat inheriting from Animal. Override the speak() method in each subclass to make
# each animal produce its characteristic sound.

class Animal:

    def __init__(self, pet_name):
        self.pname = pet_name

    def speak(self):
        print(f'{self.pname} speaks')

    def move(self):
        print(f'{self.pname} moves')

class Dog(Animal):
    
    def __init__(self, pet_name, food):
        super().__init__(pet_name)
        self.food = food

    def eat(self):
        print(f'{self.pname} eat {self.food}')

    def speak(self):
        print(f'{self.pname} sounds woof woof!')

class Cat(Animal):

    def __init__(self, pet_name, toy):
        super().__init__(pet_name)
        self.toy = toy

    def play(self):
        print(f'{self.pname} love to play with {self.toy}')

    def speak(self):
        print(f'{self.pname} sounds meow meow!')
    
    
dog = Dog('Tomy', 'Biscuits')
dog.eat()
dog.speak()

print()

cat = Cat('Mano', 'Rubber Ball')
cat.play()
cat.speak()

