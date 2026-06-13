import os
print(os.path.dirname(__file__))
print(os.getcwd())

with open('employees.txt', 'w') as f:
    f.write("Rama")

with open("employees.txt", 'a') as b:
    b.write("\nShiva")

with open("employees.txt", 'a') as b:
    b.write("\nKrishna")
