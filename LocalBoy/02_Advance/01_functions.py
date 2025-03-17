# functions

# function definition
"""
def avg():
    num1 = int(input("Enter any numbers: "))
    num2 = int(input("Enter any numbers: "))
    num3 = int(input("Enter any numbers: "))
    num4 = int(input("Enter any numbers: "))

    sum = num1 + num2 + num3 + num4
    result = sum / 4
    print("The avg of numbers: ", result)


avg()  # call the function.
"""

# problem
"""
def greet(name):
    print(f"Hello {name}")


greet("shubham")
"""


# Types of function:
# 1) bult-in function : made by python
# 2) user defined function : made by user

# def good(name, end):
#     print("good day " + name)
#     print(end)
#
#
# good("shubham", "thank you")

# function return
# def my_fun(name):
#     print("hello " + name)
#     return "Done"
#
#
# my_friend = my_fun("neha")
# print(my_friend)

# function by default

def my_func(name, nationality="Indian"):
    print(f"Your Name is {name}")
    print(f"your Nationality is {nationality}")
    return "Information Submitted successfully."


user = my_func("shubham", "USA")
print(user)


