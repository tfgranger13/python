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

    def __str__(self):
        return str(self.int_rate)

    @classmethod
    def bank_account_info(cls):
            print(cls)


account1 = BankAccount(0.0325, 28000)
account2 = BankAccount(0.025, 34000)

account1.deposit(400).deposit(7000).deposit(1234).withdraw(4000).yield_interest().display_account_info()
account2.deposit(100).deposit(900).withdraw(300).withdraw(125).yield_interest().display_account_info()

account1.bank_account_info()