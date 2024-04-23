
# Question No 14

# 1) Define a class called Employee with attributes name, position, and salary.
# 2) Include a method promote(new_position, new_salary) that updates the employee's position and salary.
# 3) Create an instance of Employee, promote them, and print their new position and salary.


class Employee:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def promote(self, new_position, new_salary):
        print(f"Employee Name: {self.name}\nEmployee's Position: {self.position}\nEmployee's Salary: {self.salary}")
        self.position = new_position
        self.salary = new_salary
        print(f"\nEmployee's New Position: {self.position}\nEmployee's Updated Salary: {self.salary}")


emp1 = Employee('Shayan', 'Junior Front end developer', 35000)
emp1.promote('Senior Front end developer', 50000)
