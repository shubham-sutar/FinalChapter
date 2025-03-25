# Class Methods

class Emp:
    a = 45

    @classmethod
    def show(cls):
        print(f"This is the class method {cls.a}")


obj = Emp()
print(obj.a)

obj.a = 60
obj.show()
