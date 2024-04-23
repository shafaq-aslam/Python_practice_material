
# Question No 11

# 1) Define a class called BankAccount with attributes balance and owner_name.
# 2) Include methods deposit(amount) and withdraw(amount) to modify the balance.
# 3) Create an instance of BankAccount and perform some deposit and withdrawal 
#    operations.


class BankAccount:

    def __init__(self, balance, owner_name):
        self.owner_name = owner_name
        self.balance = balance


    def deposit(self,amount):
        print("\n\nOwner Name: "+self.owner_name,"\nBalance: ",self.balance)
        self.balance = self.balance + amount
        print("\nDeposite: Rs.",amount,"has been deposited\nTotal Balance: ",self.ava_balance())

    def withdraw(self,amount):
        print("\n\nOwner Name: "+self.owner_name,"\nBalance: ",self.balance,)
        self.balance = self.balance - amount
        print("\nWithdraw: Rs.",amount,"has been withdrew\nTotal Balance: ",self.ava_balance())

    def ava_balance(self):
        return self.balance


owner_name = input('Enter your name: ')
acc1 = BankAccount(8000, owner_name)

dep_amount = int(input('\nEnter amount you want to deposit: '))
acc1.deposit(dep_amount)

withdraw_amount = int(input('\nEnter amount you want to withdraw: '))
acc1.withdraw(withdraw_amount)