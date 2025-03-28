# Inheritance

# Single Inheritance

# class Father:
#     key = "abc@123"
#
#     def father_method(self):
#         return "father method"
#
#     @staticmethod
#     def stats():
#         print("hi father.")


# class Child(Father):
#
#     def child_method(self):
#         return "child_method"
#
#
# obj = Child()
# output = obj.child_method()
# print(output)
#
# output1 = obj.father_method()
# print(output1)
#
# Father.stats()  # call the static method

class MyClass:

    @property
    def name(self):
        return f"my name is {self.fname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]

    @property
    def salary(self):
        return f"{self.esalary}"

    @salary.setter
    def salary(self, value):
        self.esalary = value

    @property
    def mobile_num(self):
        return f"{imobile_num}"

    @mobile_num.setter
    def mobile_num(self, value):
        self.imobile_num = value


obj9 = MyClass()
obj9.imobile_num = "9156364230"
print(obj9.imobile_num)

obj1 = MyClass()
obj1.esalary = "15000"
print(obj1.esalary)

obj = MyClass()
obj.fname = "shubham sutar"
print(obj.fname)
