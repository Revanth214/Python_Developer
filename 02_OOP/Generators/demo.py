def demo():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3

g=demo()
print(next(g))
print(next(g))