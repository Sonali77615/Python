class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)

# Create an object
acc = BankAccount("Rahul", 5000)

# Deposit money and display balance
acc.deposit(2000)
acc.display()