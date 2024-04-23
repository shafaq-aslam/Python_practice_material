
# Question No 08
# Write a Python program to create a person class. Include attributes  
# like name, country and date of birth. Implement a method to  determine 
# the person’s age. 

from datetime import datetime

class Person:

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth


    def age_calculator(self):
        dob = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        current_date = datetime.now()
        age = current_date.year - dob.year
        return age

name = input('\nEnter your name: ')
countryName = input('Enter your country name: ')
birthDate = input('Enter your date of birth (YYYY-MM-DD): ')

person1 = Person(name, countryName, birthDate)
print(f'Name: {person1.name}\nCountry: {person1.country}\nDate of Birth: {person1.date_of_birth}')
print(f'Age: {person1.age_calculator()}')