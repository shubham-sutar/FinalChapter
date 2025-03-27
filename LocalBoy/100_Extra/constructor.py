# constructor

class Programmer:
    company = "Mircosoft"
    name = None
    id = None
    salary = None

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def show(self):
        print(f"The working Employee Information as below...\nname = {self.company}, {self.name}, {self.id},"
              f" {self.salary}")


obj = Programmer("shubham", 1001, 50000)
obj.show()


