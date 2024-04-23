
# Question No 28

# Create a base class Person with attributes like name and age. Then, create subclasses Student 
# and Teacher that inherit from Person.

class Person:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

class Student(Person):

    def __init__(self, name, age, std_id, major, percentage, comments):
        super().__init__(name, age)
        self.std_id = std_id
        self.major = major
        self.percentage = percentage
        self.comments = comments
    
    def grade(self):
        if 99 >= self.percentage >= 95.99:
            self.Grade = 'Got 1st Position'
        elif 95.99 > self.percentage >= 90.99:
            self.Grade = 'Got 2nd Position'
        elif 90.99 > self.percentage >= 80:
            self.Grade = 'Got 3rd Position'
        elif 80 > self.percentage >= 75.99:
            self.Grade = 'Got A+ Grade'
        elif 75.99 > self.percentage >= 70:
            self.Grade = 'Got A Grade'
        elif 70 > self.percentage >= 60:
            self.Grade = 'Got B Grade'
        elif 60 > self.percentage >= 50:
            self.Grade = 'Got C Grade'
        elif 50 > self.percentage >= 40:
            self.Grade = 'Got D Grade'
        else:
            print('Need Hardwork!')

        return self.Grade

    def stdInfo(self):
        print(f'\nStudent ID: {self.std_id}\nName: {self.name}\nMajor: {self.major}\nPercentage: {self.percentage}\nGrade: {self.grade()}\nPerformance: {self.comments}')
        

class Teacher(Person):

    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject
    
    def teacher_info(self):
        print(f'\nTeacher ID: {self.employee_id}\nName: {self.name}\nSubject taught: {self.subject}')
    

std1 = Student('Shayan', 18, 'A102', 'Computer', 90, 'His class performance is excellent')
std1.stdInfo()

teacher1 = Teacher('Ali', 50, 'T202', 'Maths')
teacher1.teacher_info()

