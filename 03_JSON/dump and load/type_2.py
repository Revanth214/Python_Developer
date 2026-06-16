import json

with open("Student.json", "r") as file:
    data=json.load(file)

print(data)
print(type(data))