def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}")
greet("Revanth")
# Here 'Revanth' first goes to the wrapper function. Then come back  to greet(name) as a func("Revanth")
# name="Revanth"

# After decoration, the name 'greet' points to 'wrapper', so all calls and arguments reach 'wrapper' first. 
# The wrapper then decides whether and how to pass those arguments to the original function.