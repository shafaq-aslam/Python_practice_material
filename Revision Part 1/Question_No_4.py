"""Write a Python program to find those numbers which are divisible by 7 and 
multiples of 5, between 1500 and 2700 (both included)."""

for i in range(1500,2700+1):
    if i%7==0 and i%5==0:
        print(i, end='  ')

