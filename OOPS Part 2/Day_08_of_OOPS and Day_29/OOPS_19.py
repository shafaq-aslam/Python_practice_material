
# Question No 19

# 1) Define a class called Transaction with attributes date, amount, and description.
# 2) Include methods to record transactions, calculate the total balance, and generate a summary report.
# 3) Test the methods by recording multiple transactions.

import datetime

class Transaction:

    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

    
class Account:
    
    def __init__(self):
        self.transactions = []

    def transactions_record(self, transaction):
        self.transactions.append(transaction)

    def calculate_balance(self):
        total_balance = 0
        for transaction in self.transactions:
            total_balance += transaction.amount
        return total_balance
    
    def transaction_summary(self):
        print('\nSummary Report')
        for transaction in self.transactions:
            print(f'\nTransaction Date: {transaction.date}\nAmount: {transaction.amount}\nDescription: {transaction.description}')
        print(f'\nTotal Balance: {self.calculate_balance()}')


trans1 = Transaction(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), 50000, 'Salary')
trans2 = Transaction(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), -10000, 'Donation')
trans3 = Transaction(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), -5000, 'Shopping')
trans4 = Transaction(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"), -2000, 'Fast food')

record = Account()
record.transactions_record(trans1)
record.transactions_record(trans2)
record.transactions_record(trans3)
record.transactions_record(trans4)

record.transaction_summary()