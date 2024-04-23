"""Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it."""

a = 0
b = 1
print(a,b,end=' ')
for i in range(2,51):
    a,b=b,a+b
    print(b, end=' ')