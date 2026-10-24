class Device:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price
class Smartphone(Device):
    def __init__(self, brand, price, storage):
        super().__init__(brand, price)
        self.storage=storage

phone=Smartphone("Samsung",9999999,"256GB")
print(phone.brand)
print(phone.storage)