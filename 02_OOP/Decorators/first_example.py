def greet():
    print("Hello")

def decorator(fun):

    def wrapper():
        print("Before")
        fun()
        print("After")
    return wrapper  # It is equal to wrapper() but we need to remove abc() from code
abc=decorator(greet)
abc()