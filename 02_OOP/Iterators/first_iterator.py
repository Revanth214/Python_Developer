num=[100, 200, 300]

abc=iter(num)
print(next(abc))
print(next(abc))
print(next(abc))

# It can't start from beginning

# How to Start Again?

# Create a new iterator:

numbers = [100, 200, 300]

it = iter(numbers)

print(next(it))
print(next(it))

it = iter(numbers)   # new iterator

print(next(it))  # use for loop for iterators in the upcoming future