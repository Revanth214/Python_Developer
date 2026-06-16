# What is JSON?

# JSON stands for:

# JavaScript Object Notation

# It's simply a text format for storing and exchanging data.

# You'll use it in:

# Django REST Framework
# APIs
# Frontend ↔ Backend communication
# AI APIs
# Configuration files

import json

my_dict={
    "Name": "Revanth",
    "Age": 20,
    "Place": "Andhra"
}

json_data=json.dumps(my_dict) # Converting dictionary to JSON string
print(json_data) # Now output is a string

# Converting JSON string into python dictioinary

json_string='{"Name": "Rama", "Age": 20, "City": "Ayodhya"}'

student=json.loads(json_string) # Here JSON string converts into python dictionary
print(student) 