
# Question No 25

# Create a hierarchy of animals using multiple inheritance. Define a base class Animal 
# with common attributes like name, age, and species. Then, create subclasses like Mammal, 
# Bird, and Fish. Finally, create specific animals like Dog, Cat, Eagle, Parrot, Goldfish, 
# etc., inheriting from appropriate classes.

class Animal:

    def __init__(self, name, age, species):
        self.name = name 
        self.age = age
        self.species = species

class Bird(Animal):

    def __init__(self, name, age, species, food):
        super().__init__(name, age, species)
        self.food = food
    
    def eat(self):
        print(f"I'm {self.name} and I eat {self.food}")

class Mammal(Animal):
    
    def __init__(self, name, age, species, food, voice):
        super().__init__(name, age, species)
        self.voice = voice
        self.food = food

    def speak(self):
        print(f"I speak {self.voice}")

    def eat(self):
        print(f"I eat {self.food}")

class Fish(Animal):
    
    def live(self):
        print(f"I live in under water")

class Dog(Mammal):

    def guard(self):
        print(f"I'm a {self.name}.\nI'm German Shepherd, belong to the {self.species} species.\nI protect my owners from thief and robbers.I am {self.age} years old.")

class Cat(Mammal):

    def pet(self):
        print(f"I'm a {self.name},\nI belong to the {self.species} species.\nI live in a big house with my owners they love me soo much.I am {self.age} years old.")

class Eagle(Bird):

    def sharp_eyesight(self):
        print(f"I'm a {self.name}.\nI belong to the {self.species} species.\nI have sharpe eyesight, my prey doesn't escape from me")

class Parrot(Bird):

    def mimic(self):
        print(f"Hi I'm {self.name}.\nI belong to the {self.species} speices.\nI can mimic a human.\nI am {self.age} years old.")

class Goldfish(Fish):

    def pet(self):
        print(f"I'm {self.name}.\nI am a goldfish, belong to the {self.species} species.\nHuman keep me as a pet in aquarium")


dog = Dog('Max', 8, 'Canis lupus familiaris', 'Meat and Fish', 'Bhao Bhao!')
dog.guard()
dog.eat()
print('\n')
cat = Cat('Whiskers', 2, 'Felis catus', 'Tuna', 'Meow Meow!')
cat.pet()
cat.speak()
print('\n')
fish = Goldfish('Bubbles', 2, 'Carassius auratus')
fish.pet()
fish.live()
print('\n')
