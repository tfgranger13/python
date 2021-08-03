# declare a class and give it a user
class User:
    # declaring class attribute
    bank_name = "First National Dojo"
    def __init__(self, name, email_address, account_balance):
        self.name = name
        self.email = email_address
        # the account balance is set to 0
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
    def transfer_money(self, amount, transfer_user):
        self.make_withdrawal(amount)
        transfer_user.make_deposit(amount)

user1 = User("Harold", 'harold@codingdojo.com', 40000)
user2 = User('Harriet', 'harriet@codingdojo.com', 99000)
user3 = User("Maude", 'maude@codingdojo.com', 23)

user1.make_deposit(500)
user1.make_deposit(7000)
user1.make_deposit(23)
user1.make_withdrawal(4000)
user1.display_user_balance()

user2.make_deposit(500000)
user2.make_deposit(3000)
user2.make_withdrawal(32)
user2.make_withdrawal(4000)
user2.display_user_balance()

user3.make_deposit(4800000000)
user3.make_withdrawal(500000)
user3.make_withdrawal(2500000)
user3.display_user_balance()

user1.transfer_money(500, user3)
user1.display_user_balance()
user3.display_user_balance()