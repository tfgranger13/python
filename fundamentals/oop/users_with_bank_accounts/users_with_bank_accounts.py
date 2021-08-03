class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount >=0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Your current balance is: ${self.balance}")

    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self

class User:
    # declaring class attribute
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self
    
    def transfer_money(self, amount, transfer_user):
        self.make_withdrawal(amount)
        transfer_user.make_deposit(amount)
        return self

user1 = User("Bob", 'bob@codingdojo.com')

user1.make_deposit(500).make_deposit(7000).make_deposit(23).make_withdrawal(4000).display_user_balance()