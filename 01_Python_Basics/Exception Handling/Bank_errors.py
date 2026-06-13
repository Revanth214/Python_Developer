try:
    balance = 50000
    withdraw = int(input("Enter amount: "))

    if withdraw > balance :
        raise ValueError("Insufficient balance")
    
except ValueError as e:
    print("Error: ", e)
    
else:
    balance -= withdraw
    print("Remaining balance: ", balance)