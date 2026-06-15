# The important thing to realize is:

# Generators are not faster because they avoid loops.

# They are useful because they avoid storing everything at once.

def numbers():               
    for i in range(1, 6):    
        yield i

for num in numbers():
    print(num)

"""
python does: 

Generate 1 → Print 1
Generate 2 → Print 2
Generate 3 → Print 3
Generate 4 → Print 4
Generate 5 → Print 5

"""

# You don't call next() manually.

# The for loop calls next() behind the scenes.