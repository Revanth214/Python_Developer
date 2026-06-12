# dict.update(other) adds key/value pairs from another dictionary or iterable of pairs
# Existing keys are overwritten, new keys are added.

my_dict = {"apple": 1, "banana": 2}
print("before update:", my_dict)

# update from another dict
my_dict.update({"banana": 5, "orange": 3})
print("after update:", my_dict)

# update from an iterable of key/value pairs
my_dict.update([("pear", 4), ("apple", 9)])
print("final dict:", my_dict)

my_dict["apple"] = 5 # For single key
print("Final: ",my_dict)

# adding one key
my_dict["Mango"]=25
print("After last adding key: ", my_dict)