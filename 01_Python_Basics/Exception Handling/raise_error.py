#Next: raise
#raise :- Sometimes you want to create an error intentionally.

balance = 50000
withdraw = int(input("Enter amount: "))

if withdraw > balance :
    raise ValueError("Insufficient balance")

balance -= withdraw
print("Remaining balance: ", balance)