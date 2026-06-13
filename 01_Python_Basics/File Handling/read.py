with open('employees.txt', 'r') as file:
    content=file.read() # Method 1: Read entire file

print(content)

with open("employees.txt", "r") as file:
    data=file.readline() # Method 2: Read one line and goes to new line. Actually it prints 'Rama\n'.
print(data)

with open("employees.txt", "r") as file:
    data=file.readlines() # Method 3: Read Lines as a List
print(data)