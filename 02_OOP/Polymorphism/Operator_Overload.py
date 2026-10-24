# Polymorphism doesn't just apply to named methods; it applies to operators like +,-, ==
# But we must use special methods such as __add__(self, other), __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __eq__, __ne__

class ShoppingCart:
    def __init__(self, items_dict):
        self.items_dict=items_dict
    def __add__(self, other):
        if not isinstance(other, ShoppingCart):
            raise TypeError("You can only add another ShoppingCart object!")
        new_items=self.items_dict.copy()
        for item, quantity in other.items_dict.items():
            new_items[item]=new_items.get(item,0)+quantity
        return ShoppingCart(new_items)
    def __str__(self):
        return f"Cart Items: {self.items_dict}"

cart1=ShoppingCart({"apples":2, "banana":3})
cart2=ShoppingCart({"apples":1, "milk":2})
combined_cart=cart1+cart2
print(combined_cart)