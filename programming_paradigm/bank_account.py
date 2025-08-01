# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit must be greater than zero")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True  # ✅ Important for main.py to check
        else:
            return False  # Return False if withdrawal fails

    def get_balance(self):
        return self._balance

    def display_balance(self):
        print(f"Current balance: ${self._balance}")

    def __str__(self):
        return f"BankAccount(balance={self._balance})"
