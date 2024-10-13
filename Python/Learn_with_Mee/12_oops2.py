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
