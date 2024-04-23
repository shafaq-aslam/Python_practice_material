
# 25. Write a function called print_pattern that takes integer number as an 
# argument and prints following pattern if input number is 3, 

# *
# **
# ***

# if input is 4 then it should print

# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. Default value for n is 5. So if function caller doesn't
# supply the input number then it will assume it to be 5

def print_pattern(number=5):
     for i in range(1, number + 1):
         print('*' * i)

num = input('Enter a number: ')
if num != '':
     num = int(num)
else:
     num = 5

print_pattern(num)