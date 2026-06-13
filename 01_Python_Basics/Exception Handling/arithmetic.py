try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a/b)

except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("Can't divide by Zero")

else:
    print("Division completedwithout error")  # Runs only if no exception occurs

finally:
    print("Program finished") # Runs whether an exception occurs or not
