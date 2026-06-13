import os
print(os.getcwd())
try:
    with open("Notes App. txt", "w") as file:
        file.write(input("Enter data into Notes App : "))

    with open("Notes App. txt", "r") as file:
        info=file.read()
    print(info)

    with open("Rama.txt", "r") as file:
        data=file.read()

except FileNotFoundError as e:
    print(e)
