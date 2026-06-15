# What is an Iterator?

# An iterator is an object that remembers:

# Where it currently is
# What the next value should be

# Creating an Iterator


numbers = [10, 20, 30]

it = iter(numbers)

print(it)
print(next(it)) # we have to use next() if we want vlaue

# iter(): converts an iterable into an iterator.