import json

data = """
    {
        "student": {
        "Name":"Revanth",
        "Sibling":"Bharath"
    }
    }"""

info = json.loads(data)
print(info["student"]["Name"])