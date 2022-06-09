class BankAccount:
    all_instances = []
    #anytime a bank account is created, it creates an object 
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        #Anytime an object is made, its added to all_instance list
        BankAccount.all_instances.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Current balance is: {self.balance}")
        if self.balance < 0:
            print("go get a job dude...")
    
    def yield_interest(self, percentage):
        self.balance = self.balance * (percentage/100) + self.balance

    @classmethod
    def print_all_instances(cls):
        for account in cls.all_instances:
            print(account.balance)

checking = BankAccount(2, 5000)
savings = BankAccount(2, 100000)

checking.deposit(500).deposit(600).deposit(2000).withdraw(6000).display_account_info()

BankAccount.print_all_instances()