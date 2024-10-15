# Exception
# It is an event that occurs during the execution of a program
# that disrupts the normal flow of instructions.

"""
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

result = num1 / num2  # 10/0 Exception occurs (ZeroDivisionError: division by zero)
print(result)
"""

# How to resolve issue by Exception Handling
"""
try:
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))

    result = num1 / num2  # 10/0 Exception occurs (ZeroDivisionError: division by zero)
    print(result)

except Exception as e:
    print(e)
    print("Please Enter Valid Number!")

# Type Error
result = 5 + "5"
print(result)

# Value Error
int("shubham")

# Index out of bound
my_list = [11, 23, 34]
print(my_list[3])

# Key Error: 'c'
my_dict = {
    "a": 2,
    "b": 3
}
print(my_dict["c"])

# Try, Except, Finally

try:
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))
    result = num1 + num2
    # print("result is", result)

except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)

else:
    print("result is", result)

finally:
    print("happy coding ❤")
"""


