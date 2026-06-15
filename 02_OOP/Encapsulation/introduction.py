# What is Encapsulation?

# Encapsulation means:

# Bundling data and methods together and controlling access to the data.

# In simple terms:

# We don't want users of our class to directly modify everything.

# Problem without Encapsulation

class Bank:
    def __init__(self, balance):
        self.balance=balance
account=Bank(1000000)
account.balance=-1000000
print(account.balance)

# This is dangerous.

# A bank account should never have a negative balance because someone directly changed the attribute.

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

# The single underscore means:

# "This attribute is intended for internal use."

# It's a convention, not strict protection.

# Private attributes

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount(100000)
account.get_balance()