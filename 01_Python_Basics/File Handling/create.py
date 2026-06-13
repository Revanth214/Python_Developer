import os
print(os.getcwd()) # get current working directory

file=open("notes.txt", "w")
file.write("Hi, I am Revanth. It's nice to meet you.")

with open ('Personal details.txt', 'w') as file:
    file.write("Name: Revanth\n")
    file.write("Age: 20\n")
    file.write("City: Banglore")