"""Write a Python program that accepts a string and calculates the number of digits and letters."""

string = input("Enter a string: ")

letters = 0
digits = 0
for i in string:
    if i.isalpha():
        letters=letters+1
    elif i.isdigit():
        digits=digits+1

print('Letters: ',letters)
print('Digits: ', digits)