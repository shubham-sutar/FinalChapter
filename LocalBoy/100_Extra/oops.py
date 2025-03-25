# understanding oops

class Person:
    name = None
    id = None
    age = None
    phone_num = None

    def talk(self, phone_num):
        print(f"my fone number is {phone_num} and talking with sayali.")

    def walk(self):
        print("Im walking on the streets.")

    def sleep(self, name):
        print(f"{name} is sleeping.")


obj = Person()
obj.talk(9156364230)

obj1 = Person()
obj1.walk()

obj2 = Person()
obj2.sleep("shubham")

obj3 = Person()
obj3.name = "sayali"
print(sleep(obj3.name))


