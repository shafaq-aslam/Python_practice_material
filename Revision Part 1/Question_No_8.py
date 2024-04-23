"""Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" 
instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz"."""

for i in range(1,51):
    if i%3==0 and i%5==0:
        print('Fizz') 
        continue
    elif i%3==0:
        print('Buzz')
        continue
    elif i%5==0:
        print('FizzBuzz')
        continue
    print(i)