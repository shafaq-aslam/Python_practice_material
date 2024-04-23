
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
        self.transaction = []

    def record_transactions(self):
        print(f'\nTransaction Record\nTime: {self.date}\nAmount: {self.amount}')

    def total_balance(self):
        total_balance = 0
        total_balance += self.amount
        print(f'Total Balance: {total_balance}')

    def report(self):
        print(self.description)


rec1 = Transaction(datetime.datetime.now().strftime("%d/%m/%Y : %H:%M:%S"), 50200, 'Amount has been credit to your account')
rec1.record_transactions()
rec1.total_balance()
rec1.report()

rec2 = Transaction(datetime.datetime.now().strftime("%d/%m/%Y : %H:%M:%S"), 600, 'Amount has been dabited to your account')
rec2.record_transactions()
rec2.total_balance()
rec2.report()