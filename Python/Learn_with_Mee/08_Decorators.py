# Decorators
"""
def my_decorator(func):
    def wrapper():
        print("Stars Execution of the program...")
        print("------------------------------")
        func()
        print("------------------------------")
        print("End Program...")

    return wrapper()


@my_decorator
def say_hello():
    print("hello Naruto")
"""

"""
def my_Decor(func):
    def wrapper():
        print("======================================")
        print("hello world")
        func()
        print("good BYE")
        print("++++++++++++++++++++++++++++++++++++++")

    return wrapper()


@my_Decor
def my_world():
    print("Itachi said That, Time is doesn't heal everyone, \nIts teach us how to live with pain")

"""

"""
def my_decorator(func):
    def wrapper():
        print("+++++++++++++++++++++++")
        func()
        print("+++++++++++++++++++++++")

    return wrapper()


@my_decorator
def say_something():
    print("Next Move...")
"""

# Dictionary
# Key and Value
# A dictionary is an unordered collection of data
# in a kay-value format.
# mutable in nature
# keys should be unique but values not.

my_dict = {
    "name": "shubham",
    "salary": "35k",
    "EmpId": 1001

}

print(my_dict)
print(len(my_dict))

print(my_dict["salary"])
print(my_dict.get("EmpId"))

# change name
my_dict["name"] = "sayali"
print(my_dict)

print(my_dict.keys())
print(my_dict.values())




