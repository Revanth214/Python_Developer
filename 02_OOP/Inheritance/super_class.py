class Vehicle:
    def drive(self):
        print("Vehicle is moving........")

class Car(Vehicle):
    def drive(self):
        super().drive() # means: "Call the parent class's work() method."
        print("BMW is my favourite")

c=Car()
c.drive()