# oops.
# object-oriented programming
# Object ?
# Procedural PL --> Functions
# Student --> Attributes, behaviour
"""
class Person:
    name = None
    id = None
    age = None
    phone_number = None

    def talk(self):
        print("I can talk")

    def another(self):
        print("Im Method")

    def sleep(self, name):
        print("Im a Method")
        print("sleep", name)

    def walk(self):
        print("I am Walking")


surya = Person()
surya.name = "Surya Prakash"
surya.talk()
surya.sleep("surya")

sayali = Person()
sayali.name = "Sayali Sutar"
sayali.walk()


# Constructor
"""
class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Constructor ?
    # Use to initialize the values
    # of the instance variables (Attributes)

    def bark(self):
        print("Bhow Bhow")


dog1 = Dog()
dog1.name = "jaymes"
print(dog1.name)
"""
# dog2 = Dog()

# obj = Dog()
# obj.bark()
"""

"""
class Employee:
    name = None  # instance variable
    id = None  # instance variable
    pin = None  # instance variable

    # Constructor
    def __init__(self, name, id, pin):
        self.name = name
        self.id = id
        self.pin = pin

    def salary(self):
        print(f"{Emp_obj1.name} Your salary will be arrives next two days.")


Emp_obj1 = Employee("salina", "1001", "4004")
print(f"{Emp_obj1.name} {Emp_obj1.id} {Emp_obj1.pin}")

Emp_obj1.salary()
"""

"""
class Calc:

    def sum(self, num1, num2):
        return num1 + num2

    def mult(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 // num2


obj1 = Calc()

output = obj1.sum(12, 23)  # sum of numbers
print(output)

output = obj1.mult(11, 11)  # multiplication
print(output)

output = obj1.div(120, 20)  # Division
print(output)
"""