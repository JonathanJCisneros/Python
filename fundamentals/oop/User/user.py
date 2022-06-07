class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def print_account_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Balance is:", self.account_balance)
        if self.account_balance < 0:
            print("go get a job...")
        return self

    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            print("Warning: Insufficient Funds!")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        if self.account_balance < 0:
            print("go get a job...")

jonathan = User("Jonathan", "example@gmail.com", 1000)

# jonathan.print_account_info()
# jonathan.make_deposit(300)
# jonathan.make_deposit(500)
# jonathan.make_deposit(500)
# jonathan.display_user_balance()

jonathan.make_deposit(300).make_deposit(500).make_deposit(500).display_user_balance()



kevin = User("Kevin", "whocares@yahoo.com", 1500)

# kevin.print_account_info()
# kevin.make_deposit(500)
# kevin.make_deposit(300)
# kevin.make_withdrawal(700)
# kevin.make_withdrawal(300)
# kevin.display_user_balance()

kevin.make_deposit(500).make_deposit(300).make_withdrawal(700).make_withdrawal(300).display_user_balance()

sarah = User("Sarah", "imbroke@poverty.com", 200)

# sarah.make_deposit(600)
# sarah.make_withdrawal(400)
# sarah.make_withdrawal(100)
# sarah.make_withdrawal(600)
# sarah.print_account_info()

sarah.make_deposit(600).make_withdrawal(400).make_withdrawal(100).make_withdrawal(600).display_user_balance()
