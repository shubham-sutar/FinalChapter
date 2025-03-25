# Operator Overloading

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


n = Number(15)
m = Number(25)

print(n + m)
