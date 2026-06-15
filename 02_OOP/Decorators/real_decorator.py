def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper

@decorator  # this whole function equal to greet = decorator(greet)
def greet():
    print("Hello")

greet()