
# 36 a. Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name
# object initializes id and name dynamically for every Employee object created.

# emp = Employee(1, "coder")

# class Employee():

#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         print(f'Employee ID: {self.id}\nEmployee Name: {self.name}')


# emp1 = Employee(101, 'Shayan')
# emp2 = Employee(102, 'Shafaq')

# b. Use del property to first delete id attribute and then the entire object.

class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        print(f'Employee ID: {self.id}\nEmployee Name: {self.name}')

emp1 = Employee(101, 'Shayan')

del emp1.id

# try:
#     print(emp1.id)
# except AttributeError as error:
#     print(error)

# del emp1

# try:
#     print(emp1)
# except NameError as error:
#     print(error)