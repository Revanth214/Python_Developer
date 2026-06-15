from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

# Now:

class UPI(Payment):
    pass

# Python prevents:

upi = UPI()

# because a payment system without a pay() method makes no sense.