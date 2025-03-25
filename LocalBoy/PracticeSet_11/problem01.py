# problem 01
# 1. Create a class (2D vector) and use it to create another class representing a 3D vector.

class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")


class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k  ")


obj1 = TwoDvector(1, 2)
obj1.show()

obj2 = ThreeDvector(1, 2, 3)
obj2.show()
