class Transaction:
    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

class Account:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, transaction):
        self.transactions.append(transaction)

    def calculate_total_balance(self):
        total_balance = 0
        for transaction in self.transactions:
            total_balance += transaction.amount
        return total_balance

    def generate_summary_report(self):
        summary = "Transaction Summary:\n"
        for transaction in self.transactions:
            summary += f"Date: {transaction.date}, Amount: {transaction.amount}, Description: {transaction.description}\n"
        summary += f"Total Balance: {self.calculate_total_balance()}\n"
        return summary

# Testing the methods
if __name__ == "__main__":
    # Create an instance of Account
    account = Account()

    # Record multiple transactions
    transaction1 = Transaction("2024-04-01", 1000, "Salary")
    transaction2 = Transaction("2024-04-05", -200, "Groceries")
    transaction3 = Transaction("2024-04-08", -50, "Dinner")
    transaction4 = Transaction("2024-04-10", -300, "Shopping")

    account.record_transaction(transaction1)
    account.record_transaction(transaction2)
    account.record_transaction(transaction3)
    account.record_transaction(transaction4)

    # Generate and print summary report
    print(account.generate_summary_report())
