from abc import ABC, abstractmethod

class Shape(ABC):# ABC = Abstract Base Classes
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    pass
s=Square()
s.area()