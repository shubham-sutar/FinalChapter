# functions
# Built in functions
# ex. max()

# User defined functions

def say_hello():
    print("hello shubham")


say_hello()


def say_hello_args(name="shubham"):
    print(f"hello {name}")


say_hello_args()
say_hello_args("ajay")
say_hello_args(name="Sachin")


# when we return a value we must have to print function
def test_sum(num1, num2):
    return num1 + num2


result = test_sum(5, 6)
print(result)


def ex_fn(num1, num2, num3):
    return num1 + num2 + num3


result = ex_fn(12, 22, 33)
print(result)


# args

def my_fun(a=10, b=10, c=20):
    return a + b + c


result1 = my_fun(10, 10, 10)
result2 = my_fun(c=24)
print(result1, result2)

"""
def print_args(*args):
    for i in args:
        print(i, end=" ")


print_args("shubham", 23, 44, 2.9)
"""
"""
my_list = [12, "shubham", 23.2]

for i in my_list:
    print(i, end=" ")
"""

"""
def make_pizza(*topings):
    for topin in topings:
        print(topin)


make_pizza("tomato", "orange")
make_pizza("lichi", "cherry")

---------------------------------

def make_pizza(*topings, base):
    print(topings, base)


make_pizza("tomato", "mushroom", base="thin crust")
"""

"""
# leap year program
# divisible by 4
# but not by 100 unless it is also divisible by 400

year = 2022

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap Year")
else:
    print("not leap leap year")
"""


# Factorial

fact = int(input("enter any number:"))
en = 1
for i in range(fact, 0, -1):
    en = i * en

print(f"Factorial of {fact} is {en}.")


