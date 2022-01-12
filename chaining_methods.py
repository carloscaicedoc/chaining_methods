class User:
    # class attributes - defined in the class
    bank_name = "First National Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0 
    # deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    # withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    # display user balance method
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def tranfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


santana = User("Carlos Santana", "santan@python.com")
jacob = User("Jacob Collier", "jacob@python.com")
bowie = User("David Bowie", "d.bowie@python.com")

santana.make_deposit(4000).make_deposit(2300).make_deposit(3700).display_user_balance().tranfer_money(bowie, 2350).display_user_balance()

jacob.make_deposit(15000).make_deposit(2000).make_withdrawal(500).make_withdrawal(1200).display_user_balance()

bowie.make_deposit(18000).make_withdrawal(2500).make_withdrawal(350).display_user_balance()