


class User:
    bank_name = "Boeing Employees Credit Union"
    def __init__(self):
        self.name = "Jonathan"
        self.email = "struggle@fail.com"
        self.account_balance = 100

jonathan = User()
kevin = User()
tyler = User()

kevin.name = "Kevin"
tyler.name = "Tyler"
kevin.bank_name = "BECU"
tyler.bank_name = "US Bank"


print(jonathan.name)
print(jonathan.email)
print(jonathan.account_balance)
print(kevin.name)
print(tyler.name)
print(kevin.bank_name)
print(tyler.bank_name)
print(jonathan.bank_name)

User.bank_name = "Bank of America"
print(jonathan.bank_name)


# *****Redo user assignment below for practice


class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -=amount
        return self
    
    def transfer(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount
        self.print_balance()
        user.print_balance()

    def print_balance(self):
        print(f"Current balance: {self.account_balance}")

amber = User("Amber", "test@example.com", 500)
kevin = User("Kevin", "lost@hello.com", 1000)

print(amber.email)

amber.make_deposit(700).make_deposit(900).make_withdrawal(1000).transfer(kevin, 600)

kevin.print_balance()

amber.print_balance()