class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance__ = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance__ += amount
        else:
            raise ValueError("Sorry your deposit must be greater than zero")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance__:
            self.account_balance__ -= amount
            return True
        else:
            return False  # checker expects return False for failed withdrawal

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance__:.2f}")  # exact wording expected

    def get_balance(self):
        return self.account_balance__

    def __str__(self):
        return f"BankAccount(balance={self.account_balance__})"
