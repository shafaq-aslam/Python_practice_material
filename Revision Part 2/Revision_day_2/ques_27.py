
# 27. You are given following list of stocks and their prices in last 3 days,

#       Stock	Prices
#       info	[600,630,620]
#       ril	    [1430,1490,1567]
#       mtl	    [234,180,160]

# Write a program that asks user for operation. Value of operations could be,
# a. print: When user enters print it should print following,
#       info ==> [600, 630, 620] ==> avg:  616.67
#       ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#       mtl ==> [234, 180, 160] ==> avg:  191.33
# b. add: When user enters 'add', it asks for stock ticker and price. If stock already 
#    exist in your list (like info, ril etc) then it will append the price to the list. 
#    Otherwise it will create new entry in your dictionary. For example entering 'tata' 
#    and 560 will add tata ==> [560] to the dictionary of stocks.

stocks = {
    
    'info' : [600, 630, 620],
    'ril' : [1430, 1490, 1567],
    'mtl' : [234, 180, 160]
}

def Print():

    for i in stocks.keys():
        num_lst = stocks[i]
        sum = 0
        for j in num_lst:
            sum += j
        print(f'{i} ==> {stocks[i]} ==> avg: {round(sum/len(num_lst),2)}')


def add():

    stock_ticker = input('Enter stock ticker you want to add: ')
    price = int(input('Enter the price: '))

    if stock_ticker in stocks:
        stocks[stock_ticker].append(price)
    else:
        stocks[stock_ticker] = [price]
    Print()

y_n = 'y'
while y_n == 'y':

    choice = input('Enter (print/add): ')
    if choice == 'print':
        Print()
    elif choice == 'add':
        add()
    else:
        print('Invalid input')
    y_n = input('Want to start again: ')
