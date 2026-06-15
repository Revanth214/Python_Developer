# Polymorphism: One interface, many forms.

class Bird:
    def move (self):
        print("Flying")

class Fish:
    def move (self):
        print("Swimming")

obj=[Bird(), Fish()]
for i in obj:
    i.move()

a=Fish()
a.move()
a=Bird()
a.move()