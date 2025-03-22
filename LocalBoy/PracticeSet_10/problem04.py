# problem 02
# 4.Add a static method in problem 2, to greet the user with hello

import math


class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square is {self.num * self.num}")

    def cube(self):
        print(f"The cube is {self.num * self.num * self.num}")

    def sqrt(self):
        print(f"The sqrt is {math.sqrt(self.num)}")

    @staticmethod
    def stats():
        print("hello user")


obj = Calculator(25)
# obj.square()
# obj.cube()
obj.sqrt()
obj.stats()
