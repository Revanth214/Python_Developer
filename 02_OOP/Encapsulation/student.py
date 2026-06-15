class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def show_details(self):
        print(f"Name: {self.name}")
    def get_marks(self):
        return self.__marks
    
st=Student("Krishna", 100)
st.show_details()
print(st.get_marks())
print(st.__dict__)
print(st.__marks)
