
#Question No 04

#Create Account class wich 2 attributes - balance and account no.
#Create methods for debit, credit and printing the balance.

class Account:

    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance = self.balance - amount
        print(f"Rs.{amount} has been debited from your account")
        print(f"Your total balance is: Rs.{self.ava_balance()}")

    def credit(self, amount):
        self.balance = self.balance + amount
        print(f"Rs.{amount} has been credit to your account")
        print(f"Your total balance is: Rs.{self.ava_balance()}")

    def ava_balance(self):
       return self.balance
    

account1 = Account(50000, "ABC000124586536900")
account1.debit(20000)
account1.credit(2300)