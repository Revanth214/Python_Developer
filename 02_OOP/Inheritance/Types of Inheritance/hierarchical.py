class PaymentProcessor:
    def __init__(self, amount):
        self.amount=amount
    def generate_receipt(self):
        return f"Receipt generated for ₹{self.amount}"

class StripProcessor(PaymentProcessor):
    def process_payment(self):
        return f"Processing card via Strip API for ₹{self.amount}"
class PayPalProcessor(PaymentProcessor):
    def process_payment(self):
        return f"Redirected to PayPal login portal for ₹{self.amount}"

payment_a=StripProcessor(50)
payment_b=PayPalProcessor(100)
print(payment_a.process_payment())
print(payment_b.process_payment())
print(payment_a.generate_receipt())