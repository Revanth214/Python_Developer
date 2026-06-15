class Mobile :

    def __init__(self, brand, price) :
        self.brand = brand
        self.price = price

# Create objects:

m1 = Mobile("Samsung", 120000)
m2 = Mobile("Apple", 100000)

# Access attributes:

print(m1.brand)
print(m2.brand)
print(m1.price)
print(m2.price)