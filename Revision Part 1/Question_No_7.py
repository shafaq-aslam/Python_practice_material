"""Write a program to print a table
- Ask from user to enter a number you want to print a table
- Ask from user to enter starting value
- Ask from user to enter ending value"""

table = int(input("Enter any number you want to print a table: "))
startingNum = int(input("Enter starting value: "))
endingNum = int(input("Enter ending value: "))

for i in range(startingNum,endingNum+1):
    print(table, "X" , i , "=" , table*i )