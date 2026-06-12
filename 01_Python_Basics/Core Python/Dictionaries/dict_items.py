my_dict=dict(apple=1, banan=5, leo=1) # Iterate over keys and values together
for i, j in my_dict.items():
    print(i, j)

# Convert to a list

pairs = list(my_dict.items())
print(pairs)  # [('apple', 1), ('banana', 2)]

# Loop and unpack
for fruit, count in my_dict.items():
    print(f"{fruit} -> {count}")

# Use in dictionary comparisions
if ("apple", 1) in my_dict.items():
    print("apple has value 1")