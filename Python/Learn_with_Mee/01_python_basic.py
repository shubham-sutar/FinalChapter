print("hello world")
# self - concept in Oops which points to itself
# *args - unlimited number of arguments
# sep=' ' - how you want to separate the arguments
# end='\n' - in the end what you want to do
# file=None - File IO

print("Hello", 'world', 123, True, 3.14)  # Hello world 123 True 3.14
print("Hello", 'world', 123, True, 3.14, sep="-")
# Hello-world-123-True-3.14

print("mango", 'grapes', 250, True, 25.5, sep="-")  # 6 arguments

# To Lines in one line
print("ant", "Parrot", "Rat", "Elephant")
print("Apple", "Grapes", "Cherry", "Nuts")
# output of this two lines is separated by new line
# like this : -
'''
ant Parrot Rat Elephant
Apple Grapes Cherry Nuts
'''
# Now we want to do output prints in single line.
# Let's see How to do it

print("ant", "Parrot", "Rat", "Elephant", end=" ")
print("Apple", "Grapes", "Cherry", "Nuts")

# Output Looks like this
'''
ant Parrot Rat Elephant Apple Grapes Cherry Nuts
'''

# you must remember always sep = "" and end= "" comes on last place always
# def print(self, *args, sep=" ", end=" ", file=None)

'''
# Example :

print("I am a Super Boy", end="__")
print("I am a Super Girl")

# What will be Output of this code
# Ans - I am a Super Boy__I am a Super Girl
'''
# Indentation in Python
# Python is Case Sensitive
# you cannot write print as like this Print()

# Program to find the max in multiple numbers
print(max(12, 56, 234, -89, 0, 34, 22, 456, -23, 785, 234))
# Ans - 785

# Program to find the min in multiple numbers
print(min(12, 56, 234, -89, 0, 34, 22, 456, -23, 785, 234))
# Ans - -89

# Dynamically Typed
# Dynamic Type - Type of Data that Python supports
# Types which are supported in the Python
'''
Integers = Positive and negative whole numbers
example.. 1, 123, -12

Floating point Numbers
example.. 18.000, 14,5

String
"Hashnode" , "123", "12.5"

Boolean
True, False
'''

# How do I check the type of the variable.
marks = 86
print(type(marks))  # <class 'int'>

marks = "86"
print(type(marks))  # <class 'str'>

# Python - Complex Number
complex_number = 5+3j

# complex data types in python
'''
List
Tuple
Dictionary
Set
Class 
Object
Function
Modules
Packages
'''

# variable
name = "ishubh.hashnode.dev"
print(type(name))  # <class 'str'>

# variables names starts from A-Z, a-z
# exp - name = "hashnode" , Age = 35

# variable name should not be starts with number
# exp - 12name = "Dhiraj"

# variable name should not be any keyword
# Keyword is a reserved word - 'True', 'str', 'None', And
# exp - And = 12

# variable name should not be any Special character
# exp - @name = "shubham", $name = 45
_salary = 50000
print(_salary)  # only '_' is allowing

# variable name should not be any space
# first name = "shubham"

# variable name should not be any special character
# shubham& = 77

# python loves snake case
# exp - "hello_world", first_name_and_last_name

# take an input from the user

name = input("Enter your name:")
empId = input("Enter your employee Id:")
designation = input("Enter your designation:")
print("-------------your Information----------------")
print("Name:"+name, "employee Id:"+empId, "designation:"+designation)








