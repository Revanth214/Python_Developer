import os
print(os.path.dirname(__file__))

with open('student.txt', 'w') as file:
    file.write("Name: Revanth kumar\n")
    file.write("Age: 20\n")
    file.write("City: Banglore")

with open('student.txt', 'a') as file:
    file.write("\nSkill: Python Developer")