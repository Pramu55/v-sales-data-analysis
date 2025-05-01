class A:
    _z=20
    def__init__(self,x)
        self._x = x
class B(A):
    def__init__(self,y):
        self._y = y
    def__add__(self,other):
        x = self._y + other._x
        return B(x)
    def__str__(self):
        return f"{self._y},{self._z}"
obj1 = A(7)
obj2 = B(5)
print(obj2 + obj1)