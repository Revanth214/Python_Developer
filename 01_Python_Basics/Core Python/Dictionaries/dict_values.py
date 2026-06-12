my_dict = {"apple": 1, "banana": 2} # Iterate over values
for value in my_dict.values():
    print(value)

value_list = list(my_dict.values()) # Convert values to a list
print(value_list)  # [1, 2]

total = sum(my_dict.values()) # Use with sum()
print(total)  # 3

if 2 in my_dict.values(): # Check if a value exists
    print("value exists")


person = {"name": "Leo", "age": 25}
for value in person.values():
    print(value)