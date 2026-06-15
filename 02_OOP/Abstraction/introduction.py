# What is Abstraction?

# Abstraction means:

# Show what an object does, hide how it does it.

# Example:

# When you drive a car:

# Start Engine
# Accelerate
# Brake

# You don't need to know:

# Fuel Injection
# Spark Timing
# Engine Compression

# Those details are hidden.

# Why Use Abstraction?

# It forces child classes to implement required methods.
from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    ...

class UPI(Payment):
    ...