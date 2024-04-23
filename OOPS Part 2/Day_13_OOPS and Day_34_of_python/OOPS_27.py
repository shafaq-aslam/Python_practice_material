
# Question No 27

# Create a base class Employee with attributes like name, salary, and methods like calculate_bonus().
# Then, create subclasses Manager and Engineer that inherit from Employee and have additional attributes
# like department and methods like manage_team() and write_code().


class Employee:

    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_bonus(self):
        return self.salary*(self.bonus/100)

class Manager(Employee):

    def __init__(self, name, salary, bonus, department):
        super().__init__(name, salary, bonus)
        self.department = department

    @staticmethod
    def manage_team():
        print(f"Conducting performance review of team..")

    def info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}")

class Engineer(Employee):

    def __init__(self, name, salary, bonus, project_assigned):
        super().__init__(name, salary, bonus)
        self.project_assigned = project_assigned

    def write_code(self):
        print("Writing code of assigned project..")

    def info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nAssigned Project: {self.project_assigned}")


emp1 = Manager('Arbaz', 150000, 20, 'Software')
emp1.info()
print(f"Bonus: {emp1.calculate_bonus()}")
emp1.manage_team()
