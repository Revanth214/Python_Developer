class Student :

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def profile(self):  # It is instance method. Because it works on an instance (object)
        print(f"{self.name} is {self.age} years old and studying at {self.school}")

a1=Student("Revanth", 20, "Haki High School")
a2=Student("Bharath", 18, "Leaf Ninja High School")

a1.profile() # a1.profile() == Student.profile(a1)
a2.profile()
 # a2.profile() == Student.profile(a2) That's why every instance method must have : self as the first parameter.

"""
What's happening?

When you write:

s1.introduce()

Python internally does:

Student.introduce(s1)

That's why every instance method must have:

self

as the first parameter.

"""