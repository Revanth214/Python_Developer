class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner=owner
        self.__balance=initial_balance
    def get_balance(self):
        print(f"[log] accessing balance for {self.owner}......")
        return self.__balance
    def set_balance(self, amount):
        if amount<0:
            raise ValueError(" Error: Balance cannot be negative")
        print(f"[Log] Updating balance for {self.owner} to ₹{amount}")

account=BankAccount("Revanth", 5000)
current_funds=account.get_balance()
print(f"{account.owner}'s balance is : ₹{current_funds}")

account.set_balance(2500)
print(f"New verified balance: ₹{account.get_balance()}\n")

try:
    account.set_balance(-500)
except ValueError as error:
    print(error)