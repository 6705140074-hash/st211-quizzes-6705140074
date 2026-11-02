class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient function")
        self.balance = amount 
        return self.balance