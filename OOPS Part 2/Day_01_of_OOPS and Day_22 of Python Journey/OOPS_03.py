
# Question No 03
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mult(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

calc = Calculator(num1, num2)

print(calc.add())
print(calc.sub())
print(calc.mult())
print(calc.div())