# What is self?

# Many beginners find self confusing.

# Think of it as : "the current object"

class Mobile:

    def __init__(self, brand):
        self.brand = brand

# When:

m1 = Mobile("Samsung")

# Python internally does something similar to:

Mobile.__init__(m1, "Samsung")

# So:

# 'self' refers to : m1

print(m1.brand)