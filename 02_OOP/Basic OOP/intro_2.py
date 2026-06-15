#One Limitation : Suppose you want 100 mobiles.

class Mobile:
    pass

m1 = Mobile()
m1.brand = "Samsung"
m1.price = 120000

m2 = Mobile()
m2.brand = "Apple"
m2.price = 150000

m3 = Mobile()
m3.brand = "OnePlus"
m3.price = 50000

#This becomes repetitive.
#Python provides a special method called a constructor.