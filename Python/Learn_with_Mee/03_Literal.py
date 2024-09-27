# Literals
# var_name = variable_value
name = "Pramod"
# var_name --> Identifier
# var_val --> Literals
# Literals are the actual values assigned
# Literals can be Numeric and Non-Numeric.

age = 12
pi = 3.14

# Boolean literals
is_married = True
is_raining = False

# Strings
name1 = 'tanaji'

name2 = "shahaji"

multiple_string_line = """
Just you Type here Information or
project description
"""

# Assignment Operators
Number = 45
Employee_name = "Kriti"

# Compare Operator(bool)
cond_1 = (1 == True)  # In Python 1 --> True
cond_2 = (0 == False)  # In Python 0 --> False
print(cond_1)
print(cond_2)

# Not Operator
is_rain = True
print(is_rain)  # output - True
print(not is_rain)  # output - False

# is Operator
num1 = 1
num2 = 2
num3 = False
print(num1 is num2)  # False

# Arithmetic Operator
num1 = 12
num2 = 13
print(f"result = {num1 + num2}")
print(f"result = {num1 - num2}")
print(f"result = {num1 * num2}")
print(f"result = {num1 / num2}")
print(f"result = {num1 % num2}")

print(3 ** 2)  # 9
print(pow(3, 2))  # 9

# Logical Operator

num1 = 20
num2 = 5
print(f"result = {num1 > num2}")  # greater Than
print(f"result = {num1 < num2}")  # less than
print(f"result = {num1 >= num2}")  # greater than is equal to
print(f"result = {num1 <= num2}")  # less than equal to
print(f"result = {num1 == num2}")  # equal to
print(f"result = {num1 != num2}")  # not equal to
print(bin(num2))  # find binary value of number

# Ternary Operator
num1 = 10
num2 = 20
print("num1 is big" if num2 < num1 else "num2 is big")

# Program - Calculate the area of circle
# formula for area of circle = pi*r*r

radius = float(input("Enter the radius:"))
pi = 3.14
area_of_circle = pi*(radius*radius)
print(f"Area of Circle is {area_of_circle}")
print(type(area_of_circle))






