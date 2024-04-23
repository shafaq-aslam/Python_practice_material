
# Question No 01:
#Craete student class that takes name and marks of 3 subjects as arguments in constructor. 
#Then create a method to print the average.

class Students:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = (self.marks[0] + self.marks[1] + self.marks[2])/3
        print(f"{self.name} Your average score is: {avg}")

name = input('Enter your name: ')
marks = []

for i in range(1,4):
    mark = float(input(f'Enter marks {i}: '))
    marks.append(mark)

std1 = Students(name, marks)
std1.average()