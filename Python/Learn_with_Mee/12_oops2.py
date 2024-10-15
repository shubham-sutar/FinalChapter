# Inheritance
# Acquiring the attribute and Behaviour


# Single Inheritance
"""
class Grandparents:
    key = "abc@123"

    def grandpa_method(self):
        return "Grandparent method"


class Father(Grandparents):
    def parent_method(self):
        return "parent's method"


parent = Father()
parent.parent_method()
parent.grandpa_method()
print(parent.key)
"""

"""
class Parents:
    gold = "2kg"

    def BHK2(self):
        print("2bhk")


class Child(Parents):
    def child(self):
        print("3bhk")


child_obj = Child()
child_obj.BHK2()
print(child_obj.gold)
child_obj.child()
"""

# Hierarchical Inheritance

# Father - Multiple Children
"""
class Father:
    def father_BHK1(self):
        print("Father has 1BHK flat")


class Shubham(Father):
    def shubham_BHK2(self):
        print("shubham has 2BHK flat")


class Sayali(Father):
    def sayali_BHK3(self):
        print("Sayali has 3BHK flat")


class Rani(Father):
    def rani_BHK2(self):
        print("Rani has 2BHK flat")


print("---------- shubham Information ----------")
obj_shubham = Shubham()
obj_shubham.shubham_BHK2()
obj_shubham.father_BHK1()

print("\n---------- Sayali Information ----------")
obj_sayali = Sayali()
obj_sayali.father_BHK1()
obj_sayali.sayali_BHK3()

print("\n---------- Rani Information ----------")
obj_rani = Rani()
obj_rani.father_BHK1()
obj_rani.rani_BHK2()
"""

# multilevel Inheritance
"""
class Grandfather:
    def grandfather_method(self):
        print("Hey I'm Your Grandfather")


class Father(Grandfather):
    def father_method(self):
        print("Hey I'm Your Father")


class Child(Father):
    def child_method(self):
        print("Hey I'm child")


print("---------- Child Class--------")  # Access all data of father and grandpa
child_obj = Child()
child_obj.child_method()
child_obj.father_method()
child_obj.grandfather_method()

print("\n---------- Father Class--------")  # Access all data of grandpa not child

father_obj = Father()
father_obj.father_method()
father_obj.grandfather_method()

print("\n---------- Grandfather Class--------")  # Access only self data

grandfather_obj = Grandfather()
grandfather_obj.grandfather_method()
"""

# Multiple Inheritance

"""
class Father:
    def father_method(self):
        return "father have 10rs"

    def home(self):
        print("father at home")


class Mother:
    def mother_method(self):
        return "mother have 50rs"

    def home(self):
        print("mother at home")


class Child(Father, Mother):
    def child_method(self):
        return "I have no money"

    # def home(self):
    #     print("Im out of the home")


child_obj = Child()
print(child_obj.father_method())
print(child_obj.mother_method())
child_obj.home()
"""

# Hybrid Inheritance
# multiple types of inheritance, such as single, multiple, and multilevel inheritance
"""
class A:
    def method_A(self):
        return "Method A"


class B(A):
    def method_B(self):
        return "Method B"


class C(A):
    def method_C(self):
        return "Method C"


class D(B, C):
    def method_D(self):
        return "method D"


obj1 = D()
print(obj1.method_D())
print(obj1.method_A())
print(obj1.method_B())
print(obj1.method_C())
"""


# Polymorphism
# polymorphism allows object of
# different classes to be treated as
# object of a common superclass.

# Method Overriding - same name in the parent and child of method
# child will always override the parent functions
# super means call my parent function


class Shape:
    def area(self):
        print("Area of Shape")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        super().area()
        return 3.14 * self.radius * self.radius


obj1 = Rectangle(5, 2)
print(obj1.area())

obj2 = Circle(3)
print(obj2.area())

# Method Overloading
# Python does not support method overloading
# in the traditional sense

# Abstraction
# Hiding the details and showing the functionality

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("barking")


class Cat(Animal)
    def sound(self):
        print("myaw, myaw")

        