# Property Decorators

class Emp:
    a = 45

    @classmethod
    def show(cls):
        print(f"This is the class method {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


obj = Emp()
print(obj.a)

obj.a = 60
obj.show()

obj.name = "shubham sutar"
print(obj.fname)
print(obj.lname)
