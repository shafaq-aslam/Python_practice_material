""" Create pattern
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
"""
for i in range(6):
    for j in range(i+1):
        print('*',end=' ')
    print('\n')
for i in range(6-1,0,-1):
    for j in range(i+1):
        print('*',end=' ')
    print('\n')