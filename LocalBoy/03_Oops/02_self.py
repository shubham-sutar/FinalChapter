# Self

class Employee:
    name = "shubham"  # variables/ class attributes
    language = "python"
    salary = 50000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod  # not required to use object
    def greet():
        print("Happy Coding ❤")


obj = Employee()
# obj.name = "sayali"  # instance attribute01_class.py
new_user = obj.name, obj.language, obj.salary
# print(f"--------- New Employee Informaion ---------\n{new_user}")
obj.getInfo()
# obj.greet()

