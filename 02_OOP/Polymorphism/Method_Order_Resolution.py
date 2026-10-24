class A:
    def show(self):
        print("Inside Class A")
class B(A):
    def show(self):
        print("Inside Class B")
class C(A):
    def show(self):
        print("Inside Class C")
class D(B,C):
    def show(self):
        print("Inside Class D")
obj=D()
obj.show()
print(D.__mro__)