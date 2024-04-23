
# 30. Write a program that takes two numbers as input from the user and divides the first number
# by the second number. Handle the ZeroDivisionError exception if the user tries to divide by zero.

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

try:
    result = num1/num2
    print(result)
except ZeroDivisionError as error:
    print('Error occured: ',error)

# 31. Write a program that opens a file specified by the user, reads its contents, and prints them.
# Handle the FileNotFoundError exception if the specified file does not exist.

file_name = input('Enter a file name with extension you want to read: ')
try:
    with open(file_name, 'r') as file_reader:
        print(file_reader.read())
except FileNotFoundError as error:
    print('Error occured: ',error)

# 32. Write a program that takes user input and tries to convert it into an integer.
# Handle the ValueError exception if the input cannot be converted into an integer.

Input = input('Enter a number: ')
try:
    print('Before Conversion: ',type(Input), Input)
    Input = int(Input)
    print('After Conversion: ',type(Input), Input)
except ValueError as error:
    print('Value Error occured: ', error)

# 33. Write a program that asks the user to input a list of numbers and then prompts for an index
# to print the corresponding element from the list. Handle the IndexError exception if the user enters
# an index that is out of range.

num_list = list(input('Enter a list of numbers: '))
index_num = int(input('Enter index number: '))

try:
    num = num_list[index_num]
    print(f'Number at Index {index_num} is: {num}')
except IndexError as error:
    print('Index Error oocured: ', error)

# 34. Write a program that defines a dictionary and prompts the user to input a key. Handle the KeyError 
# exception if the entered key is not present in the dictionary.

dictionary = {
    'One' : 1,
    'Two' : 2,
    'Three' : 3,
    'Four' : 4,
    'Five' : 5
}

key = input('Enter a key: ')
try:
    val = dictionary[key]
    print(val)
except KeyError as error:
    print('Key Error occured: ',error," is not a key")

# 35. Write a program that defines a custom exception class called CustomError. Use this custom exception
# to handle a specific condition in your code, such as if a user tries to withdraw more money from 
# their account than their balance.

class CustomError(Exception):
    pass

balance = 15000
withdraw = int(input('Enter amount you want to withdraw: '))

try:
    if withdraw > balance:
        raise CustomError('Insufficient balance')
    balance-=withdraw
    print('Remaining balance is: ',balance)

except CustomError as error:
    print(error)
