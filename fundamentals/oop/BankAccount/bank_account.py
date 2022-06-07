class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Account Balance: {self.balance}")

    def yield_interest(self):
        if self.balance > 0.00:
            self.balance = self.balance * (self.int_rate / 100) + self.balance
            return self

    def print_all(cls):
        print(cls)

checking = BankAccount(2, 300)

checking.deposit(200).deposit(400).deposit(1000).withdraw(100).yield_interest().display_account_info()

savings = BankAccount(5, 700)

savings.deposit(1000).deposit(4231).withdraw(200).withdraw(450).withdraw(220).withdraw(400).yield_interest().display_account_info()
