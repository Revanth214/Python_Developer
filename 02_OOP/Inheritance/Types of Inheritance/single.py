class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def get_display_info(self):
        return f"{self.name} - ₹{self.price}"

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size=size

shirt=Clothing("Vintage leather Jacket", 120, "L")
print(shirt.get_display_info())