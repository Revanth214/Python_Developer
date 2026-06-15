# In Python, everything is an object, including strings, lists, integers, functions, and even classes.
# Output:

# <class 'str'>
# <class 'list'>

# str and list are classes, and the values created from them are objects.

def freedom():
    return "Liberation"
print(freedom)  # freedom is different from freedom(). freedom is an object and freedom() is a function call

# Store a function in variable

def free():
    return "Joy Boy"
l=free # function free is stored in 'l' variable
print(l()) # here l()==free()

# Here, I call the function by using variable name 'l'. Because we stored free in 'l'.