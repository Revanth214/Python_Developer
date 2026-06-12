import greeting

result = greeting.add(5, 7)
print(result)

print(greeting.greet("Sam"))

""""
--That style is called modular programming in Python.

-> 'greeting.py' is a module
-> 'main.py' imports it with 'import functions'
-> the code is split into reusable pieces
*You can also call it:

1. using modules
2. importing modules
3. code reuse
4.  separation of concerns
It's the normal Python way to organize code across multiple files."""