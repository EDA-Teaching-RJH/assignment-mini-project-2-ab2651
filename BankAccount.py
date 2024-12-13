class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        return self.balance
    
    def deposit_money(self, amount):
        if amount <= 0:
            raise ValueError
    
    def withdraw_money(self, amount):
        if amount <= 0:
            print("Amount must be greater then 0.")
            raise ValueError
        if amount > self.balance:
            print("Insufficient funds in the account.")
            raise ValueError


    


