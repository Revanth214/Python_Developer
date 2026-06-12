# Python functions primer
# Run this file and experiment by editing the examples.

# 1. Basic function definition and call

def greet(name):
    """Say hello to someone."""
    print(f"Hello, {name}!")

# Call the function
#greet("Shiva")

# 2. Function with a return value

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

# result = add(2, 3)
#print(result)

# 3. Default arguments

def multiply(value, factor=2):
    """Multiply value by factor; factor defaults to 2."""
    return value * factor

# print(multiply(5))
# print(multiply(5, factor=4))

# 4. Keyword arguments

def describe_person(name, age, city):
    """Describe a person with named arguments."""
    return f"{name} is {age} years old and lives in {city}."

# print(describe_person(name="Jeff", city="Boston", age=34))

# 5. Variable-length arguments

def summarize(*values, title="Summary"):
    """Summarize an arbitrary number of values."""
    total = sum(values)
    return f"{title}: count={len(values)}, total={total}"

# print(summarize(1, 2, 3, 4, title="Numbers"))

# 6. Function that modifies lists (mutable objects)

def append_item(collection, item):
    """Append an item to a list and return the updated list."""
    collection.append(item)
    return collection

# items = [1, 2]
# print(append_item(items, 3))
# print(items)

# 7. Function that does not modify input (immutable objects)

def square(x):
    """Return the square of x without modifying x."""
    return x * x

# print(square(6))

# 8. Helper function example

def is_even(n):
    return n % 2 == 0


def even_numbers(items):
    """Return only the even numbers from a list."""
    return [x for x in items if is_even(x)]

# print(even_numbers([1, 2, 3, 4, 5, 6]))

# 9. Higher-order function: functions as arguments

def apply_operation(values, operation):
    """Apply a function to each value in a list."""
    return [operation(v) for v in values]

# print(apply_operation([1, 2, 3], square))

# 10. Docstrings and inspection

def explain_function():
    """Print the docstring of the add function."""
    print(add.__doc__)

# explain_function()

if __name__ == "__main__":
    # Quick interactive demo: uncomment the calls you want to test.
    greet("Alice")
    print(add(2, 3))
    print(multiply(5))
    print(multiply(5, factor=4))
    print(describe_person(name="Jeff", city="Boston", age=34))
    print(summarize(1, 2, 3, 4, title="Numbers"))
    items = [1, 2]
    print(append_item(items, 3))
    print(items)
    print(square(6))
    print(even_numbers([1, 2, 3, 4, 5, 6]))
    print(apply_operation([1, 2, 3], square))
    explain_function()
