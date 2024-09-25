# Advance data types in python
# List, Tuples, Set, Dictionary
# These are useful for API and Web Automation.

# Take a User Input
# input() always returns str value so here we use int() for conversion.

'''
# addition program
num1 = int(input("Enter first number:"))  # taking input num1
num2 = int(input("Enter second number:"))  # taking input num2

result = num1 + num2  # Addition

print("Result is:", result)  # Result
'''

# conversion
'''
conversion str to int
example- 

num1 = "35"  # string
int_num1 = int(num1)  # int
print(type(int_num1)) 

# int to str --> str()
# str to int --> int()

# float to int --> int()
example-
updated_bill = 155.78
updated_bill = int(155.78)
print(updated_bill)  # 155
print(type(updated_bill))  # <class 'int'>
'''

'''
# Auto conversion in python
# example-
num1 = 155  # int
num2 = 3  # int

result = num1 / num2
print(result)  # 51.66 float
'''

# raw string
openfp = r'C:\media\abc.jpeg'
print(openfp)

# Format of the string
f_name = "john"
l_name = "deo"

print(f_name + " " + l_name)  # output- john deo
print(f_name, l_name)  # output- john deo

# f - Formatting - it will replace the values of the variables
# {} - placeholder
print(f'Your Full Name is {f_name} {l_name}')  # output-Your Full Name is john deo

# In built Functions -
# Function -> Repeat a task - You can use a function.
# print(), input, type(), format(), max, min, id(), len(), sum(), avg()
# There are lot of function available take a look https://docs.python.org/3/library/functions.html

# String
name = "Amena"
print(name)
print(type(name))
print(id(name))  # id - memory address where it is Stored
print(len(name))  # length of string, starts from 1 always

upper_name = name.upper()
print(upper_name)  # AMENA

lower_name = name.lower()
print(lower_name)  # amena

count_char = name.count('m')
print(count_char)
print(name[3])  # n

# None Type of Data
val = None
print(val)
print(type(val))  # <class 'NoneType'>

# Nothing
# None is not default value
# None is not 0
# None is not an empty string
# None is not the same as false

# List - its assume that shopping list
# List of a milk, bread, butter, poha
# You can just
# 1. add items
# 2. remove items
# 3. update item
# 4. view item
# 5. Exit

shopping_list = ["milk", "butter", "bread", "poha"]
print(shopping_list)
print(len(shopping_list))
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("biscuit")  # add item in last place of list
print(f"new shopping list is {shopping_list}")

count_of = shopping_list.count("poha")
print(count_of)

shopping_list.insert(0, "chocobar")
print(shopping_list)

shopping_list.extend(["chips", "chilli"])
print(shopping_list)

shopping_list.remove("poha")
print(shopping_list)

shopping_list.pop()
print(shopping_list)  # it will removes last index of item

print(shopping_list.index("butter"))

shopping_list.reverse()
print(shopping_list)

shopping_list.sort()
print(shopping_list)

shuffle_list = [112, 56, 10.23, 'D', True, "Neha"]
print(shuffle_list)

# Escape sequence
print("Good \"Morning\"")
print("Good \nMorning")
print("Good \tMorning")
print("Good \bMorning")
