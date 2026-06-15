# What is a Generator?

def numeric():
    return 10

abc=numeric()
print(abc)
# A generator is a special function that uses: 'yield' instead of 'return'

# After return, the function ends completely.

# After yield, the function pauses instead of ending.

def numbers():
    yield 10
    yield 20
    yield 30

a=numbers()
print(next(a))
print(next(a)
      )
print(next(a))

# Why Not Use a List?
# List: Everything is stored in memory immediately.
# Generator: Values are produced only when requested.