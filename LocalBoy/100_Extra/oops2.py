# understanding oops

"""
class Person:
    name = None
    id = None
    age = None
    phone_num = None

    def talk(self, phone_num):
        print(f"my fone number is {phone_num} and talking with sayali.")

    def walk(self):
        print("Im walking on the streets.")

    def sleep(self, name):
        print(f"{name} is sleeping.")


obj = Person()
obj.talk(9156364230)

obj1 = Person()
obj1.walk()

obj2 = Person()
obj2.sleep("shubham")

obj3 = Person()
obj3.name = "sayali"
print(f"I love {obj3.name}")
"""

"""
class Calc:
    def sum(self, num1, num2):
        return num1 + num2

    def mult(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 // num2


obj1 = Calc()
output = obj1.sum(12, 13)
print(output)

output = obj1.mult(12, 12)
print(output)

output = obj1.divide(120, 10)
print(output)
"""

"""
class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def bark(self):
        print(f"bow bow")


obj = Dog("rock", 1001)
# obj.name = "jayems"
# print(f"The dog name is {obj.name}")

obj.bark()
"""

"""
class Employee:
    name = None
    id = None
    age = None
    salary = None

    def __init__(self, name, id, age, salary):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary

    def show(self):
        return f"Employee name is {self.name}\n Id is {self.id}\n Age of {self.age}\n Salary is {self.salary}"


obj = Employee("sarika", 1001, 45, 45000)
output = obj.show()
print(output)
"""

"""
class Person:
    name = "amit"
    age = None

    def display(self, age):
        self.age = age
        id = 1001
        print("Im Simple Method")
        print("Hi", self.age)
        print(id)


obj = Person()
obj.display(22)
"""

"""
class Car:
    name = None
    car_no = None
    fuel = None
    made_in = None

    def __init__(self, name, car_no, fuel, made_in):
        self.name = name
        self.car_no = car_no
        self.fuel = fuel
        self.made_in = made_in

    def display(self):
        print(f"The car name is : {self.name}")
        print(f"car no : {self.car_no}")
        print(f"car fuel : {self.fuel}")
        print(f"car is made in : {self.made_in}")


obj = Car("camero", "1001", "disel", "Japan")
obj.display()
"""