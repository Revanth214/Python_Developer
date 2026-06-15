def numbers():
    for i in range(1,6):
        yield i

a=numbers()
print(next(a))
print(next(a))

# Real Benifit : Where there is a billion numbers
# Memory usage stays tiny because only one number exists at a time.