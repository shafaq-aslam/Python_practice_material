
# Question No 09

# 1) Define a class called Person with attributes name, age, and gender.
# 2) Include a method greet() that prints a greeting message using the person's name.
# 3) Create an instance of Person and call the greet() method.

class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f'\nGood Morning {self.name} Have a good day ahead')

name = input('\nEnter your name: ')
age = int(input('Enter your age: '))
gender = input('Enter your gender: ')

person1 = Person(name, age, gender)
person1.greet()