
# Question No 23

# Create a class Animal with methods like speak() and move(). 
# Then, create subclasses like Dog, Cat, and Bird, each with 
# their own implementations of speak() and move().

class Animal:

    def speak(self):
        pass

    def move(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Dog speaks Bhoo! Bhoo!")

    def move(self):
        print("Dog moves by feet")

class Cat(Animal):

    def speak(self):
        print("Cat speaks Meow! Meow!")

    def move(self):
        print("Cat moves by feet")

class Bird(Animal):

    def speak(self):
        print("Crow Bird speaks crow crow")

    def move(self):
        print("Bird fly")

cat = Cat()
dog = Dog()
bird = Bird()

cat.speak()
cat.move()

dog.speak()
dog.move()

bird.speak()
bird.move()