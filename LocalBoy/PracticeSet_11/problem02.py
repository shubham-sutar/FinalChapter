# problem 02
# 2. Create a class 'pet' from 'Animals' amd further create a class "Dog" from "pets". Add a method 'bark' to class
# "Dog"

class Animals:
    pass


class Pets(Animals):
    name = "charu"

    def pet_name(self, name):
        self.name = name


class Dog(Pets):
    def bark(self):
        print(f"Dog Name {self.name} are barking.")


obj3 = Dog()
obj3.bark()
