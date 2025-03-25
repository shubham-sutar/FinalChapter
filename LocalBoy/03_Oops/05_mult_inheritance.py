# Inheritance
# multiple Inheritance

class Employee:
    company = "Softcorp India"
    name = "Default_name"

    def show(self):
        print(f"The name is {self.name} and the company is {self.company} ")


class Coder:
    language = "python"

    def print_language(self):
        print(f"The coding language of company preferred is {self.language}")


class Programmer(Employee, Coder):
    company = "Two Engineers"

    def show_language(self):
        print(f"The name is {self.company} and he  is good with {self.language}")


obj1 = Employee()
obj2 = Programmer()
# print(obj1.company, obj2.company)
# obj1.show()
# obj2.show_language()

obj2.show()
obj2.show_language()
obj2.print_language()
