from extra_practice.bank_account import BankAccount

class User(BankAccount):
    
    # other methods
    def make_deposit(self, amount):
        self.balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore

