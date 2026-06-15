class Student :
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


s1 = Student("Revanth", 20, 'English')
s2 = Student("Bharath", 18, "Drawing")

print(s1.name, s1.age, s1.course)
print(s2.name, s2.age, s2.course)