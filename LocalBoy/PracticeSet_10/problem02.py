# problem 02
# 2. Write a class "Calculator" capable of finding square, cube and square root of a number.

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


obj = Calculator(25)
# obj.square()
# obj.cube()
obj.sqrt()
