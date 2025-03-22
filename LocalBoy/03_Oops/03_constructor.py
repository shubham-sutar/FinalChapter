# constructor

class Employee:
    name = "shubham"  # variables/ class attributes
    language = "python"
    salary = 50000

    def __init__(self, name, language, salary):  # dunder method automatically call
        self.name = name
        self.language = language
        self.salary = salary
        print("I Executed first without any Object.")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod  # not required to use object
    def greet():
        print("Happy Coding ❤")


obj = Employee("shubham", "JavaScript", 30000)
# obj.name = "sayali"  # instance attribute01_class.py
# new_user = obj.name, obj.language, obj.salary
# print(f"--------- New Employee Informaion ---------\n{new_user}")
# obj.getInfo()
# obj.greet()

