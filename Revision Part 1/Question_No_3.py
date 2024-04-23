"""write a program to find the sum of first 10 odd numbers using while loop"""

sum = 0
i = 1
oddNum = 1
while i<=10:
    print(oddNum)
    sum=sum+oddNum
    oddNum=oddNum+2
    i=i+1
    
print('The sum of first 10 ODD numbers are: ',sum)


    