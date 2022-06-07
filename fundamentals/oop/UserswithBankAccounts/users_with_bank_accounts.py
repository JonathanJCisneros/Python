class User:
    def __init__(self):
        self.name = "Jonathan Cisneros"
        self.email = "jonathan.james.cisneros@outlook.com"
        self.account = BankAccount(int_rate=0.02, balance=1000)	# added this line

    def make_deposit(self,amount):
        self.account.deposit(amount)
        print(self.account.balance)

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(self.account.display_account_info())


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

jonathan = User()

jonathan.make_deposit(100)
jonathan.display_user_balance()
