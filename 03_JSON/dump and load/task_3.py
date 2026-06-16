import json

data = '{"name":"Rama","marks":[90,95,100]}'

student = json.loads(data)

print(student["marks"][1])