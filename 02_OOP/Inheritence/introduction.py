# Inheritance means:

# A child class can reuse attributes and methods from a parent class.

# The parent class method uses self for exactly the same reason as any other instance method:
# it operates on the object that calls it.

# Key Rule: If a method belongs to an object (instance method), it almost always needs:

class Animal:
    def eat(self): # Inside eat(): 'self' refers to 'd'
        print("Eating")
class Dog(Animal):
    pass

d=Dog()
d.eat()

# Even though Dog doesn't have an eat() method, it inherits it from Animal.
