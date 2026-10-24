# In Java or C#, 'super' points directly to the single parent class.
# In Python, 'super()' does not point to the parent class; it points to the next class in the MRO chain
class LeftParent:
    def __init__(self):
        super().__init__()
        print("LeftParent initialized")
class Rightparent:
    def __init__(self):
        super().__init__()
        print("RightParent initialized")
class Child(LeftParent, Rightparent):
    def __init__(self):
        super().__init__()
        print("Child initialized")
c=Child()