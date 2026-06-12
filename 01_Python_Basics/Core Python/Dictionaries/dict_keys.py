my_dict=dict(apple=1,banan=5,guo=10)
for i in my_dict.keys(): # Iterate over keys
    print(i)

if 'apple' in my_dict.keys(): # Membership test
    print("apple is a key ")

key_list=list(my_dict.keys()) # Convert keys to a list
print(key_list)

keys_a = my_dict.keys() # Use with set operations
keys_b = {"apple", "orange"}
print(keys_a & keys_b)  # intersection of keys

keys = my_dict.keys() # When you want only the keys, not values
print(keys)  # dict_keys(['apple', 'banana'])