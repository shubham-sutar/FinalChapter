# Inheritance
# Single Inheritance

class Employee:
    company = "Softcorp India"
    name = "shubham sutar"
    language = "python"

    def show(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee):
    company = "Two Engineers"

    def show_language(self):
        print(f"The name is {self.name} and he  is good with {self.language}")


obj1 = Employee()
obj2 = Programmer()
print(obj1.company, obj2.company)
# obj1.show()
obj2.show_language()

