import json

student = {"Name": "Krishna", "Age": 20, "City": "Ayodhya"}
with open("student.json", "w") as file :
    json.dump(student, file, indent=4)