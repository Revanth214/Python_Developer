def greet(): # Basic function
    return "Hello World!"
print(greet())

def greeting(name): # Returning values
    return f"Hello, {name}"
a=greeting('Rama')
print(a)

def multiply(num, factor=5): # Default agrument
    return num*factor
a=multiply(5)
print(a)
print(multiply(5, factor=10))

def discribe(name, age, city):
    return f"{name} is {age} years old and lives in {city}."
a=discribe('Rama',20,'Ayodhya')
print(a)
b=discribe(name='Krishna',city='Dwaraka',age=20) # Keyword arguments
print(b)

def summary(*k2, title='Summary'): # *args style variable arguments
    total=sum(k2)
    return f"{title}: count={len(k2)} and total={total}"
abc=summary(1,2,3,4,5,6)
print(abc)

def modify(collectioin, item):
    collectioin.append(item) # mutable functions
    return collectioin
lst=[1,5]
abc=modify(lst, 10)
print(abc)

def unmodify(x): # it doesn't modify the input
    return x**x
a=unmodify(5)
print(a)

def is_even(n):
    return n%2 == 0
def even_numbers(lst):
    return [x for x in lst if is_even(x)] # In this two functions are helping each other
a=even_numbers([1,2,3,4,5,5,6,7,8])
print(a)

def high(items, function): # Higher-order function: functions as arguments
    return [function(r) for r in items]
abd=high([1,2,3], unmodify)
print(abd)

