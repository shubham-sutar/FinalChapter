# problem 01
# 1. create a class for programmer for storing information a few programmers working on at microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


obj = Programmer("shubham", 250000, 416012)
print(obj.name, obj.salary, obj.pin)

obj1 = Programmer("ravina", 50000, 416002)
print(obj1.name, obj1.salary, obj1.pin)


