
# Question No 10

# 1) Define a class called Student with attributes name, age, and grade.
# 2) Include a method display_info() that prints out the student's information.
# 3) Create multiple instances of Student with different information and display their info.

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f'\nName is: {self.name}\nAge is: {self.age}\nGrade is: {self.grade}')


name1 = input('\nEnter your name here: ')
age1 = int(input('Enter your age here: '))
grade1 = input('Enter your grade here: ')

std1 = Student(name1, age1, grade1)
std1.display_info()

name2 = input('\nEnter your name here: ')
age2 = int(input('Enter your age here: '))
grade2 = input('Enter your grade here: ')

std2 = Student(name2, age2, grade2)
std2.display_info()