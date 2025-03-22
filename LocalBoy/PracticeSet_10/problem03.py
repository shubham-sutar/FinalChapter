# problem 03
# 3. create a class with a class attribute a; create an object from it and set 'a' directly using object. a = 0. Does
# this change the class attribute?

class MyClass:
    a = 5


object = MyClass()
print(object.a)

object.a = 0
print(object.a)
